"""
Note
    - You need to configure your environment variable GEMINI_API_KEY to run this code
    - You have to generate an API key from https://aistudio.google.com/api-keys
"""
import os
from google import genai

def summarize_text(text: str) -> str:
    """
    Summarize a given text using Gemini.
    """

    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
    )

    prompt = f"""
            You are a technical documentation analyst.

            Summarize the following text clearly and concisely.
            Focus on:
            - What the project is
            - What problem it solves
            - Who it is for

            Text:
            {text}
        """

    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":
    sample_text = (
        "This repository contains a Python library for interacting with the GitHub API. "
        "It allows developers to fetch repository data, manage issues, and automate "
        "common GitHub workflows."
    )

    summary = summarize_text(sample_text)

    print("Summary")
    print("-------")
    print(summary)
