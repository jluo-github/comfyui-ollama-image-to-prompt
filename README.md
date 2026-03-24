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
The **Ollama Image to Prompt** custom node is designed to run local Vision-Language Models (VLMs) like Qwen directly inside ComfyUI workflows. It automates vision-to-prompt pipelines, extracting detailed natural language, Danbooru tags, and video motion instructions using 11 specialized prompting architectures.

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
| `tags` / `detail_tags` | Structured Danbooru hierarchy for anime models (e.g., Illustrious). |
| `natural_language` / `detail_natural_language` | Pixel-level extraction optimized for Flux, Qwen, Z-Image, and modern Transformers. |
| `video_wan` / `video_dynamic` | Direct motion physics for SOTA video models (e.g., Wan2.2). |
| `video_storyboard` / `video_reconstruction` | Shot-by-shot directorial sequences and rigid motion tracking. |
| `image_edit_instructions` | Precise modification instructions for Qwen-Image-Edit. |
| `expand_natural_language` / `expand_portrait` | Text-to-text keyword expansion engine. |

### Settings
| Parameter | Default | Description |
| :--- | :--- | :--- |
| `ollama_url` | `http://localhost:11434` | Your local Ollama endpoint. |
| `model` | `qwen3.5:9b` | Local vision model name. |
| `mode` | `natural_language` | Select prompting architecture. |
| `seed` | `0` | Lock the seed for deterministic outputs during prompt engineering. |
| `keep_alive` | `0` | VRAM cache duration (in minutes, use `-1` for permanent). |
| `thinking_mode` | `False` (Disabled) | **Enable** = Enable thinking. **Disable** = Disable thinking. Disabling speeds up generation by skipping reasoning tokens. |
| `custom_prompt` | (Empty) | Override the built-in system prompt. Leave empty to use the selected mode preset. |
| `keywords` | (Empty) | Append modifiers/instructions to the selected mode. |

### Outputs
- `text`: Generated prompt/tags.
- `thought_process`: (Optional) Latent reasoning from `<think>` models.

---

<div align="center">
    Made with ❤️ for the ComfyUI community
</div>