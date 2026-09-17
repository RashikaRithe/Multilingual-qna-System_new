# 📘 Multilingual Q&A Generation System

An end-to-end NLP application that extracts text from PDF documents, generates question-answer pairs using transformer-based language models, translates them into Hindi and Marathi, and exports the results as a downloadable Excel report — all through an interactive Streamlit interface.

## Features

- **PDF text extraction** — upload any PDF and extract its raw text
- **Text cleaning & chunking** — preprocesses and splits extracted text into manageable chunks for generation
- **Automated Q&A generation** — generates a question and answer for each text chunk using Hugging Face Transformer models
- **Multilingual translation** — translates every generated Q&A pair into **English, Hindi, and Marathi**
- **Excel export** — compiles all Q&A pairs (in all three languages) into a structured, downloadable `.xlsx` report
- **Simple web UI** — upload, preview, and download, all from a single Streamlit page

## Tech Stack

| Component | Technology |
|---|---|
| Web Interface | Streamlit |
| PDF Extraction | PyPDF |
| Text Preprocessing | NLTK |
| Q&A Generation | Hugging Face Transformers, PyTorch |
| Tokenization | SentencePiece |
| Translation | Deep Translator |
| Report Generation | OpenPyXL, python-docx |
| Deployment | Render |

## Project Structure

```
Multilingual-qna-System_new/
├── excel/
│   └── excel_writer.py        # builds and saves the multilingual Excel report
├── extractors/
│   └── pdf_reader.py          # extracts raw text from uploaded PDFs
├── preprocessing/
│   ├── cleaner.py             # cleans extracted text
│   └── chunker.py             # splits text into chunks for Q&A generation
├── qna/
│   ├── qa_generator.py        # generates a question for each text chunk
│   └── answer_generator.py    # generates the corresponding answer
├── translation/
│   └── translator.py          # translates Q&A pairs into Hindi and Marathi
├── input_files/                # sample/input PDF files
├── streamlit_app.py            # main Streamlit application
├── app.py                      # application entry point
├── download_nltk.py            # downloads required NLTK data
├── requirements.txt
├── runtime.txt
├── render.yaml                 # Render deployment configuration
├── test.py / test_qa.py / test_excel.py   # test scripts
└── README.md
```

## How It Works

1. **Upload** — user uploads a PDF through the Streamlit interface
2. **Extract** — `pdf_reader.py` extracts raw text from the PDF
3. **Clean & Chunk** — text is cleaned and split into chunks via `cleaner.py` and `chunker.py`
4. **Generate** — for each chunk, `qa_generator.py` generates a question and `answer_generator.py` generates the matching answer
5. **Translate** — each Q&A pair is translated into Hindi and Marathi using `translator.py`
6. **Export** — all English, Hindi, and Marathi Q&A pairs are compiled into an Excel file via `excel_writer.py`
7. **Download** — the user previews all Q&A pairs on screen and downloads the final `.xlsx` report

## Setup and Run Locally

### Prerequisites

- Python 3.9+
- pip

### Steps

```bash
# clone the repository
git clone https://github.com/RashikaRithe/Multilingual-qna-System_new.git
cd Multilingual-qna-System_new

# create a virtual environment
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux

# install dependencies
pip install -r requirements.txt

# download required NLTK data
python download_nltk.py

# run the app
streamlit run streamlit_app.py
```

### Run Tests

```bash
pytest test_qa.py test_excel.py -v
```

## Output

The app produces a downloadable Excel file (`QnA_<timestamp>.xlsx`) containing three sheets/sections of question-answer pairs — English, Hindi, and Marathi — generated from the uploaded document.

## Future Improvements

- Support for additional Indian and international languages
- Configurable chunk size and number of Q&A pairs per document
- Answer quality scoring/filtering before export
- Support for `.docx` and `.txt` file uploads in addition to PDF

## Author

**Rashika Rithe**
[GitHub](https://github.com/RashikaRithe) · [LinkedIn](#)
