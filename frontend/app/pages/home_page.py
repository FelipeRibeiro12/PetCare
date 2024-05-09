import flet as ft

from components import Gap
from navigation import Routes
from styles import colors

class HomePage:
    def __init__(self, page: ft.Page):
        self._page = page
        
        self._page.floating_action_button = ft.FloatingActionButton(
            icon=ft.icons.SUPPORT_AGENT,
            on_click=self._handle_open_dog,
            bgcolor=colors.primary_color,
        )
        self._page.update()

    def get_content(self):
        return ft.Container(
            width=self._page.width,
            height=self._page.height,
            bgcolor=colors.background,
            content=self._get_content(),
        )

    def _get_content(self):
        return ft.Column(
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    ft.Image(
                        src="logonew.png",
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    height=200,
                    alignment=ft.alignment.center,
                ),

               ft.Container(
                width=300,
                height=530,
                bgcolor=ft.colors.BLACK,
               ),

               Gap(100),
            ]
        )

    def _handle_start_chatbot(self, event: ft.ControlEvent):
        self._page.go(Routes.CHATBOT_PAGE.value)

    def _handle_open_settings(self, event: ft.ControlEvent):
        print("OPEN SETTINGS")
        self._page.go(Routes.WELCOME_PAGE.value)
    
    def _handle_open_dog(self, event: ft.ControlEvent):
        print("OPEN DOG")
        self._page.go(Routes.DOG_PAGE.value)
