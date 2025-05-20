from fasthtml.common import Div, Main, Link

def get_ui():
    return Main(
        Div("Hello World", cls="child"),
        Link(rel="stylesheet", href="styles.css"),
        cls="parent"
    )
