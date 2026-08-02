from pydantic import BaseModel


class ResearchInsight(BaseModel):

    topics: list[str]

    relevance_score: float

    priority: str

    why_it_matters: str

    summary: str