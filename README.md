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

The **Ollama Image to Prompt** custom node is designed to run local Vision-Language Models (VLMs) like Qwen directly inside ComfyUI workflows. It generates highly detailed natural language prompts, extracts strict Danbooru-style tags, performs text-to-text keyword expansion, and creates motion storyboards for AI video generation.

It handles batch processing efficiently, allowing you to process large folders of images or video frames all at once.

---

## 🚀 Showcase Features

### 🔌 11 Dynamic Prompting Modes
Forget rigid captioning. This node ships with **11 highly-specialized, native-English prompting architectures** built to push VLMs to their theoretical limits:
- **`tags` / `detail_tags`**: Generates pure Danbooru hierarchy tags for anime models.
- **`natural_language` / `detail_natural_language`**: Deep pixel-level extraction of materials, lighting, and anatomical positioning for Flux/SD3.
- **`video_wan` / `video_dynamic`**: Translates static reference images into chronological physics-based motion instructions (e.g., fabric inertia, center of gravity shifts) for Wan/Sora.
- **`video_storyboard` / `video_reconstruction`**: Deconstructs scenes into formal directorial Shot: N sequences or tracks rigid motion for video-to-video transfers.
- **`image_edit_instructions`**: Analyzes the original image and outputs precise Qwen-Image-Edit replacement and semantic inpainting matrices.
- **`expand_natural_language` / `expand_portrait`**: Text-to-text expansion converting simple keywords into rich, domain-specific visual jargon. *(Just pass your simple keywords into the new `keywords` input field)*.

### 🛡️ Hardened Tag Engine & Slop Filter
VLMs love to talk ("Here are the tags for this image..."). This node implements a ruthless, heuristic-based sanitizer:
- Automatically strips conversational preambles and chat fragments.
- Intelligently removes numbered bullet markers (`1. `) without destroying critical character tags (like `1girl`, `2boys`).
- Enforces strict Danbooru-style lowercase extraction with case-insensitive deduplication.

### 🧠 Intelligent `<think>` Engine & Speed Toggle
Models like **Qwen3-VL** natively generate invisible `<think>` blocks to reason about spatial layout before generating standard tags.
If you need maximum reasoning capabilities (like accurate finger counting or specific physical interactions), leave `thinking_mode` **True**. The node captures the internal thought process and outputs it to the `thought_process` pin.
If you prioritize **Speed** and want the model to generate tags instantly without wasting time, toggle `thinking_mode` to **False**. The node will systematically inject a strict anti-thinking instruction to bypass the model's reasoning phase entirely and return results substantially faster.



## 📦 Installation

This node relies on [Ollama](https://ollama.com/) to perform the heavy lifting locally.

### 1. Set Up Ollama
1. Download and install Ollama from [ollama.com](https://ollama.com/).
2. Pull a vision-capable model. We highly recommend **Qwen3.5** (9B or 4B) for its exceptional early-fusion multimodal reasoning that outperforms previous generation VLMs.
   ```bash
   ollama pull qwen3.5:9b
   ollama pull qwen3.5:4b
   ```

### 2. Install the Custom Node
Navigate to your ComfyUI `custom_nodes` directory and clone the repository:

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/jluo-github/comfyui-ollama-image-to-prompt.git
cd comfyui-ollama-image-to-prompt
pip install -r requirements.txt
```

Restart ComfyUI.

---

## 💡 Usage Configuration

1. Search for the node **"Ollama Image to Prompt"**.
2. Connect an **IMAGE** input.
3. Configure the parameters below.

### Inputs / Outputs

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `image` | `IMAGE` | (Input) The source image(s) to be analyzed by the vision model. Supports batches. |
| `text` | `STRING` | (Output) The generated prompt (either natural language description or tags). |
| `thought_process` | `STRING` | (Output) The internal chain-of-thought extracted from the model (if applicable). |

### Node Settings

| Parameter | Default | Description |
| :--- | :--- | :--- |
| `ollama_url` | `http://localhost:11434` | The API endpoint for your Ollama instance. |
| `model` | `qwen3.5:9b` | Select the locally pulled VLM model. |
| `mode` | `natural_language` | Dynamically populated dropdown listing all 11 professional prompt presets. |
| `seed` | `0` | Lock the seed for deterministic outputs during prompt engineering. |
| `keep_alive` | `0` | Minutes to keep the model loaded in VRAM. Use `-1` for indefinite. |
| `thinking_mode` | `False` | Enable to parse and extract the model's internal reasoning from `<think>` tags into the `thought_process` output. |
| `custom_prompt` | *(Empty)* | Override the built-in system prompt. Leave empty to use the selected `mode` preset. |
| `keywords` | *(Empty)* | Add targeted keywords or extra instructions without overriding the selected mode's built-in system instructions. |

---

## 🤝 Contributing & License

Contributions, issues, and feature requests are welcome! 
Feel free to check the [issues page](https://github.com/jluo-github/comfyui-ollama-image-to-prompt/issues).

Distributed under the **MIT License**. See `LICENSE` for more information.

---

<div align="center">
    Made with ❤️ for the ComfyUI community
</div>