import streamlit as st


def render_header():
    """
    Render the ScoutAI application header.
    """

    st.set_page_config(
        page_title="ScoutAI",
        page_icon="🔬",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.markdown(
        """
        <style>
        .hero {
            background: linear-gradient(135deg,#2563EB,#7C3AED);
            padding:1.2rem;
            border-radius:18px;
            color:white;
            margin-bottom:25px;
        }

        .hero h1{
            margin-bottom:0.3rem;
            font-size:2.2rem;
        }

        .hero p{
            font-size:1rem;
            opacity:0.95;
        }

        .hero small{
            opacity:0.85;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="hero">

        <h1>🔬 ScoutAI</h1>

        <p><b>AI Research Intelligence Platform</b></p>

        <small>
        Discover • Analyze • Prioritize • Learn
        </small>

        </div>
        """,
        unsafe_allow_html=True,
    )