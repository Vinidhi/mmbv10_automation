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

def test_cloud_setup_sets(driver):
    driver.switch_to.window(driver.window_handles[0])
    select_sets_setup = driver.find_element_by_css_selector('div.actions.tools-setup > button:nth-child(7) >'
                                                                 ' span.tools-alt')
    select_sets_setup.click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)

    sets_budget_highlighted = driver.find_element_by_css_selector('div:nth-child(1) > div.cell.body.text.name.editable.read-only')
    sets = sets_budget_highlighted.text
    select_upload_to_cloud = driver.find_element_by_css_selector('div.tools-actions > div > a:nth-child(4)')
    select_upload_to_cloud.click()
    time.sleep(2)
    upload_continue_button = driver.find_element_by_css_selector('div.actions > button.ui.small.primary.button')
    upload_continue_button.click()
    time.sleep(2)
    select_cloud_sets = driver.find_element_by_css_selector('div.cloud-libs-switch.no-select > span.cloud-library')
    select_cloud_sets.click()
    time.sleep(2)
    sets_moved_to_cloud = driver.find_element_by_css_selector('div:nth-child(1) > div.cell.body.text.name.editable.read-only')
    sets_moved_to_cloud.click()
    assert sets_moved_to_cloud.text == sets
    time.sleep(2)

def test_add_sets_details(driver):
    select_add_sets_category=driver.find_element_by_css_selector('div.action-buttons.no-select > a:nth-child(1) > i')
    select_add_sets_category.click()
    driver.implicitly_wait(10)
    select_added_category=driver.find_element_by_css_selector('input.grid-input-cell')
    select_added_category.click()
    driver.implicitly_wait(10)
    category_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    edit_field(driver, select_added_category, category_string)
    driver.implicitly_wait(5)

    select_add_sets = driver.find_element_by_css_selector('div.tools-actions > div > a:nth-child(1) > i')
    select_add_sets.click()
    driver.implicitly_wait(10)
    select_added_sets = driver.find_element_by_css_selector('input.grid-input-cell')
    select_added_sets.click()
    driver.implicitly_wait(10)
    sets_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    edit_field(driver, select_added_sets, sets_string)
    driver.implicitly_wait(3)

    sets_desc_field = driver.find_element_by_css_selector('div.cell.body.text.description.editable.read-only')
    sets_desc_field.click()
    driver.implicitly_wait(2)
    desc_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    edit_field(driver, sets_desc_field, desc_string)
    driver.implicitly_wait(2)

    delete_sets = driver.find_element_by_css_selector('div.tools-actions > div > a:nth-child(2) > i')
    delete_sets.click()
    driver.implicitly_wait(2)

    move_to_category_dropdown_icon = driver.find_element_by_css_selector('div.tools-actions > div > div > i')
    move_to_category_dropdown_icon.click()
    driver.implicitly_wait(10)
    select_uncategorized_from_dropdown = driver.find_element_by_css_selector('div.tools-actions > div > div > div > div:nth-child(1) > span')
    select_uncategorized_from_dropdown.click()
    driver.implicitly_wait(10)
    category_uncategorized = driver.find_element_by_css_selector('div.active-section.with-action-buttons > div:nth-child(1) > div > span')
    category_uncategorized.click()
    sets_moved_uncategorized = driver.find_element_by_css_selector('div:nth-child(1) > div.cell.body.text.name.editable.read-only > span')
    assert sets_moved_uncategorized.text == sets_string
    time.sleep(2)

    download_budget = driver.find_element_by_css_selector('div.tools-actions > div > a:nth-child(4)')
    download_budget.click()
    driver.implicitly_wait(10)
    continue_download = driver.find_element_by_css_selector('div.actions > button.ui.small.primary.button')
    continue_download.click()
    time.sleep(3)

    find_set=driver.find_element_by_css_selector('div.cell.body.text.name.editable.read-only > span[title="7513"]')
    find_set.click()

    # x = driver.find_element_by_css_selector('div:nth-child(2) > div.cell.body.text.name.editable.read-only > span')
    # y = x.text
    # x1 = driver.find_element_by_css_selector('div:nth-child(1) > div.cell.body.text.name.editable.read-only > span')
    # y1 = x1.text
    #
    # if y == find_set:
    #    x.click()
    # elif y1 == find_set:
    #    x1.click()

    time.sleep(3)
    click_delete1 = driver.find_element_by_css_selector('div.tools-actions > div > a:nth-child(2) > i')
    click_delete1.click()
    driver.implicitly_wait(10)
    delete_sets_library1 = driver.find_element_by_css_selector('div:nth-child(1) > div.cell.body.text.name.editable.read-only > span')
    delete_sets_library1.click()
    driver.implicitly_wait(5)
    click_delete1.click()
    driver.implicitly_wait(10)

    switch_to_budget_library = driver.find_element_by_css_selector('div.cloud-libs-switch.no-select > span.budget-library > span')
    switch_to_budget_library.click()
    time.sleep(3)

    select_downloaded_sets = driver.find_element_by_css_selector('div:nth-child(18) > div.cell.body.text.name.editable.read-only > span')
    select_downloaded_sets.click()
    driver.implicitly_wait(5)
    click_delete1 = driver.find_element_by_css_selector('div.tools-actions > div > a:nth-child(2) > i')
    click_delete1.click()
    driver.implicitly_wait(15)

    close_setup = driver.find_element_by_css_selector('div.action > button')
    close_setup.click()
    time.sleep(2)