import os
from sys import argv

from dotenv import load_dotenv

from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    prompt, verbose = get_inputs()
    if prompt:

        messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]
        response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)

        print(response.text)
        if verbose:
            show_response_details(prompt, response)
    
    else:
        print("Error: Missing Prompt")
        exit(1)

def show_response_details(prompt, response):
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

def get_inputs():
    verbose = False

    if len(argv) >= 2:
        if not argv[1].startswith("-"):
            if "--verbose" in argv:
                verbose = True

            return argv[1], verbose
    
    return None, verbose

if __name__ == "__main__":
    main()
