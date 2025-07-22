# prompt_templates.py

def resume_feedback_prompt(resume_text):
    return f"""
You are a senior AI career advisor.
Here is a candidate's resume:\n\n{resume_text}\n\n
Please give personalized, actionable feedback on:
1. Technical clarity
2. Impact statements
3. Job fit
4. ATS optimization
Limit to 300 words. Be honest but encouraging.
"""
