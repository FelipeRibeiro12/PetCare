import flet as ft

from components import Gap
from navigation import Routes
from styles import colors

class HomePage:
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
                    height=40,
                ),
                ft.Container(
                    ft.Image(
                        src="logonew.png",
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    height=70,
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    height=10,
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

        dogs_button_style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            color=colors.black,
            bgcolor=colors.white,
            side=ft.border.BorderSide(width=2, color=colors.black),
        )
        cats_button_style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            color=colors.black,
            bgcolor=colors.white,
            side=ft.border.BorderSide(width=2, color=colors.black),
        )
        birds_button_style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            color=colors.black,
            bgcolor=colors.white,
            side=ft.border.BorderSide(width=2, color=colors.black),
        )
        chatbot_button_style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            color=colors.black,
            bgcolor=colors.white,
            side=ft.border.BorderSide(width=2, color=colors.black),
        )

        buttons = ft.Column(
            controls=[
                ft.ElevatedButton(
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Image(
                                src="dog.png", 
                                height=50,
                                fit=ft.ImageFit.COVER,
                            ),
                            ft.Text("CACHORROS", weight=ft.FontWeight.BOLD, size=20),
                        ]
                    ),
                    width=300,
                    height=100,
                    style=dogs_button_style,
                    on_click=self._handle_dogs_button,
                ),
                Gap(10),
                ft.ElevatedButton(
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Image(
                                src="cat.png", 
                                height=50,
                                fit=ft.ImageFit.COVER,
                            ),
                            ft.Text("GATOS", weight=ft.FontWeight.BOLD, size=20),
                        ]
                    ),
                    width=300,
                    height=100,
                    style=cats_button_style,
                    on_click=self._handle_cats_button,
                ),
                Gap(10),
                ft.ElevatedButton(
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Image(
                                src="bird.png", 
                                height=50,
                                fit=ft.ImageFit.COVER,
                            ),
                            ft.Text("AVES", weight=ft.FontWeight.BOLD, size=20),
                        ]
                    ),
                    width=300,
                    height=100,
                    style=birds_button_style,
                    on_click=self._handle_birds_button,
                ),
                Gap(80),
                ft.ElevatedButton(
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text("PetCare IA", weight=ft.FontWeight.BOLD, size=20),
                        ]
                    ),
                    width=300,
                    height=60,
                    style=chatbot_button_style,
                    on_click=self._handle_start_chatbot,
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
        
    def _handle_dogs_button(self, event: ft.ControlEvent):
        self._page.go(Routes.DOG_PAGE.value)
        
    def _handle_cats_button(self, event: ft.ControlEvent):
        self._page.go(Routes.CAT_PAGE.value)
        
    def _handle_birds_button(self, event: ft.ControlEvent):
        self._page.go(Routes.BIRD_PAGE.value)

    def _handle_start_chatbot(self, event: ft.ControlEvent):
        self._page.go(Routes.CHATBOT_PAGE.value)