
import streamlit as st
from Agents import agent


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="City AI Assistant",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =====================================================
# CUSTOM CSS - LIGHT THEME
# =====================================================

st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #F8FAFC !important;
    color: #1E293B !important;
}

/* Main content area */
[data-testid="stMain"] {
    background-color: #F8FAFC !important;
}

/* Header */
[data-testid="stHeader"] {
    background-color: #F8FAFC !important;
}

/* Main headings */
.stApp h1, .stApp h2, .stApp h3, .stApp h4 {
    color: #172554 !important;
}

/* Normal text */
.stApp p,
.stApp li,
.stApp label {
    color: #334155 !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #EFF6FF !important;
    border-right: 1px solid #DBEAFE;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] h4 {
    color: #1E3A8A !important;
}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] small {
    color: #475569 !important;
}

/* Feature cards */
.feature-card {
    background-color: #FFFFFF;
    border: 1px solid #DBEAFE;
    border-radius: 14px;
    padding: 16px;
    margin-bottom: 12px;
}

.feature-card h4 {
    color: #1D4ED8 !important;
    margin-top: 0;
}

.feature-card p,
.feature-card small {
    color: #64748B !important;
}

/* Main title */
.main-title {
    text-align: center;
    color: #1E3A8A !important;
    font-size: 38px;
    font-weight: 800;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #64748B !important;
    font-size: 16px;
    margin-bottom: 30px;
}

/* Chat messages */
[data-testid="stChatMessage"] {
    background-color: #FFFFFF !important;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    padding: 16px;
    margin-bottom: 12px;
}

[data-testid="stChatMessage"] p,
[data-testid="stChatMessage"] li {
    color: #334155 !important;
}

/* Chat input container */
[data-testid="stChatInput"] {
    background-color: #FFFFFF !important;
    border: 1px solid #CBD5E1 !important;
    border-radius: 14px !important;
}

/* Chat input text */
[data-testid="stChatInput"] textarea {
    background-color: #FFFFFF !important;
    color: #1E293B !important;
    caret-color: #2563EB !important;
}

[data-testid="stChatInput"] textarea::placeholder {
    color: #94A3B8 !important;
}

/* Buttons */
.stButton > button {
    background-color: #FFFFFF !important;
    color: #1D4ED8 !important;
    border: 1px solid #BFDBFE !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    transition: 0.2s ease;
}

.stButton > button:hover {
    background-color: #DBEAFE !important;
    border-color: #2563EB !important;
}

/* Info boxes */
[data-testid="stAlert"] {
    background-color: #EFF6FF !important;
    border: 1px solid #BFDBFE !important;
}

[data-testid="stAlert"] p {
    color: #1E3A8A !important;
}

/* Links */
.stApp a {
    color: #2563EB !important;
}

/* Divider */
hr {
    border-color: #DBEAFE !important;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# SESSION STATE
# =====================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.markdown("## 🌍 City AI")
    st.caption("Your intelligent city assistant")

    st.divider()

    st.markdown("### ✨ Features")

    st.markdown("""
    <div class="feature-card">
        <h4>🌦️ Weather Updates</h4>
        <small>Get current weather and temperature of any city.</small>
    </div>

    <div class="feature-card">
        <h4>📰 Latest News</h4>
        <small>Discover the latest news and updates about cities.</small>
    </div>

    <div class="feature-card">
        <h4>🤖 AI Assistant</h4>
        <small>Ask questions using natural language.</small>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("### 💡 Try asking")

    examples = [
        "What is the weather in Surat?",
        "Get latest news about Ahmedabad",
        "Tell me weather and news of Bharuch"
    ]

    for example in examples:

        if st.button(example, use_container_width=True):
            st.session_state.pending_prompt = example
            st.rerun()

    st.divider()

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.caption("Powered by Gemini • Tavily • OpenWeather")


# =====================================================
# MAIN HEADER
# =====================================================

st.markdown(
    '<div class="main-title">🌍 City AI Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Your smart companion for weather and city news'
    '</div>',
    unsafe_allow_html=True
)


# =====================================================
# WELCOME SCREEN
# =====================================================

if not st.session_state.messages:

    st.markdown("### 👋 Welcome!")

    st.write(
        "Ask me about any Indian city. "
        "I can help you find its current weather "
        "and latest news."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.info(
            "🌦️ **Weather Updates**\n\n"
            "Check current temperature, humidity "
            "and weather conditions."
        )

    with col2:
        st.info(
            "📰 **City News**\n\n"
            "Discover the latest news and updates "
            "about your city."
        )


# =====================================================
# DISPLAY CHAT HISTORY
# =====================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# =====================================================
# RESPONSE EXTRACTION
# =====================================================

def extract_response(result):

    messages = result.get("messages", [])

    # Find the last AI message without tool calls
    for msg in reversed(messages):

        if (
            getattr(msg, "type", "") == "ai"
            and not getattr(msg, "tool_calls", [])
            and getattr(msg, "content", "")
        ):

            content = msg.content

            if isinstance(content, str):
                return content

            if isinstance(content, list):

                text_parts = []

                for block in content:

                    if isinstance(block, dict):
                        if block.get("type") == "text":
                            text_parts.append(block.get("text", ""))

                return "\n".join(text_parts)

    return "Sorry, I couldn't generate a response. Please try again."


# =====================================================
# CHAT INPUT
# =====================================================

prompt = st.chat_input(
    "Ask about weather or news in any city..."
)

# Handle example questions from sidebar
if "pending_prompt" in st.session_state:
    prompt = st.session_state.pop("pending_prompt")


if prompt:

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("🤖 City AI is searching and thinking..."):

            try:

                result = agent.invoke({
                    "messages": [
                        {
                            "role": msg["role"],
                            "content": msg["content"]
                        }
                        for msg in st.session_state.messages
                    ]
                })

                answer = extract_response(result)

            except Exception as e:

                error = str(e)

                if "429" in error or "RESOURCE_EXHAUSTED" in error:

                    answer = (
                        "⚠️ **Gemini API quota exceeded!**\n\n"
                        "Your free-tier request limit has been reached. "
                        "Please wait for your quota to reset.\n\n"
                        "[Check Gemini API usage](https://ai.dev/rate-limit)"
                    )

                else:
                    answer = (
                        "⚠️ **Something went wrong!**\n\n"
                        f"```text\n{error}\n```"
                    )

        st.markdown(answer)

    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
