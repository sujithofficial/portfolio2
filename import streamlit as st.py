import streamlit as st
import random
st.title("Number Guessing Game")
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.guesses = 0
guess = st.number_input("Enter your guess (between 1 and 100):", min_value=1, max_value=100, step=1)
if st.button("Submit Guess"):
    st.session_state.guesses += 1
    if guess < st.session_state.number:
        st.write("Too low! Try again.")
    elif guess > st.session_state.number:
        st.write("Too high! Try again.")
    else:
        st.write(f"Congratulations! You've guessed the number {st.session_state.number} in {st.session_state.guesses} attempts.")
        if st.button("Play Again"):
            st.session_state.number = random.randint(1, 100)
            st.session_state.guesses = 0
else:
    st.write("Make your guess!")
st.write(f"Number of guesses: {st.session_state.guesses}")
