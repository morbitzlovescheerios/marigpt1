import streamlit as st
import random
import time
import os


st.set_page_config(page_title="MarkiGPT 1.0", page_icon="⬛", layout="centered")


if "messages" not in st.session_state:
    st.session_state.messages = []

# --- VERSION SELECTOR ---
with st.sidebar:
    if os.path.exists("logo.png"):
        st.image("logo.png", use_container_width=True)
    elif os.path.exists("logo.jpg"):
        st.image("logo.jpg", use_container_width=True)
        
    st.header("Settings")
    version = st.selectbox("Version", ["1.2", "1.0"])

if version == "1.2":
    # --- 1.2 MODERN THEME ---
    st.markdown("""
    <style>
        .stApp {
            background-color: #1a1a1a;
            color: #FFFFFF;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .stTextInput input {
            background-color: #0a0a0a;
            color: white;
            border: 1px solid #333;
            border-radius: 25px;
        }
        div.stButton > button {
            background-color: #FFFFFF;
            color: black;
            border-radius: 25px;
            border: none;
            font-weight: bold;
            width: 100%;
        }
        div.stButton > button:hover {
            background-color: #cccccc;
            border: none;
            color: black;
        }
        h1, h2, h3 {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-weight: 700;
        }
    </style>
    """, unsafe_allow_html=True)
else:
    # --- 1.0 CLASSIC THEME ---
    st.markdown("""
    <style>
        .stApp {
            background-color: #000000;
            color: #FFFFFF;
            font-family: monospace;
        }
        .stTextInput input {
            background-color: #111;
            color: white;
            border: 1px solid #333;
            border-radius: 5px;
            font-family: monospace;
        }
        div.stButton > button {
            background-color: #FFFFFF;
            color: black;
            border-radius: 5px;
            border: none;
            font-weight: bold;
            width: 100%;
            font-family: monospace;
        }
        h1, h2, h3 {
            font-family: monospace;
            font-weight: 700;
        }
    </style>
    """, unsafe_allow_html=True)


GENERIC_RESPONSES = [
    "That's a really interesting point.",
    "I'm not sure I know the answer to that, but tell me more!",
    "Hmm, I see what you mean.",
    "Could you explain that a bit more?",
    "I'm just a local script, but I'm doing my best to keep up!",
    "That sounds pretty cool.",
    "I'm listening...",
    "Wow, really?",
    "I'm learning new things every day (well, sort of).",
    "Let's keep chatting about that."
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
        return "I can't see outside, but I hope it's nice wherever you are!"
    elif "meaning of life" in user_input:
        return "42. Obviously."
    elif "status" in user_input:
        return "I'm feeling great! Systems are running smoothly."
    elif "python" in user_input or "code" in user_input:
        return """Here is a Python example for you:
```python
def hello_world():
    print("Hello from MarkiGPT!")
```"""
    else:
        return random.choice(GENERIC_RESPONSES)


st.title(f"MarkiGPT {version}")
st.caption("A custom-built Artificial Intelligence.")


with st.sidebar:
    # Only show advanced settings in 1.2
    if version == "1.2":
        thinking_time = st.slider("Thinking Time (seconds)", 0.0, 5.0, 1.0)
    else:
        thinking_time = 0 # Instant in 1.0

    if st.button("Clear Chat History"):
        st.session_state.messages = []
        
    
    chat_str = "\n".join([f"{m['role'].upper()}: {m['content']}" for m in st.session_state.messages])
    st.download_button(
        label="Download Conversation",
        data=chat_str,
        file_name="markigpt_history.txt",
        mime="text/plain"
    )


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Message MarkiGPT..."):

    st.chat_message("user").markdown(prompt)
   
    st.session_state.messages.append({"role": "user", "content": prompt})

    
    with st.chat_message("assistant"):
        
        with st.spinner("Thinking..."):
            time.sleep(thinking_time) 
            response = get_response(prompt)
            st.markdown(response)
            
   
    st.session_state.messages.append({"role": "assistant", "content": response})
