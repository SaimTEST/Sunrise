import streamlit as st


IMAGE_URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhumCMHdOcA1iWXpHchaqrl2IqMQhZTHC9dA&s"

NO_MESSAGES = [
    "Are you sure? 🥺",
    "Please think again 🌅",
    "My sunrise deserves a yes 💛",
    "Don't break my little heart 😭",
    "The YES button looks better anyway 😅",
    "I'll keep waiting 🌅",
]


def initialize_state() -> None:
    """Create the tiny interaction state used by the two buttons."""
    if "no_clicks" not in st.session_state:
        st.session_state.no_clicks = 0
    if "forgiven" not in st.session_state:
        st.session_state.forgiven = False


def inject_styles(no_clicks: int, forgiven: bool) -> None:
    yes_scale = min(1 + no_clicks * 0.22, 2.65)
    no_scale = max(1 - no_clicks * 0.13, 0.2)
    yes_font = min(1.05 + no_clicks * 0.18, 2.15)
    no_font = max(1.0 - no_clicks * 0.1, 0.35)

    st.markdown(
        f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

            :root {{
                --sunrise-gold: #ffd166;
                --warm-coral: #ff7a59;
                --rose: #ff5c8a;
                --deep-plum: #2a1534;
                --cream: #fff8ee;
            }}

            html {{
                scroll-behavior: smooth;
            }}

            body {{
                font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
            }}

            .stApp {{
                min-height: 100vh;
                background:
                    radial-gradient(circle at 20% 12%, rgba(255, 209, 102, 0.42), transparent 26rem),
                    radial-gradient(circle at 82% 18%, rgba(255, 92, 138, 0.28), transparent 24rem),
                    linear-gradient(135deg, #fff3df 0%, #ffd7bd 34%, #ff9a7b 64%, #4f244f 100%);
                color: var(--deep-plum);
            }}

            .block-container {{
                max-width: 940px;
                padding: clamp(1.25rem, 4vw, 3rem) 1rem 2.5rem;
            }}

            header, footer, [data-testid="stToolbar"], [data-testid="stDecoration"] {{
                display: none !important;
            }}

            .sunrise-shell {{
                width: min(100%, 780px);
                margin: clamp(0.5rem, 4vh, 2rem) auto 0;
                display: flex;
                align-items: center;
                justify-content: center;
                animation: fadeIn 850ms ease both;
            }}

            .sunrise-card {{
                width: 100%;
                position: relative;
                overflow: hidden;
                text-align: center;
                border: 1px solid rgba(255, 255, 255, 0.72);
                border-radius: 32px;
                padding: clamp(1.35rem, 5vw, 3.2rem);
                background: rgba(255, 250, 244, 0.64);
                box-shadow: 0 28px 80px rgba(66, 24, 52, 0.24);
                backdrop-filter: blur(24px);
            }}

            .sunrise-card::before {{
                content: "";
                position: absolute;
                inset: 0;
                pointer-events: none;
                background: linear-gradient(145deg, rgba(255,255,255,0.78), transparent 38%, rgba(255,209,102,0.18));
            }}

            .sunrise-content {{
                position: relative;
                z-index: 1;
            }}

            .eyebrow {{
                margin: 0 0 0.75rem;
                color: rgba(42, 21, 52, 0.72);
                font-size: clamp(0.78rem, 2.8vw, 0.95rem);
                font-weight: 700;
                letter-spacing: 0;
                text-transform: uppercase;
            }}

            .main-title {{
                margin: 0 auto;
                max-width: 760px;
                color: var(--deep-plum);
                font-size: clamp(2.15rem, 8vw, 5.15rem);
                line-height: 0.98;
                font-weight: 800;
                letter-spacing: 0;
                text-wrap: balance;
                text-shadow: 0 10px 34px rgba(255, 255, 255, 0.52);
                animation: floatIn 900ms 120ms ease both;
            }}

            .sunrise-image {{
                display: block;
                width: min(100%, 440px);
                aspect-ratio: 1 / 1;
                object-fit: cover;
                margin: clamp(1.25rem, 4vw, 2.1rem) auto 1rem;
                border-radius: clamp(22px, 5vw, 34px);
                border: 7px solid rgba(255, 255, 255, 0.62);
                box-shadow: 0 26px 58px rgba(77, 33, 62, 0.26), 0 4px 14px rgba(255, 122, 89, 0.22);
                transition: transform 240ms ease, box-shadow 240ms ease;
                animation: softZoom 900ms 220ms ease both;
            }}

            .sunrise-image:hover {{
                transform: translateY(-4px) scale(1.015);
                box-shadow: 0 34px 76px rgba(77, 33, 62, 0.3), 0 8px 20px rgba(255, 122, 89, 0.24);
            }}

            .message-line {{
                min-height: 2.1rem;
                margin: 0.75rem auto 0.9rem;
                color: #66304f;
                font-size: clamp(1rem, 3.6vw, 1.22rem);
                font-weight: 700;
                animation: fadeIn 420ms ease both;
            }}

            .button-caption {{
                margin: 1rem 0 0;
                color: rgba(42, 21, 52, 0.62);
                font-size: 0.92rem;
                font-weight: 600;
            }}

            [data-testid="stHorizontalBlock"] {{
                width: min(100%, 580px);
                margin: 0.35rem auto 0;
                align-items: center;
                gap: clamp(0.4rem, 2vw, 1rem);
            }}

            [data-testid="stHorizontalBlock"] [data-testid="column"]:first-child .stButton button {{
                min-height: clamp(3.35rem, 9vw, 4.25rem);
                border: 0;
                border-radius: 999px;
                color: #311323;
                background: linear-gradient(135deg, #fff4a8 0%, #ffd166 48%, #ff8f70 100%);
                box-shadow: 0 18px 36px rgba(255, 142, 86, 0.34);
                font-size: {yes_font}rem;
                font-weight: 800;
                transform: scale({yes_scale});
                transform-origin: center;
                transition: transform 220ms ease, box-shadow 220ms ease, filter 220ms ease;
            }}

            [data-testid="stHorizontalBlock"] [data-testid="column"]:first-child .stButton button:hover {{
                filter: brightness(1.03);
                box-shadow: 0 22px 46px rgba(255, 142, 86, 0.42);
                transform: scale(calc({yes_scale} + 0.04));
            }}

            [data-testid="stHorizontalBlock"] [data-testid="column"]:last-child .stButton button {{
                min-height: clamp(2.25rem, 7vw, 3.55rem);
                border: 1px solid rgba(82, 38, 66, 0.18);
                border-radius: 999px;
                color: #512747;
                background: rgba(255, 255, 255, 0.56);
                box-shadow: 0 12px 24px rgba(67, 28, 58, 0.12);
                font-size: {no_font}rem;
                font-weight: 800;
                transform: scale({no_scale});
                transform-origin: center;
                opacity: {max(0.38, no_scale)};
                transition: transform 220ms ease, opacity 220ms ease, background 220ms ease;
            }}

            [data-testid="stHorizontalBlock"] [data-testid="column"]:last-child .stButton button:hover {{
                background: rgba(255, 255, 255, 0.72);
                transform: scale(calc({no_scale} + 0.03));
            }}

            .stButton button {{
                width: 100%;
                white-space: nowrap;
            }}

            .celebration {{
                width: min(100%, 620px);
                margin: 1.2rem auto 0;
                padding: clamp(1.25rem, 5vw, 2.4rem);
                border-radius: 30px;
                background:
                    linear-gradient(135deg, rgba(255,255,255,0.88), rgba(255,245,222,0.74)),
                    linear-gradient(135deg, rgba(255,209,102,0.42), rgba(255,92,138,0.22));
                border: 1px solid rgba(255, 255, 255, 0.78);
                box-shadow: 0 24px 70px rgba(62, 22, 49, 0.24);
                animation: popIn 560ms cubic-bezier(.2, .9, .2, 1.2) both;
            }}

            .celebration h2 {{
                margin: 0 0 0.6rem;
                font-size: clamp(2rem, 8vw, 4.6rem);
                line-height: 1;
                color: #3b172b;
                letter-spacing: 0;
            }}

            .celebration p {{
                margin: 0.35rem auto;
                max-width: 520px;
                color: #653052;
                font-size: clamp(1rem, 3.6vw, 1.35rem);
                font-weight: 700;
            }}

            .sparkles {{
                margin-top: 1rem;
                font-size: clamp(1.5rem, 7vw, 3rem);
                animation: pulseGlow 1.6s ease-in-out infinite;
            }}

            .floating-hearts {{
                position: fixed;
                inset: auto 0 1.2rem 0;
                pointer-events: none;
                text-align: center;
                font-size: clamp(1.35rem, 5vw, 2.2rem);
                opacity: {1 if forgiven else 0};
                animation: heartsRise 3.2s ease-in-out infinite;
            }}

            @keyframes fadeIn {{
                from {{ opacity: 0; }}
                to {{ opacity: 1; }}
            }}

            @keyframes floatIn {{
                from {{ opacity: 0; transform: translateY(18px); }}
                to {{ opacity: 1; transform: translateY(0); }}
            }}

            @keyframes softZoom {{
                from {{ opacity: 0; transform: scale(0.94); }}
                to {{ opacity: 1; transform: scale(1); }}
            }}

            @keyframes popIn {{
                from {{ opacity: 0; transform: translateY(16px) scale(0.9); }}
                to {{ opacity: 1; transform: translateY(0) scale(1); }}
            }}

            @keyframes pulseGlow {{
                0%, 100% {{ transform: scale(1); filter: drop-shadow(0 0 0 rgba(255, 209, 102, 0)); }}
                50% {{ transform: scale(1.08); filter: drop-shadow(0 0 18px rgba(255, 209, 102, 0.7)); }}
            }}

            @keyframes heartsRise {{
                0% {{ transform: translateY(0); opacity: 0; }}
                25% {{ opacity: 1; }}
                100% {{ transform: translateY(-56px); opacity: 0; }}
            }}

            @media (max-width: 620px) {{
                .block-container {{
                    padding: 0.75rem 0.6rem 1.4rem;
                }}

                .sunrise-card {{
                    border-radius: 24px;
                    padding: 1.15rem 0.85rem 1.35rem;
                }}

                .sunrise-image {{
                    width: min(88vw, 340px);
                    border-width: 5px;
                }}

                [data-testid="stHorizontalBlock"] {{
                    gap: 0.35rem;
                }}
            }}

            @media (max-width: 390px) {{
                .main-title {{
                    font-size: clamp(1.82rem, 11vw, 2.45rem);
                }}

                [data-testid="stHorizontalBlock"] [data-testid="column"]:first-child .stButton button {{
                    font-size: min({yes_font}rem, 1.55rem);
                }}
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def no_message(no_clicks: int) -> str:
    if no_clicks <= 0:
        return ""
    return NO_MESSAGES[min(no_clicks, len(NO_MESSAGES)) - 1]


def render_intro() -> None:
    st.markdown(
        f"""
        <div class="sunrise-shell">
            <section class="sunrise-card">
                <div class="sunrise-content">
                    <p class="eyebrow">A little note for My Sunrise</p>
                    <h1 class="main-title">Will you forgive me, my sunrise? 🌅</h1>
                    <img class="sunrise-image" src="{IMAGE_URL}" alt="Romantic sunrise" />
                </div>
            </section>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_reaction_message() -> None:
    message = no_message(st.session_state.no_clicks)
    st.markdown(
        f'<p class="message-line">{message}</p>' if message else '<p class="message-line">&nbsp;</p>',
        unsafe_allow_html=True,
    )


def render_buttons() -> None:
    no_clicks = st.session_state.no_clicks
    yes_ratio = min(2 + no_clicks, 9)
    no_ratio = max(2 - no_clicks * 0.22, 0.24)

    left, right = st.columns([yes_ratio, no_ratio], gap="medium")

    with left:
        if st.button("YES 💛", use_container_width=True):
            st.session_state.forgiven = True
            st.balloons()

    with right:
        if st.button("NO 😔", use_container_width=True):
            st.session_state.no_clicks += 1
            st.session_state.forgiven = False
            st.rerun()

    st.markdown('<p class="button-caption">Choose carefully. The sunrise is watching.</p>', unsafe_allow_html=True)


def render_celebration() -> None:
    if not st.session_state.forgiven:
        return

    st.markdown(
        """
        <div class="celebration">
            <h2>WAAOUH YAY! 💛🌅</h2>
            <p>Thank you my sunrise, you made my day brighter.</p>
            <div class="sparkles">✨ ❤️ 🌅 🥰</div>
        </div>
        <div class="floating-hearts">✨ ❤️ 🌅 🥰</div>
        """,
        unsafe_allow_html=True,
    )


def main() -> None:
    st.set_page_config(
        page_title="My Sunrise",
        page_icon="🌅",
        layout="centered",
        initial_sidebar_state="collapsed",
    )

    initialize_state()
    inject_styles(st.session_state.no_clicks, st.session_state.forgiven)
    render_intro()
    render_reaction_message()
    render_buttons()
    render_celebration()


if __name__ == "__main__":
    main()
