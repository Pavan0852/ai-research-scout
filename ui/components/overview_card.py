import streamlit as st


def render_overview(digest):
    """
    Render the dashboard overview section.
    """

    st.markdown("## 📊 Today's Research Overview")

    total_items = digest.total_items

    papers = len(digest.featured_papers)

    repositories = len(digest.featured_repositories)

    trends = len(digest.top_trends)

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            label="⭐ Research Score",
            value=f"{digest.research_score}/5",
        )

    with col2:

        st.metric(
            label="📄 Papers",
            value=papers,
        )

    with col3:

        st.metric(
            label="💻 GitHub",
            value=repositories,
        )

    with col4:

        st.metric(
            label="🔥 Trends",
            value=trends,
        )

    st.markdown("---")

    st.markdown("### 📝 Executive Summary")

    st.info(digest.overview)

    st.caption(
        f"Today's digest analyzed **{total_items}** research items "
        "from multiple AI research sources."
    )