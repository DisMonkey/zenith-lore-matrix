import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
from langchain_groq import ChatGroq

st.set_page_config(page_title="Zenith Lore Matrix", layout="wide")

# 1. AI BRAIN SETUP (With Hard-Coded Lore Truths)
llm = None
if "GROQ_API_KEY" in st.secrets:
    llm = ChatGroq(groq_api_key=st.secrets["GROQ_API_KEY"], model_name="llama-3.3-70b-versatile")

# 2. STABLE IMAGE DATABASE
# If these don't show in the web, the sidebar 'Visual Intel' tab will still show them properly.
CHARACTERS = {
    "William Afton": "https://raw.githubusercontent.com/DisMonkeyArchive/fnaf-assets/main/afton.png",
    "Gabriel (Freddy)": "https://raw.githubusercontent.com/DisMonkeyArchive/fnaf-assets/main/freddy.png",
    "Springtrap": "https://raw.githubusercontent.com/DisMonkeyArchive/fnaf-assets/main/springtrap.png",
    "The Puppet": "https://raw.githubusercontent.com/DisMonkeyArchive/fnaf-assets/main/puppet.png"
}

# 3. SIDEBAR SELECTION
with st.sidebar:
    st.title("👁️ ZENITH ARCHIVE")
    subject = st.selectbox("Subject Files:", ["Main Terminal"] + list(CHARACTERS.keys()))
    st.markdown("---")
    st.info("System: DisMonkey | 2025")

# 4. THE LORE TABS (The fix you asked for)
if subject == "Main Terminal":
    st.title("👁️ ZENITH LORE TERMINAL")
    st.markdown("### Accessing Fazbear Records... System Clear.")
    st.write("Welcome to the Archive. Select a character to analyze their evolution.")
else:
    st.title(f"📊 DATA ENTRY: {subject}")
    
    # --- CREATING THE TABS ---
    tab1, tab2, tab3 = st.tabs(["🖼️ Visual Intel", "📜 Deep Lore", "🧬 Evolution"])

    with tab1:
        st.subheader("Physical Description")
        # st.image is much more stable than the web nodes for showing photos
        st.image(CHARACTERS[subject], width=400, caption=f"Visual Confirmation: {subject}")

    with tab2:
        st.subheader("Historical Records")
        if llm:
            with st.spinner("Analyzing Remnant..."):
                # FORCED LORE RULES: Gabriel is a victim, not a son.
                prompt = f"""
                Analyze the character '{subject}'. 
                RULES: 
                - Gabriel is the soul in Freddy. He is a VICTIM of William Afton.
                - Gabriel is NOT William Afton's son.
                - William's children are Michael, Elizabeth, and the Crying Child.
                Describe {subject}'s specific contribution to the FNaF timeline.
                """
                response = llm.invoke(prompt)
                st.markdown(response.content)

    with tab3:
        st.subheader("Evolution Sequence")
        if "Afton" in subject or "Spring" in subject:
            st.markdown("**Sequence:** William Afton → Springlock Failure → Springtrap → Scraptrap → Glitchtrap → Burntrap")
        elif "Gabriel" in subject:
            st.markdown("**Sequence:** Child (Gabriel) → MCI Victim → Freddy Fazbear → Molten Freddy → Happiest Day")

# 5. THE CONNECTION WEB (Fixed Highlighting)
st.markdown("---")
st.subheader("🕸️ THE CONNECTION MATRIX")

nodes = [
    Node(id="Afton", label="William Afton", color="#800080", size=30),
    Node(id="Gabriel", label="Gabriel (Freddy)", color="#654321", size=30),
    Node(id="Springtrap", label="Springtrap", color="#556B2F", size=30),
    Node(id="Puppet", label="The Puppet", color="#FFFFFF", size=30)
]

edges = [
    Edge(source="Afton", target="Gabriel", label="Murderer (1985 MCI)", color="red"),
    Edge(source="Puppet", target="Gabriel", label="Gave Life", color="blue"),
    Edge(source="Afton", target="Springtrap", label="Evolution", color="purple")
]

config = Config(width=1200, height=600, directed=True, nodeHighlightBehavior=True, highlightColor="#ff4b4b")
agraph(nodes=nodes, edges=edges, config=config)