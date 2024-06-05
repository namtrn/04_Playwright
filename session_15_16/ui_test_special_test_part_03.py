from playwright.sync_api import Page, expect


# 8. Dynamic tables
# http://www.uitestingplayground.com/dynamictable

def test_elements_dynamic_table_example(page: Page):
    page.goto("http://www.uitestingplayground.com/dynamictable")
    comparable_text = page.locator("//p[@class='bg-warning']").inner_text()
    cpu_comparable_text = comparable_text.split()[-1]
    print(cpu_comparable_text)

    cpu_column = None
    column_header = page.get_by_role("columnheader")
    for index in range(column_header.count()):
        if column_header.nth(index).inner_text() == 'CPU':
            cpu_column = index
            break
    assert cpu_column is not None

    chrome_row = None
    list_of_row = page.get_by_role("rowgroup").last.get_by_role("row")

    # for row in range(list_of_row.count()):
    #     list_of_cell = list_of_row.nth(row).get_by_role("cell")
    #     for cell in range(list_of_cell.count()):
    #         if list_of_cell.nth(cell).inner_text() == 'Chrome':
    #             chrome_row = list_of_row.nth(row)
    #             break

    for row in range(list_of_row.count()):
        list_of_cell = list_of_row.nth(row).get_by_role("cell")
        if list_of_cell.nth(0).inner_text() == 'Chrome':
            chrome_row = list_of_row.nth(row)
            break

    chrome_cpu = chrome_row.get_by_role("cell").nth(cpu_column)
    expect(chrome_cpu).to_have_text(cpu_comparable_text)


def test_special_case_verify_text(page: Page):
    page.goto("http://www.uitestingplayground.com/verifytext")
    # Normal case
    # title_h3 = page.locator("//h3")
    # expect(title_h3).to_have_text("Verify Text")

    # Special Case
    content_to_verify = "Welcome UserName!"
    text_verify = page.locator("//div[@class='bg-primary']").get_by_text("Welcome")
    expect(text_verify).to_have_text(content_to_verify)

