import os

def create_svg(filename, width, height, is_dark, content):
    bg_color = "#0d1117" if is_dark else "#ffffff"
    text_color = "#c9d1d9" if is_dark else "#24292f"
    accent_color = "#58a6ff" if is_dark else "#0969da"
    grid_color = "#30363d" if is_dark else "#e1e4e8"
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
    <defs>
        <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
            <rect width="40" height="40" fill="none" stroke="{grid_color}" stroke-width="0.5" stroke-dasharray="2,2"/>
        </pattern>
        <pattern id="dots" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
            <circle cx="2" cy="2" r="1.5" fill="{grid_color}" opacity="0.5"/>
        </pattern>
        <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:{accent_color};stop-opacity:1" />
            <stop offset="100%" style="stop-color:#b392f0;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="{width}" height="{height}" fill="{bg_color}" rx="8" />
    <rect width="{width}" height="{height}" fill="url(#grid)" rx="8" />
    <style>
        .title {{ font: 700 28px 'Fira Code', 'Courier New', monospace; fill: {text_color}; letter-spacing: -0.5px; }}
        .subtitle {{ font: 400 16px 'Fira Code', 'Courier New', monospace; fill: {text_color}; opacity: 0.7; }}
        .mono {{ font: 400 14px 'Fira Code', 'Courier New', monospace; fill: {text_color}; }}
        .mono-small {{ font: 400 12px 'Fira Code', 'Courier New', monospace; fill: {text_color}; opacity: 0.6; }}
        .accent {{ fill: {accent_color}; font-weight: 600; }}
        .highlight {{ font: 600 14px 'Segoe UI', Ubuntu, Sans-Serif; fill: {accent_color}; }}
        .text {{ font: 400 15px 'Segoe UI', Ubuntu, Sans-Serif; fill: {text_color}; }}
        .box {{ fill: {bg_color}; stroke: {grid_color}; stroke-width: 1; rx: 6px; }}
    </style>
    {content}
    <rect width="{width}" height="{height}" fill="none" stroke="{grid_color}" stroke-width="2" rx="8" />
</svg>"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg)

def generate_header(is_dark):
    accent = "#58a6ff" if is_dark else "#0969da"
    content = f"""
    <rect x="0" y="0" width="10" height="180" fill="url(#grad1)" rx="4"/>
    <g transform="translate(50, 50)">
        <text class="title" x="0" y="0">VEDANT_ADULKAR</text>
        <text class="mono" x="0" y="30">&gt; <tspan fill="{accent}">sys.role</tspan> = "Data / AI Engineer"</text>
        <text class="mono" x="0" y="55">&gt; <tspan fill="{accent}">sys.specialty</tspan> = ["LLMs", "RAG", "Enterprise AI Systems"]</text>
        <text class="mono" x="0" y="80">&gt; <tspan fill="{accent}">sys.status</tspan> = "Infusing intelligent AI technologies for global clients."</text>
        
        <!-- Live Links Section -->
        <g transform="translate(0, 115)">
            <rect class="box" x="0" y="-20" width="375" height="30" fill="#238636" fill-opacity="0.1" stroke="#238636"/>
            <circle cx="15" cy="-5" r="4" fill="#238636" />
            <text class="mono" x="28" y="0">Live Profile: <tspan class="accent">profile-site-2-0.onrender.com</tspan></text>
        </g>
    </g>
    <rect x="700" y="20" width="80" height="140" fill="url(#dots)"/>
    """
    path = "assets/dark/header.svg" if is_dark else "assets/header.svg"
    create_svg(path, 800, 200, is_dark, content)

def generate_whoami(is_dark):
    accent = "#58a6ff" if is_dark else "#0969da"
    content = f"""
    <g transform="translate(30, 40)">
        <text class="title" x="0" y="0">01 — whoami</text>
        <line x1="0" y1="15" x2="740" y2="15" stroke="{accent}" stroke-width="2" stroke-opacity="0.5"/>
        
        <g transform="translate(20, 50)">
            <rect class="box" x="0" y="0" width="700" height="145" />
            <circle cx="20" cy="20" r="5" fill="#ff5f56"/>
            <circle cx="40" cy="20" r="5" fill="#ffbd2e"/>
            <circle cx="60" cy="20" r="5" fill="#27c93f"/>
            <line x1="0" y1="40" x2="700" y2="40" stroke="#30363d" stroke-width="1"/>
            
            <text class="mono" x="20" y="65"><tspan class="accent">vedant@core</tspan>:~$ cat professional_summary.log</text>
            <text class="mono" x="20" y="90">Experienced Data/AI Engineer specializing in Large Language Models (LLMs) &amp; RAG.</text>
            <text class="mono" x="20" y="115">Architecting scalable AI infrastructure and delivering robust</text>
            <text class="mono" x="20" y="140">machine learning solutions for enterprise clients.</text>
        </g>
    </g>
    """
    path = "assets/dark/whoami.svg" if is_dark else "assets/whoami.svg"
    create_svg(path, 800, 245, is_dark, content)

