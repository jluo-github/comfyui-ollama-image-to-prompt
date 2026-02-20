from __future__ import annotations

import base64
import io

import numpy as np
import torch
from PIL import Image


def tensor_to_base64(image: torch.Tensor) -> str:
    """Converts a single image tensor (H, W, C) to a base64-encoded PNG string."""
    i = 255.0 * image.cpu().numpy()
    img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))

    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")


import json
import os
import re

# Global cache for Danbooru tags
_VALID_DANBOORU_TAGS: set[str] | None = None


def load_danbooru_tags() -> set[str]:
    """Loads the tags_v1.json file and flattens all English tag values into a set."""
    global _VALID_DANBOORU_TAGS
    if _VALID_DANBOORU_TAGS is not None:
        return _VALID_DANBOORU_TAGS

    local_tags: set[str] = set()
    try:
        # Assuming tags_v1.json is in the root of the node directory
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        json_path = os.path.join(current_dir, "tags_v1.json")

        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        def extract_tags(d):
            if isinstance(d, dict):
                for k, v in d.items():
                    extract_tags(v)
            elif isinstance(d, str):
                # The JSON values can be comma-separated like "low resolution, worst quality"
                # Split them and clean spacing
                for tag in d.split(","):
                    local_tags.add(tag.strip().lower())

        extract_tags(data)
        print(f"Loaded {len(local_tags)} strict Danbooru tags from tags_v1.json.")
        _VALID_DANBOORU_TAGS = local_tags
    except Exception as e:
        print(f"Warning: Failed to load tags_v1.json for strict filtering. {e}")
        _VALID_DANBOORU_TAGS = set()

    return _VALID_DANBOORU_TAGS


def clean_tags(
    raw_text: str, trailing_separator: bool = True, enforce_strict: bool = False
) -> str:
    """Cleans up raw model output into a comma-separated tag string.

    Args:
        raw_text: The raw text from the model (may contain newlines, bullets).
        trailing_separator: If True, appends ``", "`` to the end of non-empty output.
        enforce_strict: If True, filters tags against tags_v1.json.

    Returns:
        A cleaned, comma-separated tag string.
    """
    # Strip common conversational prefixes and markdown
    cleaned = re.sub(
        r"(?i)^(here are.*?:|\*\*?tags:?\*\*?|\*\*?prompt:?\*\*?|prompt:)",
        "",
        raw_text.strip(),
    )
    # Remove quotes and asterisks
    cleaned = cleaned.replace('"', "").replace("*", "")

    cleaned = cleaned.replace("\n", ", ").replace("- ", "")

    tags = [t.strip() for t in cleaned.split(",") if t.strip()]

    if enforce_strict:
        valid_set = load_danbooru_tags()
        if valid_set:
            tags = [t for t in tags if t.lower() in valid_set]

    cleaned = ", ".join(tags)
    if cleaned and trailing_separator:
        cleaned += ", "
    return cleaned
