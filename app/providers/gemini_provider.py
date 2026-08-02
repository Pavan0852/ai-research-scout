
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# def invoke(prompt: str, model: str | None = None) -> str:

#     response = client.models.generate_content(
#         model=model or "gemini-2.5-flash",
#         contents=prompt
#     )

#     return response.text

import time
from google.genai.errors import ServerError


def invoke(prompt: str, model: str | None = None):

    model_name = model or "gemini-2.5-flash"
    retries = 3

    for attempt in range(retries):

        try:

            response = client.models.generate_content(
                model=model_name,
                contents=prompt
            )

            return response.text

        except ServerError:

            wait_time = 2 ** attempt

            print(
                f"Retrying in {wait_time}s..."
            )

            time.sleep(wait_time)

    raise Exception(
        "Gemini unavailable after retries"
    )