def generate_experience(is_dark):
    accent = "#58a6ff" if is_dark else "#0969da"
    grid = "#30363d" if is_dark else "#e1e4e8"
    content = f"""
    <g transform="translate(30, 40)">
        <text class="title" x="0" y="0">02 — telemetry_&amp;_timeline</text>
        <line x1="0" y1="15" x2="740" y2="15" stroke="{accent}" stroke-width="2" stroke-opacity="0.5"/>
        
        <!-- Timeline Line -->
        <line x1="40" y1="60" x2="40" y2="280" stroke="{grid}" stroke-width="2" />
        
        <!-- ICRA Analytics -->
        <g transform="translate(40, 80)">
            <circle cx="0" cy="0" r="6" fill="{accent}" />
            <circle cx="0" cy="0" r="10" fill="none" stroke="{accent}" stroke-width="1.5">
                <animate attributeName="r" values="8;16;8" dur="3s" repeatCount="indefinite"/>
                <animate attributeName="opacity" values="1;0;1" dur="3s" repeatCount="indefinite"/>
            </circle>
            <text class="mono accent" x="25" y="-5">Data / AI Engineer @ ICRA Analytics - Fintellix</text>
            <text class="mono-small" x="25" y="15">1+ Years • Building Enterprise AI Systems • LLMs • RAG Models</text>
            
            <rect class="box" x="20" y="25" width="650" height="30" fill="{accent}" fill-opacity="0.05" stroke-opacity="0"/>
            <text class="mono-small" x="30" y="45">&gt; Spearheading the implementation of generative AI architectures for major clients.</text>
        </g>

        <!-- Earlier Work / Evolution -->
        <g transform="translate(40, 180)">
            <circle cx="0" cy="0" r="5" fill="{grid}" />
            <text class="mono" x="25" y="-5" fill="{grid}">Project Evolution &amp; Foundation</text>
            <text class="mono-small" x="25" y="15">Developed multiple AI pipelines including DocQ summarizer &amp; autonomous drones.</text>
            <text class="mono-small" x="25" y="35">Expertise built across Python, ML Algorithms, and APIs.</text>
        </g>
    </g>
    """
    path = "assets/dark/experience.svg" if is_dark else "assets/experience.svg"
    create_svg(path, 800, 300, is_dark, content)


def generate_stack(is_dark):
    accent = "#58a6ff" if is_dark else "#0969da"
    content = f"""
    <g transform="translate(30, 40)">
        <text class="title" x="0" y="0">03 — technical_stack</text>
        <line x1="0" y1="15" x2="740" y2="15" stroke="{accent}" stroke-width="2" stroke-opacity="0.5"/>
        
        <g transform="translate(0, 40)">
            <!-- Column 1 -->
            <rect class="box" x="0" y="0" width="230" height="120"/>
            <text class="mono accent" x="15" y="25">AI &amp; Models</text>
            <text class="mono" x="15" y="50">LLMs • RAG</text>
            <text class="mono" x="15" y="70">TensorFlow • PyTorch</text>
            <text class="mono" x="15" y="90">Scikit-learn • Keras</text>
            <text class="mono" x="15" y="110">OpenAI API</text>

            <!-- Column 2 -->
            <rect class="box" x="250" y="0" width="230" height="120"/>
            <text class="mono accent" x="265" y="25">Core &amp; Backend</text>
            <text class="mono" x="265" y="50">Python • Java • C/C++</text>
            <text class="mono" x="265" y="70">SQL • JDBC</text>
            <text class="mono" x="265" y="90">Flask • FastAPI</text>
            <text class="mono" x="265" y="110">JavaScript • Angular</text>

            <!-- Column 3 -->
            <rect class="box" x="500" y="0" width="240" height="120"/>
            <text class="mono accent" x="515" y="25">Data &amp; Cloud</text>
            <text class="mono" x="515" y="50">AWS • Docker</text>
            <text class="mono" x="515" y="70">PostgreSQL • MongoDB</text>
            <text class="mono" x="515" y="90">Power BI • Pandas</text>
            <text class="mono" x="515" y="110">Git • CI/CD Pipelines</text>
        </g>
    </g>
    """
    path = "assets/dark/stack.svg" if is_dark else "assets/stack.svg"
    create_svg(path, 800, 220, is_dark, content)

