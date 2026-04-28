import os
from typing import Optional

import dotenv
from google import genai

from utils.config import SYSTEM_PROMPT


dotenv.load_dotenv()


class LLMClient:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")

        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found. Please set it in your .env file.")

        self.client = genai.Client(api_key=self.api_key)
        self.model = "gemini-2.5-flash"

    def call_api(self, user_query: str) -> str:
        prompt = f"""
{SYSTEM_PROMPT}

User Query:
{user_query}

Follow the output format exactly as described in the prompt.
"""

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        if response and response.text:
            return response.text.strip()

        return "Sorry, I could not generate a response."


def answer_student_query(query: str) -> str:
    try:
        llm_client = LLMClient()
        return llm_client.call_api(query)

    except ValueError as e:
        return f"Configuration Error: {str(e)}"

    except Exception as e:
        return f"API Error: {str(e)}"


def main():
    test_queries = [
        "When is the Tech Fest happening?",
        "Where is the Career Fair located?",
        "Tell me about the Hackathon",
        "What's the schedule for the Music Concert?",
        "Tell me a joke",
        "What's the weather like?"
        "Tell me about the Sports Day"
    ]

    print("Campus Event Q&A Assistant")
    print("=" * 40)

    for query in test_queries:
        print(f"\nQuery: {query}")
        result = answer_student_query(query)
        print(f"Response: {result}")
        print("-" * 40)


if __name__ == "__main__":
    main()