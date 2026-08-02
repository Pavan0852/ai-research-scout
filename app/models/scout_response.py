from pydantic import BaseModel

from app.models.research_digest import ResearchDigest
from app.models.research_item import ResearchItem
from app.models.research_insight import ResearchInsight


class ResearchResult(BaseModel):
    paper: ResearchItem
    insight: ResearchInsight


class ScoutResponse(BaseModel):
    digest: ResearchDigest
    results: list[ResearchResult]