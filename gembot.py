import streamlit as st
import google.generativeai as genai

# Configure the Gemini API
GOOGLE_API_KEY = 'AIzaSyC89g3QWLs6H8fx7fhZVYEuKZeUG6wzEuo'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')
# Set Streamlit page configuration
st.set_page_config(
    page_title="GemBOT",
    page_icon="💎🤖",
    layout="centered"
)

# Check for messages in session and create a title if not exists
st.title(":blue[Howdy, this is :grey[GEMBOT V1 💎🤖] How may I help you today?]")
st.image(r"C:\Users\user\OneDrive\Desktop\10years-for-visual-wonder-robo-rajinikanth.gif")
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello, this is GemBOT and how I can help you today?"}
    ]
    #st.title(":blue[Hey whatsup, this is :grey[GEMBOT V1 💎🤖] use me as your assistent?]")
    #                                                                                                                                                                                                                                                                                                                                                                  st.image(r"C:\Users\user\OneDrive\Desktop\10years-for-visual-wonder-robo-rajinikanth.gif")
# Display all messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
# Receive user input
user_input = st.chat_input()

# Store user input in session
if user_input is not None:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
# Generate AI response and display
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Loading..."):
            ai_response = model.generate_content(user_input)
            st.write(ai_response.text)
    new_ai_message = {"role": "assistant", "content": ai_response.text}
    st.session_state.messages.append(new_ai_message)