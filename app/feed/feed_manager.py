from app.collectors.feed_collector import build_feed
from app.analyst.research_analyst import analyze_research_item


def get_top_research(
    interests,
    max_results=5,
):

    feed = build_feed(
        interests=interests,
        max_results=max_results,
    )

    insights = []

    for item in feed:

        insight = analyze_research_item(
            title=item.title,
            summary=item.summary,
            interests=interests,
        )

        insights.append(
            {
                "paper": item,
                "insight": insight,
            }
        )

    insights.sort(
        key=lambda x: x["insight"].relevance_score,
        reverse=True,
    )

    return insights