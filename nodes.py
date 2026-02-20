from __future__ import annotations

import re
from typing import Any

import requests
import torch

try:
    from .core.image_utils import clean_tags, tensor_to_base64
    from .presets import (
        DEFAULT_MODEL,
        DEFAULT_URL,
        NATURAL_LANGUAGE_PROMPT,
        OLLAMA_MODELS,
        TAGS_PROMPT,
    )
except ImportError:
    from core.image_utils import clean_tags, tensor_to_base64
    from presets import (
        DEFAULT_MODEL,
        DEFAULT_URL,
        NATURAL_LANGUAGE_PROMPT,
        OLLAMA_MODELS,
        TAGS_PROMPT,
    )


class OllamaImageToPrompt:
    @classmethod
    def INPUT_TYPES(cls) -> dict[str, Any]:
        return {
            "required": {
                "image": ("IMAGE",),
                "ollama_url": (
                    "STRING",
                    {"multiline": False, "default": DEFAULT_URL},
                ),
                "model": (OLLAMA_MODELS, {"default": DEFAULT_MODEL}),
                "mode": (["natural_language", "tags"], {"default": "natural_language"}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF}),
                "keep_alive": ("INT", {"default": 5, "min": -1, "max": 60, "step": 1}),
                "thinking_mode": ("BOOLEAN", {"default": False}),
            },
            "optional": {
                "custom_prompt": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "",
                        "placeholder": "Optional: Override default system prompt. Leave empty to use 'mode'.",
                    },
                ),
            },
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("text", "thought_process")
    OUTPUT_IS_LIST = (True, True)
    FUNCTION = "generate_prompt"
    CATEGORY = "Ollama"

    def generate_prompt(
        self,
        image: torch.Tensor,
        ollama_url: str,
        model: str,
        mode: str,
        seed: int,
        keep_alive: int,
        thinking_mode: bool,
        custom_prompt: str = "",
    ) -> tuple[list[str], list[str]]:

        # Initialize output lists
        generated_texts: list[str] = []
        thought_processes: list[str] = []

        # Determine prompt once
        final_prompt = ""
        if custom_prompt and custom_prompt.strip():
            final_prompt = custom_prompt
        elif mode == "tags":
            final_prompt = TAGS_PROMPT
        else:  # natural_language
            final_prompt = NATURAL_LANGUAGE_PROMPT

        # Support batch processing
        # ComfyUI passes images as (B, H, W, C)
        for img_tensor in image:
            img_b64 = tensor_to_base64(img_tensor)

            # Prepare payload
            payload = {
                "model": model,
                "prompt": final_prompt,
                "images": [img_b64],
                "stream": False,
                "options": {
                    "seed": seed,
                },
            }

            if keep_alive == -1:
                payload["keep_alive"] = -1  # Indefinite
            else:
                payload["keep_alive"] = f"{keep_alive}m"

            try:
                full_url = f"{ollama_url.rstrip('/')}/api/generate"
                print(
                    f"Sending request to Ollama: {full_url} with model {model}, seed {seed}"
                )

                response = requests.post(full_url, json=payload)
                response.raise_for_status()

                result = response.json()
                generated_text = result.get("response", "")
                thought_process = ""

                # Robust Parsing for <think> ... </think>
                think_pattern = re.compile(r"<think>(.*?)</think>", re.DOTALL)
                think_match = think_pattern.search(generated_text)

                if think_match:
                    captured_thought = think_match.group(1).strip()
                    generated_text = think_pattern.sub("", generated_text).strip()

                    if thinking_mode:
                        thought_process = captured_thought

                # Post-processing for tags mode
                if mode == "tags" and not custom_prompt:
                    generated_text = clean_tags(generated_text, enforce_strict=True)

                generated_texts.append(generated_text)
                thought_processes.append(thought_process)

            except requests.exceptions.RequestException as e:
                print(f"Error communicating with Ollama: {e}")
                generated_texts.append(f"Error: {str(e)}")
                thought_processes.append("Error")
            except Exception as e:
                print(f"Unexpected error: {e}")
                generated_texts.append(f"Error: {str(e)}")
                thought_processes.append("Error")

        return (generated_texts, thought_processes)
