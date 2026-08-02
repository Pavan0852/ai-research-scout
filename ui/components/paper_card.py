import streamlit as st


def render_featured_papers(digest):
    """
    Render featured research papers.
    """

    st.subheader("📄 Featured Papers")

    if not digest.featured_papers:
        st.info("No featured papers available.")
        return

    for index, paper in enumerate(
        digest.featured_papers,
        start=1,
    ):

        with st.expander(
            f"{index}. {paper.title}",
            expanded=(index == 1),
        ):

            col1, col2 = st.columns([4, 1])

            with col1:
                st.markdown(f"**Source:** {paper.source}")

            with col2:
                st.metric(
                    "Impact",
                    paper.impact,
                )

            st.markdown("#### Why Read This?")

            st.write(paper.reason)

            st.caption(
                f"📖 Estimated Reading Time: {paper.reading_time}"
            )

            # if paper.url:
            #     st.link_button(
            #         "📄 Read Paper",
            #         paper.url,
            #         use_container_width=True,
            #     )

            if getattr(paper, "url", None):
                st.link_button(
                    label="📄 Read Paper",
                    url=paper.url,
                    use_container_width=True,
                )