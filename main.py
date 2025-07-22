# main.py
bash
pip install openai

import openai
from resume_parser import extract_text_from_pdf
from prompt_templates import resume_feedback_prompt

openai.api_key = "YOUR_API_KEY"

def get_resume_feedback(resume_path):
    text = extract_text_from_pdf(resume_path)
    prompt = resume_feedback_prompt(text)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

# Run
print(get_resume_feedback("your_resume.pdf"))
