import os
from dotenv import load_dotenv
from google import genai


# -----------------------------------------
# LOAD ENVIRONMENT VARIABLES
# -----------------------------------------

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")


# -----------------------------------------
# CHECK API KEY
# -----------------------------------------

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is missing. "
        "Please add it to your .env file."
    )


# -----------------------------------------
# CREATE GEMINI CLIENT
# -----------------------------------------

client = genai.Client(
    api_key=API_KEY
)


# -----------------------------------------
# GEMINI MODEL
# -----------------------------------------

MODEL = "gemini-3.8-flash"


# -----------------------------------------
# GENERATE STUDY MATERIAL
# -----------------------------------------

def generate_study_material(
    transcript,
    student_level="Intermediate",
    note_style="Exam Notes",
    language="English"
):

    prompt = f"""
You are an AI academic assistant.

Analyze the following lecture transcript
and create personalized study material.

Student Level:
{student_level}

Note Style:
{note_style}

Output Language:
{language}


LECTURE TRANSCRIPT
==================

{transcript}


Generate the following sections:

1. Lecture Title

2. Short Summary

3. Detailed Notes

4. Key Concepts

5. Important Definitions

6. Important Formulas

If there are no formulas, say:
"No formulas found."

7. Exam Important Points

8. Five Important Questions

9. Five MCQs

For every MCQ provide:
- Question
- Four options
- Correct answer
- Short explanation

10. Five Flashcards

Format:

Question:
Answer:

11. Topics To Revise

12. Personalized Revision Plan


IMPORTANT:

- Use simple language.
- Make the notes exam-friendly.
- Organize the content clearly.
- Do not invent information that is not present
  in the lecture.
"""


    # -----------------------------------------
    # CALL GEMINI
    # -----------------------------------------

    interaction = client.interactions.create(
        model=MODEL,
        input=prompt,
        generation_config={
            "thinking_level": "low"
        }
    )


    # -----------------------------------------
    # RETURN AI RESPONSE
    # -----------------------------------------

    return interaction.output_text