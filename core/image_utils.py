from __future__ import annotations

import base64
import io
import re

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


def clean_tags(raw_text: str, trailing_separator: bool = True) -> str:
    """Cleans up raw model output into a comma-separated tag string.

    Args:
        raw_text: The raw text from the model (may contain newlines, bullets).
        trailing_separator: If True, appends ``", "`` to the end of non-empty output.

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

    cleaned = ", ".join(tags)
    if cleaned and trailing_separator:
        cleaned += ", "
    return cleaned
