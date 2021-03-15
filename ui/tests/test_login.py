from playwright.sync_api import Page


def test_search(page: Page):
    page.goto('https://playwright.dev/python')
    assert page.title() == 'Fast and reliable end-to-end testing for modern web apps | Playwright'