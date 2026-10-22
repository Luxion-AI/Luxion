import os

assets_dir = "/home/luxion/Projects/Luxion-AI/assets/readme"

# 1. Title Header SVG
title_header_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 210" width="100%" height="210">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e142e"/>
      <stop offset="50%" stop-color="#281a3e"/>
      <stop offset="100%" stop-color="#1a1228"/>
    </linearGradient>
    <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffb3d9"/>
      <stop offset="35%" stop-color="#d8b4fe"/>
      <stop offset="70%" stop-color="#bae6fd"/>
      <stop offset="100%" stop-color="#fed7aa"/>
    </linearGradient>
    <linearGradient id="textGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff99cc"/>
      <stop offset="40%" stop-color="#fbcfe8"/>
      <stop offset="75%" stop-color="#bae6fd"/>
      <stop offset="100%" stop-color="#f5d0fe"/>
    </linearGradient>
    <filter id="pixelGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <style>
    .font-pixel { font-family: 'Courier New', 'Consolas', monospace; font-weight: bold; }
    .font-cute { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Quicksand', sans-serif; font-weight: 600; }
    .pixel-text { font-family: 'Press Start 2P', 'Courier New', monospace; font-weight: 900; letter-spacing: 5px; }
  </style>

  <!-- Outer Window Shadow -->
  <rect x="14" y="14" width="872" height="186" rx="14" fill="#0c0714" opacity="0.6"/>

  <!-- Main Window Frame -->
  <rect x="10" y="10" width="872" height="186" rx="14" fill="url(#bgGrad)" stroke="#ffb3d9" stroke-width="2.5"/>
  <rect x="14" y="14" width="864" height="178" rx="10" fill="none" stroke="#d8b4fe" stroke-width="1" stroke-dasharray="4,4" opacity="0.6"/>

  <!-- Window Header Bar -->
  <path d="M 10 24 C 10 16 16 10 24 10 L 868 10 C 876 10 882 16 882 24 L 882 46 L 10 46 Z" fill="#2b1a45"/>
  <line x1="10" y1="46" x2="882" y2="46" stroke="#ffb3d9" stroke-width="1.5"/>

  <!-- Window Dots / Buttons -->
  <rect x="26" y="22" width="12" height="12" rx="3" fill="#ff70a6" stroke="#ffffff" stroke-width="1"/>
  <rect x="46" y="22" width="12" height="12" rx="3" fill="#ffd166" stroke="#ffffff" stroke-width="1"/>
  <rect x="66" y="22" width="12" height="12" rx="3" fill="#06d6a0" stroke="#ffffff" stroke-width="1"/>

  <!-- Window Title -->
  <text x="96" y="32" fill="#fbcfe8" class="font-pixel" font-size="12" font-weight="bold">LUXION_OS_v3.8 :: ~/universe/profile</text>

  <!-- Window Top Right Badges -->
  <g transform="translate(680, 20)">
    <rect x="0" y="0" width="85" height="16" rx="4" fill="#ff70a6" opacity="0.25" stroke="#ff70a6" stroke-width="1"/>
    <text x="42" y="12" fill="#fbcfe8" class="font-pixel" font-size="10" text-anchor="middle">LVL.99</text>

    <rect x="95" y="0" width="95" height="16" rx="4" fill="#06d6a0" opacity="0.25" stroke="#06d6a0" stroke-width="1"/>
    <circle cx="106" cy="8" r="3" fill="#06d6a0"/>
    <text x="148" y="12" fill="#a7f3d0" class="font-pixel" font-size="10" text-anchor="middle">ONLINE</text>
  </g>

  <!-- Decorative Sparkles Left -->
  <g fill="#ffc6ff" opacity="0.8">
    <path d="M 45 90 L 50 100 L 60 105 L 50 110 L 45 120 L 40 110 L 30 105 L 40 100 Z"/>
    <circle cx="80" cy="80" r="3" fill="#bae6fd"/>
    <circle cx="65" cy="140" r="2" fill="#ffd7aa"/>
    <path d="M 85 130 L 88 135 L 93 138 L 88 141 L 85 146 L 82 141 L 77 138 L 82 135 Z" fill="#fbcfe8"/>
  </g>

  <!-- Decorative Sparkles Right -->
  <g fill="#bae6fd" opacity="0.8">
    <path d="M 845 90 L 850 100 L 860 105 L 850 110 L 845 120 L 840 110 L 830 105 L 840 100 Z"/>
    <circle cx="810" cy="80" r="3" fill="#ffc6ff"/>
    <circle cx="825" cy="140" r="2" fill="#ffd7aa"/>
    <path d="M 805 130 L 808 135 L 813 138 L 808 141 L 805 146 L 802 141 L 797 138 L 802 135 Z" fill="#fbcfe8"/>
  </g>

  <!-- Main Hero Title -->
  <g filter="url(#pixelGlow)">
    <!-- 3D Shadow -->
    <text x="453" y="108" fill="#4c1d68" class="pixel-text" font-size="44" text-anchor="middle">✧ LUXION ✧</text>
    <text x="450" y="106" fill="url(#textGrad)" class="pixel-text" font-size="44" text-anchor="middle">✧ LUXION ✧</text>
  </g>

  <!-- Tagline Badge -->
  <rect x="220" y="128" width="460" height="30" rx="8" fill="#2d1742" stroke="#ffb3d9" stroke-width="1.2"/>
  <text x="450" y="148" fill="#fbcfe8" class="font-cute" font-size="14" text-anchor="middle" letter-spacing="1.5">
    ♡ cute pixels, dangerous amounts of code ♡
  </text>

  <!-- Tiny status footer row -->
  <text x="450" y="180" fill="#a5b4fc" class="font-pixel" font-size="11" text-anchor="middle">
    [ SYSTEM: ARCH LINUX ] • [ WM: HYPRLAND ] • [ CLASS: FULL-STACK MAGUS ] • [ TEAM: ACPTEAM ]
  </text>
</svg>
'''

with open(os.path.join(assets_dir, "title-header.svg"), "w") as f:
    f.write(title_header_svg)

print("Saved title-header.svg")
