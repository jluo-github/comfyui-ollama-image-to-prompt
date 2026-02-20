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
    "Analyze this image and extract a highly detailed, comma-separated list of Danbooru-style tags to exactly mimic its aesthetic, style, and content. "
    "Act as an expert AI image prompter for top-tier Civitai anime/illustration models. Be extremely exhaustive (60+ tags). "
    "Structure your tag generation by prioritizing these categories:\n"
    "1. QUALITY & META: Always include premium tags: masterpiece, best quality, very aesthetic, absurdres, highres. Include medium (anime artwork, official art, key visual, illustration).\n"
    "2. SUBJECT: Character count (1girl, solo, etc.), hair (color, length, style, ahoge, twin braids, etc.), eyes (color, intricate detailed eyes), skin, body type.\n"
    "3. EXPRESSION & FACE: Be hyper-specific. (e.g., looking at viewer, parted lips, blush, heavy eyeliner, detailed face, smug, crying, glowing eyes). Capture the exact emotion.\n"
    "4. POSE & CAMERA: Angle (dutch angle, from below, dynamic angle, extreme close-up, cowboy shot). Pose (dynamic pose, contrapposto, reaching towards viewer, foreshortening, floating, sitting). Hand gestures (v sign, hands on hips, adjusting hair).\n"
    "5. ATTIRE: Specific clothing (pleated skirt, mechanical armor, thighhighs), fabric texture (latex, wet clothes, translucent, metallic), details (frills, lace, belts, intricate clothing).\n"
    "6. ENVIRONMENT: Setting (detailed background, cityscape, ruined ruins, outdoors, starry sky), props (holding sword, floating petals, chains).\n"
    "7. ATMOSPHERE & LIGHTING: cinematic lighting, dramatic lighting, volumetric lighting, rim lighting, depth of field (dof), chromatic aberration, light particles, dust, god rays, bloom.\n"
    "8. ART STYLE: Mimic the specific vibe and skill (intricate details, thick lines, pastel colors, retro artstyle, cel shading, impasto, masterpiece shading).\n"
    "CRITICAL RULE: Output ONLY a single, continuous comma-separated string of tags. Do NOT use markdown formatting, bullet points, numbering, or conversational text. NO intro, NO outro."
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
