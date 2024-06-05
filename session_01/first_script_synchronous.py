from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # laucnh a browser
    browser_chrome = playwright.chromium.launch(headless=False, slow_mo=1000)
    # create a new tab
    page = browser_chrome.new_page()
    # Navigate to "https://playwright.dev/"
    page.goto("https://playwright.dev/")

    doc_links = page.get_by_role("link", name="Docs")
    doc_links.click()

    print("Docs:", page.url)
    page.close()