import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config

st.set_page_config(page_title="Lore Engine", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<marquee style='color:#ff4b4b; font-size:22px; font-family:monospace;'><b>SYSTEM ALERT:</b> Analyzing Fazbear Leaks • New Bendy 'The Cage' Files Found • Visual Matrix Online...</marquee>", unsafe_allow_html=True)

st.title("👁️ OMNI-LORE ARCHIVE")
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