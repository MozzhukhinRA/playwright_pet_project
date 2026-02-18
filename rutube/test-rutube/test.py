import time

from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page

from rutube.methods.methods import MethodRutube
from rutube.methods.selector_site import name


def test_example(page: Page) -> None:
    page.goto("https://rutube.ru/")
    page.get_by_role("button", name="Закрыть").click()
    page.get_by_role("textbox", name="Поиск").click()
    page.get_by_role("textbox", name="Поиск").fill("Avatar")
    page.get_by_role("button", name="Отправить форму поиска").click()
    expect(page.get_by_role("button", name="Фильтры")).to_be_visible()
    page.get_by_role("button", name="Фильтры").click()
    page.get_by_text("ДлительностьЛюбаяДо 5 минут5–").click()
    page.get_by_role("button", name="Более 60 минут").click()
    page.get_by_role("button", name="За год").click()
    expect(page.get_by_role("main")).to_contain_text("Аватар: Пламя и пепел (2025)")


def test(page: Page):
    rutube = MethodRutube(page)
    rutube.open_url()
    rutube.fiend_element_role_button(name.tab_action_close)

    time.sleep(2)

