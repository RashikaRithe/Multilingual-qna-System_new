import streamlit as st
import time

from extractors.pdf_reader import read_pdf
from preprocessing.cleaner import clean_text
from preprocessing.chunker import chunk_text

from qna.qa_generator import generate_question
from qna.answer_generator import generate_answer

from translation.translator import translate_text
from excel.excel_writer import save_excel


st.set_page_config(
    page_title="Multilingual Q&A System",
    layout="wide"
)

st.title("📘 Multilingual Q&A Generation System")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    text = read_pdf("temp.pdf")
    text = clean_text(text)
    chunks = chunk_text(text)

    st.success(f"Total Chunks: {len(chunks)}")

    english = []
    hindi = []
    marathi = []

    for i, chunk in enumerate(chunks):

        question = generate_question(chunk)

        answer = generate_answer(
            question,
            chunk
        )

        st.subheader(f"Question {i+1}")
        st.write(question)

        st.subheader("Answer")
        st.write(answer)

        st.markdown("---")

        english.append({
            "Question": question,
            "Answer": answer
        })

        hindi.append({
            "Question": translate_text(question, "hi"),
            "Answer": translate_text(answer, "hi")
        })

        marathi.append({
            "Question": translate_text(question, "mr"),
            "Answer": translate_text(answer, "mr")
        })

    output_file = f"output/QnA_{int(time.time())}.xlsx"

save_excel(
    english,
    hindi,
    marathi,
    output_file
)

st.success("Excel file created successfully!")

with open(output_file, "rb") as file:

    st.download_button(
        label="📥 Download Excel File",
        data=file,
        file_name="QnA.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )