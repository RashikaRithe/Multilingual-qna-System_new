from qna.qa_generator import generate_question, generate_answer

text = """
Artificial Intelligence is the simulation of human intelligence by machines.
Machine Learning is a subset of Artificial Intelligence.
Deep Learning is a subset of Machine Learning.
"""

question = generate_question(text)
print("Question:", question)

answer = generate_answer(question, text)
print("Answer:", answer)