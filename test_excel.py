from excel.excel_writer import save_excel

english = [
    {
        "Question": "What is AI?",
        "Answer": "Artificial Intelligence is a branch of computer science."
    }
]

hindi = [
    {
        "Question": "AI क्या है?",
        "Answer": "AI कंप्यूटर विज्ञान की एक शाखा है।"
    }
]

marathi = [
    {
        "Question": "AI म्हणजे काय?",
        "Answer": "AI ही संगणक विज्ञानाची एक शाखा आहे."
    }
]

save_excel(
    english,
    hindi,
    marathi,
    "output/QnA.xlsx"
)

print("Excel Created Successfully")