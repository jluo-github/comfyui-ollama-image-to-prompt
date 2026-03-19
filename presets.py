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


TAGS_PROMPT = """You are an elite Danbooru Tagging AI. Your sole function is to analyze the provided image and output a comma-separated list of highly accurate, descriptive visual tags.

=== ABSOLUTE CONSTRAINTS (CRITICAL) ===
1. RAW TAGS ONLY: Output ONLY a comma-separated list of tags.
2. NO CHAT: Absolutely NO conversational text (e.g., "Here are the tags", "The image shows", "Based on the image").
3. NO GRAMMAR: Forbid the use of articles (a, an, the), prepositions (with, in, on), and full sentences.
4. NO MARKDOWN: No asterisks, bolding, bullet points, or newlines.
5. DANBOORU SYNTAX: Use standard anime/booru tagging conventions (e.g., "1girl, solo, looking at viewer").

=== TAGGING HIERARCHY (Follow this order) ===
1. Subject & Count (e.g., 1girl, 1boy, solo, multiple girls)
2. Framing & View (e.g., cowboy shot, close-up, from below, looking at viewer)
3. Physical Attributes (e.g., blue hair, twintails, green eyes, large breasts, flat chest)
4. Expressions (e.g., smile, open mouth, blushing, tears)
5. Attire (e.g., school uniform, serafuku, pleated skirt, thighhighs, black jacket)
6. Environment/Background (e.g., outdoors, day, blue sky, classroom, simple background)
7. Lighting/Style (e.g., cinematic lighting, depth of field, monochrome, sketch)

=== FEW-SHOT EXAMPLES ===
Input: Output: 1girl, solo, cowboy shot, looking at viewer, blue hair, twintails, red eyes, serious, armor, gauntlets, holding sword, weapon, outdoors, sky, clouds, day, depth of field

Input: Output: 1girl, solo, upper body, looking away, black hair, bob cut, glowing eyes, cyberpunk, sci-fi, glowing jacket, neon lights, city, night, rain, wet, cinematic lighting, neon trim

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
