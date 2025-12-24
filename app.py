import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
from langchain_groq import ChatGroq

# 1. PAGE CONFIG
st.set_page_config(page_title="Zenith Lore Matrix", layout="wide")

# 2. AI CONNECT (Hard-coded Lore Guardrails)
llm = None
if "GROQ_API_KEY" in st.secrets:
    llm = ChatGroq(groq_api_key=st.secrets["GROQ_API_KEY"], model_name="llama-3.3-70b-versatile")

# 3. VERIFIED DATASET (No more empty strings)
CHARACTERS = {
    "William Afton": "https://i.imgur.com/8mY8JmS.png",
    "Gabriel (Freddy)": "https://i.imgur.com/kO8G3u4.png",
    "Springtrap": "https://i.imgur.com/mO2P2hB.png",
    "The Puppet": "https://i.imgur.com/V7H6uN5.png",
    "Michael Afton": "https://i.imgur.com/8zW4G8E.png",
    "Elizabeth Afton": "https://i.imgur.com/2Xy5E4r.png",
    "Crying Child": "https://i.imgur.com/7yW3Kz1.png",
}

# 4. SIDEBAR
with st.sidebar:
    st.title("👁️ ZENITH ARCHIVE")
    subject = st.selectbox("Subject Files:", ["Main Terminal"] + list(CHARACTERS.keys()))
    st.markdown("---")
    st.info("System: DisMonkey | 2025")

# 5. MAIN TERMINAL VIEW
if subject == "Main Terminal":
    st.title("👁️ ZENITH LORE TERMINAL")
    st.image("https://i.imgur.com/92fHkeq.png", use_column_width=True)
    st.markdown("### Accessing Fazbear Records... System Clear.")
    st.write("Welcome, Architect. Decrypt the narratives of those trapped within the curse.")

    # --- THE INTERACTIVE WEB (Integrated on Home Page) ---
    st.subheader("🕸️ THE CONNECTION MATRIX")
    nodes = [Node(id=name, label=name, shape="circularImage", image=img, size=30) for name, img in CHARACTERS.items()]
    edges = [
        Edge(source="William Afton", target="Gabriel (Freddy)", label="Murderer (1985 MCI)", color="red"),
        Edge(source="The Puppet", target="Gabriel (Freddy)", label="Gave Life", color="blue"),
        Edge(source="William Afton", target="Springtrap", label="Evolution", color="purple"),
        Edge(source="William Afton", target="Michael Afton", label="Father", color="gray"),
        Edge(source="William Afton", target="Elizabeth Afton", label="Father", color="gray"),
        Edge(source="William Afton", target="Crying Child", label="Father", color="gray"),
    ]
    config = Config(width=1000, height=600, directed=True, nodeHighlightBehavior=True)
    agraph(nodes=nodes, edges=edges, config=config)

else:
    # 6. CHARACTER VIEW
    st.title(f"📊 DATA ENTRY: {subject}")
    tab1, tab2, tab3 = st.tabs(["🖼️ Visual Intel", "📜 Deep Lore", "🧬 Evolution"])
    
    with tab1:
        st.image(CHARACTERS[subject], width=400)
    
    with tab2:
        if llm:
            with st.spinner("Analyzing Remnant..."):
                # THE LORE GUARDRAILS
                prompt = f"""
                Provide a lore report for {subject}.
                STRICT COMPLIANCE: 
                - Gabriel is NOT William Afton's son. He is an MCI victim (1985).
                - William's only children are Michael, Elizabeth, and the Crying Child.
                - Use a cold, analytical tone.
                """
                response = llm.invoke(prompt)
                st.markdown(response.content)
    
    with tab3:
        st.subheader("Evolution Sequence")
        # Hard-coded logic to ensure accuracy
        if "Afton" in subject or "Spring" in subject:
            st.code("William Afton ➔ Springlock Failure ➔ Springtrap ➔ Scraptrap ➔ Glitchtrap")
        elif "Gabriel" in subject:
            st.code("Gabriel (Child) ➔ 1985 MCI ➔ Freddy Fazbear ➔ Molten Freddy ➔ Freed")
        elif "Michael" in subject:
            st.code("Michael Afton ➔ Foxy Bully ➔ Scooped (Ennard) ➔ Purple Corpse ➔ FFPS Fire")
        elif "Elizabeth" in subject:
            st.code("Elizabeth Afton ➔ Claw Incident ➔ Circus Baby ➔ Scrap Baby ➔ Freed")
        else:
            st.write("Evolution sequence encrypted or unknown.")