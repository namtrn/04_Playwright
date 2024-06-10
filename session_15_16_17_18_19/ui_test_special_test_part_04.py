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

# 11. Test Visibility
# Get the locator of all buttons and then press Hide button
# Determine of other buttons is visible or not

def test_visibility_buttons(page: Page):
    page.goto("http://www.uitestingplayground.com/visibility")
    hide_btn = page.locator("//button[@id='hideButton']")
    removed_btn = page.locator("//button[@id='removedButton']")
    zero_width_btn = page.locator("//button[@id='zeroWidthButton']")
    overlapped_btn = page.locator("//button[@id='overlappedButton']")
    opacity_btn = page.locator("//button[@id='transparentButton']")
    invisibale_btn = page.locator("//button[@id='invisibleButton']")
    display_none_btn = page.locator("//button[@id='hideButton']")
    offscreen_btn = page.locator("//button[@id='hideButton']")

    expect(hide_btn).to_be_visible()
    expect(removed_btn).to_be_visible()
    expect(zero_width_btn).to_be_visible()
    expect(overlapped_btn).to_be_visible()
    expect(opacity_btn).to_be_visible()
    expect(invisibale_btn).to_be_visible()
    expect(display_none_btn).to_be_visible()
    expect(offscreen_btn).to_be_visible()

    hide_btn.click()
    # Case: Hide button is hidden => the HTML code is removed
    expect(removed_btn).to_be_hidden()
    # Case: zero_width_btn > verify if the width attribute equals 0
    expect(zero_width_btn).to_have_css("width", "0px")
    # case: overlapped button => verify if a new div is created, id = hidingLayer
    expect(page.locator("//div[@id='hidingLayer']")).to_be_visible()
    with pytest.raises(Exception):
        expect(overlapped_btn).to_be_visible(timeout=1000)
        overlapped_btn.click(timeout=1000)

    # Case: element.style {opacity: "0";} => Elements has css ("visibility", "hidden")

