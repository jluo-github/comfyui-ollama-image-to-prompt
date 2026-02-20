try:
    from .nodes import OllamaImageToPrompt
except ImportError:
    from nodes import OllamaImageToPrompt

NODE_CLASS_MAPPINGS = {"OllamaImageToPrompt": OllamaImageToPrompt}

NODE_DISPLAY_NAME_MAPPINGS = {"OllamaImageToPrompt": "Ollama Image to Prompt"}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
