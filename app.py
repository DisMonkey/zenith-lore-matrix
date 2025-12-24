import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
from langchain_groq import ChatGroq

# 1. PAGE CONFIG
st.set_page_config(page_title="Zenith Lore Matrix", layout="wide")

# 2. AI BRAIN SETUP
llm = None
if "GROQ_API_KEY" in st.secrets:
    try:
        llm = ChatGroq(
            temperature=0.7, 
            groq_api_key=st.secrets["GROQ_API_KEY"], 
            model_name="llama-3.3-70b-versatile" 
        )
    except Exception as e:
        st.error(f"AI Core Offline: {e}")

# 3. SIDEBAR
with st.sidebar:
    st.title("🗄️ FAZBEAR ARCHIVES")
    st.markdown("---")
    # Clean names without underscores
    character = st.selectbox(
        "Select Subject:", 
        ["Home", "Freddy Fazbear", "Bonnie", "Chica", "Foxy", "William Afton", "The Puppet", "Golden Freddy", "Crying Child"]
    )
    st.info("ARCHITECT: DisMonkey")

# 4. NEWS TICKER
st.markdown(f"<marquee style='color:#ff4b4b; font-size:22px; font-family:monospace;'><b>DATA STREAM:</b> Analyzing {character} • Accessing Remnant Files • System Status: Secure</marquee>", unsafe_allow_html=True)

# 5. DYNAMIC CONTENT
if character == "Home":
    st.title("👁️ ZENITH LORE MATRIX")
    st.markdown("### Welcome to the restricted Fazbear database.")
    st.write("Use the sidebar to extract intelligence. This system uses AI to decrypt hidden lore and visualize character connections.")
    st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=1000", caption="Mainframe Online", use_container_width=True)

else:
    st.title(f"📊 DATA ENTRY: {character}")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # High-Quality Image Mapping
        images = {
            "Freddy Fazbear": "https://upload.wikimedia.org/wikipedia/en/2/22/Fnaf_character_freddy_fazbear.png",
            "William Afton": "https://static.wikia.nocookie.net/fnaf-world-rpg/images/0/0b/Springtrap_FNAF3.png",
            "The Puppet": "https://static.wikia.nocookie.net/fnaf-world-rpg/images/b/b3/Puppet_jumpscare_FNAF2.gif",
            "Bonnie": "https://static.wikia.nocookie.net/fivenightsatfreddys/images/1/10/Bonnie_FNaF1.png",
            "Chica": "https://static.wikia.nocookie.net/fivenightsatfreddys/images/b/be/Chica_FNaF1.png",
            "Foxy": "https://static.wikia.nocookie.net/fivenightsatfreddys/images/7/77/Foxy_FNaF1.png",
            "Golden Freddy": "https://static.wikia.nocookie.net/fivenightsatfreddys/images/a/a7/Golden_Freddy_FNaF1.png",
            "Crying Child": "https://static.wikia.nocookie.net/fivenightsatfreddys/images/1/1a/Crying_Child_8-bit.png"
        }
        st.image(images.get(character), caption=f"Visual Confirmation: {character}")

    with col2:
        if st.button(f"Analyze {character}"):
            if llm:
                with st.spinner("Extracting Intel..."):
                    # Special logic for Golden Freddy connection
                    prompt_extra = ""
                    if character == "Golden Freddy":
                        prompt_extra = " Explain specifically his connection to Freddy Fazbear and the 'Two Souls' theory."
                    
                    messages = [
                        ("system", "You are the Zenith Lore AI. Provide dark, professional intel reports."),
                        ("user", f"Give me a detailed info report on {character} from FNAF. Include their role, dark secrets, and history.{prompt_extra}")
                    ]
                    response = llm.invoke(messages)
                    st.markdown(response.content)

# 6. ENHANCED VISUAL WEB (Larger & More Connections)
st.markdown("---")
st.subheader("🕸️ THE CONNECTION MATRIX")

nodes = [
    Node(id="Afton", label="William Afton", color="#800080", size=30),
    Node(id="Puppet", label="The Puppet", color="#FFFFFF", size=25),
    Node(id="Freddy", label="Freddy Fazbear", color="#654321", size=25),
    Node(id="Gold", label="Golden Freddy", color="#FFD700", size=30),
    Node(id="Child", label="Crying Child", color="#4682B4", size=20),
    Node(id="Cassidy", label="Cassidy", color="#FFD700", size=15)
]

edges = [
    Edge(source="Afton", target="Puppet", label="First Murder"),
    Edge(source="Puppet", target="Freddy", label="Gave Life"),
    Edge(source="Freddy", target="Gold", label="Spectral Mirror"),
    Edge(source="Child", target="Gold", label="Soul 1"),
    Edge(source="Cassidy", target="Gold", label="Soul 2"),
    Edge(source="Afton", target="Child", label="Father")
]

# Configured for a larger, better-looking web
config = Config(width=1200, height=600, directed=True, nodeHighlightBehavior=True, collapsible=True, staticGraph=False)
agraph(nodes=nodes, edges=edges, config=config)

# 7. FOOTER
st.markdown("---")
st.markdown("<div style='text-align: center; color: #555;'>ARCHITECT: <b>DisMonkey</b> | SYSTEM VERSION 3.0.0</div>", unsafe_allow_html=True)