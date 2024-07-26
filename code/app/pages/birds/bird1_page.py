import flet as ft

from components import SystemMessage, UserMessage, InputTextField
from navigation.routes import Routes
from styles import colors

class Bird1Page:
    def __init__(self, page: ft.Page):
        self._page = page

        self._page.appbar = ft.AppBar(
            ft.IconButton(
                ft.icons.ARROW_BACK,
                on_click=self._handle_back_button,
            ),
            title=ft.Text("PetCare IA", style=ft.TextStyle(color=colors.white, size=24)),
            bgcolor=colors.primary_color,
            center_title=True,
            toolbar_height=80,
        )
        self._page.update()