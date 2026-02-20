# ComfyUI Ollama Image to Prompt

A custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that leverages local [Ollama](https://ollama.com/) vision models to generate detailed prompts or Danbooru-style tags from images.

## Features

- **Local Inference**: Runs entirely locally using Ollama.
- **Batch Processing**: Supports batch processing of images (one prompt per image).
- **Dual Modes**:
  - `natural_language`: Generates detailed descriptive prompts.
  - `tags`: Generates Danbooru-style tags (useful for training or tag-based models).
- **Thinking Process**: Captures "thought process" from reasoning models like qwen3-vl (if available/supported by the model artifact).
- **Custom Prompts**: Full control over the system prompt if needed.

## Installation

1. **Install Ollama**: Download and install from [ollama.com](https://ollama.com/).
2. **Pull a Vision Model**:
   ```bash
   ollama pull qwen3-vl:8b
   ```
3. **Clone this Repository**:
   Navigate to your ComfyUI `custom_nodes` directory:
   ```bash
   cd ComfyUI/custom_nodes/
   git clone https://github.com/jluo-github/comfyui-ollama-image-to-prompt.git
   ```
4. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Search for the node **"Ollama Image to Prompt"**.
2. Connect an **IMAGE** input.
3. Configure settings:
   - **ollama_url**: URL of your Ollama instance (default: `http://localhost:11434`).
   - **model**: Select the model you pulled (e.g., `qwen3-vl:8b`).
   - **mode**: Choose between `natural_language` or `tags`.
   - **thinking_mode**: Enable to extract internal chain-of-thought (if the model outputs `<think>` tags).
4. Connect the **text** output to a CLIP Text Encode node or similar.

## Inputs

| Input | Type | Description |
| :--- | :--- | :--- |
| **image** | IMAGE | The input image(s) to analyze. |
| **ollama_url** | STRING | The API endpoint for Ollama. Default: `http://localhost:11434` |
| **model** | LIST | The vision model to use (e.g., `qwen3-vl:8b`). |
| **mode** | LIST | `natural_language` (descriptive) or `tags` (keyword list). |
| **seed** | INT | Seed for deterministic generation. |
| **keep_alive** | INT | How long to keep the model loaded in memory (in minutes). |
| **thinking_mode** | BOOLEAN | If true, enables parsing of `<think>` tags. |
| **custom_prompt** | STRING | (Optional) Override the default prompts with your own. |

## Outputs

- **text**: The generated description or tags.
- **thought_process**: The internal reasoning chain text (if `thinking_mode` is enabled and supported by the model).

## Supported Models (Examples)

This node is pre-configured with several models in `presets.py`, but you can use any vision-capable model supported by Ollama.

- `qwen3-vl:8b` (Recommended)
- `qwen3-vl:4b`
- `llava:v1.6`
- `moondream`
- `minicpm-v`
