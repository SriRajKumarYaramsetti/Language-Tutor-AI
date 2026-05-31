import streamlit as st

from services.readingTranslation_service import (
    generate_random_sentence,
    verify_translation
)


def app():

    st.header("Reading and Translation")

    st.write(
        "Test your translation skills. "
        "Translate the following Telugu sentence into English."
    )

    if "generated_sentence" not in st.session_state:
        st.session_state.generated_sentence = None

    if "translation_input" not in st.session_state:
        st.session_state.translation_input = ""

    if st.button("Start"):
        st.session_state.generated_sentence = generate_random_sentence()

    if st.session_state.generated_sentence:

        st.subheader("Sentence to Translate:")
        st.write(st.session_state.generated_sentence)

        user_translation = st.text_input(
            "Your English Translation:",
            key="translation"
        )

        if st.button("Verify Translation"):

            if user_translation:

                st.session_state.translation_input = user_translation

                feedback = verify_translation(
                    st.session_state.generated_sentence,
                    user_translation
                )

                st.subheader("Translation Feedback:")
                st.write(feedback)

            else:
                st.error(
                    "Please enter a translation before verifying."
                )