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

def test_setup_groups_changes(driver):
    driver.switch_to.window(driver.window_handles[0])
    driver.implicitly_wait(2)
    select_groups_setup=driver.find_element_by_css_selector('div.actions.tools-setup > button:nth-child(4)')
    select_groups_setup.click()
    driver.implicitly_wait(5)
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(5)
    add_group=driver.find_element_by_css_selector('div > div.tools-actions > div > a:nth-child(1) > i')
    add_group.click()
    driver.implicitly_wait(5)
    group_name = driver.find_element_by_css_selector('input.grid-input-cell')
    group_name.send_keys('G1')
    driver.implicitly_wait(5)
    group_name.send_keys(Keys.TAB)
    driver.implicitly_wait(10)

    #move_to_desc = driver.find_element_by_css_selector('div.cell.body.text.description.editable.field-range.field-range-top.
    # field-range-right.field-range-bottom.field-range-left.field-range-pivot.read-only > span > span > pre')
    desc = driver.find_element_by_css_selector('div.cell.body.text.description.editable.field-range.field-range-top.'
                                               'field-range-right.field-range-bottom.field-range-left.field-range-pivot.'
                                               'read-only')
    action = ActionChains(driver)
    action.double_click(desc)
    action.perform()
    driver.implicitly_wait(5)
    add_desc = driver.find_element_by_css_selector('input.grid-input-cell')
    add_desc.send_keys('Group to be tested')
    add_desc.send_keys(Keys.TAB)
    driver.implicitly_wait(10)

    move_to_ID = driver.find_element_by_css_selector('div.cell.body.text.ident.editable.field-range.field-range-top.'
                                                     'field-range-right.field-range-bottom.field-range-left.field-range-pivot.'
                                                     'read-only')
    action = ActionChains(driver)
    action.double_click(move_to_ID)
    action.perform()
    driver.implicitly_wait(5)
    add_ID = driver.find_element_by_css_selector('input.grid-input-cell')
    add_ID.send_keys('GR')
    driver.implicitly_wait(10)

    select_color_dropdown = driver.find_element_by_css_selector('i.caret.down.icon')
    select_color_dropdown.click()
    driver.implicitly_wait(5)
    select_color = driver.find_element_by_css_selector('div.colorSuggestions.oceanBlue')
    select_color.click()
    driver.implicitly_wait(5)

    select_checkbox = driver.find_element_by_css_selector('div.row.selected > div.cell.body.checkbox.include.'
                                                          'non-editable.read-only > div > div > div')
    select_checkbox.click()
    driver.implicitly_wait(5)

    group_status_conflict_header = driver.find_element_by_css_selector('div:nth-child(2) > div > div > div.divider.text')
    group_status_conflict_header.click()
    driver.implicitly_wait(5)
    group_status_conflict_include = driver.find_element_by_css_selector('div.visible.menu.transition > div#include.item')
    group_status_conflict_include.click()
    time.sleep(1)
    group_status_conflict_header2 = driver.find_element_by_css_selector('div:nth-child(3) > div > div > div.divider.text')
    group_status_conflict_header2.click()
    driver.implicitly_wait(5)
    group_status_conflict_include2 = driver.find_element_by_css_selector('div.visible.menu.transition > div#include.item')
    group_status_conflict_include2.click()
    time.sleep(2)

    close_setup = driver.find_element_by_css_selector('.ui.small.primary.button')
    close_setup.click()
    driver.implicitly_wait(5)
    driver.switch_to.window(driver.window_handles[0])
    driver.implicitly_wait(4)

    tpsheet=driver.find_element_by_css_selector('div:nth-child(1) > div.cell.body.index.non-editable.read-only')
    action = ActionChains(driver)
    action.double_click(tpsheet)
    action.perform()
    accntsheet=driver.find_element_by_css_selector('div:nth-child(1) > div.cell.body.index.non-editable.read-only')
    action = ActionChains(driver)
    action.double_click(accntsheet)
    action.perform()

    groups_column=driver.find_element_by_css_selector('div > div.main.detail.focused > div > div.grid-head > div.ellipsis > i')
    groups_column.click()
    driver.implicitly_wait(5)
    select_group_dropdown=driver.find_element_by_css_selector('body > div.ui.bottom.right.basic.popup.transition.'
                                                              'visible.grid-column-options.content > div:nth-child(3) > '
                                                              'div > label')
    select_group_dropdown.click()
    time.sleep(3)
    apply_group_select=driver.find_element_by_css_selector('div.splitter-pane.down > div > div > div.ui.bottom.attached.'
                                                           'segment.active.tab > div > div.grid.tools-apply-content > '
                                                           'div.grid-body.alt > div:nth-child(1) > div.cell.body.text.name.'
                                                           'non-editable.read-only > span')
    apply_group_select.click()
    select_checkbox=driver.find_element_by_css_selector('div.splitter-pane.down > div > div > div.ui.bottom.attached.'
                                                        'segment.active.tab > div > div.grid.tools-apply-content > '
                                                        'div.grid-body.alt > div:nth-child(1) > div.cell.body.custom.'
                                                        'applied.non-editable.read-only > div')
    select_checkbox.click()
    time.sleep(2)


def test_delete_group(driver):
    select_unit_group = driver.find_element_by_css_selector('div.actions.tools-setup > button:nth-child(4)')
    select_unit_group.click()
    driver.implicitly_wait(5)
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(5)
    delete_group= driver.find_element_by_css_selector('div > div.tools-actions > div > a:nth-child(2) > i')
    delete_group.click()
    driver.implicitly_wait(5)
    select_delete_button = driver.find_element_by_css_selector('div > div.actions > button.ui.basic.button')
    select_delete_button.click()
    time.sleep(2)
    close_setup = driver.find_element_by_css_selector('.ui.small.primary.button')
    close_setup.click()