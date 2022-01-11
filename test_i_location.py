import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import string
import random
from pynput.keyboard import Key, Controller
import os


def edit_field(driver, field_name, input):
    action = ActionChains(driver)
    action.double_click(field_name)
    action.perform()
    edit_field = driver.find_element_by_class_name('grid-input-cell')
    # field_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    edit_field.send_keys(input)
    time.sleep(2)
    edit_field.send_keys(Keys.TAB)
    time.sleep(2)

def enable_setup_tool(setup_item):
    setup_item.click()
    time.sleep(1)

# def add_location(driver):
#     location_code = driver.find_element_by_css_selector(
#         'div.cell.body.text.name.editable.edited.field-range.field-range-top.'
#         'field-range-right.field-range-bottom.field-range-left.'
#         'field-range-pivot.read-only')
#     location_code_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
#     edit_field(driver, location_code, location_code_string)
#     driver.implicitly_wait(10)
#     location_city = driver.find_element_by_css_selector('div.cell.body.text.city.editable.field-range.field-range-top.'
#                                                         'field-range-right.field-range-bottom.field-range-left.'
#                                                         'field-range-pivot.read-only')
#     location_city_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
#     edit_field(driver, location_city, location_city_string)
#     driver.implicitly_wait(10)
#     location_state = driver.find_element_by_css_selector(
#         'div.cell.body.text.state.editable.field-range.field-range-top.'
#         'field-range-right.field-range-bottom.field-range-left.'
#         'field-range-pivot.read-only')
#     location_state_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
#     edit_field(driver, location_state, location_state_string)
#     driver.implicitly_wait(10)
#     location_country = driver.find_element_by_css_selector(
#         'div.cell.body.text.country.editable.field-range.field-range-top.'
#         'field-range-right.field-range-bottom.field-range-left.'
#         'field-range-pivot.read-only')
#     location_country_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
#     edit_field(driver, location_country, location_country_string)
#     driver.implicitly_wait(10)

def test_add_delete_location(driver):
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    select_locations_setup = driver.find_element_by_css_selector('div.actions.tools-setup > button:nth-child(1)')
    select_locations_setup.click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    select_add_location = driver.find_element_by_css_selector('div > div.tools-actions > div > a:nth-child(1)')
    select_add_location.click()
    driver.implicitly_wait(10)
    location_code = driver.find_element_by_css_selector(
        'div.cell.body.text.name.editable.edited.field-range.field-range-top.'
        'field-range-right.field-range-bottom.field-range-left.'
        'field-range-pivot.read-only')
    location_code_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    edit_field(driver, location_code, location_code_string)
    driver.implicitly_wait(10)
    location_city = driver.find_element_by_css_selector('div.cell.body.text.city.editable.field-range.field-range-top.'
                                                        'field-range-right.field-range-bottom.field-range-left.'
                                                        'field-range-pivot.read-only')
    location_city_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    edit_field(driver, location_city, location_city_string)
    driver.implicitly_wait(10)
    location_state = driver.find_element_by_css_selector(
        'div.cell.body.text.state.editable.field-range.field-range-top.'
        'field-range-right.field-range-bottom.field-range-left.'
        'field-range-pivot.read-only')
    location_state_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    edit_field(driver, location_state, location_state_string)
    driver.implicitly_wait(10)
    location_country = driver.find_element_by_css_selector(
        'div.cell.body.text.country.editable.field-range.field-range-top.'
        'field-range-right.field-range-bottom.field-range-left.'
        'field-range-pivot.read-only')
    location_country_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    edit_field(driver, location_country, location_country_string)
    driver.implicitly_wait(10)

    delete_location = driver.find_element_by_css_selector('div.tools-actions > div > a:nth-child(2)')
    delete_location.click()
    #driver.implicitly_wait(10)
    time.sleep(2)

    close_setup = driver.find_element_by_css_selector('div.action > button')
    close_setup.click()
    time.sleep(2)
    driver.implicitly_wait(5)
    driver.switch_to.window(driver.window_handles[0])
    driver.implicitly_wait(2)

    tpsheet = driver.find_element_by_css_selector('div:nth-child(1) > div.cell.body.index.non-editable.read-only')
    action = ActionChains(driver)
    action.double_click(tpsheet)
    action.perform()
    accntsheet = driver.find_element_by_css_selector('div:nth-child(1) > div.cell.body.index.non-editable.read-only')
    action = ActionChains(driver)
    action.double_click(accntsheet)
    action.perform()

    locations_column = driver.find_element_by_css_selector(
        'div > div.main.detail.focused > div > div.grid-head > div.ellipsis > i')
    locations_column.click()
    driver.implicitly_wait(5)
    select_locations_tools = driver.find_element_by_css_selector(
        'body > div.ui.bottom.right.basic.popup.transition.visible.grid-column-options.content > div:nth-child(4) > div > label')
    select_locations_tools.click()
    time.sleep(1)

    details_add_locations = driver.find_element_by_css_selector(
        'div.row.selected.darkSalmon > div.cell.body.type_ahead.location.editable.read-only')
    action = ActionChains(driver)
    action.double_click(details_add_locations)
    action.perform()
    driver.implicitly_wait(5)
    locations_add = driver.find_element_by_css_selector('input.typeahead-input')
    locations_add.clear()
    driver.implicitly_wait(10)
    locations_add.send_keys(location_code_string)
    driver.implicitly_wait(5)
    locations_add.send_keys(Keys.TAB)
    driver.implicitly_wait(10)
    assert location_code_string in details_add_locations.text
