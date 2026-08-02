import json
import re

from app.models.research_insight import ResearchInsight
from app.providers.llm_router import invoke_for_task


def parse_llm_json(response: str):

    match = re.search(
        r"\{.*\}",
        response,
        re.DOTALL
    )

    if not match:
        raise ValueError(
            f"No JSON found in response:\n{response}"
        )

    return json.loads(match.group())


def analyze_research_item(
    title: str,
    summary: str,
    interests: list[str]
) -> ResearchInsight:

    prompt = f"""
You are an expert AI research analyst.

Return ONLY valid JSON.

Schema:

{{
    "topics": ["topic1", "topic2"],
    "relevance_score": 0-10,
    "priority": "READ_NOW | READ_THIS_WEEK | SKIP",
    "why_it_matters": "...",
    "summary": "..."
}}

User Interests:
{interests}

Research Title:
{title}

Research Summary:
{summary}
"""

    response = invoke_for_task("analysis", prompt)

    data = parse_llm_json(response)

    return ResearchInsight(**data)