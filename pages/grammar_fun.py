import streamlit as st

from services.grammar_service import (
    generate_grammar_exercise,
    check_answer
)


def app():

    st.header("Grammar and Fun")
    st.write("Sharpen your grammar skills with these exercises.")

    # Session State Initialization
    if "exercise" not in st.session_state:
        st.session_state.exercise = None

    if "user_response" not in st.session_state:
        st.session_state.user_response = ""

    # Start Button
    if st.button("Start"):
        st.session_state.exercise = generate_grammar_exercise()

    # Show Exercise
    if st.session_state.exercise:

        st.subheader("Exercise:")
        st.write(st.session_state.exercise)

        # User Input
        user_response = st.text_input(
            "Your Answer:",
            key="response"
        )

        # Check Answer Button
        if st.button("Check Answer"):

            if user_response:

                st.session_state.user_response = user_response

                feedback = check_answer(
                    st.session_state.exercise,
                    user_response
                )

                st.subheader("Feedback on Your Answer:")
                st.write(feedback)

            else:
                st.error("Please enter an answer before checking.")