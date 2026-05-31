import streamlit as st
import requests
import sounddevice as sd

from services.imageComprehension_service import (
    speech_to_text,
    describe_image,
    compare_descriptions,
    save_recording
)


def app():
    st.header("Image Comprehension")

    st.write(
        "Learn to understand and describe images in your target language. "
        "This task focuses on improving your speaking skills and vocabulary."
    )

    if "image_shown" not in st.session_state:
        st.session_state.image_shown = False

    if "image_generated" not in st.session_state:
        st.session_state.image_generated = False

    if "recording_started" not in st.session_state:
        st.session_state.recording_started = False

    # Start Exercise
    if st.button("Start"):
        st.session_state.image_shown = True
        st.session_state.image_generated = False

    if st.session_state.image_shown:

        # Generate Image Only Once
        if not st.session_state.image_generated:
            response = requests.get(
                "https://picsum.photos/1280/720"
            )

            st.session_state.image_url = response.url
            st.session_state.image_generated = True

        st.image(
            st.session_state.image_url,
            caption="Describe this image."
        )

        st.subheader(
            """
            Look carefully at the image and describe what you see.

            You will have 30 seconds to speak.
            Focus on vocabulary, details, and fluent speech.
            """
        )

        if st.button("Start Talking"):

            st.session_state.recording_started = True

            duration = 30
            sample_rate = 44100

            st.write("Recording started... Speak now!")

            recording = sd.rec(
                int(duration * sample_rate),
                samplerate=sample_rate,
                channels=1,
                dtype="int16"
            )

            sd.wait()

            st.write("Recording completed.")

            st.session_state.recording_started = False

            output_file = "output2.wav"

            save_recording(
                recording,
                output_file,
                sample_rate
            )

            user_description = speech_to_text(
                output_file
            )

            model_description = describe_image(
                st.session_state.image_url
            )

            feedback = compare_descriptions(
                model_description,
                user_description
            )

            st.subheader("Your Description")
            st.write(user_description)

            st.subheader("Model Description")
            st.write(model_description)

            st.subheader("Feedback")
            st.write(feedback)