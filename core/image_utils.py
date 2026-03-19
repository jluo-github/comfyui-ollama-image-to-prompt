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


# Words that indicate conversational "slop" leaked by instruct-tuned VLMs.
_SLOP_WORDS: frozenset[str] = frozenset(
    {
        "here",
        "are",
        "the",
        "tags",
        "image",
        "shows",
        "based",
        "on",
        "prompt",
        "this",
        "i",
        "can",
        "see",
        "a",
        "an",
        "is",
    }
)


def clean_tags(raw_text: str, trailing_separator: bool = True) -> str:
    """Aggressively strips conversational slop and formats into pure Danbooru tags.

    Args:
        raw_text: The raw text from the model (may contain newlines, bullets, chat).
        trailing_separator: If True, appends ``", "`` to the end of non-empty output.

    Returns:
        A cleaned, deduplicated, comma-separated tag string in lowercase.
    """
    # 1. Strip all markdown and structural artifacts
    cleaned = raw_text.replace('"', "").replace("*", "").replace("\n", ", ")

    # 1b. Strip colon-prefixed conversational preambles
    # e.g. "Here are the tags for this image: 1girl, solo" → "1girl, solo"
    colon_match = re.match(r"^[^,]*:\s*", cleaned)
    if colon_match:
        preamble = colon_match.group(0).lower()
        if any(w in preamble for w in ("here", "tags", "image", "prompt", "based", "following")):
            cleaned = cleaned[colon_match.end() :]

    # 2. Split into raw tokens
    raw_tags = [t.strip() for t in cleaned.split(",") if t.strip()]

    # 3. Filter out conversational slop and clean individual tags
    final_tags: list[str] = []
    seen: set[str] = set()

    for tag in raw_tags:
        words = tag.lower().split()

        # Skip long conversational sentences that slipped past commas
        if len(words) > 5 and any(w in _SLOP_WORDS for w in words[:3]):
            continue

        # Strip leading bullet dashes / asterisks (e.g. "- ", "* ")
        # and numbered list markers (e.g. "1. ", "2. ") — but NOT bare digits
        # that are part of tag names like "1girl", "1boy", "2girls"
        tag = re.sub(r"^[-*]+\s*", "", tag)
        tag = re.sub(r"^\d+\.\s*", "", tag)
        tag = tag.strip()

        # Strip trailing periods
        tag = tag.rstrip(".")

        # Lowercase for Danbooru convention
        tag = tag.lower().strip()

        # Deduplicate
        if tag and tag not in seen:
            final_tags.append(tag)
            seen.add(tag)

    cleaned_str = ", ".join(final_tags)
    if cleaned_str and trailing_separator:
        cleaned_str += ", "

    return cleaned_str
