import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
from langchain_groq import ChatGroq

st.set_page_config(page_title="Zenith Lore Matrix", layout="wide")

# Connect to AI
llm = None
if "GROQ_API_KEY" in st.secrets:
    llm = ChatGroq(groq_api_key=st.secrets["GROQ_API_KEY"], model_name="llama-3.3-70b-versatile")

# 1. THE STABLE IMAGE DATABASE (Direct Hosted)
# Note: If these show as broken, it's because these specific URLs changed. 
# You can replace them with Imgur or PostImages direct links.
CHARACTERS = {
    "William Afton": {"img": "https://img.vavel.com/afton-1634563200782.jpg", "color": "#800080"},
    "Gabriel (Freddy)": {"img": "https://p16-capcut-va.ibyteimg.com/tos-alisg-v-6433ca-sg/o0A6InEBI2BeIDEnLBAf7eEAIhA08f8tQAnmD3~tplv-nhvf63701l-webp.webp", "color": "#654321"},
    "Springtrap": {"img": "https://cdn.artstation.com/p/assets/images/images/048/850/644/large/m-the-springtrap-render.jpg", "color": "#556B2F"},
    "The Puppet": {"img": "https://m.media-amazon.com/images/I/419+jI668+L._AC_.jpg", "color": "#FFFFFF"}
}

# 2. SIDEBAR
with st.sidebar:
    st.title("👁️ ZENITH ARCHIVE")
    subject = st.selectbox("Select Subject:", ["Main Terminal"] + list(CHARACTERS.keys()))
    st.markdown("---")
    st.info("Architect: DisMonkey")

# 3. LORE CONTENT WITH TABS
if subject == "Main Terminal":
    st.title("💾 ZENITH LORE ARCHIVE")
    st.markdown("### System Online. Accessing Verified Fazbear Intel.")
    st.write("Select a subject in the sidebar to view detailed evolution and lore reports.")
else:
    st.title(f"📊 DATA ENTRY: {subject}")
    
    # --- THE LORE TAB SYSTEM ---
    tab1, tab2, tab3 = st.tabs(["🖼️ Visual Intel", "📜 Deep Lore", "🧬 Evolution Chain"])
    
    with tab1:
        st.image(CHARACTERS[subject]["img"], width=400, caption=f"Confirmed Visual: {subject}")
        
    with tab2:
        if llm:
            with st.spinner("Decrypting Archive..."):
                # FORCED LORE RULES - NO MORE ERRORS
                prompt = f"""
                Analyze the lore of {subject}. 
                STRICT COMPLIANCE: 
                - Gabriel possesses Freddy. He is a VICTIM of the 1985 MCI. 
                - Gabriel is NOT William Afton's son. 
                - Afton's children are ONLY Michael, Elizabeth, and the Crying Child.
                Describe his role in the 'Give Gifts, Give Life' event.
                """
                response = llm.invoke(prompt)
                st.markdown(response.content)
                
    with tab3:
        st.subheader("Transition History")
        if "Afton" in subject or "Spring" in subject:
            st.write("Human (Afton) → Springlock Failure → Springtrap → Scraptrap → Glitchtrap → Burntrap")
        elif "Gabriel" in subject:
            st.write("Child (Gabriel) → Victim of MCI → Freddy Fazbear → Molten Freddy → Freed Spirit")

# 4. THE CONNECTION WEB (Corrected and Stabilized)
st.markdown("---")
st.subheader("🕸️ THE CONNECTION MATRIX")

nodes = []
for name, data in CHARACTERS.items():
    nodes.append(Node(
        id=name, 
        label=name, 
        shape="circularImage", 
        image=data["img"], 
        size=35
    ))

edges = [
    Edge(source="William Afton", target="Gabriel (Freddy)", label="Murderer (MCI 1985)", color="#FF0000"),
    Edge(source="The Puppet", target="Gabriel (Freddy)", label="Gave Life", color="#00E6FF"),
    Edge(source="William Afton", target="Springtrap", label="Became", color="#800080")
]

config = Config(width=1200, height=600, directed=True, nodeHighlightBehavior=True, highlightColor="#ff4b4b")
agraph(nodes=nodes, edges=edges, config=config)