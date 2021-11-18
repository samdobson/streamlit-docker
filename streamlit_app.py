import streamlit as st
from streamlit_ace import st_ace


st.set_page_config(
    page_title="Streamlit Docker",
    page_icon=":memo:",
    layout="wide",
    initial_sidebar_state="collapsed",
)
st.sidebar.title(":memo: Editor settings")

THEMES = [
    "ambiance",
    "chaos",
    "chrome",
    "clouds",
    "clouds_midnight",
    "cobalt",
    "crimson_editor",
    "dawn",
    "dracula",
    "dreamweaver",
    "eclipse",
    "github",
    "gob",
    "gruvbox",
    "idle_fingers",
    "iplastic",
    "katzenmilch",
    "kr_theme",
    "kuroir",
    "merbivore",
    "merbivore_soft",
    "mono_industrial",
    "monokai",
    "nord_dark",
    "pastel_on_dark",
    "solarized_dark",
    "solarized_light",
    "sqlserver",
    "terminal",
    "textmate",
    "tomorrow",
    "tomorrow_night",
    "tomorrow_night_blue",
    "tomorrow_night_bright",
    "tomorrow_night_eighties",
    "twilight",
    "vibrant_ink",
    "xcode",
]

KEYBINDINGS = ["emacs", "sublime", "vim", "vscode"]

display, editor = st.beta_columns((2, 1))

INITIAL_CODE = """st.header("Streamlit in Docker")
st.write("If you are seeing this message, your Streamlit container is running!")
"""

with editor:
    st.write("### Code editor")
    code = st_ace(
        value=INITIAL_CODE,
        language="python",
        placeholder="st.header('Hello world!')",
        theme=st.sidebar.selectbox("Theme", options=THEMES, index=26),
        keybinding=st.sidebar.selectbox(
            "Keybinding mode", options=KEYBINDINGS, index=3
        ),
        font_size=st.sidebar.slider("Font size", 5, 24, 14),
        tab_size=st.sidebar.slider("Tab size", 1, 8, 4),
        wrap=st.sidebar.checkbox("Wrap lines", value=False),
        show_gutter=True,
        show_print_margin=True,
        auto_update=False,
        readonly=False,
        key="ace-editor",
    )
    st.write("Hit `CTRL+ENTER` to refresh")
    st.write("*Remember to save your code separately!*")

with display:
    exec(code)
