from playwright.sync_api import Page, expect

def test_load_delay_example(page: Page):
    page.goto("https://katalon.com/katalon-platform")
    page.locator("//button[@id='onetrust-accept-btn-handler']").click()
    onboarding_hub = page.get_by_role("link", name = "Onboarding Hub")
    onboarding_hub.scroll_into_view_if_needed(timeout=500)
    onboarding_hub.click()

    social_google = page.locator("//*[@id='social-google']")
    expect(social_google).to_be_visible(timeout=5000)
    social_google.click()

def test_wait_ajax_example(page: Page):
    page.goto("http://www.uitestingplayground.com/ajax")
    page.locator("//button[@id='ajaxButton']").click()
    success_message = page.locator("//p[@class='bg-success']")
    success_message.wait_for()
    expect(success_message).to_be_visible()

def test_element_change_after_event(page: Page):
    page.goto("http://www.uitestingplayground.com/click")
    bad_button = page.locator("//button[@id='badButton']")
    expect(bad_button).to_have_class("btn btn-primary")
    bad_button.click()
    expect(bad_button).to_have_class("btn btn-success")

    page.goto("http://www.uitestingplayground.com/textinput")
    page.locator("//input[@id='newButtonName']").fill("Tran Vinh Nam")
    primary_btn = page.locator("button.btn-primary")
    expect(primary_btn).to_have_text("Button That Should Change it's Name Based on Input Value")
    primary_btn.click()
    expect(primary_btn).to_have_text("Tran Vinh Nam")


