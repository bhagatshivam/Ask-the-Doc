import streamlit as st
from transformers import pipeline
from PyPDF2 import PdfReader
from gtts import gTTS
import tempfile
import os

# Load models
summary_model = pipeline("summarization", model="google/pegasus-xsum")
qa_model = pipeline("question-answering", model="deepset/roberta-base-squad2")

# Text to speech
def text_to_audio(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_audio.name)
    return temp_audio.name

# Extract text from PDF
def extract_text_from_pdf(pdf_file):
    pdf = PdfReader(pdf_file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text() + "\n"
    return text

# Streamlit App
st.title("📚 PDF/Text Summarizer & Q&A with Audio Output")

option = st.radio("Choose Input Type:", ["📄 Upload PDF", "📝 Enter Text"])

# Initialize variable
raw_text = ""

if option == "📄 Upload PDF":
    uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])
    if uploaded_file:
        raw_text = extract_text_from_pdf(uploaded_file)
        st.success("Text extracted from PDF successfully!")
elif option == "📝 Enter Text":
    raw_text = st.text_area("Enter text here:")

# If raw_text is not empty, continue
if raw_text:
    if st.button("Generate Summary"):
        summary = summary_model(raw_text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
        st.subheader("📄 Summary")
        st.write(summary)
        audio_path = text_to_audio(summary)
        st.audio(audio_path, format="audio/mp3")

    st.subheader("❓ Ask a Question")
    user_question = st.text_input("Type your question here:")
    if user_question:
        answer = qa_model(question=user_question, context=raw_text)['answer']
        st.write(f"Answer: {answer}")
        audio_path = text_to_audio(answer)
        st.audio(audio_path, format="audio/mp3")

