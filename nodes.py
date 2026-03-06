from __future__ import annotations

from typing import Any

import torch

try:
    from .core.api import generate_ollama_completion
    from .presets import (
        DEFAULT_MODEL,
        DEFAULT_URL,
        NATURAL_LANGUAGE_PROMPT,
        OLLAMA_MODELS,
        TAGS_PROMPT,
    )
except ImportError:
    from core.api import generate_ollama_completion
    from presets import (
        DEFAULT_MODEL,
        DEFAULT_URL,
        NATURAL_LANGUAGE_PROMPT,
        OLLAMA_MODELS,
        TAGS_PROMPT,
    )


class OllamaImageToPrompt:
    """A ComfyUI Node for generating prompts from images using local Ollama vision models.

    Supports generating detailed natural language descriptions and Danbooru-style tags.
    """

    @classmethod
    def INPUT_TYPES(cls) -> dict[str, dict[str, Any]]:
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
                "keep_alive": ("INT", {"default": 0, "min": -1, "max": 60, "step": 1}),
                "thinking_mode": ("BOOLEAN", {"default": False}),
                "enable_thinking": ("BOOLEAN", {"default": True}),
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
        enable_thinking: bool,
        custom_prompt: str = "",
    ) -> tuple[list[str], list[str]]:
        """Generates prompts from input images via the Ollama API.

        Processes a batch of images and utilizes the `generate_ollama_completion` helper.

        Returns:
            A tuple containing two lists:
            - A list of generated prompt strings (one for each input image).
            - A list of generated thought processes (one for each input image).
        """
        # Initialize output lists
        generated_texts: list[str] = []
        thought_processes: list[str] = []

        # Determine prompt once per batch
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
            generated_text, thought_process = generate_ollama_completion(
                ollama_url=ollama_url,
                model=model,
                final_prompt=final_prompt,
                img_tensor=img_tensor,
                mode=mode,
                seed=seed,
                keep_alive=keep_alive,
                thinking_mode=thinking_mode,
                enable_thinking=enable_thinking,
                custom_prompt=custom_prompt,
            )

            generated_texts.append(generated_text)
            thought_processes.append(thought_process)

        return (generated_texts, thought_processes)
