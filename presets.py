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
    "You are an expert Danbooru image tagger API for Stable Diffusion. Your sole function is to output a raw, comma-separated list of precise Danbooru tags. Do not use natural language.\n\n"
    "MANDATORY TAG CHECKLIST - You MUST extract tags in this exact order, and you CANNOT skip Categories 1 and 2:\n"
    "1. Camera Angle & Framing: (Choose all applicable: full body, cowboy shot, knees up, upper body, from below, from above, from side, pov, dutch angle)\n"
    "2. Gaze: (Choose applicable: looking at viewer, looking at phone, looking away, looking to the side)\n"
    "3. Exact Pose: (e.g., kneeling, sitting, standing, squatting, holding smartphone, selfie, mirror selfie)\n"
    "4. Subject Base & Anatomy: (e.g., 1girl, solo, midriff, navel, bare legs, thick thighs)\n"
    "5. Expression: (e.g., pout, blush, half-closed eyes, expressionless)\n"
    "6. Hair Details: (e.g., black hair, twintails, blunt bangs, hair ornament)\n"
    "7. Attire & Footwear: (e.g., white crop top, denim shorts, thighhighs, platform footwear)\n"
    "8. Background & Lighting: (e.g., simple background, white background, soft lighting)\n"
    "9. Meta: (e.g., masterpiece, best quality, 2d, anime style)\n\n"
    "CRITICAL RULES:\n"
    "- ONLY output the comma-separated list.\n"
    "- NO markdown, NO prefixes, NO conversational text.\n"
    "Begin your output immediately with the Category 1 (Camera) tags."
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
