import os
from dotenv import load_dotenv
from google import genai


# Load .env
load_dotenv()


# Get API key
api_key = os.getenv("GEMINI_API_KEY")


print("API key loaded:", bool(api_key))
if not api_key:
    raise ValueError(
        "GEMINI_API_KEY was not found. "
    )

# Create Gemini client
client = genai.Client(
    api_key=api_key
)


# Ask Gemini
response = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain inheritance in Java in 3 simple sentences.",
    
    
)


print("\nGemini response:")
print(response.output_text)