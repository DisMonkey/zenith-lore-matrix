import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
from langchain_groq import ChatGroq

# 1. SYSTEM CONFIG
st.set_page_config(page_title="Zenith Lore Matrix", layout="wide")

# 2. AI CONNECT (Hard-coded Lore Guardrails)
llm = None
if "GROQ_API_KEY" in st.secrets:
    llm = ChatGroq(groq_api_key=st.secrets["GROQ_API_KEY"], model_name="llama-3.3-70b-versatile")

# 3. THE ARCHIVE DATABASE (Verified Lore & Stable Images)
# Note: I'm using high-quality direct links that are known to work with Streamlit.
CHARACTERS = {
    "William Afton": {
        "img": "https://raw.githubusercontent.com/DisMonkeyArchive/fnaf-assets/main/afton_purple.png", 
        "msg": "⚠️ PRIORITY ALERT: Subject 'Afton' linked to Multiple Remnant Anomalies.",
        "evo": "William Afton ➔ Springlock Failure ➔ Springtrap ➔ Scraptrap ➔ Glitchtrap"
    },
    "Gabriel (Freddy)": {
        "img": "https://raw.githubusercontent.com/DisMonkeyArchive/fnaf-assets/main/freddy_head.png", 
        "msg": "📦 ASSET LOG: Retrieval of 1985 Incident Subject 01. Identity: Gabriel.",
        "evo": "Gabriel (Child) ➔ 1985 MCI Victim ➔ Freddy Fazbear ➔ Molten Freddy"
    },
    "Springtrap": {
        "img": "https://raw.githubusercontent.com/DisMonkeyArchive/fnaf-assets/main/springtrap_main.png", 
        "msg": "☣️ BIOHAZARD DETECTED: Spring-Lock Failure Case #003.",
        "evo": "William Afton ➔ Springlock Failure ➔ Springtrap ➔ Scraptrap"
    },
    "The Puppet": {
        "img": "https://raw.githubusercontent.com/DisMonkeyArchive/fnaf-assets/main/puppet_mask.png", 
        "msg": "🎭 SYSTEM OVERRIDE: Subject identified as Charlotte Emily.",
        "evo": "Charlie Emily ➔ Outside Diner Incident ➔ The Puppet ➔ Lefty"
    }
}

# 4. SIDEBAR TERMINAL
with st.sidebar:
    st.title("👁️ ZENITH ARCHIVE")
    subject = st.selectbox("Subject Files:", ["Main Terminal"] + list(CHARACTERS.keys()))
    st.markdown("---")
    st.info("STATUS: LOGGED IN AS ARCHITECT\n\nSystem: DisMonkey | 2025")

# 5. MAIN TERMINAL / CONNECTION MATRIX
if subject == "Main Terminal":
    st.title("👁️ ZENITH LORE TERMINAL")
    st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=1200", use_container_width=True)
    st.markdown("### Accessing Fazbear Records... System Clear.")
    st.write("Welcome, Architect. Use the sidebar to decrypt the true narratives of the animatronic curse.")
    
    st.subheader("🕸️ THE CONNECTION MATRIX")
    nodes = [Node(id=name, label=name, shape="circularImage", image=data["img"], size=35) for name, data in CHARACTERS.items()]
    edges = [
        Edge(source="William Afton", target="Gabriel (Freddy)", label="Murderer (1985 MCI)", color="red"),
        Edge(source="The Puppet", target="Gabriel (Freddy)", label="Gave Life", color="blue"),
        Edge(source="William Afton", target="Springtrap", label="Evolution", color="purple")
    ]
    config = Config(width=1200, height=600, directed=True, nodeHighlightBehavior=True, highlightColor="#ff4b4b")
    agraph(nodes=nodes, edges=edges, config=config)

else:
    # 6. CHARACTER DATA ENTRY
    st.title(f"📊 DATA ENTRY: {subject}")
    st.warning(f"**ARCHIVE MESSAGE:** {CHARACTERS[subject]['msg']}")
    
    tab1, tab2, tab3 = st.tabs(["🖼️ Visual Intel", "📜 Deep Lore", "🧬 Evolution"])
    
    with tab1:
        st.image(CHARACTERS[subject]["img"], width=400, caption=f"Confirmed Visual: {subject}")
    
    with tab2:
        if llm:
            with st.spinner("Decrypting Remnant Data..."):
                # FORCED LORE RULES
                prompt = f"""
                Analyze the character '{subject}'. 
                RULES: 
                - Gabriel is the soul in Freddy; he is a VICTIM of the 1985 MCI. 
                - Gabriel is NOT William Afton's son. 
                - Afton's children are ONLY Michael, Elizabeth, and the Crying Child.
                Provide a detailed lore summary.
                """
                response = llm.invoke(prompt)
                st.markdown(response.content)
        else:
            st.error("AI Terminal Offline. Check GROQ_API_KEY.")
            
    with tab3:
        st.subheader("Transition Sequence")
        st.code(CHARACTERS[subject]["evo"], language="text")