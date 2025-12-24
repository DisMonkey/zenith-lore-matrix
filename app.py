import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
from langchain_groq import ChatGroq

# 1. PAGE CONFIG
st.set_page_config(page_title="Zenith Lore Matrix", layout="wide")

# 2. AI BRAIN SETUP
llm = None
if "GROQ_API_KEY" in st.secrets:
    try:
        llm = ChatGroq(temperature=0.7, groq_api_key=st.secrets["GROQ_API_KEY"], model_name="llama-3.3-70b-versatile")
    except:
        st.error("AI Brain Offline.")

# 3. MASTER DATA DICTIONARY (Photos & Stats)
FAZBEAR_DB = {
    "Freddy Fazbear": {
        "img": "https://upload.wikimedia.org/wikipedia/en/2/22/Fnaf_character_freddy_fazbear.png",
        "platform": "Windows, iOS, Android, Console",
        "developer": "Scottgames, LLC",
        "release": "August 8, 2014",
        "role": "Lead Vocalist / Primary Antagonist"
    },
    "Golden Freddy": {
        "img": "https://static.wikia.nocookie.net/fivenightsatfreddys/images/a/a7/Golden_Freddy_FNaF1.png",
        "platform": "Spectral / Unknown",
        "developer": "Scottgames, LLC",
        "release": "August 8, 2014",
        "role": "Secret Spectral Entity"
    },
    "The Puppet": {
        "img": "https://static.wikia.nocookie.net/fnaf-world-rpg/images/b/b3/Puppet_jumpscare_FNAF2.gif",
        "platform": "FNAF 2, 6, UCN",
        "developer": "Fazbear Ent.",
        "release": "November 11, 2014",
        "role": "Spirit Guardian / Give Gifts, Give Life"
    }
}

# 4. SIDEBAR
with st.sidebar:
    st.title("🗄️ FAZBEAR WIKI MENU")
    st.markdown("---")
    character = st.selectbox("Search Archive:", ["Home Page"] + list(FAZBEAR_DB.keys()))
    st.info("ARCHITECT: DisMonkey")

# 5. MAIN CONTENT
if character == "Home Page":
    st.title("👁️ ZENITH LORE MATRIX")
    
    # --- YOUR WIKI GREETING ---
    st.markdown("""
    Welcome to the **Five Nights at Freddy's Wiki**, the comprehensive encyclopedia site about *Five Nights at Freddy's*.
    
    Join the collaborative community to detect recent information and announcements with us freely.
    > **Anyone can survive five nights. This time, there will be no second chances.**
    
    They're not just at Freddy's anymore. In 2023, Blumhouse's box-office horror phenomenon *Five Nights at Freddy's* became the highest-grossing horror film of the year. Now, a shocking new chapter of animatronic terror begins.
    
    **Latest News:** One year has passed since the supernatural nightmare at Freddy Fazbear's Pizza. As Abby sneaks out to reconnect with Freddy, Bonnie, Chica, and Foxy, it will set into motion a terrifying series of events, revealing dark secrets about the true origin of Freddy's.
    """)
    
    st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=1200", caption="Zenith Mainframe: Connected to Fazbear Servers", use_container_width=True)

else:
    # --- CHARACTER PAGE ---
    char_info = FAZBEAR_DB[character]
    st.title(f"📊 DATA ENTRY: {character}")
    
    col1, col2, col3 = st.columns([1, 1.5, 1])
    
    with col1:
        st.image(char_info["img"], caption=f"Visual Confirmation: {character}")
        
    with col2:
        if st.button(f"Extract AI Intel on {character}"):
            if llm:
                with st.spinner("Decrypting..."):
                    prompt = f"Provide a detailed lore report for {character}."
                    if character == "Golden Freddy":
                        prompt += " Specifically explain the connection to Freddy Fazbear and the Two Souls theory."
                    
                    response = llm.invoke([("system", "You are the Zenith Lore AI."), ("user", prompt)])
                    st.markdown(response.content)
            else:
                st.error("AI Brain not connected.")
                
    with col3:
        # Quick Info Table (Wiki Style)
        st.markdown(f"""
        ### Information
        **Platform:** {char_info['platform']}  
        **Developer:** {char_info['developer']}  
        **Release Date:** {char_info['release']}  
        **Role:** {char_info['role']}
        """)

# 6. ADVANCED CONNECTION WEB (Larger & Better)
st.markdown("---")
st.subheader("🕸️ THE CONNECTION MATRIX")

nodes = [
    Node(id="Afton", label="William Afton", color="#800080", size=30),
    Node(id="Puppet", label="The Puppet", color="#FFFFFF", size=25),
    Node(id="Freddy", label="Freddy Fazbear", color="#654321", size=25),
    Node(id="Gold", label="Golden Freddy", color="#FFD700", size=30),
    Node(id="Mike", label="Mike Schmidt", color="#4682B4", size=20)
]

edges = [
    Edge(source="Afton", target="Puppet", label="Murderer"),
    Edge(source="Puppet", target="Freddy", label="Gave Life"),
    Edge(source="Freddy", target="Gold", label="Spectral Mirror"),
    Edge(source="Mike", target="Freddy", label="Night Watch"),
    Edge(source="Afton", target="Gold", label="Killer of Cassidy")
]

config = Config(width=1200, height=600, directed=True, nodeHighlightBehavior=True, collapsible=True)
agraph(nodes=nodes, edges=edges, config=config)

# 7. FOOTER
st.markdown("---")
st.markdown("<div style='text-align: center; color: #555;'>ARCHITECT: <b>DisMonkey</b> | Wiki-Core v4.2</div>", unsafe_allow_html=True)