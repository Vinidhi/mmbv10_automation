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

def test_setup_sets_changes(driver):
    driver.switch_to.window(driver.window_handles[0])
    driver.implicitly_wait(2)
    select_sets_setup=driver.find_element_by_css_selector('div.actions.tools-setup > button:nth-child(7)')
    select_sets_setup.click()
    driver.implicitly_wait(5)
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(5)
    add_set = driver.find_element_by_css_selector('div > div.tools-actions > div > a:nth-child(1) > i')
    add_set.click()
    driver.implicitly_wait(5)
    set_name = driver.find_element_by_css_selector('input.grid-input-cell')
    set_name.send_keys('ST')
    driver.implicitly_wait(5)
    set_name.send_keys(Keys.TAB)
    driver.implicitly_wait(10)
    move_to_desc= driver.find_element_by_css_selector('div.cell.body.text.description.editable.field-range.'
                                                      'field-range-top.field-range-right.field-range-bottom.'
                                                      'field-range-left.field-range-pivot.read-only')
    action = ActionChains(driver)
    action.double_click(move_to_desc)
    action.perform()
    driver.implicitly_wait(5)
    add_desc = driver.find_element_by_css_selector('input.grid-input-cell')
    add_desc.send_keys('my new set value')
    add_desc.send_keys(Keys.ENTER)
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

    sets_column = driver.find_element_by_css_selector('div > div.main.detail.focused > div > div.grid-head > div.ellipsis > i')
    sets_column.click()
    driver.implicitly_wait(5)
    select_sets_tools = driver.find_element_by_css_selector('body > div.ui.bottom.right.basic.popup.transition.visible.'
                                                            'grid-column-options.content > div:nth-child(5) > div > label')
    select_sets_tools.click()
    time.sleep(.5)

    details_add_sets = driver.find_element_by_css_selector('div:nth-child(1) > div.cell.body.type_ahead.set.editable.read-only')
    action = ActionChains(driver)
    action.double_click(details_add_sets)
    action.perform()
    driver.implicitly_wait(5)
    sets_add = driver.find_element_by_css_selector('input.typeahead-input')
    sets_add.clear()
    driver.implicitly_wait(10)
    sets_add.send_keys('ST')
    driver.implicitly_wait(5)
    sets_add.send_keys(Keys.TAB)
    driver.implicitly_wait(10)
    assert 'ST' in details_add_sets.text

def test_delete_sets(driver):
        select_sets_setup = driver.find_element_by_css_selector('div.actions.tools-setup > button:nth-child(7)')
        select_sets_setup.click()
        driver.implicitly_wait(5)
        driver.switch_to.window(driver.window_handles[1])
        driver.implicitly_wait(5)
        delete_sets = driver.find_element_by_css_selector('div > div.tools-actions > div > a:nth-child(2) > i')
        delete_sets.click()
        driver.implicitly_wait(5)
        select_delete_button = driver.find_element_by_css_selector('div > div.actions > button.ui.basic.button')
        select_delete_button.click()
        time.sleep(2)
        close_setup = driver.find_element_by_css_selector('div.action > button')
        close_setup.click()
        time.sleep(1)



