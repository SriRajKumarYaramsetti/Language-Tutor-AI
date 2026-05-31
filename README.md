# Language Tutor AI

## Overview

Language Tutor AI is a multimodal language learning platform built with Streamlit and OpenAI APIs. The application helps learners improve their language skills through interactive exercises involving grammar, reading comprehension, image description, speech recognition, and translation.

The platform combines Large Language Models, Speech-to-Text capabilities, and Image Understanding models to create an engaging and personalized learning experience.

---

## Features

### Grammar Practice

* AI-generated grammar exercises
* Fill-in-the-blank and multiple-choice questions
* Instant feedback and explanations
* Beginner-friendly learning experience

### Reading & Translation

* AI-generated Telugu reading passages
* Translation exercises from Telugu to English
* Detailed feedback on translation quality
* Vocabulary and grammar improvement suggestions

### Image Comprehension

* Random image generation
* IELTS-style image description practice
* Voice recording and speech recognition using Whisper
* AI-powered evaluation of grammar, vocabulary, and fluency
* Personalized speaking feedback

### Speech Recognition

* Audio recording from microphone
* Speech-to-text conversion using OpenAI Whisper
* Automatic transcription of spoken responses

---

## Architecture

```text
Language Tutor AI
│
├── pages/
│   ├── home.py
│   ├── grammar_fun.py
│   ├── reading_translation.py
│   └── image_comprehension.py
│
├── services/
│   ├── grammar_service.py
│   ├── reading_translation_service.py
│   └── image_comprehension_service.py
│
├── utils/
│   └── config.py
│
├── .env
├── app.py
└── requirements.txt
```

---

## Technologies Used

### Frontend

* Streamlit

### Backend

* Python

### AI & Machine Learning

* OpenAI GPT Models
* OpenAI Whisper

### Libraries

* streamlit
* openai
* requests
* sounddevice
* numpy
* scipy
* python-dotenv

---

## OpenAI Services Used

### GPT Models

Used for:

* Grammar exercise generation
* Translation evaluation
* Language feedback
* Image analysis

### Whisper

Used for:

* Speech-to-text conversion
* Spoken response transcription

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/language-tutor-ai.git
cd language-tutor-ai
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=your_openai_api_key
```

---

## Run Application

```bash
streamlit run app.py
```

---

## Learning Objectives

This project demonstrates:

* Generative AI Integration
* Prompt Engineering
* OpenAI API Usage
* Speech Recognition
* Image Understanding
* Streamlit Application Development
* Service Layer Architecture
* Environment Variable Management
* State Management in Streamlit

---

## Future Enhancements

* Multi-language support
* User authentication
* Progress tracking
* Pronunciation scoring
* Vocabulary learning modules
* Conversation practice with AI tutor
* Cloud deployment

---

## Author

Sri Raj Kumar Yaramsetti

Java Full Stack Developer | Generative AI Enthusiast
