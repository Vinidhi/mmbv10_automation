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

def test_setup_currency_changes(driver, open_budget):
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(2)
    select_currency_setup = driver.find_element_by_css_selector('div.actions.tools-setup > button:nth-child(5)')
    select_currency_setup.click()
    driver.implicitly_wait(5)
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(5)
    add_currency = driver.find_element_by_css_selector('i.add.square.icon')
    add_currency.click()
    driver.implicitly_wait(5)
    currency_code = driver.find_element_by_css_selector('input.typeahead-input')
    currency_code.send_keys('I')
    driver.implicitly_wait(5)
    select_currency_IDR = driver.find_element_by_css_selector('div.cell.body.type_ahead.name.editable.edited.field-range'
                                                              '.field-range-top.field-range-right.field-range-bottom.'
                                                              'field-range-left.field-range-pivot.read-only > div > div '
                                                              '> div:nth-child(3)')
    select_currency_IDR.click()
    driver.implicitly_wait(10)
    currency_code.send_keys(Keys.TAB)
    driver.implicitly_wait(10)
    currency_description = driver.find_element_by_css_selector('div.content.focused span.ellip.no-select.pre-span')
    assert currency_description.text == 'Indonesian Rupiah'
    currency_symbol = driver.find_element_by_css_selector('div.row.selected > div.cell.body.list.symbol.editable.read-only >'
                                                          ' div > span > span ')
    currency_symbol.click()
    driver.implicitly_wait(5)
    select_symbol = driver.find_element_by_css_selector('ul > li:nth-child(2)')
    select_symbol.click()
    driver.implicitly_wait(5)
    select_checkbox = driver.find_element_by_css_selector('div.row.selected > div.cell.body.checkbox.right_align.'
                                                          'non-editable.read-only > div > div > div')
    select_checkbox.click()
    driver.implicitly_wait(5)
    separator = driver.find_element_by_css_selector('div.row.selected > div.cell.body.list.separator.editable.'
                                                           'field-range.field-range-top.field-range-bottom.read-only')
    separator.click()
    driver.implicitly_wait(5)
    select_separator = driver.find_element_by_css_selector('ul > li:nth-child(2)')
    select_separator.click()
    driver.implicitly_wait(5)
    rate = driver.find_element_by_css_selector('div.row.selected > div.cell.body.number.rate.editable.read-only')
    rate.click()
    driver.implicitly_wait(5)
    edit_field(driver, rate, 2)

    totals_subtotals_dropdown_icon = driver.find_element_by_css_selector('div:nth-child(3) > div > div > i')
    totals_subtotals_dropdown_icon.click()
    driver.implicitly_wait(5)
    select_IDR_total_subtotal = driver.find_element_by_css_selector('div.visible.menu.transition > div:nth-child(5)')
    select_IDR_total_subtotal.click()
    time.sleep(2)
    convert_base_currency_dropdown = driver.find_element_by_css_selector('div:nth-child(1) > div > div > i')
    convert_base_currency_dropdown.click()
    driver.implicitly_wait(5)
    select_IDR_convert_base_currency = driver.find_element_by_css_selector('div.visible.menu.transition > div:nth-child(5)')
    select_IDR_convert_base_currency.click()
    driver.implicitly_wait(5)
    close_setup = driver.find_element_by_css_selector('.ui.small.primary.button')
    close_setup.click()
    driver.implicitly_wait(5)
    driver.switch_to.window(driver.window_handles[0])
    driver.implicitly_wait(2)
    topsheet_total_first_value = driver.find_element_by_css_selector('div.row.selected > div.cell.body.number.total.'
                                                                     'non-editable.read-only > span:nth-child(1)')
    assert '﷼' in topsheet_total_first_value.text


def test_delete_currency(driver):
    select_currency_setup = driver.find_element_by_css_selector('div.actions.tools-setup > button:nth-child(5)')
    select_currency_setup.click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    delete_currency = driver.find_element_by_css_selector('i.trash.alternate.icon')
    delete_currency.click()
    time.sleep(2)
    delete_currency_confirmation = driver.find_element_by_css_selector('div > div.actions > button.ui.basic.button')
    delete_currency_confirmation.click()
    time.sleep(2)
    close_currency_setup = driver.find_element_by_css_selector('div.action > button')
    close_currency_setup.click()
    time.sleep(1)
