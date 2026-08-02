from app.collectors.arxiv_collector import fetch_latest_papers
from app.collectors.github_collector import fetch_github_projects


def build_feed(
    interests: list[str],
    max_results: int = 5,
):

    query = " OR ".join(interests)

    feed = []

    feed.extend(
        fetch_latest_papers(
            query=query,
            max_results=max_results,
        )
    )

    feed.extend(
        fetch_github_projects(
            query=query,
            max_results=max_results,
        )
    )

    return feed