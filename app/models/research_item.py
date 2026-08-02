from pydantic import BaseModel

class ResearchItem(BaseModel):
    source: str
    title: str
    url: str
    summary: str