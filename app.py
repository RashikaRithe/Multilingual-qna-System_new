from extractors.pdf_reader import read_pdf
from preprocessing.cleaner import clean_text
from preprocessing.chunker import chunk_text

from qna.qa_generator import generate_question
from qna.answer_generator import generate_answer

from translation.translator import translate_text

from excel.excel_writer import save_excel


text = read_pdf("input_files/IKS.pdf")

text = clean_text(text)

chunks = chunk_text(text)

english = []
hindi = []
marathi = []

for chunk in chunks:

    question = generate_question(chunk)

    answer = generate_answer(
        question,
        chunk
    )

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


save_excel(
    english,
    hindi,
    marathi,
    "output/QnA.xlsx"
)

print("Project Completed Successfully!")