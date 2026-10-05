import streamlit as st

from ai_engine import generate_study_material
from audio_processor import transcribe_audio
from youtube_handler import get_youtube_transcript


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI Lecture Analyzer",
    page_icon="🎓",
    layout="wide"
)


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "transcript" not in st.session_state:
    st.session_state.transcript = ""

if "study_material" not in st.session_state:
    st.session_state.study_material = ""


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title(
    "🎓 AI-Powered Real-Time Lecture Analysis"
)

st.subheader(
    "Personalized Study Notes Generator"
)

st.write(
    """
    Convert lectures into structured notes,
    summaries, flashcards, questions and
    personalized revision material.
    """
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("⚙️ Personalization")

student_level = st.sidebar.selectbox(
    "Student Level",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

note_style = st.sidebar.selectbox(
    "Notes Style",
    [
        "Exam Notes",
        "Short Notes",
        "Detailed Notes",
        "Revision Notes"
    ]
)

language = st.sidebar.selectbox(
    "Output Language",
    [
        "English",
        "Hindi",
        "Telugu"
    ]
)


# --------------------------------------------------
# INPUT METHOD
# --------------------------------------------------

st.header("📥 Lecture Input")

input_type = st.radio(
    "Choose input method",
    [
        "Upload Audio",
        "YouTube Lecture",
        "Enter Transcript"
    ],
    horizontal=True
)


# ==================================================
# AUDIO
# ==================================================

if input_type == "Upload Audio":

    st.subheader("🎤 Upload Lecture Audio")

    audio_file = st.file_uploader(
        "Upload WAV audio",
        type=[
            "wav"
        ]
    )

    if audio_file:

        st.audio(audio_file)

        if st.button(
            "📝 Convert Audio to Transcript"
        ):

            with st.spinner(
                "🎧 Converting speech to text..."
            ):

                transcript = transcribe_audio(
                    audio_file
                )

            st.session_state.transcript = transcript

            st.success(
                "Transcript generated!"
            )


# ==================================================
# YOUTUBE
# ==================================================

elif input_type == "YouTube Lecture":

    st.subheader("📺 YouTube Lecture")

    youtube_url = st.text_input(
        "Enter YouTube URL"
    )

    if st.button(
        "📥 Get Lecture Transcript"
    ):

        if not youtube_url:

            st.warning(
                "Please enter a YouTube URL."
            )

        else:

            with st.spinner(
                "Getting transcript..."
            ):

                transcript = get_youtube_transcript(
                    youtube_url
                )

            if transcript.startswith("ERROR"):

                st.error(transcript)

            else:

                st.session_state.transcript = transcript

                st.success(
                    "YouTube transcript loaded!"
                )


# ==================================================
# MANUAL TRANSCRIPT
# ==================================================

else:

    st.subheader("📝 Enter Lecture Transcript")

    transcript_input = st.text_area(
        "Paste your lecture transcript here",
        height=300
    )

    if st.button(
        "Use This Transcript"
    ):

        if transcript_input.strip():

            st.session_state.transcript = (
                transcript_input
            )

            st.success(
                "Transcript added!"
            )

        else:

            st.warning(
                "Please enter some text."
            )


# ==================================================
# DISPLAY TRANSCRIPT
# ==================================================

if st.session_state.transcript:

    st.divider()

    st.header("📜 Lecture Transcript")

    with st.expander(
        "View Transcript",
        expanded=False
    ):

        st.write(
            st.session_state.transcript
        )


    # ==================================================
    # AI GENERATION
    # ==================================================

    st.divider()

    st.header(
        "🧠 AI Lecture Analysis"
    )

    if st.button(
        "🚀 Generate Personalized Study Material"
    ):

        with st.spinner(
            "🤖 AI is analyzing your lecture..."
        ):

            result = generate_study_material(

                st.session_state.transcript,

                student_level,

                note_style,

                language
            )

        st.session_state.study_material = result

        st.success(
            "Study material generated!"
        )


# ==================================================
# RESULTS
# ==================================================

if st.session_state.study_material:

    st.divider()

    st.header(
        "📚 Personalized Study Material"
    )

    material = st.session_state.study_material

    st.markdown(material)


    # ==================================================
    # DOWNLOAD
    # ==================================================

    st.download_button(

        label="⬇️ Download Study Notes",

        data=material,

        file_name="personalized_lecture_notes.txt",

        mime="text/plain"
    )


# ==================================================
# FOOTER
# ==================================================

st.divider()

st.caption(
    "🎓 AI Lecture Analyzer | "
    "Personalized Learning Assistant"
)