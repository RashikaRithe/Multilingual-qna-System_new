from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)


def generate_question(context):

    prompt = f"""
Generate ONE important question from the passage.

Passage:
{context}
"""

    result = generator(
        prompt,
        max_length=64,
        do_sample=False
    )

    return result[0]["generated_text"].strip()