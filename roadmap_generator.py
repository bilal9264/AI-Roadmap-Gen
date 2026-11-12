
import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv(override=True)

# Get API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Create Groq client
client = Groq(api_key=GROQ_API_KEY)

print("Groq client initialized successfully!")





import os
from dotenv import load_dotenv
from groq import Groq

from prompts import create_roadmap_prompt

# Load environment variables
load_dotenv(override=True)

# Get API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("Groq API key not found. Check your .env file.")

# Connect to Groq
client = Groq(api_key=api_key)


def generate_roadmap(field, level, hours_per_day, duration_weeks):

    # Create our AI prompt
    prompt = create_roadmap_prompt(
        field,
        level,
        hours_per_day,
        duration_weeks
    )

    # Send prompt to Groq
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7
    )

    # Extract AI response
    roadmap = response.choices[0].message.content

    return roadmap


# Test our generator
if __name__ == "__main__":

    result = generate_roadmap(
        "Data Science",
        "Beginner",
        2,
        12
    )

    print("\nYOUR AI LEARNING ROADMAP\n")
    print(result)




