import wave
from openai import OpenAI
from utils.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def speech_to_text(file_path):
    with open(file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )

    return transcription.text


def describe_image(image_url):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Describe this image like an IELTS speaking exam."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url
                        }
                    }
                ]
            }
        ],
        max_tokens=300
    )

    return response.choices[0].message.content


def compare_descriptions(model_desc, user_desc):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an English language teacher. "
                    "Compare the model description and user description. "
                    "Evaluate grammar, vocabulary, fluency, and sentence structure. "
                    "Provide supportive feedback suitable for beginners."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Model Description: {model_desc}\n\n"
                    f"User Description: {user_desc}\n\n"
                    "Provide feedback and suggestions for improvement."
                )
            }
        ]
    )

    return completion.choices[0].message.content


def save_recording(recording, output_file, sample_rate):
    with wave.open(output_file, "w") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(recording.tobytes())

    return output_file