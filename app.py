import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
from langchain_groq import ChatGroq

# 1. PAGE CONFIG & STYLING
st.set_page_config(page_title="Zenith Lore Matrix", layout="wide")

# 2. AI CONNECT (Hard-coded Lore Guardrails)
llm = None
if "GROQ_API_KEY" in st.secrets:
    llm = ChatGroq(groq_api_key=st.secrets["GROQ_API_KEY"], model_name="llama-3.3-70b-versatile")

# 3. VERIFIED DATASET & GREETINGS
CHARACTERS = {
    "William Afton": {"img": "https://i.imgur.com/8mY8JmS.png", "msg": "⚠️ PRIORITY ALERT: Subject 'Afton' linked to Multiple Remnant Anomalies."},
    "Gabriel (Freddy)": {"img": "https://i.imgur.com/kO8G3u4.png", "msg": "📦 ASSET LOG: Retrieval of 1985 Incident Subject 01. Identity: Gabriel."},
    "Springtrap": {"img": "https://i.imgur.com/mO2P2hB.png", "msg": "☣️ BIOHAZARD DETECTED: Spring-Lock Failure Case #003."},
    "The Puppet": {"img": "https://i.imgur.com/V7H6uN5.png", "msg": "🎭 SYSTEM OVERRIDE: Subject identified as Charlotte Emily."},
    "Michael Afton": {"img": "https://i.imgur.com/8zW4G8E.png", "msg": "🧬 DNA MATCH: Terminal User recognized as 'Afton, M.'"},
    "Elizabeth Afton": {"img": "https://i.imgur.com/2Xy5E4r.png", "msg": "🍭 ASSET LOG: Circus Baby Prototype analysis... Subject: Elizabeth."},
    "Crying Child": {"img": "https://i.imgur.com/7yW3Kz1.png", "msg": "💔 CORRUPTED DATA: Subject [NULL] recovered from 1983 incident."}
}

# 4. SIDEBAR
with st.sidebar:
    st.title("👁️ ZENITH ARCHIVE")
    subject = st.selectbox("Subject Files:", ["Main Terminal"] + list(CHARACTERS.keys()))
    st.markdown("---")
    st.info("System Status: OPERATIONAL\n\nArchitect: DisMonkey")

# 5. MAIN TERMINAL / HOME PAGE
if subject == "Main Terminal":
    st.title("👁️ ZENITH LORE TERMINAL")
    st.image("https://i.imgur.com/92fHkeq.png", use_container_width=True)
    st.markdown("### Accessing Fazbear Records... System Clear.")
    
    # THE CONNECTION WEB (THE MASTER MAP)
    st.subheader("🕸️ THE CONNECTION MATRIX")
    nodes = [Node(id=name, label=name, shape="circularImage", image=data["img"], size=30) for name, data in CHARACTERS.items()]
    edges = [
        Edge(source="William Afton", target="Gabriel (Freddy)", label="Murderer (1985 MCI)", color="red"),
        Edge(source="The Puppet", target="Gabriel (Freddy)", label="Gave Life", color="blue"),
        Edge(source="William Afton", target="Springtrap", label="Evolution", color="purple"),
        Edge(source="William Afton", target="Michael Afton", label="Father", color="gray"),
        Edge(source="William Afton", target="Elizabeth Afton", label="Father", color="gray"),
        Edge(source="William Afton", target="Crying Child", label="Father", color="gray"),
    ]
    config = Config(width=1000, height=550, directed=True, nodeHighlightBehavior=True, highlightColor="#00FF00")
    agraph(nodes=nodes, edges=edges, config=config)

else:
    # 6. CHARACTER VIEW
    st.title(f"📊 DATA ENTRY: {subject}")
    st.warning(CHARACTERS[subject]["msg"]) # The "System Greeting"
    
    tab1, tab2, tab3 = st.tabs(["🖼️ Visual Intel", "📜 Deep Lore", "🧬 Evolution"])
    
    with tab1:
        st.image(CHARACTERS[subject]["img"], width=400)
    
    with tab2:
        if llm:
            with st.spinner("Analyzing Remnant..."):
                prompt = f"""Analyze lore for {subject}. 
                COMPLIANCE: Gabriel is an MCI victim (1985), NOT an Afton. 
                William's kids are ONLY Michael, Elizabeth, and Crying Child."""
                response = llm.invoke(prompt)
                st.markdown(response.content)
    
    with tab3:
        # PURE LORE SEQUENCE LOGIC
        if "Afton" in subject or "Spring" in subject:
            st.code("William Afton ➔ Springlock Failure ➔ Springtrap ➔ Scraptrap ➔ Glitchtrap")
        elif "Gabriel" in subject:
            st.code("Gabriel (Child) ➔ 1985 MCI ➔ Freddy Fazbear ➔ Molten Freddy ➔ Freed")
        elif "Michael" in subject:
            st.code("Michael Afton ➔ Foxy Bully ➔ Scooped (Ennard) ➔ Purple Corpse ➔ FFPS Fire")
        elif "Elizabeth" in subject:
            st.code("Elizabeth Afton ➔ Claw Incident ➔ Circus Baby ➔ Scrap Baby ➔ Freed")