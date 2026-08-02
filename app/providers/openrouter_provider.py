"""
OpenRouter Provider

This module is responsible for communicating with the
OpenRouter API.

It exposes a single function:

    invoke(
        model,
        prompt,
        temperature,
        max_tokens
    )

The LLM Router decides WHICH model to use.
This provider only sends the request.
"""

import os
import time
from typing import Optional

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = os.getenv(
    "OPENROUTER_BASE_URL",
    "https://openrouter.ai/api/v1",
)

APP_NAME = os.getenv(
    "APP_NAME",
    "AI Research Scout",
)

APP_URL = os.getenv(
    "APP_URL",
    "http://localhost:8501",
)


if not OPENROUTER_API_KEY:
    raise ValueError(
        "OPENROUTER_API_KEY not found in .env"
    )


client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url=OPENROUTER_BASE_URL,
)


class OpenRouterError(Exception):
    """Raised when OpenRouter fails."""


def invoke(
    model: str,
    prompt: str,
    temperature: float = 0.3,
    max_tokens: int = 2048,
    system_prompt: Optional[str] = None,
    retries: int = 3,
) -> str:
    """
    Send a prompt to OpenRouter.

    Args:
        model:
            OpenRouter model name.

        prompt:
            User prompt.

        temperature:
            Sampling temperature.

        max_tokens:
            Maximum tokens to generate.

        system_prompt:
            Optional system prompt.

        retries:
            Number of retry attempts.

    Returns:
        Generated response text.
    """

    messages = []

    if system_prompt:

        messages.append(
            {
                "role": "system",
                "content": system_prompt,
            }
        )

    messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    for attempt in range(retries):

        try:

            response = client.chat.completions.create(

                model=model,

                messages=messages,

                temperature=temperature,

                max_tokens=max_tokens,

                extra_headers={
                    "HTTP-Referer": APP_URL,
                    "X-Title": APP_NAME,
                },

            )

            if (
                not response.choices
                or response.choices[0].message.content is None
            ):
                raise OpenRouterError(
                    "Empty response received from OpenRouter."
                )

            return response.choices[0].message.content.strip()

        except Exception as exc:

            if attempt == retries - 1:

                raise OpenRouterError(
                    f"OpenRouter request failed: {exc}"
                ) from exc

            wait_time = 2 ** attempt

            print(
                f"[OpenRouter] Attempt "
                f"{attempt + 1}/{retries} failed. "
                f"Retrying in {wait_time}s..."
            )

            time.sleep(wait_time)


if __name__ == "__main__":

    response = invoke(
        model="openai/gpt-oss-20b",
        prompt="Explain Retrieval-Augmented Generation in 3 lines.",
    )

    print(response)