import streamlit as st
from gtts import gTTS
from pydub import AudioSegment
import os
from io import BytesIO

st.title("🗣️ Text-to-Speech (TTS) Demo")
st.write("Enter text below and hear it spoken aloud.")

# Input
text = st.text_area("Enter text to synthesize:", "Hello, Streamlit!")

# Generate audio when button is clicked
if st.button("Generate & Play"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Generate speech with gTTS
        tts = gTTS(text)
        tts.save("output.mp3")

        # Convert to WAV for consistent browser playback
        audio = AudioSegment.from_mp3("output.mp3")
        audio.export("output.wav", format="wav")

        # Load file into memory for playback and download
        audio_file = open("output.wav", "rb").read()
        st.audio(audio_file, format="audio/wav")

        st.download_button(
            label="Download Audio",
            data=audio_file,
            file_name="output.wav",
            mime="audio/wav"
        )

        # Optional: cleanup
        os.remove("output.mp3")
        os.remove("output.wav")
