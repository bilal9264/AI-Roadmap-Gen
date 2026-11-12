
import streamlit as st
from roadmap_generator import generate_roadmap

# Page configuration
st.set_page_config(
    page_title="AI Learning Roadmap Generator",
    page_icon="🧭",
    layout="wide"
)

# Application heading
st.title("🧭 AI Learning Roadmap Generator")

st.write(
    "Created By BILAL Ahmad  ( Ds-F25-015 ) and powered by AI."
)

st.divider()

# User input form
with st.form("roadmap_form"):

    field = st.text_input(
        "What do you want to learn?",
        placeholder="e.g. Data Science, Web Development, AI"
    )

    level = st.selectbox(
        "What is your current skill level?",
        ["Beginner", "Intermediate", "Advanced"]
    )

    hours_per_day = st.slider(
        "How many hours can you study daily?",
        min_value=1,
        max_value=12,
        value=2
    )

    duration_weeks = st.slider(
        "How many weeks do you have?",
        min_value=2,
        max_value=52,
        value=12
    )

    submitted = st.form_submit_button(
        "Generate My Learning Roadmap"
    )

# Generate roadmap when user submits
if submitted:

    if not field.strip():
        st.warning("Please enter a learning field.")

    else:
        with st.spinner("Your AI roadmap is being created..."):

            try:
                roadmap = generate_roadmap(
                    field,
                    level,
                    hours_per_day,
                    duration_weeks
                )

                st.success("Your roadmap is ready!")

                st.markdown(roadmap)

            except Exception as error:
                st.error(f"Something went wrong: {error}")
