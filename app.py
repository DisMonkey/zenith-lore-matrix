import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
from langchain_groq import ChatGroq

st.set_page_config(page_title="Zenith Lore Matrix", layout="wide")

# Connect to AI
llm = None
if "GROQ_API_KEY" in st.secrets:
    llm = ChatGroq(groq_api_key=st.secrets["GROQ_API_KEY"], model_name="llama-3.3-70b-versatile")

# 1. THE RELIABLE IMAGE DATABASE (Using Direct Links)
CHARACTERS = {
    "William Afton": {"img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/ultra-ball.png", "color": "#800080"}, # Purple placeholder
    "Gabriel (Freddy)": {"img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png", "color": "#654321"}, # Replace these with your direct hosted URLs
    "Springtrap": {"img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/123.png", "color": "#556B2F"},
}

# 2. SIDEBAR
with st.sidebar:
    st.header("🗄️ ARCHIVE CONTROLS")
    subject = st.selectbox("Select Subject:", ["Main Terminal"] + list(CHARACTERS.keys()))

# 3. LORE CONTENT (Gabriel is NOT an Afton)
if subject == "Main Terminal":
    st.title("👁️ ZENITH LORE ARCHIVE")
    st.markdown("### DATA SCAN: The Missing Children Incident vs Afton Family")
else:
    st.header(f"📊 DATA ENTRY: {subject}")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(CHARACTERS[subject]["img"], width=300)
    with col2:
        if llm:
            with st.spinner("Extracting Remnant..."):
                # FORCED LORE RULES
                prompt = f"""
                Provide a lore profile for {subject}. 
                STRICT RULES:
                1. Gabriel is NOT William Afton's son. He is a victim who possesses Freddy.
                2. William Afton's only children are Michael, Elizabeth, and the Crying Child.
                3. Describe {subject}'s evolution and their contribution to the tragedy.
                """
                response = llm.invoke(prompt)
                st.markdown(response.content)

# 4. THE CONNECTION WEB
st.markdown("---")
st.subheader("🕸️ THE EVOLUTION & CONNECTION MATRIX")

nodes = [
    Node(id="Afton", label="William Afton", shape="circularImage", image=CHARACTERS["William Afton"]["img"], size=30),
    Node(id="Gabriel", label="Gabriel (Freddy)", shape="circularImage", image=CHARACTERS["Gabriel (Freddy)"]["img"], size=30),
    Node(id="Springtrap", label="Springtrap", shape="circularImage", image=CHARACTERS["Springtrap"]["img"], size=30),
    Node(id="Puppet", label="The Puppet (Charlie)", color="#FFFFFF", size=20)
]

edges = [
    Edge(source="Afton", target="Gabriel", label="Murderer (MCI 1985)", color="red"),
    Edge(source="Puppet", target="Gabriel", label="Gave Life", color="blue"),
    Edge(source="Afton", target="Springtrap", label="Evolution (Springlock)", color="purple")
]

config = Config(width=1200, height=600, directed=True, nodeHighlightBehavior=True)
agraph(nodes=nodes, edges=edges, config=config)