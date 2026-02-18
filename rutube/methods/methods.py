from playwright.sync_api import Page


class MethodRutube:

    def __init__(self, page : Page):
        self.base_url = "https://rutube.ru/"
        self.page = page


    def open_url(self):
        self.page.goto(self.base_url)

    def fiend_element_role_button(self, name:str):
        element = self.page.get_by_role("button", name=name)
        element.click()

