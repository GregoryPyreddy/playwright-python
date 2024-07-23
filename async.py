from playwright.async_api import async_playwright
import asyncio
from WebActions.page_actions import PageActions

async def main():
    actions = PageActions()
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://odxui.dev02.odx-nonprod.o360.cloud/ncc")
        await actions.wait_for_element_to_be_clickable(page, '#username')
        await page.click('#username')
        await actions.enter_text(page, '#username', 'gpyreddy')
        await actions.enter_text(page, '#login-pwd', 'Sid@1806')
        await actions.wait_for_element_to_be_clickable(page, '#btnLogin')
        await page.click('#btnLogin')
        await actions.wait_for_element_to_be_present(page, '#lbl_secAnswer')
        await actions.enter_security_answer(page, '#secAnswer', await actions.get_text(page, '#lbl_secAnswer'))
        await page.click('#continuebtn')
        await actions.wait_for_element_to_be_present(page, "h1#table-caption")
        print("in home page")
asyncio.run(main())