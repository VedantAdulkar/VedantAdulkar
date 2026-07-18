import os

def create_svg(filename, width, height, is_dark, content):
    bg_color = "#0d1117" if is_dark else "#ffffff"
    text_color = "#c9d1d9" if is_dark else "#24292f"
    accent_color = "#58a6ff" if is_dark else "#0969da"
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
    <rect width="{width}" height="{height}" fill="{bg_color}" rx="6" />
    <style>
        .title {{ font: 600 24px 'Segoe UI', Ubuntu, Sans-Serif; fill: {text_color}; }}
        .subtitle {{ font: 400 16px 'Segoe UI', Ubuntu, Sans-Serif; fill: {text_color}; opacity: 0.8; }}
        .accent {{ fill: {accent_color}; }}
        .text {{ font: 400 14px 'Segoe UI', Ubuntu, Sans-Serif; fill: {text_color}; }}
        .highlight {{ font: 600 14px 'Segoe UI', Ubuntu, Sans-Serif; fill: {accent_color}; }}
    </style>
    {content}
</svg>"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg)

def generate_header(is_dark):
    bg_color = "#0d1117" if is_dark else "#ffffff"
    text_color = "#c9d1d9" if is_dark else "#24292f"
    accent = "#58a6ff" if is_dark else "#0969da"
    
    content = f"""
    <g transform="translate(40, 60)">
        <text class="title" x="0" y="0">Vedant Adulkar</text>
        <text class="subtitle" x="0" y="30">AI &amp; Machine Learning Engineer | Generative AI Enthusiast</text>
        <line x1="0" y1="50" x2="600" y2="50" stroke="{accent}" stroke-width="2" />
        <text class="text" x="0" y="80">Transforming data into intelligent systems.</text>
    </g>
    """
    path = "assets/dark/header.svg" if is_dark else "assets/header.svg"
    create_svg(path, 800, 180, is_dark, content)

def generate_whoami(is_dark):
    bg_color = "#0d1117" if is_dark else "#ffffff"
    text_color = "#c9d1d9" if is_dark else "#24292f"
    accent = "#58a6ff" if is_dark else "#0969da"
    
    content = f"""
    <g transform="translate(40, 40)">
        <text class="title" x="0" y="0">whoami</text>
        <text class="text" x="0" y="40">&gt; Pronouns: He/Him</text>
        <text class="text" x="0" y="70">&gt; Current Focus: <tspan class="highlight">Generative AI</tspan> and <tspan class="highlight">Reinforcement Learning</tspan></text>
        <text class="text" x="0" y="100">&gt; Passion: Building data-driven systems &amp; deploying ML models.</text>
        <text class="text" x="0" y="130">&gt; Fun Fact: I believe every dataset hides a story — my job is to make it speak!</text>
    </g>
    """
    path = "assets/dark/whoami.svg" if is_dark else "assets/whoami.svg"
    create_svg(path, 800, 200, is_dark, content)

def generate_stack(is_dark):
    content = f"""
    <g transform="translate(40, 40)">
        <text class="title" x="0" y="0">technical stack</text>
        <text class="highlight" x="0" y="40">Languages:</text> <text class="text" x="120" y="40">Python, SQL, JavaScript, C</text>
        <text class="highlight" x="0" y="70">AI/ML:</text> <text class="text" x="120" y="70">TensorFlow, PyTorch, Scikit-learn, Keras</text>
        <text class="highlight" x="0" y="100">Data Science:</text> <text class="text" x="120" y="100">NumPy, Pandas, Matplotlib, Power BI</text>
        <text class="highlight" x="0" y="130">Backend:</text> <text class="text" x="120" y="130">Flask, FastAPI, Node.js</text>
        <text class="highlight" x="0" y="160">Databases:</text> <text class="text" x="120" y="160">PostgreSQL, MySQL, MongoDB</text>
        <text class="highlight" x="0" y="190">DevOps:</text> <text class="text" x="120" y="190">Git, Docker, CI/CD</text>
    </g>
    """
    path = "assets/dark/stack.svg" if is_dark else "assets/stack.svg"
    create_svg(path, 800, 260, is_dark, content)

def generate_projects(is_dark):
    content = f"""
    <g transform="translate(40, 40)">
        <text class="title" x="0" y="0">projects ecosystem</text>
        
        <a href="https://github.com/VedantAdulkar/DroneGCS" target="_blank">
            <g transform="translate(0, 30)">
                <rect x="0" y="0" width="350" height="70" fill="none" stroke="#8b949e" stroke-width="1" rx="4"/>
                <text class="highlight" x="15" y="25">DroneGCS</text>
                <text class="text" x="15" y="50">Drone Ground Control Station</text>
            </g>
        </a>
        
        <a href="https://github.com/VedantAdulkar/KnowAI_v1" target="_blank">
            <g transform="translate(370, 30)">
                <rect x="0" y="0" width="350" height="70" fill="none" stroke="#8b949e" stroke-width="1" rx="4"/>
                <text class="highlight" x="15" y="25">KnowAI_v1</text>
                <text class="text" x="15" y="50">AI Knowledge Assistant</text>
            </g>
        </a>
        
        <a href="https://github.com/VedantAdulkar/local_RAG" target="_blank">
            <g transform="translate(0, 115)">
                <rect x="0" y="0" width="350" height="70" fill="none" stroke="#8b949e" stroke-width="1" rx="4"/>
                <text class="highlight" x="15" y="25">local_RAG</text>
                <text class="text" x="15" y="50">Local Retrieval-Augmented Generation</text>
            </g>
        </a>
        
        <a href="https://github.com/VedantAdulkar/MA_13_DocSummariser" target="_blank">
            <g transform="translate(370, 115)">
                <rect x="0" y="0" width="350" height="70" fill="none" stroke="#8b949e" stroke-width="1" rx="4"/>
                <text class="highlight" x="15" y="25">MA_13_DocSummariser</text>
                <text class="text" x="15" y="50">Document Summarization Tool</text>
            </g>
        </a>
        
        <a href="https://github.com/VedantAdulkar/Placement-Predictor" target="_blank">
            <g transform="translate(0, 200)">
                <rect x="0" y="0" width="350" height="70" fill="none" stroke="#8b949e" stroke-width="1" rx="4"/>
                <text class="highlight" x="15" y="25">Placement-Predictor</text>
                <text class="text" x="15" y="50">ML Model for Placement Prediction</text>
            </g>
        </a>
        
        <a href="https://github.com/VedantAdulkar/Profile-site-2.0" target="_blank">
            <g transform="translate(370, 200)">
                <rect x="0" y="0" width="350" height="70" fill="none" stroke="#8b949e" stroke-width="1" rx="4"/>
                <text class="highlight" x="15" y="25">Profile-site-2.0</text>
                <text class="text" x="15" y="50">Angular-based Personal Portfolio</text>
            </g>
        </a>
    </g>
    """
    path = "assets/dark/projects.svg" if is_dark else "assets/projects.svg"
    create_svg(path, 800, 340, is_dark, content)


def main():
    os.makedirs("assets/dark", exist_ok=True)
    
    for is_dark in [True, False]:
        generate_header(is_dark)
        generate_whoami(is_dark)
        generate_stack(is_dark)
        generate_projects(is_dark)
        
    print("Assets generated successfully!")

if __name__ == "__main__":
    main()
