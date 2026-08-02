from app.feed.feed_manager import get_top_research
from app.digest.digest_generator import generate_digest
from app.models.scout_response import ScoutResponse, ResearchResult
# from app.config.config_loader import get_user_interests


def generate_daily_digest(
        interests: list[str],
        max_results: int = 5,
) -> ScoutResponse:
    """
    Generate the complete ScoutAI response.
    """

    insights = get_top_research(
        interests=interests,
        max_results=max_results,
    )

    digest = generate_digest(insights)

    results = []

    for item in insights:

        results.append(
            ResearchResult(
                paper=item["paper"],
                insight=item["insight"],
            )
        )

    return ScoutResponse(
        digest=digest,
        results=results,
    )