import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import string
import random

def edit_field(driver, field_name, input):
    action = ActionChains(driver)
    action.double_click(field_name)
    action.perform()
    edit_field = driver.find_element_by_class_name('grid-input-cell')
    edit_field.clear()
    edit_field.send_keys(input)
    time.sleep(2)
    edit_field.send_keys(Keys.TAB)
    time.sleep(2)

def test_cloud_setup_groups(driver, open_budget):
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(2)
    select_groups_setup = driver.find_element_by_css_selector('div.actions.tools-setup > button:nth-child(4) >'
                                                                 ' span.tools-alt')
    select_groups_setup.click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)

    groups_budget_highlighted = driver.find_element_by_css_selector('div:nth-child(1) > div.cell.body.text.name.editable.read-only')
    groups = groups_budget_highlighted.text
    select_upload_to_cloud = driver.find_element_by_css_selector('div.tools-actions > div > a:nth-child(4)')
    select_upload_to_cloud.click()
    time.sleep(2)
    upload_continue_button = driver.find_element_by_css_selector('div.actions > button.ui.small.primary.button')
    upload_continue_button.click()
    time.sleep(2)
    select_cloud_groups = driver.find_element_by_css_selector('div.cloud-libs-switch.no-select > span.cloud-library')
    select_cloud_groups.click()
    time.sleep(2)
    groups_moved_to_cloud = driver.find_element_by_css_selector('div:nth-child(1) > div.cell.body.text.name.editable.read-only')
    groups_moved_to_cloud.click()
    assert groups_moved_to_cloud.text == groups
    time.sleep(2)

def test_add_groups_details(driver):
    select_add_groups_category=driver.find_element_by_css_selector('div.action-buttons.no-select > a:nth-child(1) > i')
    select_add_groups_category.click()
    driver.implicitly_wait(10)
    select_added_category=driver.find_element_by_css_selector('input.grid-input-cell')
    select_added_category.click()
    driver.implicitly_wait(10)
    category_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    edit_field(driver, select_added_category, category_string)
    driver.implicitly_wait(5)

    select_add_groups = driver.find_element_by_css_selector('div.tools-actions > div > a:nth-child(1) > i')
    select_add_groups.click()
    driver.implicitly_wait(10)
    select_added_groups = driver.find_element_by_css_selector('input.grid-input-cell')
    select_added_groups.click()
    driver.implicitly_wait(10)
    groups_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    edit_field(driver, select_added_groups, groups_string)
    driver.implicitly_wait(3)

    groups_desc_field = driver.find_element_by_css_selector('div.cell.body.text.description.editable.read-only > span')
    groups_desc_field.click()
    driver.implicitly_wait(2)
    desc_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    edit_field(driver, groups_desc_field, desc_string)
    driver.implicitly_wait(2)

    groups_ID_field = driver.find_element_by_css_selector('div.cell.body.text.ident.editable.read-only')
    groups_ID_field.click()
    driver.implicitly_wait(2)
    ID_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=2))
    edit_field(driver, groups_ID_field, ID_string)
    driver.implicitly_wait(2)

    select_checkbox = driver.find_element_by_css_selector('div.row.selected > div.cell.body.checkbox.include.non-editable.read-only > div > div > div')
    select_checkbox.click()
    driver.implicitly_wait(5)

    select_color_dropdown = driver.find_element_by_css_selector('i.caret.down.icon')
    select_color_dropdown.click()
    driver.implicitly_wait(5)
    select_color = driver.find_element_by_css_selector('div.colorSuggestions.darkViolet')
    select_color.click()
    driver.implicitly_wait(5)

    select_row1=driver.find_element_by_css_selector('div.cell.body.color_picker.color.editable.field-range.field-range-top.field-range-right.field-range-bottom.field-range-left.field-range-pivot.read-only > div.search > div:nth-child(1)')
    select_row1.click()
    driver.implicitly_wait(10)

    move_to_category_dropdown_icon = driver.find_element_by_css_selector('div.tools-actions > div > div > i')
    move_to_category_dropdown_icon.click()
    driver.implicitly_wait(10)
    select_uncategorized_from_dropdown = driver.find_element_by_css_selector('div.tools-actions > div > div > div > div:nth-child(1) > span')
    select_uncategorized_from_dropdown.click()
    driver.implicitly_wait(10)
    category_uncategorized = driver.find_element_by_css_selector('div.active-section.with-action-buttons > div:nth-child(1) > div > span')
    category_uncategorized.click()
    groups_moved_uncategorized = driver.find_element_by_css_selector('div:nth-child(1) > div.cell.body.text.name.editable.read-only > span')
    assert groups_moved_uncategorized.text == groups_string
    time.sleep(5)

    download_budget = driver.find_element_by_css_selector('div.tools-actions > div > a:nth-child(4)')
    download_budget.click()
    driver.implicitly_wait(10)
    continue_download = driver.find_element_by_css_selector('div.actions > button.ui.small.primary.button')
    continue_download.click()
    time.sleep(3)

    delete_groups_library = driver.find_element_by_css_selector('div:nth-child(1) > div.cell.body.text.name.editable.read-only > span')
    delete_groups_library.click()
    driver.implicitly_wait(5)
    click_delete = driver.find_element_by_css_selector('div.tools-actions > div > a:nth-child(2) > i')
    click_delete.click()
    time.sleep(2)

    switch_to_budget_library = driver.find_element_by_css_selector('div.cloud-libs-switch.no-select > span.budget-library > span')
    switch_to_budget_library.click()
    time.sleep(3)

    select_downloaded_groups = driver.find_element_by_css_selector('div:nth-child(23) > div.cell.body.text.name.editable.read-only > span')
    select_downloaded_groups.click()
    driver.implicitly_wait(5)
    click_delete1 = driver.find_element_by_css_selector('div.tools-actions > div > a:nth-child(2) > i')
    click_delete1.click()
    driver.implicitly_wait(15)

    close_setup = driver.find_element_by_css_selector('div.action > button')
    close_setup.click()
    time.sleep(2)


