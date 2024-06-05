from playwright.sync_api import Page, expect
import pytest

# 10. Verify progress bar
# URL: http://www.uitestingplayground.com/progressbar
# Create a test that clicks Start button and then waits for the progress bar to reach 35%
# Then the test should click Stop button
# The less the different between value of the stopped progress bar and 35% the better your result

def test_verify_progress_bar(page: Page):
    page.goto("http://www.uitestingplayground.com/progressbar")
    start_btn = page.locator("button.btn-primary")
    stop_btn = page.locator("button.btn-info")
    progress_bar = page.locator("div.progress-bar")

    start_btn.click()
    while True:
        value = int(progress_bar.get_attribute("aria-valuenow"))
        if value >= 35:
            break
        else:
            print(f"Percentage: {value}%")

    stop_btn.click()

    expect(progress_bar).to_have_attribute("aria-valuenow", "35")
    assert value >= 35