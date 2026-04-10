<div align="center">
  <h1>✨ ComfyUI Ollama Image to Prompt</h1>
  <p><strong>A custom ComfyUI node built to hook up local Ollama vision models for generating actually good prompts, Danbooru tags, and video motion instructions.</strong></p>

  [![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
  [![Code Style: Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![Tests](https://github.com/jluo-github/comfyui-ollama-image-to-prompt/actions/workflows/tests.yml/badge.svg)](https://github.com/jluo-github/comfyui-ollama-image-to-prompt/actions)
</div>

---

## 🌟 Overview
The **Ollama Image to Prompt** custom node is designed to run local Vision-Language Models (VLMs) like Qwen directly inside ComfyUI workflows. It automates vision-to-prompt pipelines, extracting detailed natural language, Danbooru tags, and video motion instructions using 9 specialized prompting architectures.

![Ollama Image to Prompt Node](ollama-image-to-prompt-node.jpg)

## 📦 Setup
1. **Ollama**: [Download](https://ollama.com/) and pull a vision model (e.g., `qwen3.5:9b`).
2. **Install**:
   ```bash
   cd ComfyUI/custom_nodes/
   git clone https://github.com/jluo-github/comfyui-ollama-image-to-prompt.git
   cd comfyui-ollama-image-to-prompt
   pip install -r requirements.txt
   ```
3. Restart ComfyUI.

## 💡 Usage Configuration
Connect an **IMAGE** to the node and select a **mode**.

### Prompt Architectures
| Mode | Description |
| :--- | :--- |
| `natural_language` | Dense, highly-descriptive, pixel-level prose extraction. Optimized for Flux, Qwen, Z-Image, etc. |
| `danbooru_tags` | Pure subset of booru-style tags separated by commas. Optimized for NoobAI, Illustrious, etc. |
| `expand_prompt` | Takes short user keywords and intelligently up-samples them into rich full-sentence prompts (handles portraits/scenes). |
| `expand_tags` | Takes short user keywords and optimally expands them into dense, pixel-perfect Danbooru tags. |
| `image_edit` | Structured instruction prompts for image-to-image edit models (e.g., Qwen-Image-Edit). |
| `video_prompt` | Generates dynamic, cinematic physics-based instructions designed for Wan or consistent video tracking. |
| `video_storyboard` | Shot-by-shot directorial sequences. |
| `anima` | Unified merged output (tags + natural language) strictly tailored for the Anima diffusion model. |
| `json_extract` | Extreme-detail structured JSON extraction. |

### Settings
| Parameter | Default | Description |
| :--- | :--- | :--- |
| `ollama_url` | `http://localhost:11434` | Your local Ollama endpoint. |
| `model` | `qwen3.5:9b` | Local vision model name. |
| `mode` | `natural_language` | Select prompting architecture. |
| `seed` | `0` | Lock the seed for deterministic outputs during prompt engineering. |
| `keep_alive` | `0` | VRAM cache duration (in minutes, use `-1` for permanent). |
| `thinking_mode` | `False` (Disabled) | Toggles the native reasoning engine for supported models. Disabling skips the thinking phase (skips `<think>` generation) to radically speed up inference. |
| `custom_prompt` | (Empty) | Override the built-in system prompt. Leave empty to use the selected mode preset. |
| `keywords` | (Empty) | Append modifiers/instructions to the selected mode. |

### Outputs
- `text`: Generated prompt/tags.
- `thought_process`: (Optional) Latent reasoning trace natively extracted from thinking models (e.g., Qwen3.5, DeepSeek-R1).

---

<div align="center">
    Made with ❤️ for the ComfyUI community
</div>