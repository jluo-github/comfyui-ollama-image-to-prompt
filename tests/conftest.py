from __future__ import annotations

import sys
from pathlib import Path

# Add the PARENT of the project root to sys.path so that the project directory
# itself acts as a package, enabling relative imports within nodes.py.
# e.g., sys.path gets "E:/my-apps" so "import comfyui_ollama_image_to_prompt" works.
#
# However, ComfyUI custom nodes use a directory name with hyphens which isn't
# a valid Python package name. So instead, we add the project root itself
# and patch nodes to use absolute imports at test time.

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
