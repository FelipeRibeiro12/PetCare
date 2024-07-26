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
                icon_color=colors.black,
                on_click=self._handle_back_button,
            ),
            title=ft.Text("CACHORROS", style=ft.TextStyle(color=colors.black, size=24)),
            bgcolor=colors.white,
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
                        controls=[
                            ft.Image(
                                src="pastoralemao.png", 
                                height=100,
                                fit=ft.ImageFit.COVER,
                            ),
                            ft.Text("Pastor Alemão", weight=ft.FontWeight.BOLD, size=20),
                    ],
                    alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                width=self._page.width,
                height=100,
                style=dogs_button_style,
                on_click=self._handle_dog1_button,
                ),
                ft.ElevatedButton(
                    content=ft.Row(
                        controls=[
                            ft.Image(
                                src="nf.png", 
                                height=100,
                                fit=ft.ImageFit.COVER,
                            ),
                            ft.Text("Vazio", weight=ft.FontWeight.BOLD, size=20),
                    ],
                    alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                width=self._page.width,
                height=100,
                style=dogs_button_style,
                on_click=self._handle_error,
                ),
                ft.ElevatedButton(
                    content=ft.Row(
                        controls=[
                            ft.Image(
                                src="nf.png", 
                                height=100,
                                fit=ft.ImageFit.COVER,
                            ),
                            ft.Text("Vazio", weight=ft.FontWeight.BOLD, size=20),
                    ],
                    alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                width=self._page.width,
                height=100,
                style=dogs_button_style,
                on_click=self._handle_error,
                ),
                ft.ElevatedButton(
                    content=ft.Row(
                        controls=[
                            ft.Image(
                                src="nf.png", 
                                height=100,
                                fit=ft.ImageFit.COVER,
                            ),
                            ft.Text("Vazio", weight=ft.FontWeight.BOLD, size=20),
                    ],
                    alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                width=self._page.width,
                height=100,
                style=dogs_button_style,
                on_click=self._handle_error,
                ),
                ft.ElevatedButton(
                    content=ft.Row(
                        controls=[
                            ft.Image(
                                src="nf.png", 
                                height=100,
                                fit=ft.ImageFit.COVER,
                            ),
                            ft.Text("Vazio", weight=ft.FontWeight.BOLD, size=20),
                    ],
                    alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                width=self._page.width,
                height=100,
                style=dogs_button_style,
                on_click=self._handle_error,
                ),
                ft.ElevatedButton(
                    content=ft.Row(
                        controls=[
                            ft.Image(
                                src="nf.png", 
                                height=100,
                                fit=ft.ImageFit.COVER,
                            ),
                            ft.Text("Vazio", weight=ft.FontWeight.BOLD, size=20),
                    ],
                    alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                width=self._page.width,
                height=100,
                style=dogs_button_style,
                on_click=self._handle_error,
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
        
    def _handle_dog1_button(self, event: ft.ControlEvent):
        self._page.go(Routes.DOG1_PAGE.value)
        
    def _handle_error(self, event: ft.ControlEvent):
        self._page.go(Routes.ERROR_PAGE.value)