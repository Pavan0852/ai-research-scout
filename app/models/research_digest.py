"""
Research Digest Models

These models represent the final AI Research Digest
generated from today's research feed.
"""

from typing import Optional

from pydantic import BaseModel, Field


class DigestCard(BaseModel):
    """
    Generic card used for featured papers,
    repositories and breakthroughs.
    """

    title: str = Field(
        description="Title of the paper or repository"
    )

    source: str = Field(
        description="Source such as arXiv or GitHub"
    )

    url: Optional[str] = Field(
        default=None,
        description="Original URL of the paper/repository"
    )

    reason: str = Field(
        description="Why this item is important"
    )

    impact: str = Field(
        description="Impact level"
    )

    reading_time: str = Field(
        description="Estimated reading time"
    )


class Trend(BaseModel):

    topic: str

    description: str


class ReadingPlan(BaseModel):

    quick_read: list[str]

    deep_dive: list[str]

    quick_read_time: str

    deep_dive_time: str


class ResearchDigest(BaseModel):

    date: str

    overview: str

    research_score: int = Field(
        ge=1,
        le=5
    )

    total_items: int

    top_trends: list[Trend]

    biggest_breakthrough: DigestCard

    featured_papers: list[DigestCard]

    featured_repositories: list[DigestCard]

    reading_plan: ReadingPlan

    key_takeaways: list[str]

    who_should_read: list[str]