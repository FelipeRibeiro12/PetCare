import flet as ft

from navigation.routes import Routes
import pages

class Router:
    routes_map = {
        Routes.INDEX_PAGE.value: pages.HomePage,
        Routes.HOME_PAGE.value: pages.HomePage,
        Routes.DOG_PAGE.value: pages.DogPage,
        Routes.CAT_PAGE.value: pages.CatPage,
        Routes.BIRD_PAGE.value: pages.BirdPage,
        Routes.CHATBOT_PAGE.value: pages.ChatBotPage,
    }

    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.body = ft.Container(pages.HomePage(page).get_content())

    def on_route_change(self, route: ft.RouteChangeEvent):
        page = self.routes_map[route.route](self.page)
        self.body.content = page.get_content()

        self.page.appbar = None
        self.page.floating_action_button = None
        self.body.update()
