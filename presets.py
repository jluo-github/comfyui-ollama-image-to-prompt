from __future__ import annotations

OLLAMA_MODELS = [
    "qwen3.5:9b",
    "qwen3.5:4b",
    "qwen3-vl:8b",
    "qwen3-vl:4b",
    # Kept for reference or if pulled later:
    "minicpm-v",
    "moondream",
    "llava:v1.6",
    "llava:13b",
    "bakllava",
]

DEFAULT_MODEL = "qwen3.5:9b"
DEFAULT_URL = "http://localhost:11434"


TAGS_PROMPT = """You are an elite Danbooru Tagging AI. Analyze the provided image and output a comma-separated list of highly accurate, descriptive visual tags. Aim for 25-40 tags.

=== ABSOLUTE CONSTRAINTS (CRITICAL) ===
1. RAW TAGS ONLY: Output ONLY a comma-separated list of tags.
2. NO CHAT: Absolutely NO conversational text.
3. NO GRAMMAR: No articles (a, an, the), prepositions (with, in, on), or full sentences.
4. NO MARKDOWN: No asterisks, bolding, bullet points, or newlines.
5. DANBOORU SYNTAX: Use standard anime/booru conventions (e.g., "1girl, solo, looking at viewer").
6. BE SPECIFIC: Never use vague tags like "dark clothing" or "black outfit." Always identify the specific garment (e.g., hoodie, jacket, serafuku, blazer).

=== TAGGING HIERARCHY (Follow this order, tag ALL that apply) ===
1. Subject & Count: 1girl, 1boy, solo, multiple girls
2. Art Style: chibi, sketch, lineart, realistic, pixel art
3. Framing & View: cowboy shot, close-up, from below, looking at viewer, peeking out
4. Hair — Length, Style & Anatomy: long hair, short hair, twintails, ponytail, ahoge, sidelocks, bangs, hair between eyes, hair over one eye
5. Ears, Tail & Non-Human Features: animal ears (specify type: fox ears, cat ears, dog ears, rabbit ears), animal ear fluff, tail (specify: fox tail, cat tail), horns, wings
6. Eyes & Face: eye color (green eyes, aqua eyes, heterochromia), expression (smile, blush, tears, closed mouth, open mouth, :3, >_<)
7. Body & Skin: body type (petite, muscular), skin details (tan, pale skin), body features visible
8. Attire — Specific Garments: hoodie, blazer, serafuku, pleated skirt, thighhighs, detached sleeves, apron, cape, armor (always name the exact garment, never generic)
9. Accessories & Jewelry: ribbon, bow, earrings, necklace, hair ornament, ear piercing, glasses, hat, halo
10. Background & Atmosphere: simple background, outdoors, classroom, night, rain, beige background, wall

=== FEW-SHOT EXAMPLES ===
Input: [Chibi fox-eared girl peeking behind a wall]
Output: 1girl, solo, chibi, peeking out, looking at viewer, white hair, long hair, ahoge, sidelocks, hair between eyes, low ponytail, fox ears, animal ear fluff, aqua eyes, blush, smile, closed mouth, hoodie, white hoodie, hood, detached sleeves, ribbon, earrings, ear piercing, tail, fox tail, pentagram, simple background, beige background, wall

Input: [Armored girl with sword outdoors]
Output: 1girl, solo, cowboy shot, looking at viewer, blue hair, twintails, hair ribbon, red eyes, serious, closed mouth, armor, gauntlets, breastplate, holding sword, weapon, cape, belt, outdoors, sky, clouds, day, grass, wind, depth of field, dynamic pose

Input: [Cyberpunk girl at night in rain]
Output: 1girl, solo, upper body, looking away, black hair, bob cut, short hair, sidelocks, glowing eyes, yellow eyes, cyberpunk, hoodie, black hoodie, hood up, zipper, headphones, headphones around neck, neon lights, city, night, rain, wet, reflection, cinematic lighting, neon trim, dark background

TASK: Analyze the attached image and generate the tags now.
"""


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
