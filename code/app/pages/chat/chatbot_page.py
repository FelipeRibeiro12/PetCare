import os
import time
import openai
import threading
import flet as ft

from openai import OpenAI
from .constants import OPEN_AI_API_KEY
from components import SystemMessage, UserMessage, InputTextField
from navigation.routes import Routes
from styles import colors

class ChatBotPage:
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

    def get_content(self):
        return ft.Container(
            width=self._page.width,
            height=self._page.height,
            bgcolor=colors.background_grey,
            content=self._get_content(),
        )

    def _get_content(self):
        self._input_field = InputTextField(
            hint_text="Digite qual a sua dúvida...",
            keyboard_type=ft.KeyboardType.TEXT,
            multiline=True,
            min_lines=1,
            max_lines=3,
            on_submit=self._handle_send_message,
            shift_enter=True,
            on_focus=self._handle_on_focus,
            on_blur=self._handle_on_blur,
            suffix=ft.IconButton(
                ft.icons.SEND,
                icon_color=colors.secondary_color,
                on_click=self._handle_send_message,
            )
        )

        self._chat_history = ft.ListView(
            height=600,
            padding=20,
            controls=[
                SystemMessage("Olá! Como eu posso te ajudar?").get_content(),
            ],
            auto_scroll=True,
        )

        return ft.Column(
            [
                self._chat_history,
                ft.Container(
                    self._input_field,
                    bgcolor=colors.primary_color,
                    padding=ft.Padding(top=40, bottom=40, left=30, right=30),
                    border_radius=ft.BorderRadius(20, 20, 0, 0),
                    expand=True,
                ),
            ]
        )

    def _handle_on_focus(self, event: ft.ControlEvent):
        self._input_field.hint_text = ""
        self._input_field.update()

    def _handle_on_blur(self, event: ft.ControlEvent):
        self._input_field.hint_text = "Digite qual a sua dúvida..."
        self._input_field.update()

    def _handle_back_button(self, event: ft.ControlEvent):
        self._page.go(Routes.HOME_PAGE.value)
        
    def _show_typing_indicator(self):
        time.sleep(1)
        waiting_message = SystemMessage("...").get_content()
        self._chat_history.controls.append(waiting_message)
        self._chat_history.update()

    def _handle_send_message(self, event: ft.ControlEvent):
        input_text = self._input_field.value
        if not input_text:
            return

        self._input_field.value = ""
        self._input_field.update()

        user_message = UserMessage(input_text).get_content()
        self._chat_history.controls.append(user_message)
        self._chat_history.update()
        
        waiting_message = SystemMessage("...").get_content()
        self._chat_history.controls.append(waiting_message)
        self._chat_history.update()

        client = OpenAI(api_key=OPEN_AI_API_KEY)
        messages = [
            {"role": "system", "content": "Você é um chatbot se passando por uma veterinária, que deverá responder como uma pessoa e auxiliar o usuário com suas duvidas a respeito de animais e pets. Tudo que não for a respeito de animais e pets, você deverá respoder que não sabe sobre o assunto."},
            {"role": "user", "content": input_text},
        ]
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
        )

        response_text = completion.choices[0].message.content
        response_message = SystemMessage(response_text).get_content()
        self._chat_history.controls.append(response_message)
        self._chat_history.controls.remove(waiting_message)
        self._chat_history.update()