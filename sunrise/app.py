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
    button_level = min(no_clicks, 8)
    yes_flex = min(1.45 + button_level * 0.55, 6.0)
    no_flex = max(1.1 - button_level * 0.11, 0.24)
    yes_height = min(3.55 + button_level * 0.38, 6.4)
    no_height = max(3.05 - button_level * 0.18, 1.72)
    yes_font = min(1.08 + button_level * 0.17, 2.25)
    no_font = max(0.98 - button_level * 0.075, 0.42)
    yes_mobile_font = min(1.02 + button_level * 0.115, 1.72)
    no_mobile_font = max(0.9 - button_level * 0.055, 0.38)

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
                width: min(100%, 640px);
                margin: 1rem auto 0;
                color: rgba(42, 21, 52, 0.62);
                font-size: 0.92rem;
                font-weight: 600;
                text-align: center;
            }}

            [data-testid="stHorizontalBlock"] {{
                width: min(100%, 680px);
                margin: 0.55rem auto 0;
                display: flex !important;
                flex-wrap: nowrap !important;
                align-items: stretch !important;
                justify-content: center !important;
                gap: clamp(0.5rem, 2.8vw, 1.05rem);
            }}

            [data-testid="stHorizontalBlock"] [data-testid="column"] {{
                min-width: 0 !important;
                transition: flex 260ms ease, width 260ms ease;
            }}

            [data-testid="stHorizontalBlock"] [data-testid="column"]:first-child {{
                flex: {yes_flex} 1 0 !important;
                width: auto !important;
            }}

            [data-testid="stHorizontalBlock"] [data-testid="column"]:last-child {{
                flex: {no_flex} 1 0 !important;
                width: auto !important;
                max-width: max(3.2rem, 42vw);
            }}

            [data-testid="stHorizontalBlock"] .stButton {{
                height: 100%;
            }}

            .stButton button {{
                width: 100%;
                white-space: nowrap;
                position: relative;
                isolation: isolate;
                overflow: hidden;
                transform: translateY(0);
                transition:
                    transform 220ms ease,
                    box-shadow 220ms ease,
                    filter 220ms ease,
                    min-height 260ms ease,
                    font-size 260ms ease,
                    padding 260ms ease;
                -webkit-tap-highlight-color: transparent;
            }}

            .stButton button::before {{
                content: "";
                position: absolute;
                inset: 0;
                z-index: -1;
                opacity: 0;
                transition: opacity 240ms ease, transform 420ms ease;
            }}

            .stButton button:hover {{
                transform: translateY(-2px);
            }}

            .stButton button:active {{
                transform: translateY(1px) scale(0.985);
            }}

            [data-testid="stHorizontalBlock"] [data-testid="column"]:first-child .stButton button,
            .st-key-yes_button .stButton button {{
                min-height: {yes_height}rem;
                padding: clamp(0.85rem, 2.4vw, 1.1rem) clamp(1rem, 4vw, 2rem);
                border: 0;
                border-radius: 999px;
                color: #351222;
                background:
                    radial-gradient(circle at 30% 18%, rgba(255, 255, 255, 0.85), transparent 19%),
                    linear-gradient(135deg, #fff7b8 0%, #ffd166 36%, #ff986f 72%, #ff6f91 100%);
                box-shadow:
                    0 20px 42px rgba(255, 126, 82, 0.34),
                    0 8px 18px rgba(78, 27, 57, 0.14),
                    inset 0 1px 0 rgba(255, 255, 255, 0.78),
                    inset 0 -7px 14px rgba(147, 54, 57, 0.12);
                font-size: clamp(1.05rem, calc(3.1vw + 0.2rem), {yes_font}rem);
                font-weight: 900;
                letter-spacing: 0;
                text-shadow: 0 1px 0 rgba(255, 255, 255, 0.42);
            }}

            [data-testid="stHorizontalBlock"] [data-testid="column"]:first-child .stButton button::before,
            .st-key-yes_button .stButton button::before {{
                background: linear-gradient(120deg, transparent 0%, rgba(255, 255, 255, 0.62) 42%, transparent 64%);
                transform: translateX(-120%) skewX(-18deg);
            }}

            [data-testid="stHorizontalBlock"] [data-testid="column"]:first-child .stButton button:hover,
            .st-key-yes_button .stButton button:hover {{
                filter: brightness(1.04) saturate(1.05);
                box-shadow:
                    0 26px 54px rgba(255, 126, 82, 0.43),
                    0 12px 24px rgba(78, 27, 57, 0.16),
                    inset 0 1px 0 rgba(255, 255, 255, 0.82),
                    inset 0 -7px 14px rgba(147, 54, 57, 0.1);
            }}

            [data-testid="stHorizontalBlock"] [data-testid="column"]:first-child .stButton button:hover::before,
            .st-key-yes_button .stButton button:hover::before {{
                opacity: 1;
                transform: translateX(120%) skewX(-18deg);
            }}

            [data-testid="stHorizontalBlock"] [data-testid="column"]:last-child .stButton button,
            .st-key-no_button .stButton button {{
                min-height: {no_height}rem;
                padding: clamp(0.45rem, 1.6vw, 0.85rem) clamp(0.45rem, 2.4vw, 1rem);
                border: 1px solid rgba(82, 38, 66, 0.16);
                border-radius: 999px;
                color: rgba(70, 31, 58, 0.88);
                background:
                    linear-gradient(145deg, rgba(255, 255, 255, 0.78), rgba(255, 244, 236, 0.48));
                box-shadow:
                    0 12px 26px rgba(67, 28, 58, 0.13),
                    inset 0 1px 0 rgba(255, 255, 255, 0.72),
                    inset 0 -5px 12px rgba(88, 38, 68, 0.06);
                font-size: clamp(0.42rem, calc(2.1vw + 0.12rem), {no_font}rem);
                font-weight: 800;
                letter-spacing: 0;
                opacity: {max(0.44, no_flex)};
            }}

            [data-testid="stHorizontalBlock"] [data-testid="column"]:last-child .stButton button::before,
            .st-key-no_button .stButton button::before {{
                background: linear-gradient(135deg, rgba(255, 209, 102, 0.16), rgba(255, 92, 138, 0.12));
            }}

            [data-testid="stHorizontalBlock"] [data-testid="column"]:last-child .stButton button:hover,
            .st-key-no_button .stButton button:hover {{
                background:
                    linear-gradient(145deg, rgba(255, 255, 255, 0.86), rgba(255, 244, 236, 0.6));
                box-shadow:
                    0 16px 32px rgba(67, 28, 58, 0.16),
                    inset 0 1px 0 rgba(255, 255, 255, 0.78);
            }}

            [data-testid="stHorizontalBlock"] [data-testid="column"]:last-child .stButton button:hover::before,
            .st-key-no_button .stButton button:hover::before {{
                opacity: 1;
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
                    width: min(100%, 94vw);
                    gap: clamp(0.35rem, 2.4vw, 0.7rem);
                    padding-inline: 0.1rem;
                }}

                [data-testid="stHorizontalBlock"] [data-testid="column"]:first-child {{
                    flex: {yes_flex} 1 0 !important;
                }}

                [data-testid="stHorizontalBlock"] [data-testid="column"]:last-child {{
                    flex: {no_flex} 1 0 !important;
                    min-width: clamp(2.75rem, 14vw, 5.4rem) !important;
                    max-width: 36vw;
                }}

                [data-testid="stHorizontalBlock"] [data-testid="column"]:first-child .stButton button,
                .st-key-yes_button .stButton button {{
                    min-height: clamp(3.1rem, {15 + button_level * 1.4}vw, {yes_height}rem);
                    padding-inline: clamp(0.8rem, 3vw, 1.45rem);
                    font-size: clamp(1rem, {5.1 + button_level * 0.42}vw, {yes_mobile_font}rem);
                }}

                [data-testid="stHorizontalBlock"] [data-testid="column"]:last-child .stButton button,
                .st-key-no_button .stButton button {{
                    min-height: clamp(1.55rem, {11 - min(button_level, 6) * 0.55}vw, {no_height}rem);
                    padding-inline: clamp(0.32rem, 1.8vw, 0.75rem);
                    font-size: clamp(0.38rem, {3.8 - min(button_level, 6) * 0.18}vw, {no_mobile_font}rem);
                }}
            }}

            @media (max-width: 390px) {{
                .main-title {{
                    font-size: clamp(1.82rem, 11vw, 2.45rem);
                }}
                [data-testid="stHorizontalBlock"] {{
                    width: min(100%, 96vw);
                    gap: 0.32rem;
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
        if st.button("YES 💛", key="yes_button", use_container_width=True):
            st.session_state.forgiven = True
            st.balloons()

    with right:
        if st.button("NO 😔", key="no_button", use_container_width=True):
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
