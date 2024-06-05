import asyncio
from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    chromnium = playwright.chromium
    browser = await chromnium.launch(headless=False, slow_mo=1000)
    page = await browser.new_page()
    await page.goto("https://bootswatch.com/default/")

    pwd_textbox = page.get_by_label("Password")
    await pwd_textbox.highlight()
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())




