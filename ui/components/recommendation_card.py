import streamlit as st

# from app.config.config_loader import get_user_interests


def render_recommendation(digest, interests):
    """
    Render personalized recommendation.
    """

    # interests = get_user_interests()

    paper = digest.biggest_breakthrough

    st.markdown("## 🎯 Recommended For You")

    with st.container(border=True):

        st.markdown(
            "### Based on your interests"
        )

        cols = st.columns(
            min(len(interests), 4)
        )

        for i, interest in enumerate(interests):

            cols[i % 4].success(interest)

        st.divider()

        st.markdown(
            "### 📄 Start With"
        )

        st.markdown(
            f"## {paper.title}"
        )

        st.caption(
            f"Source: {paper.source}"
        )

        st.write(
            paper.reason
        )

        st.info(
            f"🚀 Impact: {paper.impact}"
        )

        st.success(
            f"⏱ Estimated Reading Time: {paper.reading_time}"
        )