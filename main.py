from fasthtml.common import *
from user_interface import get_ui

app, rt = fast_app()

@rt("/")
def home():
    return get_ui()

serve()