def generate_projects(is_dark):
    accent = "#58a6ff" if is_dark else "#0969da"
    
    # 1. Projects Header
    header_content = f"""
    <g transform="translate(30, 40)">
        <text class="title" x="0" y="0">04 — ecosystem</text>
        <line x1="0" y1="15" x2="740" y2="15" stroke="{accent}" stroke-width="2" stroke-opacity="0.5"/>
    </g>
    """
    path_header = "assets/dark/projects_header.svg" if is_dark else "assets/projects_header.svg"
    create_svg(path_header, 800, 80, is_dark, header_content)

    # 2. Individual Projects for Grid (Width 390 to fit side-by-side)
    # Project 1: KnowAI
    p1 = f"""
    <g transform="translate(15, 15)">
        <rect class="box" x="0" y="0" width="360" height="85"/>
        <rect x="0" y="0" width="360" height="85" rx="6" fill="#238636" fill-opacity="0.05" stroke="#238636" stroke-width="1.5"/>
        <circle cx="20" cy="25" r="5" fill="#238636">
            <animate attributeName="opacity" values="1;0;1" dur="2s" repeatCount="indefinite"/>
        </circle>
        <text class="mono" x="35" y="30"><tspan class="accent">KnowAI_v1</tspan> [LIVE]</text>
        <text class="mono-small" x="35" y="50">AI Knowledge Assistant integrating LLMs.</text>
        <text class="mono-small" x="35" y="70" fill="#238636">know-ai-news.vercel.app</text>
    </g>"""
    create_svg(f"assets/dark/project_1.svg" if is_dark else f"assets/project_1.svg", 390, 115, is_dark, p1)

    # Project 2: DocQ
    p2 = f"""
    <g transform="translate(15, 15)">
        <rect class="box" x="0" y="0" width="360" height="85"/>
        <circle cx="20" cy="25" r="4" fill="{accent}"/>
        <text class="mono" x="35" y="30"><tspan class="accent">DocQ</tspan></text>
        <text class="mono-small" x="35" y="50">All format summarizer (Image/PDF/Video) via AI.</text>
        <text class="mono-small" x="35" y="70">Stack: Python / ML / Flask</text>
    </g>"""
    create_svg(f"assets/dark/project_2.svg" if is_dark else f"assets/project_2.svg", 390, 115, is_dark, p2)

    # Project 3: Drone GCS
    p3 = f"""
    <g transform="translate(15, 15)">
        <rect class="box" x="0" y="0" width="360" height="85"/>
        <circle cx="20" cy="25" r="4" fill="{accent}"/>
        <text class="mono" x="35" y="30"><tspan class="accent">Autonomous Drone GCS</tspan></text>
        <text class="mono-small" x="35" y="50">Ground Control System for Pixhawk/RaspberryPi drones.</text>
        <text class="mono-small" x="35" y="70">Stack: Python / OpenCV</text>
    </g>"""
    create_svg(f"assets/dark/project_3.svg" if is_dark else f"assets/project_3.svg", 390, 115, is_dark, p3)

    # Project 4: Voice Assistant
    p4 = f"""
    <g transform="translate(15, 15)">
        <rect class="box" x="0" y="0" width="360" height="85"/>
        <circle cx="20" cy="25" r="4" fill="{accent}"/>
        <text class="mono" x="35" y="30"><tspan class="accent">Voice Assistant</tspan></text>
        <text class="mono-small" x="35" y="50">Intelligent agent via Google Speech &amp; OpenAI API.</text>
        <text class="mono-small" x="35" y="70">Stack: Python / APIs</text>
    </g>"""
    create_svg(f"assets/dark/project_4.svg" if is_dark else f"assets/project_4.svg", 390, 115, is_dark, p4)

    # Project 5: Recipe Recommender
    p5 = f"""
    <g transform="translate(15, 15)">
        <rect class="box" x="0" y="0" width="360" height="85"/>
        <circle cx="20" cy="25" r="4" fill="{accent}"/>
        <text class="mono" x="35" y="30"><tspan class="accent">Recipe Recommender</tspan></text>
        <text class="mono-small" x="35" y="50">Suggests recipes based on available ingredients.</text>
        <text class="mono-small" x="35" y="70">Stack: Python / ML / Flask</text>
    </g>"""
    create_svg(f"assets/dark/project_5.svg" if is_dark else f"assets/project_5.svg", 390, 115, is_dark, p5)

    # Project 6: Profile-site
    p6 = f"""
    <g transform="translate(15, 15)">
        <rect class="box" x="0" y="0" width="360" height="85"/>
        <rect x="0" y="0" width="360" height="85" rx="6" fill="#238636" fill-opacity="0.05" stroke="#238636" stroke-width="1.5"/>
        <circle cx="20" cy="25" r="5" fill="#238636">
            <animate attributeName="opacity" values="1;0;1" dur="2s" repeatCount="indefinite"/>
        </circle>
        <text class="mono" x="35" y="30"><tspan class="accent">Profile-site-2.0</tspan> [LIVE]</text>
        <text class="mono-small" x="35" y="50">Personal developer portfolio web application.</text>
        <text class="mono-small" x="35" y="70" fill="#238636">profile-site-2-0.onrender.com</text>
    </g>"""
    create_svg(f"assets/dark/project_6.svg" if is_dark else f"assets/project_6.svg", 390, 115, is_dark, p6)


def main():
    os.makedirs("assets/dark", exist_ok=True)
    
    for is_dark in [True, False]:
        generate_header(is_dark)
        generate_whoami(is_dark)
        generate_experience(is_dark)
        generate_stack(is_dark)
        generate_projects(is_dark)
        
    print("Assets generated successfully!")

if __name__ == "__main__":
    main()
