import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
from langchain_groq import ChatGroq

# 1. PAGE CONFIG
st.set_page_config(page_title="Zenith Lore Matrix", layout="wide")

# 2. AI BRAIN SETUP - Improved error handling
llm = None
if "GROQ_API_KEY" in st.secrets:
    try:
        llm = ChatGroq(
            temperature=0.5, 
            groq_api_key=st.secrets["GROQ_API_KEY"], 
            model_name="llama-3.3-70b-versatile" # Updated to a more stable model
        )
    except Exception as e:
        st.error(f"AI Connection Error: {e}")
else:
    st.warning("Missing API Key in Streamlit Secrets!")

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    st.title("🗄️ ARCHIVE MENU")
    # We keep the selectbox so you can add games later!
    game_choice = st.selectbox("Select Game:", ["FNAF", "Bendy", "Home"])
    
    character = "None"
    if game_choice == "FNAF":
        character = st.selectbox("Select Character:", ["Freddy Fazbear", "Bonnie", "Chica", "Foxy", "William Afton", "The Puppet", "Golden Freddy"])
    elif game_choice == "Bendy":
        character = st.selectbox("Select Character:", ["Bendy", "Boris", "Alice Angel"])

# 4. NEWS TICKER
st.markdown(f"<marquee style='color:#ff4b4b; font-size:22px; font-family:monospace;'><b>SYSTEM ALERT:</b> Analyzing {character} • DisMonkey Secure Link Established...</marquee>", unsafe_allow_html=True)

# 5. DYNAMIC CONTENT
if game_choice == "Home":
    st.title("👁️ ZENITH LORE MATRIX")
    st.write("Welcome, Architect DisMonkey. Select a game file from the sidebar.")
else:
    st.title(f"📊 DATA ENTRY: {character}")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Better Image Mapping
        images = {
            "Freddy Fazbear": "https://upload.wikimedia.org/wikipedia/en/2/22/Fnaf_character_freddy_fazbear.png",
            "William Afton": "https://static.wikia.nocookie.net/fnaf-world-rpg/images/0/0b/Springtrap_FNAF3.png",
            "The Puppet": "https://static.wikia.nocookie.net/fnaf-world-rpg/images/b/b3/Puppet_jumpscare_FNAF2.gif",
            "Bonnie": "https://static.wikia.nocookie.net/fivenightsatfreddys/images/1/10/Bonnie_FNaF1.png",
            "Chica": "https://static.wikia.nocookie.net/fivenightsatfreddys/images/b/be/Chica_FNaF1.png",
            "Foxy": "https://static.wikia.nocookie.net/fivenightsatfreddys/images/7/77/Foxy_FNaF1.png",
            "Bendy": "https://static.wikia.nocookie.net/bendy-and-the-ink-machine/images/8/8e/Ink_Demon_Model.png"
        }
        img_url = images.get(character, "https://via.placeholder.com/300?text=SCANNING_FILE...")
        st.image(img_url, caption=f"Visual Confirmation: {character}")

    with col2:
        if st.button(f"Analyze {character} with AI"):
            if llm:
                with st.spinner("Decrypting Lore..."):
                    try:
                        # Fixed the way the prompt is sent to the AI
                        response = llm.invoke([("system", "You are the Zenith Lore AI. Provide dark, mysterious intel."), ("user", f"Lore profile for {character} from {game_choice}.")])
                        st.markdown(f"### AI INTEL REPORT\n{response.content}")
                    except Exception as e:
                        st.error(f"AI failed to process request. Check if your API key is active. Error: {e}")
            else:
                st.error("AI Brain is not configured.")

# 6. VISUAL WEB MATRIX (FNAF Focused)
st.markdown("---")
st.subheader("🕸️ THE CONNECTION WEB")
nodes = [
    Node(id="Afton", label="Afton", color="#800080", size=25),
    Node(id="Freddy", label="Freddy", color="#654321", size=20),
    Node(id="Puppet", label="The Puppet", color="#FFFFFF", size=25),
    Node(id="Gold", label="Golden Freddy", color="#FFD700", size=20)
]
edges = [
    Edge(source="Afton", target="Puppet", label="first_victim"),
    Edge(source="Puppet", target="Freddy", label="gave_life"),
    Edge(source="Freddy", target="Gold", label="connected_to")
]
agraph(nodes=nodes, edges=edges, config=Config(width=1000, height=400, directed=True))

# 7. FOOTER
st.markdown("---")
st.markdown("<div style='text-align: center; color: #555;'>ARCHITECT: <b>DisMonkey</b></div>", unsafe_allow_html=True)