import streamlit as st
from gtts import gTTS
import base64

st.title("🗣 Text-to-Speech with Auto-Play")

text = st.text_area("Enter text to speak:", "Hello from Streamlit!")

if st.button("Generate Audio"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        # Generate and save MP3
        tts = gTTS(text)
        tts.save("output.mp3")

        # Read MP3 and encode to base64
        with open("output.mp3", "rb") as f:
            audio_bytes = f.read()
            b64_audio = base64.b64encode(audio_bytes).decode()

        # Embed audio with autoplay
        audio_html = f"""
        <audio autoplay controls>
            <source src="data:audio/mp3;base64,{b64_audio}" type="audio/mp3">
            Your browser does not support the audio element.
        </audio>
        """

        # Render in Streamlit
        st.markdown(audio_html, unsafe_allow_html=True)
