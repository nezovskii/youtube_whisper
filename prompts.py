import re
import anthropic
from config import API_KEY, MODEL_NAME

def get_completion(prompt: str, system_prompt=""):
    client = anthropic.Anthropic(api_key=API_KEY)
    message = client.messages.create(
        model=MODEL_NAME,
        max_tokens=2000,
        temperature=0.0,
        system=system_prompt,
        messages=[
          {"role": "user", "content": prompt}
        ]
    )
    return message.content[0].text

if __name__ == "__main__":
    # Example usage
    prompt = "Hello, how are you?"
    response = get_completion(prompt)
    print(response) 