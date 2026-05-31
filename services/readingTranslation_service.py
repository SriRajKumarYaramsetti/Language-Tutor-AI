from openai import OpenAI
from utils.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_random_sentence():

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a language teacher. "
                    "Your job is to generate a long sentence in Telugu."
                )
            },
            {
                "role": "user",
                "content": "Please generate a long sentence in Telugu."
            }
        ]
    )

    return completion.choices[0].message.content.strip()


def verify_translation(original, translation):

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a language teacher. "
                    "Your job is to check a Telugu-to-English translation. "
                    "You will be given an original Telugu sentence and "
                    "the user's English translation. "
                    "Identify mistakes, suggest improvements, and "
                    "appreciate the user if the translation is correct."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Original sentence in Telugu: {original}\n"
                    f"User translation: {translation}\n\n"
                    "Evaluate the translation and provide feedback."
                )
            }
        ]
    )

    return completion.choices[0].message.content.strip()