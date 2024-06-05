from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto("https://demoqa.com/automation-practice-form")

    doc_link = page.locator("//span[text() = 'Text Box']")
    #doc_link.click()
    #doc_link.click(timeout = 2000)
    doc_link.click(force=True)
    browser.close()
