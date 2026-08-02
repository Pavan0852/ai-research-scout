# Takeaway Card Component
import streamlit as st


def render_takeaways(digest):
    """
    Render the key takeaways and recommended audience.
    """

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("💡 Key Takeaways")

        if digest.key_takeaways:

            for takeaway in digest.key_takeaways:

                st.success(takeaway)

        else:

            st.info("No key takeaways available.")

    with col2:

        st.subheader("👥 Who Should Read This")

        if digest.who_should_read:

            for audience in digest.who_should_read:

                st.markdown(f"✅ {audience}")

        else:

            st.info("No audience recommendations available.")