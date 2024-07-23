import flet as ft

from components import Gap
from navigation import Routes
from styles import colors

class DogPage:
    def __init__(self, page: ft.Page):
        self._page = page
        self._page.update()

    def get_content(self):
        return ft.ListView(
            width=300,
            height=2000,
            bgcolor=colors.background,
            content=self._get_content(),
            #scroll_mode=ft.ScrollMode.AUTO,
        )

    def _get_content(self):
        return ft.Column(
            [
                ft.Container(
                    border_radius=15,
                    bgcolor=ft.colors.BLACK,
                    alignment=ft.alignment.center,
                    expand=True,
                ),
                ft.Divider(leading_indent=10, thickness=3, trailing_indent=10),
                ft.Container(
                    border_radius=15,
                    bgcolor=ft.colors.BLACK,
                    alignment=ft.alignment.center,
                    expand=True,
                ),
                ft.Divider(leading_indent=10, thickness=3, trailing_indent=10),
                ft.Container(
                    border_radius=15,
                    bgcolor=ft.colors.BLACK,
                    alignment=ft.alignment.center,
                    expand=True,
                ),
                ft.Divider(leading_indent=10, thickness=3, trailing_indent=10),
                ft.Container(
                    border_radius=15,
                    bgcolor=ft.colors.BLACK,
                    alignment=ft.alignment.center,
                    expand=True,
                ),
                ft.Divider(leading_indent=10, thickness=3, trailing_indent=10),
                ft.Container(
                    border_radius=15,
                    bgcolor=ft.colors.BLACK,
                    alignment=ft.alignment.center,
                    expand=True,
                ),
                ft.Divider(leading_indent=10, thickness=3, trailing_indent=10),
                ft.Container(
                    border_radius=15,
                    bgcolor=ft.colors.BLACK,
                    alignment=ft.alignment.center,
                    expand=True,
                ),
                ft.Divider(leading_indent=10, thickness=3, trailing_indent=10),
                ft.Container(
                    border_radius=15,
                    bgcolor=ft.colors.BLACK,
                    alignment=ft.alignment.center,
                    expand=True,
                ),
                ft.Divider(leading_indent=10, thickness=3, trailing_indent=10),
                ft.Container(
                    border_radius=15,
                    bgcolor=ft.colors.BLACK,
                    alignment=ft.alignment.center,
                    expand=True,
                ),
                ft.Divider(leading_indent=10, thickness=3, trailing_indent=10),
            ],
        )