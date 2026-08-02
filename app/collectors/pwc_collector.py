from app.models.research_item import ResearchItem

def fetch_pwc_entries():

    return [
        ResearchItem(
            source="PapersWithCode",
            title="Example PWC Entry",
            url="https://paperswithcode.com",
            summary="No description"
        )
    ]