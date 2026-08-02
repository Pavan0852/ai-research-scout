# Breakthrough Card Component
import streamlit as st


def render_breakthrough(digest):
    """
    Render the biggest breakthrough section.
    """

    st.subheader("🏆 Biggest Breakthrough")

    breakthrough = digest.biggest_breakthrough

    with st.container(border=True):

        col1, col2 = st.columns([4, 1])

        with col1:
            st.markdown(f"### {breakthrough.title}")
            st.caption(f"Source: {breakthrough.source}")

        with col2:
            st.metric(
                label="Impact",
                value=breakthrough.impact
            )

        st.markdown("#### Why it Matters")

        st.write(breakthrough.reason)

        st.caption(
            f"📖 Estimated Reading Time: {breakthrough.reading_time}"
        )

        if getattr(breakthrough, "url", None):

            st.link_button(
                "📄 Read Breakthrough",
                breakthrough.url,
                use_container_width=True,
            )