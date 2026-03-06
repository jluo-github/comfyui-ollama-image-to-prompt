<div align="center">
  <h1>✨ ComfyUI Ollama Image to Prompt</h1>
  <p><strong>A powerful, fully-local ComfyUI node that leverages Ollama vision models to generate high-fidelity image prompts and Danbooru-style tags.</strong></p>

  [![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
  [![Code Style: Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![Tests](https://github.com/jluo-github/comfyui-ollama-image-to-prompt/actions/workflows/tests.yml/badge.svg)](https://github.com/jluo-github/comfyui-ollama-image-to-prompt/actions)
</div>

---

## 🌟 Overview

The **Ollama Image to Prompt** custom node brings the power of open-weight Vision-Language Models (VLMs) directly into your ComfyUI workflow. It connects to your local Ollama instance to analyze images and generate highly detailed prompts, making it perfect for image-to-image workflows, dataset curation, and creative exploration.

## 🚀 Key Features

*   🔒 **100% Local Privacy**: Runs entirely on your hardware via Ollama. No cloud dependencies.
*   ⚡ **Batch Processing Support**: Seamlessly processes batches of images, generating independent prompts for each frame.
*   🧠 **Dual Generation Modes**:
    *   `natural_language`: Crafts evocative, flowing, highly detailed descriptive paragraphs.
    *   `tags`: Generates precise, comma-separated Danbooru-style tags.
*   💭 **Chain-of-Thought Parsing**: Extracts the hidden `<think>` blocks from reasoning models (like `qwen3-vl`) to show you the model's internal logic.

## 📦 Installation

This node relies on [Ollama](https://ollama.com/) to perform the heavy lifting. 

### 1. Set Up Ollama
1. Download and install Ollama from [ollama.com](https://ollama.com/).
2. Pull a vision-capable model. We highly recommend **Qwen3-VL** for its exceptional spatial awareness.
   ```bash
   ollama pull qwen3-vl:8b
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

## 💡 Usage

1. Search for the node **"Ollama Image to Prompt"**.
2. Connect an **IMAGE** input.
3. Configure settings:
   - **ollama_url**: URL of your Ollama instance (default: `http://localhost:11434`).
   - **model**: Select the model you pulled (e.g., `qwen3-vl:8b`).
   - **mode**: Choose between `natural_language` or `tags`.
   - **thinking_mode**: Enable to extract internal chain-of-thought (if the model outputs `<think>` tags).
4. Connect the **text** output to a CLIP Text Encode node or similar.

### Inputs

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `image` | `IMAGE` | The source image(s) to be analyzed by the vision model. Supports batches. |

### Outputs

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `text` | `STRING` | The generated prompt (either natural language description or tags). |
| `thought_process` | `STRING` | The internal chain-of-thought extracted from the model (if applicable). |

### Configuration Node Parameters

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ollama_url` | Text | `http://localhost:11434` | The API endpoint for your Ollama instance. |
| `model` | Dropdown | `qwen3-vl:8b` | Select the locally pulled VLM model. |
| `mode` | Dropdown | `natural_language` | Choose between descriptive paragraphs or keyword `tags`. |
| `seed` | Integer | `0` | Lock the seed for deterministic outputs during prompt engineering. |
| `keep_alive` | Integer | `0` | Minutes to keep the model loaded in VRAM. Use `-1` for indefinite. |
| `thinking_mode` | Toggle | `False` | Enable to parse and extract the model's internal reasoning from `<think>` tags. |
| `enable_thinking` | Toggle | `True` | If set to `False`, completely skips generating reasoning logic by appending instructions to the prompt, drastically speeding up generation. |
| `custom_prompt` | Text | *(Empty)* | Override the built-in system prompt. Leave empty to use the standard mode prompts. |


## 🤝 Contributing & License

Contributions, issues, and feature requests are welcome! 
Feel free to check the [issues page](https://github.com/jluo-github/comfyui-ollama-image-to-prompt/issues).

Distributed under the **MIT License**. See `LICENSE` for more information.

---

Made with ❤️ for the ComfyUI community