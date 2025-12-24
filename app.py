import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
from langchain_groq import ChatGroq
import base64
import os

# 1. SYSTEM CONFIG
st.set_page_config(page_title="Zenith Lore Matrix", layout="wide")

# 2. IMAGE ENCODER (The "No-Fail" Method)
def get_base64_img(img_path):
    """Converts local images to base64 strings so they always load."""
    if os.path.exists(img_path):
        with open(img_path, "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        return f"data:image/png;base64,{encoded}"
    # Fallback if image is missing
    return "https://via.placeholder.com/150?text=Missing+Asset"

# 3. AI CONNECT
llm = None
if "GROQ_API_KEY" in st.secrets:
    llm = ChatGroq(groq_api_key=st.secrets["GROQ_API_KEY"], model_name="llama-3.3-70b-versatile")

# 4. DATASET (Points to your /assets/ folder)
CHARACTERS = {
    "William Afton": {
        "img": get_base64_img("assets/william_afton.png"), 
        "msg": "⚠️ PRIORITY ALERT: Subject 'Afton' linked to Multiple Remnant Anomalies.",
        "evo": "William Afton ➔ Springlock Failure ➔ Springtrap ➔ Scraptrap ➔ Glitchtrap"
    },
    "Gabriel (Freddy)": {
        "img": get_base64_img("assets/gabriel.png"), 
        "msg": "📦 ASSET LOG: Retrieval of 1985 Incident Subject 01. Identity: Gabriel.",
        "evo": "Gabriel (Child) ➔ 1985 MCI Victim ➔ Freddy Fazbear ➔ Molten Freddy"
    },
    "Springtrap": {
        "img": get_base64_img("assets/springtrap.png"), 
        "msg": "☣️ BIOHAZARD DETECTED: Spring-Lock Failure Case #003.",
        "evo": "William Afton ➔ Springlock Failure ➔ Springtrap ➔ Scraptrap"
    },
    "The Puppet": {
        "img": get_base64_img("assets/puppet.png"), 
        "msg": "🎭 SYSTEM OVERRIDE: Subject identified as Charlotte Emily.",
        "evo": "Charlie Emily ➔ Outside Diner Incident ➔ The Puppet ➔ Lefty"
    }
}

# 5. SIDEBAR
with st.sidebar:
    st.title("👁️ ZENITH ARCHIVE")
    subject = st.selectbox("Subject Files:", ["Main Terminal"] + list(CHARACTERS.keys()))
    st.markdown("---")
    st.info("System Status: OPERATIONAL\n\nArchitect: IsakC")

# 6. MAIN TERMINAL / CONNECTION MATRIX
if subject == "Main Terminal":
    st.title("👁️ ZENITH LORE TERMINAL")
    st.markdown("### Accessing Fazbear Records... System Clear.")
    
    # THE CONNECTION WEB
    nodes = [Node(id=name, label=name, shape="circularImage", image=data["img"], size=35) for name, data in CHARACTERS.items()]
    edges = [
        Edge(source="William Afton", target="Gabriel (Freddy)", label="Murderer (1985 MCI)", color="red"),
        Edge(source="The Puppet", target="Gabriel (Freddy)", label="Gave Life", color="blue"),
        Edge(source="William Afton", target="Springtrap", label="Evolution", color="purple")
    ]
    config = Config(width=1200, height=600, directed=True, nodeHighlightBehavior=True, highlightColor="#00FF00")
    agraph(nodes=nodes, edges=edges, config=config)

else:
    # 7. CHARACTER DATA ENTRY
    st.title(f"📊 DATA ENTRY: {subject}")
    st.warning(CHARACTERS[subject]["msg"])
    
    tab1, tab2, tab3 = st.tabs(["🖼️ Visual Intel", "📜 Deep Lore", "🧬 Evolution"])
    
    with tab1:
        st.image(CHARACTERS[subject]["img"], width=400)
    
    with tab2:
        if llm:
            with st.spinner("Analyzing..."):
                prompt = f"Lore for {subject}. Gabriel is MCI victim, NOT an Afton. Afton kids: Michael, Elizabeth, CC."
                response = llm.invoke(prompt)
                st.markdown(response.content)
    
    with tab3:
        st.code(CHARACTERS[subject]["evo"])