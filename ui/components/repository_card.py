import streamlit as st


def render_featured_repositories(digest):
    """
    Render featured GitHub repositories.
    """

    st.markdown("## 🚀 Featured GitHub Repositories")

    if not digest.featured_repositories:
        st.info("No featured repositories available.")
        return

    for index, repo in enumerate(
        digest.featured_repositories,
        start=1,
    ):

        with st.container(border=True):

            col1, col2 = st.columns([5, 1])

            with col1:

                st.markdown(
                    f"### {index}. {repo.title}"
                )

                st.caption(
                    f"Source: {repo.source}"
                )

            with col2:

                st.metric(
                    label="Impact",
                    value=repo.impact,
                )

            st.markdown("#### Why Explore This Repository?")

            st.write(repo.reason)

            st.caption(
                f"⏱ Estimated Exploration Time: {repo.reading_time}"
            )

            if getattr(repo, "url", None):

                st.link_button(
                    label="💻 Open Repository",
                    url=repo.url,
                    use_container_width=True,
                )

            st.divider()