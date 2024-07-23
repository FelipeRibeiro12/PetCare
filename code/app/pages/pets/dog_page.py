import flet as ft

from components import Gap
from navigation import Routes
from styles import colors

class DogPage:
    def __init__(self, page: ft.Page):
        self._page = page

        self._page.appbar = ft.AppBar(
            ft.IconButton(
                ft.icons.ARROW_BACK,
                on_click=self._handle_back_button,
            ),
            title=ft.Text("CACHORROS", style=ft.TextStyle(color=colors.white, size=24)),
            bgcolor=colors.primary_color,
            center_title=True,
            toolbar_height=80,
        )
        self._page.update()
        
    def get_content(self):
        return ft.Container(
            width=self._page.width,
            height=self._page.height,
            bgcolor=colors.white,
            content=self._get_content()
        )
        self._page.update()
        
    def _get_content(self):

        dogs_button_style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            color=colors.black,
            bgcolor=colors.white,
            side=ft.border.BorderSide(width=2, color=colors.black),
        )

        buttons = ft.Column(
            controls=[
                ft.ElevatedButton(
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text("Cão1", weight=ft.FontWeight.BOLD, size=20),
                        ]
                    ),
                    width=self._page.width,
                    height=100,
                    style=dogs_button_style,
                    #on_click=self._handle_dogs_button,
                ),
                ft.ElevatedButton(
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text("Cão2", weight=ft.FontWeight.BOLD, size=20),
                        ]
                    ),
                    width=self._page.width,
                    height=100,
                    style=dogs_button_style,
                    #on_click=self._handle_dogs_button,
                ),
                ft.ElevatedButton(
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text("Cão3", weight=ft.FontWeight.BOLD, size=20),
                        ]
                    ),
                    width=self._page.width,
                    height=100,
                    style=dogs_button_style,
                    #on_click=self._handle_dogs_button,
                ),
                ft.ElevatedButton(
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text("Cão4", weight=ft.FontWeight.BOLD, size=20),
                        ]
                    ),
                    width=self._page.width,
                    height=100,
                    style=dogs_button_style,
                    #on_click=self._handle_dogs_button,
                ),
            ]
        )

        return ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                Gap(10),
                buttons
            ],
        )
    
    def _handle_back_button(self, event: ft.ControlEvent):
        self._page.go(Routes.HOME_PAGE.value)