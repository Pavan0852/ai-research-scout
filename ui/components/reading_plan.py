# Reading Plan Component
import streamlit as st


def render_reading_plan(digest):
    """
    Render the recommended reading plan.
    """

    st.subheader("📚 Recommended Reading Plan")

    plan = digest.reading_plan

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### ⚡ Quick Read")

        st.caption(
            f"Estimated Time: {plan.quick_read_time}"
        )

        if plan.quick_read:

            for item in plan.quick_read:

                st.markdown(f"• {item}")

        else:

            st.info("No quick reading recommendations.")

    with col2:

        st.markdown("### 📖 Deep Dive")

        st.caption(
            f"Estimated Time: {plan.deep_dive_time}"
        )

        if plan.deep_dive:

            for item in plan.deep_dive:

                st.markdown(f"• {item}")

        else:

            st.info("No deep dive recommendations.")
            