import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
from langchain_groq import ChatGroq

# 1. SETUP
st.set_page_config(page_title="Zenith Lore Matrix", layout="wide")

# Connect to Groq AI
llm = None
if "GROQ_API_KEY" in st.secrets:
    llm = ChatGroq(groq_api_key=st.secrets["GROQ_API_KEY"], model_name="llama-3.3-70b-versatile")

# 2. LOCAL DATA (Hardcoded for speed, AI handles the rest)
CHARACTERS = {
    "Freddy Fazbear": "https://upload.wikimedia.org/wikipedia/en/2/22/Fnaf_character_freddy_fazbear.png",
    "Bonnie": "https://static.wikia.nocookie.net/fivenightsatfreddys/images/1/10/Bonnie_FNaF1.png",
    "Chica": "https://static.wikia.nocookie.net/fivenightsatfreddys/images/b/be/Chica_FNaF1.png",
    "Foxy": "https://static.wikia.nocookie.net/fivenightsatfreddys/images/7/77/Foxy_FNaF1.png",
    "Springtrap": "https://static.wikia.nocookie.net/fivenightsatfreddys/images/4/4c/Springtrap_FNaF3.png",
    "The Puppet": "https://static.wikia.nocookie.net/fivenightsatfreddys/images/1/10/The_Puppet.png"
}

# 3. CUSTOM IMMERSIVE GREETING (No Plagiarism)
def show_home():
    st.title("👁️ ZENITH LORE ARCHIVE")
    st.markdown("""
    ### System Initialized... Accessing Fazbear Historical Data.
    Welcome, Architect. You have entered the **Zenith Matrix**, a decentralized repository for the 
    complex history of the Fazbear Entertainment franchise. 
    
    This archive tracks the evolution of indie horror, from the 1983 'Bite' incidents to the modern 
    Blumhouse cinematic era. Explore the data entries to uncover the truth behind the spirits, 
    the steel, and the man behind the mask.
    
    **Instructions:** Use the dropdown in the sidebar to select a subject for deep-scan analysis.
    """)
    st.image("https://images.unsplash.com/photo-1614728263952-84ea206f99b6?w=1000", caption="Matrix Link Active")

# 4. SIDEBAR
with st.sidebar:
    st.header("🗄️ ARCHIVE CONTROLS")
    # Dropdown for all lore
    subject = st.selectbox("Select Subject:", ["Main Terminal"] + list(CHARACTERS.keys()) + ["Search New Subject..."])
    
    if subject == "Search New Subject...":
        custom_search = st.text_input("Enter Character Name:")
        if custom_search:
            subject = custom_search

# 5. DYNAMIC LORE GENERATOR
if subject == "Main Terminal":
    show_home()
else:
    st.header(f"📊 DATA ENTRY: {subject}")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Display Image (Local if exists, otherwise placeholder)
        img_url = CHARACTERS.get(subject, "https://via.placeholder.com/400x500?text=No+Image+Found")
        st.image(img_url, use_container_width=True)
        st.caption(f"Visual Scan: {subject}")
        
    with col2:
        if llm:
            with st.spinner(f"AI is researching {subject}..."):
                # The AI "finds" the bio and lore contribution
                prompt = f"""
                Act as a Lore Historian. Provide a report on '{subject}' from Five Nights at Freddy's.
                Include:
                1. A brief Bio.
                2. Their specific Contribution to the Lore (what they did or symbolize).
                3. A 'Deep Secret' or theory about them.
                Keep it professional and concise.
                """
                response = llm.invoke(prompt)
                st.markdown(response.content)
        else:
            st.warning("Please connect your GROQ_API_KEY in secrets to use the AI Researcher.")

# 6. LORE WEB (Visualizing the connections)
st.markdown("---")
st.subheader("🕸️ THE CONNECTION MATRIX")
nodes = [Node(id=name, label=name, size=20) for name in CHARACTERS.keys()]
edges = [Edge(source="Springtrap", target="Freddy", label="Killer")]
config = Config(width=1000, height=400, directed=True)
agraph(nodes=nodes, edges=edges, config=config)