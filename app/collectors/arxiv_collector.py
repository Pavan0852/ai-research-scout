import arxiv

from app.models.research_item import ResearchItem


def fetch_latest_papers(
    query: str,
    max_results: int = 5,
):

    client = arxiv.Client()

    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
    )

    papers = []

    for result in client.results(search):

        papers.append(
            ResearchItem(
                source="arXiv",
                title=result.title,
                url=result.entry_id,
                summary=result.summary,
            )
        )

    return papers