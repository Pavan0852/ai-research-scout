"""
ScoutAI
Main Streamlit Application
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

import streamlit as st

from app.services.scout_service import generate_daily_digest
from app.config.config_loader import (
    get_enabled_sources,
    get_llm_provider,
    get_user_interests,
)

from ui.components.header import render_header
from ui.components.overview_card import render_overview
from ui.components.recommendation_card import render_recommendation
from ui.components.trend_card import render_trends
from ui.components.breakthrough_card import render_breakthrough
from ui.components.paper_card import render_featured_papers
from ui.components.repository_card import render_featured_repositories
from ui.components.reading_plan import render_reading_plan
from ui.components.takeaway_card import render_takeaways


# -------------------------------------------------------
# Cache
# -------------------------------------------------------

# @st.cache_data(ttl=3600)
def cached_digest():
    """
    Cache the generated digest for one hour.
    """
    return generate_daily_digest()


# -------------------------------------------------------
# Sidebar
# -------------------------------------------------------

def render_sidebar():
    """
    Render application sidebar.
    """

    st.sidebar.title("⚙ ScoutAI Configuration")

    # ----------------------------
    # Interests
    # ----------------------------

    st.sidebar.markdown("### Interests")

    available_interests = get_user_interests()

    selected_interests = st.sidebar.multiselect(
        label="🎯 Personalize Today's Research Digest",
        options=available_interests,
        default=available_interests[:3],   # Default selections
    )

    for interest in selected_interests:
        st.sidebar.success(interest)

    # ----------------------------
    # Sources
    # ----------------------------

    st.sidebar.markdown("---")

    st.sidebar.markdown("### Sources")

    sources = get_enabled_sources()

    for source, enabled in sources.items():

        if enabled:
            st.sidebar.write(f"✅ {source}")
        else:
            st.sidebar.write(f"❌ {source}")

    # ----------------------------
    # LLM Provider
    # ----------------------------

    st.sidebar.markdown("---")

    st.sidebar.markdown("### LLM Provider")

    st.sidebar.info(get_llm_provider())

    st.sidebar.markdown("---")

    generate = st.sidebar.button(
        "🚀 Generate Today's Research Digest",
        use_container_width=True,
    )

    return generate, selected_interests


# -------------------------------------------------------
# Session State
# -------------------------------------------------------

if "response" not in st.session_state:

    st.session_state.response = None


# -------------------------------------------------------
# Main
# -------------------------------------------------------

def main():

    render_header()

    generate, selected_interests  = render_sidebar()

    if generate:

        with st.spinner(
            "🔍 Collecting papers...\n\n"
            "🧠 AI is analyzing research...\n\n"
            "📝 Creating today's digest..."
        ):

            # Clear previous cache so a fresh digest is generated
            # cached_digest.clear()

            st.session_state.response = generate_daily_digest(
                interests=selected_interests
            )

        st.success(
            "Today's ScoutAI Digest is ready!"
        )

    if st.session_state.response is None:

        st.info(
            "Click **Generate Today's Digest** "
            "from the sidebar."
        )

        return

    response = st.session_state.response

    digest = response.digest

    render_overview(digest)

    render_recommendation(digest, selected_interests)

    st.divider()

    col1, col2 = st.columns([1, 1])

    with col1:

        render_trends(digest)

    with col2:

        render_breakthrough(digest)

    st.divider()

    render_featured_papers(digest)

    st.divider()

    render_featured_repositories(digest)

    st.divider()

    render_reading_plan(digest)

    st.divider()

    render_takeaways(digest)

    st.divider()

    search_query = st.text_input(
        "🔍 Search Research",
        placeholder="Search title, summary or topic..."
    )

    render_detailed_results(
        response.results,
        search_query,
    )

    st.divider()

    st.caption(
        "Built with ❤️ using "
        "OpenRouter • Streamlit • arXiv • GitHub API"
    )

# -------------------------------------------------------
# Detailed Research Results
# -------------------------------------------------------


def render_detailed_results(
    results,
    search_query: str = "",
):
    """
    Render the detailed research feed.
    """

    st.header("📚 Research Feed")

    if search_query:

        st.caption(
            f"Showing results matching **{search_query}**"
        )

    shown = 0

    for idx, result in enumerate(results, start=1):

        paper = result.paper
        insight = result.insight

        searchable_text = " ".join(
            [
                paper.title,
                paper.summary,
                insight.summary,
                insight.why_it_matters,
                " ".join(insight.topics),
            ]
        ).lower()

        if (
            search_query
            and search_query.lower() not in searchable_text
        ):
            continue

        shown += 1

        with st.expander(
            f"{idx}. {paper.title}",
            expanded=False,
        ):

            col1, col2, col3 = st.columns(
                [2.5, 1.2, 1]
            )

            with col1:

                st.markdown(
                    f"### {paper.title}"
                )

                st.caption(
                    f"Source: {paper.source}"
                )

            with col2:

                st.metric(
                    "Priority",
                    insight.priority.replace(
                        "_",
                        " "
                    ),
                )

            with col3:

                st.metric(
                    "Relevance",
                    f"{insight.relevance_score}/10",
                )

            st.markdown("#### 🏷 Topics")

            topic_cols = st.columns(
                min(
                    len(insight.topics),
                    4,
                )
            )

            for i, topic in enumerate(
                insight.topics
            ):

                topic_cols[
                    i % len(topic_cols)
                ].info(topic)

            st.markdown(
                "#### 📝 AI Summary"
            )

            st.write(
                insight.summary
            )

            st.markdown(
                "#### 💡 Why It Matters"
            )

            st.write(
                insight.why_it_matters
            )

            st.link_button(
                "📄 Read Original Paper",
                paper.url,
                use_container_width=True,
            )

    if shown == 0:

        st.warning(
            "No research matched your search."
        )

    render_footer()


# -------------------------------------------------------
# Footer
# -------------------------------------------------------

def render_footer():

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:

        st.caption("Built with")

        st.write(
            "🤖 OpenRouter\n\n"
            "📚 arXiv\n\n"
            "💻 GitHub API"
        )

    with c2:

        st.caption("Framework")

        st.write(
            "⚡ Streamlit\n\n"
            "🐍 Python\n\n"
            "📦 Pydantic"
        )

    with c3:

        st.caption("ScoutAI")

        st.write(
            "AI Research Intelligence Platform\n\n"
            "Powered by Task-specific LLM Routing"
        )

    st.divider()

    st.caption(
        "© 2026 ScoutAI • Built by Pavan Kumar Gudla"
    )


# -------------------------------------------------------
# Run
# -------------------------------------------------------

if __name__ == "__main__":

    main()

    # render_footer()