import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
from langchain_groq import ChatGroq
import json
import os

# 1. SETUP & PERMANENT STORAGE
st.set_page_config(page_title="Zenith Lore Matrix", layout="wide")

# File to store characters permanently
DB_FILE = "lore_registry.json"

def load_lore():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return {
        "William Afton": {"img": "https://static.wikia.nocookie.net/fivenightsatfreddys/images/0/0b/Springtrap_FNAF3.png", "type": "human"},
        "Freddy Fazbear": {"img": "https://upload.wikimedia.org/wikipedia/en/2/22/Fnaf_character_freddy_fazbear.png", "type": "animatronic"},
        "The Puppet": {"img": "https://static.wikia.nocookie.net/fivenightsatfreddys/images/1/10/The_Puppet.png", "type": "spirit"}
    }

def save_lore(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f)

if "lore_db" not in st.session_state:
    st.session_state.lore_db = load_lore()

# Connect to AI
llm = None
if "GROQ_API_KEY" in st.secrets:
    llm = ChatGroq(groq_api_key=st.secrets["GROQ_API_KEY"], model_name="llama-3.3-70b-versatile")

# 2. SIDEBAR: THE ARCHIVE COMMAND
with st.sidebar:
    st.header("🗄️ ARCHIVE CONTROLS")
    subject = st.selectbox("Current Subjects:", ["Main Terminal"] + list(st.session_state.lore_db.keys()))
    
    st.markdown("---")
    st.subheader("Add New Entity")
    new_char = st.text_input("Name (e.g. Scraptrap):")
    new_img = st.text_input("Image URL:")
    if st.button("Commit to Archive"):
        if new_char and new_img:
            st.session_state.lore_db[new_char] = {"img": new_img, "type": "custom"}
            save_lore(st.session_state.lore_db)
            st.success(f"{new_char} added to permanent records!")
            st.rerun()

# 3. LORE DISPLAY (With Gabriel Fix)
if subject == "Main Terminal":
    st.title("👁️ ZENITH LORE ARCHIVE")
    st.write(f"The matrix is currently tracking {len(st.session_state.lore_db)} entities.")
    st.image("https://images.unsplash.com/photo-1614728263952-84ea206f99b6?w=1200", use_container_width=True)
else:
    st.header(f"📊 DATA ENTRY: {subject}")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(st.session_state.lore_db[subject]["img"], width=400)
    with col2:
        if llm:
            with st.spinner("Analyzing Remnant..."):
                # HARD-CODED LORE TRUTH
                prompt = f"Provide a lore profile for {subject}. TRUTH: Freddy Fazbear is Gabriel. Describe their evolution and importance to the Afton story."
                response = llm.invoke(prompt)
                st.markdown(response.content)

# 4. THE EVOLUTION MATRIX (With Connections)
st.markdown("---")
st.subheader("🕸️ THE CONNECTION MATRIX")

nodes = []
for name, data in st.session_state.lore_db.items():
    nodes.append(Node(id=name, label=name, shape="circularImage", image=data["img"], size=35))

# Logic for Afton Family/Evolution lines
edges = [
    Edge(source="William Afton", target="Freddy Fazbear", label="Killed Gabriel"),
    Edge(source="The Puppet", target="Freddy Fazbear", label="Gave Life")
]

# Add specific evolution lines if the characters exist in your DB
if "Springtrap" in st.session_state.lore_db:
    edges.append(Edge(source="William Afton", target="Springtrap", label="Evolution"))
if "Scraptrap" in st.session_state.lore_db:
    edges.append(Edge(source="Springtrap", target="Scraptrap", label="Evolution"))

config = Config(width=1200, height=700, directed=True, nodeHighlightBehavior=True, highlightColor="#ff4b4b")
agraph(nodes=nodes, edges=edges, config=config)