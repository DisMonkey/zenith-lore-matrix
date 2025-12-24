import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config

# 1. PAGE CONFIG & THEME
st.set_page_config(page_title="Zenith Lore Matrix", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    </style>
    """, unsafe_allow_html=True)

# 2. THE NEWS TICKER
st.markdown("<marquee style='color:#ff4b4b; font-size:22px; font-family:monospace;'><b>SYSTEM ALERT:</b> Analyzing Fazbear Leaks • New Bendy 'The Cage' Files Found • Visual Matrix Online...</marquee>", unsafe_allow_html=True)

# 3. TITLE & FEATURED IMAGE
st.title("👁️ ZENITH LORE MATRIX")

# This adds an image of Freddy. You can change the URL to any image you want!
st.image("https://upload.wikimedia.org/wikipedia/en/2/22/Fnaf_character_freddy_fazbear.png", 
         caption="DATA SCAN: Freddy Fazbear (Primary Intel)", 
         width=300)

# 4. THE VISUAL WEB MATRIX
nodes = [
    Node(id="Afton", label="William Afton", color="#800080", size=25),
    Node(id="Spring", label="Springtrap", color="#228B22", size=20),
    Node(id="Ink", label="Ink Demon", color="#000000", size=25)
]
edges = [
    Edge(source="Afton", target="Spring", label="becomes"),
    Edge(source="Spring", target="Ink", label="void_connection")
]

config = Config(width=800, height=400, directed=True, nodeHighlightBehavior=True, collapsible=True)
agraph(nodes=nodes, edges=edges, config=config)

# 5. CHAT INTERFACE
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Query the Archive..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        st.write("Analysing data-stream for: " + prompt)

# 6. FOOTER CREDITS (STAYING SIMPLE)
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #555; font-family: monospace;'>"
    "ARCHIVE VERSION: 1.0.5 | ARCHITECT: <b>DisMonkey</b><br>"
    "© 2025 ZENITH-LORE-MATRIX"
    "</div>", 
    unsafe_allow_html=True
)