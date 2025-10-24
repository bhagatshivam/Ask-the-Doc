# Ask the Doc: Generative AI for Knowledge Management

This is a Streamlit-based application that allows users to:

- Upload a PDF or enter custom text
- Automatically summarize the content using a transformer model
- Ask questions based on the uploaded content
- Get answers with audio output using text-to-speech

Powered by HuggingFace Transformers and gTTS, this tool offers a lightweight yet effective way to interact with text-based documents using AI.

## Features

- Text Summarization using `google/pegasus-xsum`
- Question-Answering using `deepset/roberta-base-squad2`
- Text-to-Speech using Google Text-to-Speech (gTTS)
- PDF file support
- Audio output for both summary and answers
- Built with Streamlit for a simple user interface

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ask-the-doc.git
cd ask-the-doc
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
```
#### On Windows:
```bash
venv\Scripts\activate
```
#### On macOS/Linux:
```bash
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt

```

### 4. Run the app
```bash
streamlit run app.py

```

## Requirements

Make sure to have the following installed:

- Python 3.8 or higher
- Streamlit
- Transformers
- gTTS
- PyPDF2

All dependencies are listed in the requirements.txt file.

## Notes

- Large PDFs or transformer models may require more system memory.
- If you encounter memory issues:
    - Increase your system's virtual memory (paging file size)
    - Switch to a smaller model such as distilbert-base-uncased-distilled-squad

## Project Structure
```bash
ask-the-doc/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── assets/                 # Optional: audio files or other assets

```

## Models Used

- Summarization: google/pegasus-xsum
- Question Answering: deepset/roberta-base-squad2

##  Acknowledgments

- HuggingFace Transformers
- Google Text-to-Speech (gTTS)
- Streamlit Community
