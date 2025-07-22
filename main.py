# main.py

import openai
from dotenv import load_dotenv
import os
from resume_parser import extract_text_from_pdf
from prompt_templates import resume_feedback_prompt

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_resume_feedback(resume_path):
    text = extract_text_from_pdf(resume_path)
    prompt = resume_feedback_prompt(text)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

# Run
if __name__ == "__main__":
    resume_path = "your_resume.pdf"  # Replace with your file name
    feedback = get_resume_feedback(resume_path)

    os.makedirs("output", exist_ok=True)
    with open("output/resume_feedback.txt", "w") as f:
        f.write(feedback)

    print("✅ Resume feedback saved to output/resume_feedback.txt")
