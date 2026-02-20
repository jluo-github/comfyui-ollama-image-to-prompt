from __future__ import annotations

from presets import (
    DEFAULT_MODEL,
    DEFAULT_URL,
    NATURAL_LANGUAGE_PROMPT,
    OLLAMA_MODELS,
    TAGS_PROMPT,
)


class TestPresets:
    def test_models_list_is_not_empty(self) -> None:
        assert len(OLLAMA_MODELS) > 0

    def test_default_model_in_models_list(self) -> None:
        assert DEFAULT_MODEL in OLLAMA_MODELS

    def test_default_url_is_valid(self) -> None:
        assert DEFAULT_URL.startswith("http")

    def test_tags_prompt_is_non_empty(self) -> None:
        assert isinstance(TAGS_PROMPT, str)
        assert len(TAGS_PROMPT) > 50

    def test_natural_language_prompt_is_non_empty(self) -> None:
        assert isinstance(NATURAL_LANGUAGE_PROMPT, str)
        assert len(NATURAL_LANGUAGE_PROMPT) > 50

    def test_tags_prompt_mentions_danbooru(self) -> None:
        assert "danbooru" in TAGS_PROMPT.lower()

    def test_natural_language_prompt_mentions_expression(self) -> None:
        assert "expression" in NATURAL_LANGUAGE_PROMPT.lower()
