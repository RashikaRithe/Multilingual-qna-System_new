from qna.answer_generator import generate_answer

context = """
Artificial Intelligence is a branch of computer science.
It enables machines to mimic human intelligence.
AI is used in healthcare, education and finance.
"""

question = "What is Artificial Intelligence?"

answer = generate_answer(
    question,
    context
)

print(answer)