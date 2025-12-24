import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
from langchain_groq import ChatGroq

# 1. PAGE CONFIG & THEME
st.set_page_config(page_title="Zenith Lore Matrix", layout="wide")

# 2. AI BRAIN SETUP
# This connects to the Secret Key you added to Streamlit
try:
    llm = ChatGroq(
        temperature=0.5, 
        groq_api_key=st.secrets["GROQ_API_KEY"], 
        model_name="llama3-8b-8192"
    )
except Exception as e:
    st.warning("AI Core Offline. Check your Streamlit Secrets for the GROQ_API_KEY.")

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    st.title("🗄️ ARCHIVE MENU")
    st.markdown("---")
    game_choice = st.selectbox("Select Game:", ["Home", "FNAF", "Bendy"])
    
    character = "None"
    if game_choice == "FNAF":
        character = st.selectbox("Select Character:", ["Freddy Fazbear", "Bonnie", "Chica", "Foxy", "William Afton", "The Puppet"])
    elif game_choice == "Bendy":
        character = st.selectbox("Select Character:", ["Bendy", "Boris", "Alice Angel", "Sammy Lawrence", "The Projectionist"])

# 4. NEWS TICKER
st.markdown(f"<marquee style='color:#ff4b4b; font-size:22px; font-family:monospace;'><b>SYSTEM ALERT:</b> AI Core Online • Analyzing {character} • Source: DisMonkey Archives</marquee>", unsafe_allow_html=True)

# 5. DYNAMIC CONTENT
if game_choice == "Home":
    st.title("👁️ ZENITH LORE MATRIX")
    st.write("Welcome, Architect. Use the sidebar to extract intelligence from the Fazbear and Joey Drew archives.")
    st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&q=80&w=1000", caption="Zenith Mainframe Online", use_container_width=True)

else:
    st.title(f"📊 DATA ENTRY: {character}")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # IMAGE LOGIC
        if "Freddy" in character: img = "https://upload.wikimedia.org/wikipedia/en/2/22/Fnaf_character_freddy_fazbear.png"
        elif "Afton" in character: img = "https://static.wikia.nocookie.net/fnaf-world-rpg/images/0/0b/Springtrap_FNAF3.png"
        elif "Bendy" in character: img = "https://static.wikia.nocookie.net/bendy-and-the-ink-machine/images/8/8e/Ink_Demon_Model.png"
        elif "Puppet" in character: img = "https://static.wikia.nocookie.net/fnaf-world-rpg/images/b/b3/Puppet_jumpscare_FNAF2.gif"
        else: img = "https://via.placeholder.com/300?text=SCANNING_FILE..."
        
        st.image(img, caption=f"Visual Confirmation: {character}")

    with col2:
        if st.button(f"Analyze {character} with AI"):
            with st.spinner("Accessing encrypted files..."):
                # The AI generates the lore for you!
                response = llm.invoke(f"Provide a brief, mysterious lore profile for {character} from the game {game_choice}. Include their role and a dark secret.")
                st.markdown(f"### AI INTEL REPORT\n{response.content}")
        else:
            st.info("Click the button above to have the AI generate the character lore.")

# 6. VISUAL WEB MATRIX (The graph you requested)
st.markdown("---")
st.subheader("🕸️ THE CONNECTION WEB")
nodes = [
    Node(id="Afton", label="Afton", color="#800080", size=25),
    Node(id="Spring", label="Springtrap", color="#228B22", size=20),
    Node(id="Ink", label="Ink Demon", color="#000000", size=25),
    Node(id="Puppet", label="The Puppet", color="#FFFFFF", size=20)
]
edges = [
    Edge(source="Afton", target="Spring", label="becomes"),
    Edge(source="Spring", target="Ink", label="corrupted_link"),
    Edge(source="Afton", target="Puppet", label="first_victim")
]

config = Config(width=1000, height=400, directed=True, nodeHighlightBehavior=True, collapsible=True)
agraph(nodes=nodes, edges=edges, config=config)

# 7. FOOTER CREDITS (DisMonkey)
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #555; font-family: monospace;'>"
    "ARCHIVE VERSION: 2.0.1 | ARCHITECT: <b>DisMonkey</b><br>"
    "© 2025 ZENITH-LORE-MATRIX"
    "</div>", 
    unsafe_allow_html=True
)