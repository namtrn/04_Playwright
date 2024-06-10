import time
from playwright.sync_api import Page, expect
import pytest
import pyperclip

# Test Mouse Over

def test_mouse_over(page: Page):
    page.goto("http://www.uitestingplayground.com/mouseover")
    hover_link = page.locator("//a[@title='Click me']")
    hover_link.hover()
    text_warning = page.locator("//a[@class='text-warning']")
    text_warning.click(click_count=4)
    expect(page.locator("//span[@id='clickCount']")).to_have_text("4")


#15. Overlapped element
#http://www.uitestingplayground.com/overlapped
def test_example_overlapped_element(page: Page):
    page.goto("http://www.uitestingplayground.com/overlapped")
    name_text_box = page.get_by_placeholder("Name")

    #get the parent div
    parent_div = name_text_box.locator("..")
    parent_div.hover()
    page.mouse.wheel(0, 200)
    name_text_box.click()
    name_text_box.fill("Nguyễn Ngọc Hương Quỳnh")
    expect(name_text_box).to_have_value("Nguyễn Ngọc Hương Quỳnh")

#16 Shadown DOM
def test_example_shadow_dom(page: Page):
    # page.goto("http://www.uitestingplayground.com/shadowdom")

    # # page.locator("guid-generator .edit-field").fill("1234567890")
    # page.locator("guid-generator .button-generate").click(timeout=30000)
    # page.locator("guid-generator .button-copy").click(timeout=30000)
    #
    # compare_text = pyperclip.paste()
    # expect(page.locator("guid-generator .edit-field")).to_have_text(compare_text )
    apptitle = "BOOKS"
    #time.sleep(5)
    page.goto("https://books-pwakit.appspot.com")
    page.locator("book-app[apptitle='BOOKS'] #input").fill("Nguyễn Ngọc Hương Quỳnh")
    time.sleep(5)

# 17. iframe example
# Example: https://ui.vision/demo/webtest/frames/
# Example: https://the-internet.herokuapp.com/iframe
def test_iframe_example(page: Page):
    # page.goto("https://ui.vision/demo/webtest/frames/")
    # textbox = page.frame_locator("//*[@src='frame_1.html']").locator('//input')
    # textbox.fill("Testing4Everyone")
    # page.pause()

    page.goto("https://the-internet.herokuapp.com/iframe")
    # page.locator("//body[@id='tinymce']").click(timeout=2000)
    email_textbox = page.frame_locator('//*[@id="mce_0_ifr"]').locator('//body')
    email_textbox.click(timeout=1500)
    email_textbox.fill(" Testing4Everyone", timeout=1500)
    page.pause()