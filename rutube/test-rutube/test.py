from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://rutube.ru/")
    page.get_by_role("button", name="Закрыть", exact=True).click()
    page.get_by_role("textbox", name="Поиск").click()
    page.get_by_role("textbox", name="Поиск").fill("Avatar")
    page.get_by_role("textbox", name="Поиск").press("Enter")
    page.get_by_role("link", name="avatar", exact=True).click()
    page.get_by_role("button", name="Фильтры").click()
    page.get_by_role("button", name="Более 60 минут").click()
    page.get_by_role("button", name="За месяц").click()
    expect(page.get_by_role("link", name="Аватар: Пламя и пепел (2025) / Avatar: Fire and Ash", exact=True)).to_be_visible()
