# Trend Card Component
import streamlit as st


def render_trends(digest):
    """
    Render the AI research trends section.
    """

    st.subheader("📈 AI Landscape Today")

    if not digest.top_trends:
        st.info("No trends identified.")
        return

    for trend in digest.top_trends:

        with st.container(border=True):

            st.markdown(f"### 🚀 {trend.topic}")

            st.write(trend.description)