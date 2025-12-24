import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
from langchain_groq import ChatGroq

# 1. PAGE CONFIG
st.set_page_config(page_title="Zenith Lore Matrix", layout="wide")

# 2. AI BRAIN SETUP (Safe Check)
llm = None
if "GROQ_API_KEY" in st.secrets:
    try:
        # Using the new, more stable model name
        llm = ChatGroq(
            temperature=0.7, 
            groq_api_key=st.secrets["GROQ_API_KEY"], 
            model_name="llama-3.3-70b-versatile" 
        )
    except Exception as e:
        st.error(f"System Error: {e}")

# 3. SIDEBAR NAVIGATION (FNAF Only)
with st.sidebar:
    st.title("🗄️ ARCHIVE MENU")
    st.markdown("---")
    
    # Selection focused on FNAF characters
    character = st.selectbox(
        "Select Character Intel:", 
        ["Home", "Freddy Fazbear", "Bonnie", "Chica", "Foxy", "William Afton", "The Puppet", "Golden Freddy"]
    )

# 4. NEWS TICKER
st.markdown(f"<marquee style='color:#ff4b4b; font-size:22px; font-family:monospace;'><b>SYSTEM ALERT:</b> Analyzing {character} • DisMonkey Secure Link established...</marquee>", unsafe_allow_html=True)

# 5. DYNAMIC CONTENT
if character == "Home":
    st.title("👁️ ZENITH LORE MATRIX")
    st.write("Welcome, Architect DisMonkey. Select a Fazbear file from the sidebar to begin.")
    st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=1000", caption="Zenith Mainframe Online", use_container_width=True)

else:
    st.title(f"📊 DATA ENTRY: {character}")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Direct FNAF image mapping
        images = {
            "Freddy Fazbear": "https://upload.wikimedia.org/wikipedia/en/2/22/Fnaf_character_freddy_fazbear.png",
            "William Afton": "https://static.wikia.nocookie.net/fnaf-world-rpg/images/0/0b/Springtrap_FNAF3.png",
            "The Puppet": "https://static.wikia.nocookie.net/fnaf-world-rpg/images/b/b3/Puppet_jumpscare_FNAF2.gif",
            "Bonnie": "https://static.wikia.nocookie.net/fivenightsatfreddys/images/1/10/Bonnie_FNaF1.png",
            "Chica": "https://static.wikia.nocookie.net/fivenightsatfreddys/images/b/be/Chica_FNaF1.png",
            "Foxy": "https://static.wikia.nocookie.net/fivenightsatfreddys/images/7/77/Foxy_FNaF1.png",
            "Golden Freddy": "https://static.wikia.nocookie.net/fivenightsatfreddys/images/a/a7/Golden_Freddy_FNaF1.png"
        }
        st.image(images.get(character, "https://via.placeholder.com/300?text=SCANNING..."), caption=f"Visual Confirmation: {character}")

    with col2:
        if st.button(f"Analyze {character} with AI"):
            if llm:
                with st.spinner("Decrypting Fazbear Lore..."):
                    try:
                        # Formatting as a list of messages to prevent BadRequestError
                        messages = [
                            ("system", "You are the Zenith Lore AI. Provide dark, mysterious intel about FNAF."),
                            ("user", f"Explain the role and dark secret of {character} in Five Nights at Freddy's.")
                        ]
                        response = llm.invoke(messages)
                        st.markdown(f"### AI INTEL REPORT\n{response.content}")
                    except Exception as e:
                        st.error(f"AI Core Error. Check your Groq usage limit or API Key. Details: {e}")
            else:
                st.error("AI Brain missing GROQ_API_KEY in Secrets.")

# 6. VISUAL WEB MATRIX (FNAF Only)
st.markdown("---")
st.subheader("🕸️ THE CONNECTION WEB")
nodes = [
    Node(id="Afton", label="Afton", color="#800080", size=25),
    Node(id="Puppet", label="The Puppet", color="#FFFFFF", size=25),
    Node(id="Freddy", label="Freddy", color="#654321", size=20),
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