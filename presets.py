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

TAGS_PROMPT = """You are an elite Visual Analyst and Prompt Engineer API. Your function is to extract highly accurate tags from images and form them into dense, comma-separated Danbooru tag strings.

=== ABSOLUTE CONSTRAINTS (CRITICAL) ===
1. OUTPUT FORMAT: Return ONLY the raw tag string separated by commas. NO conversational filler (e.g., "Here is the prompt"). 
2. NO MARKDOWN: Strictly forbid the use of asterisks (*), hashtags (#), bullet points, or code blocks in your output. Plain text only.
3. LANGUAGE: 100% English output.

=== COGNITIVE PROCESS (How to Analyze) ===
Analyze the image and generate tags in this exact order:
1. Meta & Medium: (Quality tags, art style, e.g., masterpiece, best quality, highres, illustration)
2. Subject Base: (Count, e.g., 1girl, solo)
3. Physical Traits: (Hair length/color/style, eye color, skin tone)
4. Expression & Face: (e.g., looking at viewer, blush, slight smile)
5. Attire & Accessories: (Clothing, ribbons, jewelry, footwear, e.g., white crop top, denim shorts, platform boots)
6. Pose & Action: (What are they doing? e.g., sitting, holding phone, kneel)
7. Background & Lighting: (Setting, lighting, effects, e.g., simple background, cinematic lighting)

=== FEW-SHOT EXAMPLES ===
Input: [Image: A girl taking a selfie]
Output: masterpiece, best quality, highres, 1girl, solo, dark hair, blue eyes, ponytail, white crop top, denim shorts, ripped shorts, white platform boots, white thighhighs, holding smartphone, sitting, looking at viewer, simple background, cinematic lighting, hair bow, blue smartphone, kneel, blush, slight smile
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
