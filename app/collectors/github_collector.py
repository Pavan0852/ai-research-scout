import requests

from app.models.research_item import ResearchItem


def fetch_github_projects(
    query: str,
    max_results: int = 5,
):

    url = "https://api.github.com/search/repositories"

    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": max_results,
    }

    response = requests.get(
        url,
        params=params,
        timeout=30,
    )

    response.raise_for_status()

    data = response.json()

    projects = []

    for repo in data.get("items", []):

        projects.append(
            ResearchItem(
                source="GitHub",
                title=repo["name"],
                url=repo["html_url"],
                summary=repo.get("description") or "",
            )
        )

    return projects