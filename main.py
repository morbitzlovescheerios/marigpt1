import streamlit as st
import random
import time
import os

# --- 1. CONFIGURATION & GREEN THEME ---
st.set_page_config(page_title="MarkiGPT 1.0", page_icon="⬛", layout="centered")

# --- INITIALIZE SESSION STATE EARLY ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Custom CSS for the "Spotify" look (Dark Mode + Green Accents)
st.markdown("""
<style>
    /* Main Background */
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
        font-family: monospace;
    }
    
    /* Input Box Styling */
    .stTextInput input {
        background-color: #0a0a0a;
        color: white;
        border: 1px solid #333;
        border-radius: 8px;
    }
    
    /* Buttons (High Contrast White on Black) */
    div.stButton > button {
        background-color: #FFFFFF;
        color: black;
        border-radius: 8px;
        border: none;
        font-weight: bold;
        width: 100%;
    }
    div.stButton > button:hover {
        background-color: #cccccc;
        border: none;
        color: black;
    }

    /* Headers */
    h1, h2, h3 {
        font-family: monospace;
        font-weight: 700;
        letter-spacing: -1px;
    }
    
    /* Metrics */
    div[data-testid="stMetricValue"] {
        color: #FFFFFF;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. AI BRAIN (Generic Responses) ---
GENERIC_RESPONSES = [
    "I am processing your request...",
    "That is a very interesting perspective.",
    "As an AI, I don't have feelings, but if I did, I'd be confused.",
    "Could you please rephrase that?",
    "I am MarkiGPT 1.0, running on local Python logic.",
    "My calculations suggest that is correct.",
    "I am unable to connect to the mothership right now.",
    "Beep boop. I am listening.",
    "I am analyzing the quantum fluctuations of your request.",
    "My neural networks are currently optimizing.",
    "That input exceeds my current emotional capacity.",
    "404: Context not found. Just kidding, I am listening.",
    "I am a simple AI build with Streamlit and Python logic.",
    "The person who made me is a genius, but I am not sure how to respond to that, his name is Jam1o!"
]

def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Greetings! I am MarkiGPT. How can I assist you today?"
    elif "name" in user_input:
        return "My name is MarkiGPT 1.0."
    elif "joke" in user_input:
        return "Why did the Python programmer break up with the C++ programmer? They didn't have any class."
    elif "music" in user_input:
        return "I have deleted my music database to focus on pure intelligence."
    elif "weather" in user_input:
        return "I do not have windows, but I predict it is dark inside the server."
    elif "meaning of life" in user_input:
        return "42. Obviously."
    elif "status" in user_input:
        return "All systems operational. CPU temperature is nominal."
    elif "python" in user_input or "code" in user_input:
        return """Here is a Python example for you:
```python
def hello_world():
    print("Hello from MarkiGPT!")
```"""
    else:
        return random.choice(GENERIC_RESPONSES)

# --- 3. UI HEADER ---
st.title("MarkiGPT 1.0")
st.caption("A custom-built Artificial Intelligence.")

# --- 3.5 SIDEBAR SETTINGS ---
with st.sidebar:
    # Check if a logo file exists and display it
    if os.path.exists("logo.png"):
        st.image("logo.png", use_container_width=True)
    elif os.path.exists("logo.jpg"):
        st.image("logo.jpg", use_container_width=True)

    st.header("Settings")
    
    # QoL: Adjustable thinking speed
    thinking_time = st.slider("Thinking Time (seconds)", 0.0, 5.0, 1.0)

    if st.button("Clear Chat History"):
        st.session_state.messages = []
        
    # QoL: Download Chat History
    chat_str = "\n".join([f"{m['role'].upper()}: {m['content']}" for m in st.session_state.messages])
    st.download_button(
        label="Download Conversation",
        data=chat_str,
        file_name="markigpt_history.txt",
        mime="text/plain"
    )

# --- 4. CHAT INTERFACE ---
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Message MarkiGPT..."):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        # Simulate thinking time
        with st.spinner("Thinking..."):
            time.sleep(thinking_time) 
            response = get_response(prompt)
            st.markdown(response)
            
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})