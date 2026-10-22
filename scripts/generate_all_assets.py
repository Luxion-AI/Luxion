import os, glob
import xml.etree.ElementTree as ET

assets_dir = "/home/luxion/Projects/Luxion-AI/assets/readme"

# 2. Pixel Divider SVG
pixel_divider_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 36" width="100%" height="36" shape-rendering="crispEdges">
  <defs>
    <linearGradient id="divGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffb7d5" stop-opacity="0"/>
      <stop offset="15%" stop-color="#ffb7d5" stop-opacity="0.8"/>
      <stop offset="35%" stop-color="#dcc6ff" stop-opacity="1"/>
      <stop offset="50%" stop-color="#bde0fe" stop-opacity="1"/>
      <stop offset="65%" stop-color="#dcc6ff" stop-opacity="1"/>
      <stop offset="85%" stop-color="#ffb7d5" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#ffb7d5" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <!-- Center Heart and Stars -->
  <g transform="translate(400, 18)">
    <!-- Center Pixel Heart -->
    <g fill="#ff70a6" transform="translate(-10, -8)">
      <rect x="2" y="0" width="6" height="3"/>
      <rect x="12" y="0" width="6" height="3"/>
      <rect x="0" y="3" width="10" height="4"/>
      <rect x="10" y="3" width="10" height="4"/>
      <rect x="0" y="7" width="20" height="3"/>
      <rect x="2" y="10" width="16" height="3"/>
      <rect x="5" y="13" width="10" height="3"/>
      <rect x="8" y="16" width="4" height="2"/>
    </g>

    <!-- Flanking Stars Left -->
    <g fill="#fde047" transform="translate(-40, -5)">
      <rect x="4" y="0" width="2" height="10"/>
      <rect x="0" y="4" width="10" height="2"/>
      <rect x="3" y="3" width="4" height="4"/>
    </g>
    <g fill="#bde0fe" transform="translate(-75, -4)">
      <rect x="3" y="0" width="2" height="8"/>
      <rect x="0" y="3" width="8" height="2"/>
      <rect x="2" y="2" width="4" height="4"/>
    </g>

    <!-- Flanking Stars Right -->
    <g fill="#fde047" transform="translate(30, -5)">
      <rect x="4" y="0" width="2" height="10"/>
      <rect x="0" y="4" width="10" height="2"/>
      <rect x="3" y="3" width="4" height="4"/>
    </g>
    <g fill="#bde0fe" transform="translate(67, -4)">
      <rect x="3" y="0" width="2" height="8"/>
      <rect x="0" y="3" width="8" height="2"/>
      <rect x="2" y="2" width="4" height="4"/>
    </g>

    <!-- Pixel Dots -->
    <rect x="-105" y="-2" width="4" height="4" fill="#ffc6ff"/>
    <rect x="-125" y="-1" width="3" height="3" fill="#ffd1dc"/>
    <rect x="101" y="-2" width="4" height="4" fill="#ffc6ff"/>
    <rect x="122" y="-1" width="3" height="3" fill="#ffd1dc"/>
  </g>

  <!-- Left Horizontal Dotted Pixel Bar -->
  <line x1="40" y1="18" x2="250" y2="18" stroke="url(#divGrad)" stroke-width="2" stroke-dasharray="6,4"/>
  <!-- Right Horizontal Dotted Pixel Bar -->
  <line x1="550" y1="18" x2="760" y2="18" stroke="url(#divGrad)" stroke-width="2" stroke-dasharray="6,4"/>
</svg>
'''

with open(os.path.join(assets_dir, "pixel-divider.svg"), "w") as f:
    f.write(pixel_divider_svg)

# 3. Section Headers Function (Escaping & as &amp;)
def make_section_header(title, subtitle, icon_type, badge_color="#ff70a6"):
    # escape ampersands for XML
    safe_title = title.replace("&", "&amp;")
    safe_subtitle = subtitle.replace("&", "&amp;")
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 68" width="100%" height="68">
  <defs>
    <linearGradient id="secGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#2a1842"/>
      <stop offset="50%" stop-color="#3b225c"/>
      <stop offset="100%" stop-color="#2a1842"/>
    </linearGradient>
    <linearGradient id="txtGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffb7d5"/>
      <stop offset="50%" stop-color="#dcc6ff"/>
      <stop offset="100%" stop-color="#bde0fe"/>
    </linearGradient>
  </defs>

  <style>
    .sec-title {{ font-family: 'Press Start 2P', 'Courier New', monospace; font-size: 15px; font-weight: bold; letter-spacing: 2px; }}
    .sec-sub {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Quicksand', sans-serif; font-size: 12px; font-weight: 500; }}
  </style>

  <!-- Container Box -->
  <rect x="4" y="4" width="792" height="60" rx="10" fill="url(#secGrad)" stroke="#ffb7d5" stroke-width="1.8"/>
  <rect x="7" y="7" width="786" height="54" rx="7" fill="none" stroke="#dcc6ff" stroke-width="1" stroke-dasharray="4,4" opacity="0.6"/>

  <!-- Pixel Icon Box Left -->
  <rect x="20" y="16" width="36" height="36" rx="6" fill="#1b102b" stroke="{badge_color}" stroke-width="1.5"/>
  <text x="38" y="40" font-size="20" text-anchor="middle">{icon_type}</text>

  <!-- Title & Subtitle -->
  <text x="72" y="34" fill="url(#txtGrad)" class="sec-title">{safe_title}</text>
  <text x="73" y="52" fill="#c4b5fd" class="sec-sub">{safe_subtitle}</text>

  <!-- Right Pixel Tag -->
  <g transform="translate(650, 22)">
    <rect x="0" y="0" width="125" height="24" rx="5" fill="#1b102b" stroke="#bae6fd" stroke-width="1.2"/>
    <circle cx="14" cy="12" r="3" fill="#38bdf8"/>
    <text x="68" y="16" fill="#bae6fd" font-family="'Courier New', monospace" font-size="10" font-weight="bold" text-anchor="middle">QUEST ACTIVE</text>
  </g>
</svg>
'''

sections = [
    ("section-about.svg", "01 // CHARACTER PROFILE", "Stats, origin, and companion", "🎀"),
    ("section-skills.svg", "02 // RPG SKILL TREE", "Frontend, backend, systems & AI abilities", "⚡"),
    ("section-quests.svg", "03 // QUEST BOARD & BUILDS", "Verified projects & software artifacts", "⚔️"),
    ("section-workstation.svg", "04 // BATTLESTATION ARCHITECTURE", "Linux, hardware, and runtime environment", "🖥️"),
    ("section-garden.svg", "05 // GITHUB DATA GARDEN", "Contributions, metrics & telemetry", "🌷"),
    ("section-philosophy.svg", "06 // CODING PHILOSOPHY", "Guiding engineering principles & tenets", "📜"),
    ("section-contact.svg", "07 // TAVERN & CONTACT", "Connect, collaborate, or say hello", "💌"),
]

for filename, title, subtitle, icon in sections:
    with open(os.path.join(assets_dir, filename), "w") as f:
        f.write(make_section_header(title, subtitle, icon))

print("Regenerated all section headers with XML-safe escaping.")
