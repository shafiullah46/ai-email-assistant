# ✉️ AI Email Assistant 🤖
An automated Python tool developed to rewrite informal or brief team messages into polite, structured, and professional emails using the OpenAI API.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-API-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

An intelligent, lightweight Python utility designed to automate written communication. This tool transforms rushed, informal, or rough team messages into polite, structured, and professional corporate emails using the OpenAI API.

---

## 🚀 Key Features

- **Advanced Prompt Engineering:** Constructs precise, parameterized prompts to enforce professional tone and structure.
- **Controlled Generation:** Optimized with low temperature (`0.1`) for consistent, deterministic outputs and a strict token ceiling (`max_tokens=60`) for concise responses.
- **Secure Configuration:** Dynamically loads credentials and base URLs via system environment variables (`OPENAI_API_KEY`, `OPENAI_BASE_URL`).
- **Hands-on Lab Origin:** Developed as part of an applied AI engineering lab demonstrating LLM integration workflows.

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Library:** `openai` (Official Python SDK)
- **Environment:** Virtual Environment (`venv`)

---

## 📂 Project Structure

```text
ai-email-assistant/
│
├── email_assistant.py      # Core logic and OpenAI API integration script
├── requirements.txt        # Project dependencies
├── .gitignore              # Ignored files (virtual environment, cache)
└── README.md               # Project documentation
