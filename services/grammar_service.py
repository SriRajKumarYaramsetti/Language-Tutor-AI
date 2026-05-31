from openai import OpenAI
from utils import config

client = OpenAI(api_key=config.OPENAI_API_KEY)


def generate_grammar_exercise():

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a language teacher. "
                    "Your job is to teach people English grammar "
                    "through fun and interesting short exercises. "
                    "Give only one question."
                )
            },
            {
                "role": "user",
                "content": (
                    "Create a fun grammar exercise "
                    "(fill in the blanks or multiple choice). "
                    "Give only one question."
                )
            }
        ]
    )

    return completion.choices[0].message.content.strip()


def check_answer(question, user_answer):

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a language teacher. "
                    "You will be given a grammar question "
                    "and a user's answer. "
                    "Evaluate the answer and provide supportive feedback."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Question: {question}\n"
                    f"Answer: {user_answer}\n"
                    "Evaluate the correctness of the answer and provide feedback."
                )
            }
        ]
    )

    return completion.choices[0].message.content.strip()