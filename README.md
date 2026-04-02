# Resume Job Matcher

An AI-powered resume analysis tool that reads a PDF resume and returns GPT-4 feedback on technical clarity, impact statements, job fit, and ATS optimization.

## What It Does

1. Parses a PDF resume using `pdfplumber`
2. Sends the extracted text to GPT-4 with a structured career advisor prompt
3. Returns actionable, honest feedback in under 300 words
4. Saves output to `output/resume_feedback.txt`

## Stack

- **Python** — core logic
- **OpenAI GPT-4** — feedback generation
- **pdfplumber** — PDF text extraction
- **python-dotenv** — environment variable management

## Setup

```bash
git clone https://github.com/Carey1534/resume_job_matcher.git
cd resume_job_matcher
pip install -r requirements.txt
```

Create a `.env` file:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

```bash
python main.py
```

Place your resume PDF in the project root and update `resume_path` in `main.py`:
```python
resume_path = "your_resume.pdf"
```

Feedback will be saved to `output/resume_feedback.txt`.

## Feedback Categories

- **Technical clarity** — is your stack and experience clearly communicated?
- **Impact statements** — are results quantified and specific?
- **Job fit** — how well does the resume map to target roles?
- **ATS optimization** — keyword density and formatting for applicant tracking systems

## Author

**Connor Carey**
[LinkedIn](https://linkedin.com/in/connor-carey15) • [GitHub](https://github.com/Carey1534)
