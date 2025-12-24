import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
from langchain_groq import ChatGroq
import base64
import os
from fetch_assets import fetch_specific_image # Import our new function

# 1. PAGE SETUP
st.set_page_config(page_title="Zenith Lore Matrix", layout="wide")

# 2. IMAGE ENCODER
def get_image(file_name):
    path = os.path.join("assets", file_name)
    if os.path.exists(path):
        with open(path, "rb") as f:
            return f"data:image/png;base64,{base64.b64encode(f.read()).decode()}"
    return "https://img.icons8.com/nolan/512/security-configuration.png"

# 3. AI CONNECTION
llm = None
if "GROQ_API_KEY" in st.secrets:
    llm = ChatGroq(groq_api_key=st.secrets["GROQ_API_KEY"], model_name="llama-3.3-70b-versatile")

# 4. INITIAL DATABASE
if 'db' not in st.session_state:
    st.session_state.db = {
        "William Afton": {"img": "william_afton.png", "type": "Family"},
        "Michael Afton": {"img": "michael_afton.png", "type": "Family"},
        "Elizabeth Afton": {"img": "elizabeth_afton.png", "type": "Family"},
        "Crying Child": {"img": "crying_child.png", "type": "Family"},
        "Gabriel (Freddy)": {"img": "gabriel.png", "type": "Victim"},
        "The Puppet": {"img": "puppet.png", "type": "Victim"},
        "Springtrap": {"img": "springtrap.png", "type": "Evolution"}
    }

# 5. SIDEBAR: ADD NEW CHARACTER
with st.sidebar:
    st.title("👁️ ZENITH ARCHIVE")
    new_char = st.text_input("Decrypt New Subject (e.g. 'The Mimic'):")
    if st.button("Initialize Decryption") and new_char:
        with st.spinner(f"Fetching data for {new_char}..."):
            fname = f"{new_char.lower().replace(' ', '_')}.png"
            # Trigger the fetcher
            fetch_specific_image(new_char, fname)
            # Add to local session database
            st.session_state.db[new_char] = {"img": fname, "type": "New Entry"}
            st.success(f"{new_char} added to Matrix.")

    subject = st.selectbox("Select Subject:", ["Main Terminal"] + list(st.session_state.db.keys()))

# 6. MAIN DISPLAY
if subject == "Main Terminal":
    st.title("🕸️ THE CONNECTION MATRIX")
    
    nodes = [Node(id=name, label=name, shape="circularImage", image=get_image(data["img"]), size=35) 
             for name, data in st.session_state.db.items()]
    
    # Automatic Family Linking
    edges = []
    for name in st.session_state.db:
        if "Afton" in name and name != "William Afton":
            edges.append(Edge(source="William Afton", target=name, label="Father", color="purple"))
    
    # Manual Plot Links
    edges.append(Edge(source="William Afton", target="Gabriel (Freddy)", label="Murderer", color="red"))
    edges.append(Edge(source="The Puppet", target="Gabriel (Freddy)", label="Gave Life", color="blue"))

    config = Config(width=1200, height=700, directed=True, nodeHighlightBehavior=True)
    agraph(nodes=nodes, edges=edges, config=config)

else:
    # 7. AI LORE TAB
    st.title(f"📊 DATA ENTRY: {subject}")
    tab1, tab2 = st.tabs(["🖼️ Visual", "📜 Deep Lore"])
    with tab1:
        st.image(get_image(st.session_state.db[subject]["img"]), width=400)
    with tab2:
        if llm:
            prompt = f"""Identify lore for {subject}. 
            CRITICAL: Gabriel is MCI victim, NOT an Afton. 
            Relate {subject} to the Afton family if applicable.
            Tone: Investigative Journalist."""
            st.write(llm.invoke(prompt).content)