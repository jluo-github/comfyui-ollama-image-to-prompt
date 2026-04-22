from __future__ import annotations

from presets import (
    DANBOORU_TAGS,
    DEFAULT_MODEL,
    DEFAULT_URL,
    PROMPT,
    OLLAMA_MODELS,
)


class TestPresets:
    def test_models_list_is_not_empty(self) -> None:
        assert len(OLLAMA_MODELS) > 0

    def test_default_model_in_models_list(self) -> None:
        assert DEFAULT_MODEL in OLLAMA_MODELS

    def test_default_url_is_valid(self) -> None:
        assert DEFAULT_URL.startswith("http")

    def test_danbooru_tags_prompt_is_non_empty(self) -> None:
        assert isinstance(DANBOORU_TAGS, str)
        assert len(DANBOORU_TAGS) > 50

    def test_prompt_prompt_is_non_empty(self) -> None:
        assert isinstance(PROMPT, str)
        assert len(PROMPT) > 50

    def test_danbooru_tags_prompt_is_valid(self) -> None:
        # Just test it's a valid string since wording might change
        assert isinstance(DANBOORU_TAGS, str)

    def test_prompt_prompt_mentions_expression(self) -> None:
        assert "expression" in PROMPT.lower()
