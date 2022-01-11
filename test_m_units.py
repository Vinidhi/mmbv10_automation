import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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

def test_setup_units_changes(driver):
    driver.switch_to.window(driver.window_handles[0])
    driver.implicitly_wait(2)
    select_units_setup=driver.find_element_by_css_selector('div.actions.tools-setup > button:nth-child(6)')
    select_units_setup.click()
    driver.implicitly_wait(5)
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(5)
    add_unit=driver.find_element_by_css_selector('div > div.tools-actions > div > a:nth-child(1) > i')
    add_unit.click()
    driver.implicitly_wait(5)
    unit_name=driver.find_element_by_css_selector('input.grid-input-cell')
    unit_name.send_keys('U1')
    driver.implicitly_wait(5)
    unit_name.send_keys(Keys.TAB)
    driver.implicitly_wait(10)

    move_to_plural=driver.find_element_by_css_selector('div.cell.body.text.plural.editable.field-range.field-range-top.'
                                                       'field-range-right.field-range-bottom.field-range-left.'
                                                       'field-range-pivot.read-only')
    action = ActionChains(driver)
    action.double_click(move_to_plural)
    action.perform()
    driver.implicitly_wait(5)
    add_plural=driver.find_element_by_css_selector('input.grid-input-cell')
    add_plural.send_keys('U1s')
    add_plural.send_keys(Keys.TAB)
    driver.implicitly_wait(10)

    move_to_description=driver.find_element_by_css_selector('div.cell.body.text.description.editable.field-range.'
                                                            'field-range-top.field-range-right.field-range-bottom.'
                                                            'field-range-left.field-range-pivot.read-only')
    action = ActionChains(driver)
    action.double_click(move_to_description)
    action.perform()
    driver.implicitly_wait(5)
    add_description=driver.find_element_by_css_selector('input.grid-input-cell')
    add_description.send_keys('My unit')
    driver.implicitly_wait(5)
    add_description.send_keys(Keys.TAB)
    driver.implicitly_wait(10)

    move_to_hours=driver.find_element_by_css_selector('div.cell.body.number.hours.editable.field-range.field-range-top.'
                                                      'field-range-right.field-range-bottom.field-range-left.'
                                                      'field-range-pivot.read-only')
    action = ActionChains(driver)
    action.double_click(move_to_hours)
    action.perform()
    driver.implicitly_wait(5)
    add_description = driver.find_element_by_css_selector('input.grid-input-cell')
    add_description.send_keys('10')
    add_description.send_keys(Keys.ENTER)
    time.sleep(3)

    close_setup = driver.find_element_by_css_selector('.ui.small.primary.button')
    close_setup.click()
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

    details_add_unit=driver.find_element_by_css_selector('div > div.grid-body.alt > div:nth-child(1) > '
                                                         'div.cell.body.type_ahead.unit.editable.read-only')
    action = ActionChains(driver)
    action.double_click(details_add_unit)
    action.perform()
    driver.implicitly_wait(5)
    unit_add = driver.find_element_by_css_selector('input.typeahead-input')
    #unit_add = driver.find_element_by_css_selector('typeahead')
    unit_add.clear()
    unit_add.send_keys('U1')
    driver.implicitly_wait(5)
    unit_add.send_keys(Keys.TAB)
    driver.implicitly_wait(10)
    assert 'U1' in details_add_unit.text

def test_delete_unit(driver):
    select_unit_setup = driver.find_element_by_css_selector('div.actions.tools-setup > button:nth-child(6)')
    select_unit_setup.click()
    driver.implicitly_wait(5)
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(5)
    delete_unit = driver.find_element_by_css_selector('div > div.tools-actions > div > a:nth-child(2) > i')
    delete_unit.click()
    driver.implicitly_wait(5)
    select_delete_button=driver.find_element_by_css_selector('div > div.actions > button.ui.basic.button')
    select_delete_button.click()
    time.sleep(2)
    close_setup = driver.find_element_by_css_selector('.ui.small.primary.button')
    close_setup.click()
