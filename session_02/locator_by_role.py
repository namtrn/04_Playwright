import asyncio
from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = await chromium.launch(headless=False, slow_mo=500)

    page = await browser.new_page()
    await page.goto("https://www.saucedemo.com")

    user_name = page.get_by_role("textbox", name="username")
    pwd = page.get_by_role("textbox", name="Password")
    await user_name.highlight()
    await user_name.fill("visual_user")

    await pwd.highlight()
    await pwd.fill("secret_sauce")

    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
