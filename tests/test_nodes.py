from __future__ import annotations

from unittest.mock import MagicMock, patch

import torch

from nodes import OllamaImageToPrompt


class TestInputTypes:
    def test_has_required_keys(self) -> None:
        input_types = OllamaImageToPrompt.INPUT_TYPES()
        assert "required" in input_types
        assert "optional" in input_types

    def test_optional_has_image(self) -> None:
        optional = OllamaImageToPrompt.INPUT_TYPES()["optional"]
        assert "image" in optional

    def test_required_has_model(self) -> None:
        required = OllamaImageToPrompt.INPUT_TYPES()["required"]
        assert "model" in required

    def test_optional_has_custom_prompt(self) -> None:
        optional = OllamaImageToPrompt.INPUT_TYPES()["optional"]
        assert "custom_prompt" in optional

    def test_optional_has_keywords(self) -> None:
        optional = OllamaImageToPrompt.INPUT_TYPES()["optional"]
        assert "keywords" in optional


class TestNodeAttributes:
    def test_return_types(self) -> None:
        assert OllamaImageToPrompt.RETURN_TYPES == ("STRING", "STRING")

    def test_output_is_list(self) -> None:
        assert OllamaImageToPrompt.OUTPUT_IS_LIST == (True, True)

    def test_function_name(self) -> None:
        assert OllamaImageToPrompt.FUNCTION == "generate_prompt"


class TestPromptSelection:
    """Tests that the correct prompt is chosen based on mode."""

    def _make_batch(self, batch_size: int = 1) -> torch.Tensor:
        return torch.rand(batch_size, 4, 4, 3)

    @patch("core.api.requests.post")
    def test_natural_language_mode(self, mock_post: MagicMock) -> None:
        mock_response = MagicMock()
        mock_response.json.return_value = {"response": "A beautiful scene."}
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        node = OllamaImageToPrompt()
        texts, thoughts = node.generate_prompt(
            image=self._make_batch(),
            ollama_url="http://localhost:11434",
            model="qwen3-vl:8b",
            mode="prompt",
            seed=42,
            keep_alive=5,
            thinking_mode=False,
        )

        assert len(texts) == 1
        assert texts[0] == "A beautiful scene. BREAK "
        call_args = mock_post.call_args[1]["json"]
        assert "CRITICAL: Do NOT output any thinking process." in call_args["prompt"]

    @patch("core.api.requests.post")
    def test_tags_mode_cleans_output(self, mock_post: MagicMock) -> None:
        mock_response = MagicMock()
        mock_response.json.return_value = {"response": "- tag1\n- tag2\n- tag3"}
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        node = OllamaImageToPrompt()
        texts, _ = node.generate_prompt(
            image=self._make_batch(),
            ollama_url="http://localhost:11434",
            model="qwen3-vl:8b",
            mode="danbooru_tags",
            seed=42,
            keep_alive=5,
            thinking_mode=False,
        )

        assert "tag1" in texts[0]
        assert "\n" not in texts[0]
        assert texts[0].endswith(" BREAK ")

    @patch("core.api.requests.post")
    def test_custom_prompt_overrides_mode(self, mock_post: MagicMock) -> None:
        mock_response = MagicMock()
        mock_response.json.return_value = {"response": "custom output"}
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        node = OllamaImageToPrompt()
        texts, _ = node.generate_prompt(
            image=self._make_batch(),
            ollama_url="http://localhost:11434",
            model="qwen3-vl:8b",
            mode="danbooru_tags",
            seed=0,
            keep_alive=5,
            thinking_mode=False,
            custom_prompt="My custom instruction",
        )

        # With custom_prompt, tags cleanup should NOT run
        assert texts[0] == "custom output BREAK "

    @patch("core.api.requests.post")
    def test_keywords_appended_to_prompt(self, mock_post: MagicMock) -> None:
        mock_response = MagicMock()
        mock_response.json.return_value = {"response": "expanded output"}
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        node = OllamaImageToPrompt()
        texts, _ = node.generate_prompt(
            image=self._make_batch(),
            ollama_url="http://localhost:11434",
            model="qwen3-vl:8b",
            mode="prompt",
            seed=0,
            keep_alive=5,
            thinking_mode=False,
            keywords="1girl, neon",
        )

        assert texts[0] == "expanded output BREAK "
        # Verify the prompt sent to the API contains both instruction AND keywords
        call_args = mock_post.call_args[1]["json"]
        assert "User Keywords / Instructions:" in call_args["prompt"]
        assert "1girl, neon" in call_args["prompt"]
        assert "professional AI Visual Prompt Engineer" in call_args["prompt"]


class TestThinkTagParsing:
    def _make_batch(self) -> torch.Tensor:
        return torch.rand(1, 4, 4, 3)

    @patch("core.api.requests.post")
    def test_think_tags_extracted_when_enabled(self, mock_post: MagicMock) -> None:
        mock_response = MagicMock()
        mock_response.json.return_value = {"response": "<think>I need to analyze this.</think>A girl with blue hair."}
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        node = OllamaImageToPrompt()
        texts, thoughts = node.generate_prompt(
            image=self._make_batch(),
            ollama_url="http://localhost:11434",
            model="qwen3-vl:8b",
            mode="prompt",
            seed=0,
            keep_alive=5,
            thinking_mode=True,
        )

        assert texts[0] == "A girl with blue hair. BREAK "
        assert thoughts[0] == "I need to analyze this."
        call_args = mock_post.call_args[1]["json"]
        assert "CRITICAL: Do NOT output any thinking process." not in call_args["prompt"]

    @patch("core.api.requests.post")
    def test_think_tags_stripped_when_disabled(self, mock_post: MagicMock) -> None:
        mock_response = MagicMock()
        mock_response.json.return_value = {"response": "<think>Hidden thought.</think>Main output."}
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        node = OllamaImageToPrompt()
        texts, thoughts = node.generate_prompt(
            image=self._make_batch(),
            ollama_url="http://localhost:11434",
            model="qwen3-vl:8b",
            mode="prompt",
            seed=0,
            keep_alive=5,
            thinking_mode=False,
        )

        assert texts[0] == "Main output. BREAK "
        assert thoughts[0] == ""


class TestBatchProcessing:
    @patch("core.api.requests.post")
    def test_processes_multiple_images(self, mock_post: MagicMock) -> None:
        mock_response = MagicMock()
        mock_response.json.return_value = {"response": "Description."}
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        node = OllamaImageToPrompt()
        batch = torch.rand(3, 4, 4, 3)  # 3 images
        texts, thoughts = node.generate_prompt(
            image=batch,
            ollama_url="http://localhost:11434",
            model="qwen3-vl:8b",
            mode="prompt",
            seed=0,
            keep_alive=5,
            thinking_mode=False,
        )

        assert len(texts) == 3
        assert len(thoughts) == 3
        assert mock_post.call_count == 3
