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

def test_cloud_setup_units(driver):
    driver.switch_to.window(driver.window_handles[0])
    driver.implicitly_wait(2)
    select_units_setup = driver.find_element_by_css_selector('div.actions.tools-setup > button:nth-child(6) >'
                                                                 ' span.tools-alt')
    select_units_setup.click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)

    units_budget_highlighted = driver.find_element_by_css_selector('div:nth-child(2) > div.cell.body.text.name.editable.read-only')
    units_budget_highlighted.click()
    driver.implicitly_wait(5)
    units = units_budget_highlighted.text
    select_upload_to_cloud = driver.find_element_by_css_selector('div.tools-actions > div > a:nth-child(4)')
    select_upload_to_cloud.click()
    time.sleep(2)
    upload_continue_button = driver.find_element_by_css_selector('div.actions > button.ui.small.primary.button')
    upload_continue_button.click()
    time.sleep(2)
    select_cloud_units = driver.find_element_by_css_selector('div.cloud-libs-switch.no-select > span.cloud-library')
    select_cloud_units.click()
    time.sleep(2)


def test_add_units_details(driver):
    select_add_units_category=driver.find_element_by_css_selector('div.action-buttons.no-select > a:nth-child(1) > i')
    select_add_units_category.click()
    driver.implicitly_wait(10)
    select_added_category=driver.find_element_by_css_selector('input.grid-input-cell')
    select_added_category.click()
    driver.implicitly_wait(10)
    category_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    edit_field(driver, select_added_category, category_string)
    driver.implicitly_wait(5)

    select_add_units = driver.find_element_by_css_selector('div.tools-actions > div > a:nth-child(1) > i')
    select_add_units.click()
    driver.implicitly_wait(10)
    select_added_units = driver.find_element_by_css_selector('input.grid-input-cell')
    select_added_units.click()
    driver.implicitly_wait(10)
    units_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    edit_field(driver, select_added_units, units_string)
    driver.implicitly_wait(3)

    add_plural=driver.find_element_by_css_selector('div.cell.body.text.plural.editable.read-only')
    add_plural.click()
    driver.implicitly_wait(2)
    units_string1= ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    edit_field(driver,add_plural,units_string1)
    driver.implicitly_wait(2)

    #units_desc_field = driver.find_element_by_css_selector('div.cell.body.text.description.editable.read-only > span')
    units_desc_field = driver.find_element_by_css_selector('div > div.cell.body.text.description.editable.field-range.'
                                                           'field-range-top.field-range-right.field-range-bottom.'
                                                           'field-range-left.field-range-pivot.read-only')
    units_desc_field.click()
    driver.implicitly_wait(2)
    desc_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    edit_field(driver, units_desc_field, desc_string)
    driver.implicitly_wait(2)

    units_Hrs=driver.find_element_by_css_selector('div.cell.body.number.hours.editable.read-only')
    units_Hrs.click()
    driver.implicitly_wait(2)
    Hrs_string =''.join(random.choices(string.digits, k=2))
    edit_field(driver,units_Hrs,Hrs_string)
    driver.implicitly_wait(2)

    delete_units = driver.find_element_by_css_selector('div.tools-actions > div > a:nth-child(2) > i')
    delete_units.click()
    driver.implicitly_wait(2)

    move_to_category_dropdown_icon = driver.find_element_by_css_selector('div.tools-actions > div > div > i')
    move_to_category_dropdown_icon.click()
    driver.implicitly_wait(10)
    select_uncategorized_from_dropdown = driver.find_element_by_css_selector('div.tools-actions > div > div > div > div:nth-child(1) > span')
    select_uncategorized_from_dropdown.click()
    driver.implicitly_wait(10)
    category_uncategorized = driver.find_element_by_css_selector('div.active-section.with-action-buttons > div:nth-child(1) > div > span')
    category_uncategorized.click()
    units_moved_uncategorized = driver.find_element_by_css_selector('div:nth-child(1) > div.cell.body.text.name.editable.read-only > span')
    assert units_moved_uncategorized.text == units_string
    time.sleep(2)

    download_budget = driver.find_element_by_css_selector('div.tools-actions > div > a:nth-child(4)')
    download_budget.click()
    driver.implicitly_wait(10)
    continue_download = driver.find_element_by_css_selector('div.actions > button.ui.small.primary.button')
    continue_download.click()
    time.sleep(3)

    delete_units_library = driver.find_element_by_css_selector('div:nth-child(1) > div.cell.body.text.name.editable.read-only > span')
    delete_units_library.click()
    #driver.implicitly_wait(5)
    time.sleep(2)
    click_delete = driver.find_element_by_css_selector('div.tools-actions > div > a:nth-child(2) > i')
    click_delete.click()
    #driver.implicitly_wait(10)
    time.sleep(2)
    #delete_units_library1 = driver.find_element_by_css_selector('div:nth-child(3) > div.cell.body.text.name.editable.read-only > span')
    delete_units_library1 = driver.find_element_by_css_selector(
        'div.cell.body.text.name.editable.read-only > span[title="Day"]')
    delete_units_library1.click()
    #driver.implicitly_wait(10)
    time.sleep(2)
    click_delete1 = driver.find_element_by_css_selector('div.tools-actions > div > a:nth-child(2) > i')
    click_delete1.click()
    time.sleep(2)
    #driver.implicitly_wait(10)

    switch_to_budget_library = driver.find_element_by_css_selector('div.cloud-libs-switch.no-select > span.budget-library > span')
    switch_to_budget_library.click()
    time.sleep(3)

    select_downloaded_units = driver.find_element_by_css_selector('div:nth-child(54) > div.cell.body.text.name.editable.read-only > span')
    select_downloaded_units.click()
    driver.implicitly_wait(5)
    click_delete1 = driver.find_element_by_css_selector('div.tools-actions > div > a:nth-child(2) > i')
    click_delete1.click()
    driver.implicitly_wait(15)

    # select_delete_unit = driver.find_element_by_css_selector('div > div.actions > button.ui.basic.button')
    # select_delete_unit.click()
    # driver.implicitly_wait(15)

    select_library = driver.find_element_by_css_selector('div > div.cloud-libs-switch.no-select > span.cloud-library')
    select_library.click()
    time.sleep(2)
    select_new_lib_cat = driver.find_element_by_css_selector('div.active-section.with-action-buttons > div:nth-child(2)')
    select_new_lib_cat.click()
    time.sleep(2)
    delete_new_lib_cat = driver.find_element_by_css_selector('div > div.action-buttons.no-select > a:nth-child(2)')
    delete_new_lib_cat.click()
    time.sleep(2)

    close_setup = driver.find_element_by_css_selector('div.action > button')
    close_setup.click()
    time.sleep(2)
