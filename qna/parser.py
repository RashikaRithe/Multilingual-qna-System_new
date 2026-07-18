import re

def parse_questions(text):

    questions = []

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if "?" in line:

            questions.append(line)

    return questions