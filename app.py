import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
from langchain_groq import ChatGroq

# 1. SETUP
st.set_page_config(page_title="Zenith Lore Matrix", layout="wide")

# Connect to AI
llm = None
if "GROQ_API_KEY" in st.secrets:
    llm = ChatGroq(groq_api_key=st.secrets["GROQ_API_KEY"], model_name="llama-3.3-70b-versatile")

# 2. UPDATED DATA (Fixed Gabriel & Added Evolution Chain)
CHARACTERS = {
    "Freddy Fazbear": "https://upload.wikimedia.org/wikipedia/en/2/22/Fnaf_character_freddy_fazbear.png",
    "William Afton": "https://static.wikia.nocookie.net/fivenightsatfreddys/images/1/1a/Crying_Child_8-bit.png", # Placeholder for human Afton
    "Springtrap": "https://static.wikia.nocookie.net/fivenightsatfreddys/images/4/4c/Springtrap_FNaF3.png",
    "Scraptrap": "https://static.wikia.nocookie.net/fivenightsatfreddys/images/0/05/Scraptrap_Pizzeria_Simulator.png",
    "Glitchtrap": "https://static.wikia.nocookie.net/fivenightsatfreddys/images/d/d3/Glitchtrap_Help_Wanted.png",
    "Burntrap": "https://static.wikia.nocookie.net/fivenightsatfreddys/images/6/60/Burntrap_Security_Breach.png",
    "The Puppet": "https://static.wikia.nocookie.net/fivenightsatfreddys/images/1/10/The_Puppet.png"
}

# 3. SIDEBAR CONTROLS
with st.sidebar:
    st.header("🗄️ ARCHIVE CONTROLS")
    subject = st.selectbox("Select Subject:", ["Main Terminal"] + list(CHARACTERS.keys()))
    st.info("Architect: DisMonkey")

# 4. DYNAMIC LORE & EVOLUTION LOGIC
if subject == "Main Terminal":
    st.title("👁️ ZENITH LORE ARCHIVE")
    st.markdown("### Accessing Fazbear Historical Data...")
    st.write("Select a subject to view their evolution through the franchise.")
else:
    st.header(f"📊 DATA ENTRY: {subject}")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image(CHARACTERS.get(subject), use_container_width=True)
        
    with col2:
        if llm:
            with st.spinner("Analyzing Remnant..."):
                # FORCED KNOWLEDGE: Gabriel is the soul.
                prompt = f"""
                You are a Lore Historian. Provide a report on '{subject}'. 
                CRITICAL FACT: Freddy Fazbear is possessed by GABRIEL. Never use the name Charles.
                
                Include:
                1. Bio & Evolution: Explain their transition through different games.
                2. Lore Contribution: What is their role in the timeline?
                3. Deep Secret: A hidden detail or theory.
                """
                response = llm.invoke(prompt)
                st.markdown(response.content)

# 5. THE EVOLUTION MATRIX (The Web)
st.markdown("---")
st.subheader("🕸️ THE EVOLUTION MATRIX")

# Define Nodes with unique colors for Afton's evolution
nodes = [
    Node(id="Afton", label="William Afton", color="#800080", size=25),
    Node(id="Springtrap", label="Springtrap", color="#556B2F", size=25),
    Node(id="Scraptrap", label="Scraptrap", color="#8B4513", size=25),
    Node(id="Glitchtrap", label="Glitchtrap", color="#DA70D6", size=25),
    Node(id="Burntrap", label="Burntrap", color="#FF4500", size=25),
    Node(id="Freddy", label="Freddy Fazbear (Gabriel)", color="#654321", size=20),
    Node(id="Puppet", label="The Puppet", color="#FFFFFF", size=20)
]

# Define Edges with evolution labels
edges = [
    Edge(source="Afton", target="Springtrap", label="Springlock Failure"),
    Edge(source="Springtrap", target="Scraptrap", label="Fire Survivor"),
    Edge(source="Scraptrap", target="Glitchtrap", label="Digital Virus"),
    Edge(source="Glitchtrap", target="Burntrap", label="Physical Rebirth"),
    Edge(source="Afton", target="Puppet", label="First Murder"),
    Edge(source="Puppet", target="Freddy", label="Gave Life")
]

# Highlighting Logic: When a user selects a character, the web emphasizes them
config = Config(
    width=1200, 
    height=600, 
    directed=True, 
    nodeHighlightBehavior=True, # This enables the highlighting you asked for
    highlightColor="#00E6FF", 
    collapsible=True,
    staticGraph=False
)

agraph(nodes=nodes, edges=edges, config=config)

st.markdown("---")
st.markdown("<div style='text-align: center; color: #555;'>SYSTEM: ZENITH | ARCHITECT: <b>DisMonkey</b></div>", unsafe_allow_html=True)