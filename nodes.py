from __future__ import annotations

from typing import Any

import torch

try:
    from .core.api import generate_ollama_completion
    from .presets import (
        DEFAULT_MODEL,
        DEFAULT_URL,
        OLLAMA_MODELS,
        PROMPT_PRESETS,
    )
except ImportError:
    from core.api import generate_ollama_completion
    from presets import (
        DEFAULT_MODEL,
        DEFAULT_URL,
        OLLAMA_MODELS,
        PROMPT_PRESETS,
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
                "mode": (list(PROMPT_PRESETS.keys()), {"default": "natural_language"}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF}),
                "keep_alive": ("INT", {"default": 0, "min": -1, "max": 60, "step": 1}),
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
                "keywords": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "",
                        "placeholder": "Optional: Keywords for 'expand' modes or additional rules.",
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
        keywords: str = "",
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
        else:
            final_prompt = PROMPT_PRESETS.get(mode, PROMPT_PRESETS.get("natural_language", ""))

        if keywords and keywords.strip():
            final_prompt += f"\n\nUser Keywords / Instructions:\n{keywords.strip()}"

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
                custom_prompt=custom_prompt,
            )

            generated_texts.append(generated_text)
            thought_processes.append(thought_process)

        return (generated_texts, thought_processes)

    @classmethod
    def IS_CHANGED(cls, seed: int, **kwargs: Any) -> float | int | str:
        """Forces ComfyUI to re-evaluate the node if the seed changes."""
        return seed
