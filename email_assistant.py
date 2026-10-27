import os
from openai import OpenAI

# Initialize OpenAI client using environment variables
api_key = os.environ.get('OPENAI_API_KEY')
base_url = os.environ.get('OPENAI_BASE_URL') or os.environ.get('OPENAI_API_BASE')

client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

def rewrite_email(text: str) -> str:
    prompt = (
        f"Rewrite the following informal email text into a polite and professional email:\n\n"
        f"Original: {text}"
    )
    
    response = client.chat.completions.create(
        model="gpt-5.6-luna",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=60,
        temperature=0.1
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    raw_email = "hey send me that report asap"
    response = rewrite_email(raw_email)
    print(response)
