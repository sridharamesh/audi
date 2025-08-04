import streamlit as st
from gtts import gTTS
import base64

st.title("🗣️ Auto-Play Text-to-Speech")

text = st.text_area("Enter text to speak:", "Hello Streamlit!")

if st.button("Speak"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        # Generate MP3 with gTTS
        tts = gTTS(text)
        tts.save("output.mp3")

        # Read and base64-encode
        with open("output.mp3", "rb") as f:
            audio_data = f.read()
            b64 = base64.b64encode(audio_data).decode()

        # Inject invisible auto-playing audio
        audio_html = f"""
        <audio autoplay style="display:none;">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)
