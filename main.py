import os
from sys import argv

from dotenv import load_dotenv

from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    prompt = getPrompt()
    if prompt:

        messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]
        response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
        
        print(response.text)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    
    else:
        print("Error: Missing Prompt")
        exit(1)

def getPrompt():
    if len(argv) >= 2:
        return argv[1]
    return None

if __name__ == "__main__":
    main()
