from __future__ import annotations

import base64
import io

import torch
from PIL import Image

from core.image_utils import clean_tags, tensor_to_base64


class TestTensorToBase64:
    def _make_dummy_tensor(self, h: int = 4, w: int = 4, c: int = 3) -> torch.Tensor:
        """Creates a small random (H, W, C) float tensor in [0, 1]."""
        return torch.rand(h, w, c)

    def test_returns_string(self) -> None:
        tensor = self._make_dummy_tensor()
        result = tensor_to_base64(tensor)
        assert isinstance(result, str)

    def test_output_is_valid_base64(self) -> None:
        tensor = self._make_dummy_tensor()
        result = tensor_to_base64(tensor)
        decoded = base64.b64decode(result)
        # Should be a valid PNG (starts with PNG signature)
        assert decoded[:4] == b"\x89PNG"

    def test_output_decodes_to_correct_size(self) -> None:
        tensor = self._make_dummy_tensor(h=8, w=16)
        result = tensor_to_base64(tensor)
        decoded = base64.b64decode(result)
        img = Image.open(io.BytesIO(decoded))
        assert img.size == (16, 8)  # PIL reports (width, height)


class TestCleanTags:
    def test_basic_cleanup(self) -> None:
        raw = "tag1, tag2,  tag3"
        result = clean_tags(raw)
        assert result == "tag1, tag2, tag3, "

    def test_removes_newlines(self) -> None:
        raw = "tag1\ntag2\ntag3"
        result = clean_tags(raw)
        assert "\n" not in result
        assert "tag1" in result
        assert "tag3" in result

    def test_removes_bullet_dashes(self) -> None:
        raw = "- tag1\n- tag2\n- tag3"
        result = clean_tags(raw)
        assert "- " not in result

    def test_trailing_separator(self) -> None:
        raw = "tag1, tag2"
        result = clean_tags(raw, trailing_separator=True)
        assert result.endswith(", ")

    def test_no_trailing_separator(self) -> None:
        raw = "tag1, tag2"
        result = clean_tags(raw, trailing_separator=False)
        assert not result.endswith(", ")
        assert result == "tag1, tag2"

    def test_empty_input(self) -> None:
        result = clean_tags("")
        assert result == ""

    def test_removes_empty_tags(self) -> None:
        raw = "tag1,, , ,tag2"
        result = clean_tags(raw)
        assert result == "tag1, tag2, "

    # --- New tests for hardened slop filter ---

    def test_filters_conversational_slop(self) -> None:
        """Long sentence-like fragments starting with slop words should be discarded."""
        raw = "Here are the tags for this image: 1girl, solo, blue hair"
        result = clean_tags(raw)
        # The preamble "Here are the tags for this image:" is >5 words w/ slop -> dropped
        assert "1girl" in result
        assert "solo" in result
        assert "here" not in result.lower().split(", ")

    def test_deduplicates_tags(self) -> None:
        """Repeated tags (case-insensitive) should appear only once."""
        raw = "1girl, solo, 1Girl, SOLO, blue hair"
        result = clean_tags(raw)
        tags = [t.strip() for t in result.rstrip(", ").split(",")]
        assert tags.count("1girl") == 1
        assert tags.count("solo") == 1

    def test_strips_trailing_periods(self) -> None:
        raw = "1girl., solo., blue hair."
        result = clean_tags(raw)
        assert "." not in result

    def test_strips_numbered_bullets(self) -> None:
        """Numbered list items like '1. tag' should be cleaned to just the tag."""
        raw = "1. 1girl\n2. solo\n3. blue hair"
        result = clean_tags(raw)
        assert "1girl" in result
        assert "solo" in result
        assert "blue hair" in result
        # No leading numbers
        for tag in result.rstrip(", ").split(", "):
            assert not tag[0].isdigit() or tag == "1girl"

    def test_preserves_valid_multi_word_tags(self) -> None:
        """Short multi-word tags (Danbooru style) should be preserved."""
        raw = "looking at viewer, holding sword, long hair"
        result = clean_tags(raw)
        assert "looking at viewer" in result
        assert "holding sword" in result
        assert "long hair" in result

    def test_lowercases_output(self) -> None:
        """All output should be lowercased per Danbooru convention."""
        raw = "Blue Hair, RED EYES, Cowboy Shot"
        result = clean_tags(raw)
        assert result == "blue hair, red eyes, cowboy shot, "
