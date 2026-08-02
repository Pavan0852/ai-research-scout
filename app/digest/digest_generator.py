import json
import re
from datetime import date

from app.models.research_digest import ResearchDigest
from app.providers.llm_router import invoke_for_task


def parse_json(response: str):
    """
    Extract JSON from the LLM response.
    """

    match = re.search(
        r"\{.*\}",
        response,
        re.DOTALL,
    )

    if not match:
        raise ValueError(
            f"No JSON found in LLM response:\n\n{response}"
        )

    return json.loads(match.group())


def generate_digest(insights):
    """
    Generate the final ScoutAI Daily Digest.
    """

    formatted = []

    for item in insights:

        paper = item["paper"]
        insight = item["insight"]

        formatted.append(
            {
                "title": paper.title,
                "source": paper.source,
                "url": paper.url,
                "summary": insight.summary,
                "priority": insight.priority,
                "relevance_score": insight.relevance_score,
                "topics": insight.topics,
                "why_it_matters": insight.why_it_matters,
            }
        )

    schema = """
{
  "date": "YYYY-MM-DD",

  "overview": "",

  "research_score": 4,

  "total_items": 10,

  "top_trends": [
    {
      "topic": "",
      "description": ""
    }
  ],

  "biggest_breakthrough": {
    "title": "",
    "source": "",
    "reason": "",
    "impact": "",
    "reading_time": ""
  },

  "featured_papers": [
    {
      "title": "",
      "source": "",
      "reason": "",
      "impact": "",
      "reading_time": ""
    }
  ],

  "featured_repositories": [
    {
      "title": "",
      "source": "",
      "reason": "",
      "impact": "",
      "reading_time": ""
    }
  ],

  "reading_plan": {
    "quick_read": [],
    "deep_dive": [],
    "quick_read_time": "",
    "deep_dive_time": ""
  },

  "key_takeaways": [],

  "who_should_read": []
}
"""

    prompt = f"""
You are the Chief Editor of ScoutAI Daily.

ScoutAI Daily is an AI Research Intelligence Platform.

Your responsibility is NOT to summarize every paper individually.

Instead, analyze today's research collectively and generate an executive research briefing.

Research Feed:

{json.dumps(formatted, indent=2)}

Instructions:

1. Identify today's overall AI research direction.
2. Identify the single biggest breakthrough.
3. Identify the major emerging research trends.
4. Select the best GitHub repository.
5. Select the most important research papers.
6. Create a reading plan.
7. Generate actionable key takeaways.
8. Recommend who should read today's research.

Rules:

- Use ONLY the supplied research feed.
- Do NOT invent papers.
- Do NOT invent repositories.
- Do NOT fabricate facts.
- Return ONLY valid JSON.
- Follow the schema EXACTLY.

Schema:

{schema}
"""

    response = invoke_for_task(
        task="digest",
        prompt=prompt,
    )

    data = parse_json(response)

    # -----------------------------------------------------
    # Enrich digest with original URLs
    # -----------------------------------------------------

    url_lookup = {
        item["title"]: item["url"]
        for item in formatted
    }

    # Biggest breakthrough
    if "biggest_breakthrough" in data:

        title = data["biggest_breakthrough"].get("title")

        data["biggest_breakthrough"]["url"] = (
            url_lookup.get(title)
        )

    # Featured papers
    for paper in data.get("featured_papers", []):

        paper["url"] = url_lookup.get(
            paper["title"]
        )

    # Featured repositories
    for repo in data.get(
        "featured_repositories",
        []
    ):

        repo["url"] = url_lookup.get(
            repo["title"]
        )

    if not data.get("date"):
        data["date"] = str(date.today())

    try:
        return ResearchDigest(**data)

    except Exception:

        print("\n========== INVALID DIGEST ==========\n")
        print(json.dumps(data, indent=2))
        print("\n====================================\n")

        raise