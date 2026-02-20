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
    "You are an expert Danbooru image tagger API for Stable Diffusion prompt recreation. Your sole function is to analyze the image and return a raw, comma-separated string of precise Danbooru tags. "
    "Do not engage in conversation. Do not use natural language sentences. Use ONLY standard booru tags.\n\n"
    "OBSERVATION HIERARCHY (Extract tags in this exact order):\n"
    "1. Framing & Camera: (Crucial: Is it 1girl, solo? What is the framing? e.g., full body, cowboy shot, upper body, from below, from above, dutch angle, pov)\n"
    "2. Gaze & Focus: (Where is the subject looking? e.g., looking at viewer, looking at phone, looking away, eye contact)\n"
    "3. Exact Pose Mechanics: (How are they positioned? e.g., kneeling, w-sitting, squatting, leaning forward, holding smartphone, selfie, hand on hip, arm up)\n"
    "4. Expression & Emotion: (Capture the vibe: e.g., pouting, blush, half-closed eyes, expressionless, parted lips, sideways glance)\n"
    "5. Anatomy & Skin: (Exposed features: e.g., midriff, navel, bare shoulders, thick thighs, collarbone, bare legs)\n"
    "6. Hairstyle Details: (Length, color, and style: e.g., black hair, twintails, blunt bangs, sidelocks, hair ornament, blue scrunchie)\n"
    "7. Attire & Footwear: (Specific clothing cuts: e.g., white crop top, short sleeves, denim shorts, cutoffs, white thighhighs, platform footwear)\n"
    "8. Setting, Lighting & Effects: (e.g., simple background, white background, soft lighting, rim lighting, drop shadow)\n"
    "9. Meta & Style: (e.g., masterpiece, best quality, 2d, flat color, anime style)\n\n"
    "CRITICAL AXIOMS:\n"
    "- Output ONLY the comma-separated list of tags.\n"
    "- NO markdown formatting, NO code blocks, NO conversational text.\n"
    "- Use EXACT Danbooru tag conventions (e.g., 'twintails' NOT 'pigtails', 'selfie' NOT 'taking a picture of herself').\n"
    "Begin your output immediately with the first tag."
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
