from __future__ import annotations

import re
from typing import Any

import requests

try:
    from .image_utils import clean_tags, tensor_to_base64
except ImportError:
    from core.image_utils import clean_tags, tensor_to_base64


def generate_ollama_completion(
    ollama_url: str,
    model: str,
    final_prompt: str,
    img_tensor: Any,  # Expected to be a torch.Tensor
    mode: str,
    seed: int,
    keep_alive: int,
    thinking_mode: bool,
    custom_prompt: str = "",
) -> tuple[str, str]:
    """Sends a request to the Ollama API to generate a text completion from an image.

    Args:
        ollama_url: The base URL of the Ollama instance (e.g., "http://localhost:11434").
        model: The name of the vision model to use (e.g., "qwen3.5-vl").
        final_prompt: The complete prompt to send to the model.
        img_tensor: A PyTorch tensor representing the image.
        mode: The generation mode ("natural_language" or "tags").
        seed: The random seed for generation to ensure reproducibility.
        keep_alive: The duration (in minutes) to keep the model loaded in memory, or -1 for indefinite.
        thinking_mode: Whether to parse and extract the model's `<think>` output block.
        custom_prompt: An optional custom prompt string. If provided and `mode` is "tags", tag cleaning is bypassed.

    Returns:
        A tuple containing (generated_text, thought_process). If `thinking_mode` is False or no
        `<think>` block is found, `thought_process` will be an empty string. On error, both strings
        will contain error descriptions.
    """
    img_b64 = tensor_to_base64(img_tensor)

    if not thinking_mode:
        final_prompt += (
            "\n\nCRITICAL: Do NOT output any thinking process. "
            "Do NOT use <think> tags. Provide the final output immediately."
        )

    # Prepare payload
    payload = {
        "model": model,
        "prompt": final_prompt,
        "images": [img_b64],
        "stream": False,
        "think": thinking_mode,
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
        print(f"Sending request to Ollama: {full_url} with model {model}, seed {seed}")

        response = requests.post(full_url, json=payload, timeout=300)  # Add timeout
        response.raise_for_status()

        result = response.json()
        generated_text = result.get("response", "")
        
        # Native Ollama handling: it separates thoughts into a dedicated field
        thought_process = result.get("thinking", "").strip()

        # Fallback: Robust Parsing for <think> ... </think> in case of proxies or older models
        think_pattern = re.compile(r"<think>(.*?)(?:</think>|$)", re.DOTALL)
        think_match = think_pattern.search(generated_text)

        if think_match:
            captured_thought = think_match.group(1).strip()
            generated_text = think_pattern.sub("", generated_text).strip()

            if not thought_process:  # Use fallback if native field was missing
                thought_process = captured_thought
                
        if not thinking_mode:
            thought_process = ""

        # Post-processing for tags mode
        if mode in ["danbooru_tags", "expand_tags"] and not custom_prompt:
            generated_text = clean_tags(generated_text)

        # Append BREAK token for non-JSON modes, or clean markdown JSON blocks
        if mode == "json_extract":
            # Attempt to strip markdown code block boundaries if the model wraps the JSON
            json_match = re.search(r'```(?:json)?\s*(.*?)\s*```', generated_text, re.DOTALL)
            if json_match:
                generated_text = json_match.group(1).strip()
            else:
                generated_text = generated_text.strip()
        else:
            generated_text = f"{generated_text.rstrip(', ')}, BREAK,"

        return generated_text, thought_process

    except requests.exceptions.RequestException as e:
        print(f"Error communicating with Ollama: {e}")
        return f"Error: {str(e)}", "Error"
    except Exception as e:
        print(f"Unexpected error when calling Ollama: {e}")
        return f"Error: {str(e)}", "Error"
