import flet as ft

from components import Gap
from navigation import Routes
from styles import colors

class ErrorPage:
    def __init__(self, page: ft.Page):
        self._page = page
        
    def get_content(self):
        return ft.Container(
            width=self._page.width,
            height=self._page.height,
            bgcolor=colors.white,
            content=self._get_content()
        )

    def _get_content(self):
        return ft.Column(
            [
                ft.Container(
                    height=20,
                ),
                ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Image(
                            src="error.png", 
                            height=512,
                            fit=ft.ImageFit.COVER,
                        ),
                        ft.Text("Oops!", weight=ft.FontWeight.BOLD, size=20, color=colors.black),
                        ft.Text("Pagina Nao Encontrada", size=16, color=colors.black),
                    ]
                ),
                ft.Container(
                    self._get_content2(),
                    alignment=ft.alignment.center,
                    padding=10,
                    expand=True,
                ),
            ]
        )
        
    def _get_content2(self):
        home_button_style = ft.ButtonStyle(
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
                                src="home.png", 
                                height=600,
                                fit=ft.ImageFit.COVER,
                            ),
                            ft.Text("Voltar", weight=ft.FontWeight.BOLD, size=20, color=colors.black),
                    ],
                    alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                width=200,
                height=60,
                style=home_button_style,
                on_click=self._handle_home_button,
                ),
            ]
        )
        
        return ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                Gap(20),
                buttons
            ],
        )
        
    def _handle_home_button(self, event: ft.ControlEvent):
        self._page.go(Routes.HOME_PAGE.value)