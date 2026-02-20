from __future__ import annotations

OLLAMA_MODELS = [
    "qwen3-vl:8b",
    "qwen3-vl:4b",
    # Kept for reference or if pulled later:
    "minicpm-v",
    "moondream",
    "llava:v1.6",
    "llava:13b",
    "bakllava",
]

DEFAULT_MODEL = "qwen3-vl:8b"
DEFAULT_URL = "http://localhost:11434"

TAGS_PROMPT = (
    "Extract a comma-separated list of Danbooru tags describing this image.\n"
    "CRITICAL AXIOMS:\n"
    "1. Format: comma-separated list ONLY. No sentences, no grammar, no structure.\n"
    "2. NO markdown (`**`), NO prefixes (`Prompt:`), NO suffixes (`Enjoy!`, 🎨✨).\n\n"
    "Categories to tag:\n"
    "- Meta: masterpiece, best quality, highres\n"
    "- Subject: 1girl, solo, dark hair, blue eyes, ponytail\n"
    "- Clothing: crop top, shorts, boots, thighhighs\n"
    "- Pose: holding smartphone, sitting, looking at viewer\n"
    "- Setting & Lighting: simple background, cinematic lighting\n\n"
    "OUTPUT FORMAT: tag1, tag2, tag3, ..., tag40\n"
    "Begin output immediately with the first tag."
)

NATURAL_LANGUAGE_PROMPT = (
    "Analyze this image and write a highly detailed, evocative natural language prompt designed to perfectly recreate it using an AI image generator (like Flux, Midjourney, or SD3). "
    "Write in flowing, descriptive prose without conversational filler. Focus intensely on the following elements:\n"
    "1. **Subject & Pose**: Describe the subject(s) with extreme precision. Detail their exact physical appearance, hair styling, eye color, and clothing (including fabric types like silk, worn denim, or glossy latex). "
    "Crucially, describe their exact **Pose** (e.g., leaning against a wall, contrapposto, reaching out) and **Expression** (e.g., a melancholic gaze, a vibrant smirk, heavy eyelids). Capture the emotional weight.\n"
    "2. **Camera & Framing**: Define the shot type (e.g., extreme close-up, medium cowboy shot, wide establishing shot, dutch angle, shot from below). Describe the depth of field (shallow focus, bokeh) and perspective.\n"
    "3. **Environment & Context**: What surrounds the subject? Detail the background elements, props, architecture, or nature. Ground the subject in a specific setting.\n"
    "4. **Lighting & Atmosphere**: This is critical for the vibe. Is the lighting cinematic, harsh neon, soft volumetric god rays, or dramatic chiaroscuro? Describe the shadows, the time of day, and the overall mood (e.g., eerie, ethereal, cyberpunk, serene).\n"
    "5. **Artistic Style & Medium**: Define the exact aesthetic. Is it a 90s retro anime screencap, a hyper-realistic photograph on 35mm film, an oil painting with thick impasto brushstrokes, or a clean digital illustration with cel shading? "
    "Describe the color grading (e.g., pastel, desaturated, vibrant neon, sepia).\n"
    "CRITICAL RULE: Output a cohesive, highly descriptive paragraph (or series of short descriptive paragraphs). Do not use bullet points or numbered lists in your final output. Begin directly with the description."
)
