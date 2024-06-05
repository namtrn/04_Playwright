import asyncio

from playwright.async_api import async_playwright, Playwright


async def run(playwright: Playwright):
    # ehre we defind all actions that control and act on browser
    browser = await playwright.chromium.launch(headless=False, slow_mo=10)
    page = await browser.new_page()
    await page.goto("https://playwright.dev/")

    doc_links = page.get_by_role("link", name="Docs")
    doc_links.click()
    print("Docs:", page.url)
    await page.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
