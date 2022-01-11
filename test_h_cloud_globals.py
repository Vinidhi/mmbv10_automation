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

def test_cloud_setup_globals(driver):
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(2)
    select_globals_setup = driver.find_element_by_css_selector('div.actions.tools-setup > button:nth-child(3) >'
                                                                 ' span.tools-alt')
    select_globals_setup.click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    globals_budget_highlighted = driver.find_element_by_css_selector('div:nth-child(1) > div.cell.body.text.name.editable.read-only')
    globals = globals_budget_highlighted.text
    select_upload_to_cloud = driver.find_element_by_css_selector('div.tools-actions > div > a:nth-child(4)')
    select_upload_to_cloud.click()
    time.sleep(2)
    upload_continue_button = driver.find_element_by_css_selector('div.actions > button.ui.small.primary.button')
    upload_continue_button.click()
    time.sleep(2)
    select_cloud_globals = driver.find_element_by_css_selector('div.cloud-libs-switch.no-select > span.cloud-library')
    select_cloud_globals.click()
    time.sleep(2)
    globals_moved_to_cloud = driver.find_element_by_css_selector('div:nth-child(1) > div.cell.body.text.name.editable.read-only')
    globals_moved_to_cloud.click()
    assert globals_moved_to_cloud.text == globals
    time.sleep(2)

def test_add_globals_details(driver):
    select_add_globals_category=driver.find_element_by_css_selector('div.action-buttons.no-select > a:nth-child(1) > i')
    select_add_globals_category.click()
    driver.implicitly_wait(10)
    select_added_category=driver.find_element_by_css_selector('input.grid-input-cell')
    select_added_category.click()
    driver.implicitly_wait(10)
    category_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    edit_field(driver, select_added_category, category_string)
    driver.implicitly_wait(5)

    select_add_globals=driver.find_element_by_css_selector('div.tools-actions > div > a:nth-child(1) > i')
    select_add_globals.click()
    driver.implicitly_wait(10)
    select_added_globals= driver.find_element_by_css_selector('input.grid-input-cell')
    select_added_globals.click()
    driver.implicitly_wait(10)
    globals_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    edit_field(driver, select_added_globals, globals_string)
    driver.implicitly_wait(3)

    globals_desc_field = driver.find_element_by_css_selector('div.cell.body.text.description.editable.read-only > span')
    globals_desc_field.click()
    driver.implicitly_wait(2)
    desc_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    edit_field(driver, globals_desc_field, desc_string)
    driver.implicitly_wait(2)

    globals_calc_field = driver.find_element_by_css_selector('div.cell.body.type_ahead_with_formula.calculation.editable.read-only > span')
    globals_calc_field.click()
    driver.implicitly_wait(2)
    action = ActionChains(driver)
    action.double_click(globals_calc_field)
    action.perform()
    add_calc = driver.find_element_by_css_selector('input.typeahead-input')
    add_calc.clear()
    driver.implicitly_wait(5)
    add_calc.send_keys('100')
    driver.implicitly_wait(2)
    add_calc.send_keys(Keys.TAB)

    globals_unit_field = driver.find_element_by_css_selector('div.cell.body.type_ahead.unit.editable.read-only')
    globals_unit_field.click()
    driver.implicitly_wait(2)
    action = ActionChains(driver)
    action.double_click(globals_unit_field)
    action.perform()
    add_unit = driver.find_element_by_css_selector('input.typeahead-input')
    add_unit.clear()
    driver.implicitly_wait(5)
    add_unit.send_keys('%')
    driver.implicitly_wait(2)
    add_unit.send_keys(Keys.TAB)

    globals_dec_field = driver.find_element_by_css_selector('div.cell.body.number.dec.editable.read-only > span')
    globals_dec_field.click()
    driver.implicitly_wait(2)
    dec_string = ''.join(random.choices(string.digits, k=1))
    if (dec_string < '8'):
        edit_field(driver, globals_dec_field, dec_string)
    else:
        globals_dec_field.send_keys(dec_string)
        driver.implicitly_wait(5)
        message=driver.find_element_by_css_selector('div.content.bottom > div > div > span')
        assert 'Dec must be between 0 and 7.' in message.text
        globals_dec_field.clear()
        globals_dec_field.send_keys('5')
        globals_dec_field.send_keys(Keys.ENTER)
        time.sleep(3)

    delete_globals = driver.find_element_by_css_selector('div.tools-actions > div > a:nth-child(2) > i')
    delete_globals.click()
    driver.implicitly_wait(2)

    move_to_category_dropdown_icon = driver.find_element_by_css_selector('div.tools-actions > div > div > i')
    move_to_category_dropdown_icon.click()
    driver.implicitly_wait(10)
    select_uncategorized_from_dropdown = driver.find_element_by_css_selector('div.tools-actions > div > div > div > div:nth-child(1) > span')
    select_uncategorized_from_dropdown.click()
    driver.implicitly_wait(10)
    category_uncategorized = driver.find_element_by_css_selector('div.active-section.with-action-buttons > div:nth-child(1) > div > span')
    category_uncategorized.click()
    globals_moved_uncategorized = driver.find_element_by_css_selector('div:nth-child(1) > div.cell.body.text.name.editable.read-only > span')
    assert globals_moved_uncategorized.text == globals_string
    time.sleep(5)

    download_budget = driver.find_element_by_css_selector('div.tools-actions > div > a:nth-child(4)')
    download_budget.click()
    driver.implicitly_wait(10)
    continue_download = driver.find_element_by_css_selector('div.actions > button.ui.small.primary.button')
    continue_download.click()
    time.sleep(3)

    delete_globals_library = driver.find_element_by_css_selector('div:nth-child(1) > div.cell.body.text.name.editable.read-only > span')
    delete_globals_library.click()
    driver.implicitly_wait(5)
    click_delete = driver.find_element_by_css_selector('div.tools-actions > div > a:nth-child(2) > i')
    click_delete.click()
    driver.implicitly_wait(10)

    switch_to_budget_library = driver.find_element_by_css_selector('div.cloud-libs-switch.no-select > span.budget-library > span')
    switch_to_budget_library.click()
    time.sleep(3)

    select_downloaded_globals = driver.find_element_by_css_selector('div:nth-child(3) > div.cell.body.text.name.editable.read-only > span')
    select_downloaded_globals.click()
    driver.implicitly_wait(5)
    click_delete1 = driver.find_element_by_css_selector('div.tools-actions > div > a:nth-child(2) > i')
    click_delete1.click()
    driver.implicitly_wait(15)

    close_setup = driver.find_element_by_css_selector('div.action > button')
    close_setup.click()
    time.sleep(2)
    