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

def test_cloud_setup_fringes(driver):
    driver.switch_to.window(driver.window_handles[0])
    driver.implicitly_wait(2)
    select_fringes_setup = driver.find_element_by_css_selector('div.actions.tools-setup > button:nth-child(2) >'
                                                                 ' span.tools-alt')
    select_fringes_setup.click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    fringes_budget_highlighted = driver.find_element_by_css_selector('div:nth-child(1) > div.cell.body.text.name.editable.read-only')
    fringes = fringes_budget_highlighted.text
    select_upload_to_cloud = driver.find_element_by_css_selector('div.tools-actions > div > a:nth-child(4)')
    select_upload_to_cloud.click()
    time.sleep(2)
    upload_continue_button = driver.find_element_by_css_selector('div.actions > button.ui.small.primary.button')
    upload_continue_button.click()
    time.sleep(2)
    select_cloud_fringes = driver.find_element_by_css_selector('div.cloud-libs-switch.no-select > span.cloud-library')
    select_cloud_fringes.click()
    time.sleep(2)
    fringes_moved_to_cloud = driver.find_element_by_css_selector('div:nth-child(1) > div.cell.body.text.name.editable.read-only')
    fringes_moved_to_cloud.click()
    assert fringes_moved_to_cloud.text == fringes
    time.sleep(2)

def test_add_fringe_details(driver):
    select_add_fringe_category=driver.find_element_by_css_selector('div.action-buttons.no-select > a:nth-child(1) > i')
    select_add_fringe_category.click()
    driver.implicitly_wait(10)
    select_added_category=driver.find_element_by_css_selector('input.grid-input-cell')
    select_added_category.click()
    driver.implicitly_wait(10)
    category_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    edit_field(driver, select_added_category, category_string)
    driver.implicitly_wait(5)

    select_add_fringe=driver.find_element_by_css_selector('div.tools-actions > div > a:nth-child(1) > i')
    select_add_fringe.click()
    driver.implicitly_wait(10)
    select_added_Fringe= driver.find_element_by_css_selector('input.grid-input-cell')
    select_added_Fringe.click()
    driver.implicitly_wait(10)
    fringe_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    edit_field(driver, select_added_Fringe, fringe_string)
    driver.implicitly_wait(3)

    Fringe_desc_field = driver.find_element_by_css_selector('div > div.cell.body.text.description.editable.read-only')
    Fringe_desc_field.click()
    driver.implicitly_wait(2)
    desc_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    edit_field(driver, Fringe_desc_field, desc_string)
    driver.implicitly_wait(2)

    Fringe_ID_field = driver.find_element_by_css_selector('div > div.cell.body.text.ident.editable.read-only')
    Fringe_ID_field.click()
    driver.implicitly_wait(2)
    ID_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=2))
    edit_field(driver, Fringe_ID_field, ID_string)
    driver.implicitly_wait(2)

    Fringe_rate_field = driver.find_element_by_css_selector('div > div.cell.body.number.rate.editable.read-only')
    Fringe_rate_field.click()
    driver.implicitly_wait(2)
    action = ActionChains(driver)
    action.double_click(Fringe_rate_field)
    action.perform()
    add_rate = driver.find_element_by_css_selector('input.grid-input-cell')
    add_rate.clear()
    driver.implicitly_wait(5)
    rate_string = ''.join(random.choices(string.digits, k=1))
    if (rate_string > '-1'):
        edit_field(driver,add_rate,rate_string)
    else:
        add_rate.send_keys(rate_string)
        driver.implicitly_wait(5)
        message=driver.find_element_by_css_selector('div.content.bottom > div > div > span')
        assert 'Rate must be positive.' in message.text
        add_rate.clear()
        add_rate.send_keys(10)
        add_rate.send_keys(Keys.ENTER)
        time.sleep(3)


    Fringe_unit_field = driver.find_element_by_css_selector('div > div.cell.body.type_ahead.unit.editable.read-only')
    Fringe_unit_field.click()
    driver.implicitly_wait(2)
    action = ActionChains(driver)
    action.double_click(Fringe_unit_field)
    action.perform()
    add_unit = driver.find_element_by_css_selector('input.typeahead-input')
    add_unit.clear()
    driver.implicitly_wait(5)
    add_unit.send_keys('%')
    driver.implicitly_wait(3)

    Fringe_cutoff_field = driver.find_element_by_css_selector('div > div.cell.body.number.cutoff.editable.read-only')
    Fringe_cutoff_field.click()
    driver.implicitly_wait(2)
    cutoff_string = ''.join(random.choices(string.digits, k=2))
    edit_field(driver, Fringe_cutoff_field, cutoff_string)
    driver.implicitly_wait(2)

    delete_fringe=driver.find_element_by_css_selector('div.tools-actions > div > a:nth-child(2) > i')
    delete_fringe.click()
    driver.implicitly_wait(2)

    move_to_category_dropdown_icon = driver.find_element_by_css_selector('div.tools-actions > div > div > i')
    move_to_category_dropdown_icon.click()
    driver.implicitly_wait(10)
    select_uncategorized_from_dropdown = driver.find_element_by_css_selector('div.tools-actions > div > div > div > div:nth-child(1) > span')
    select_uncategorized_from_dropdown.click()
    driver.implicitly_wait(10)
    category_uncategorized = driver.find_element_by_css_selector('div.active-section.with-action-buttons > div:nth-child(1) > div > span')
    category_uncategorized.click()
    Fringe_moved_uncategorized = driver.find_element_by_css_selector('div:nth-child(1) > div.cell.body.text.name.editable.read-only > span')
    assert Fringe_moved_uncategorized.text == fringe_string
    time.sleep(2)

    download_budget = driver.find_element_by_css_selector('div.tools-actions > div > a:nth-child(4)')
    download_budget.click()
    driver.implicitly_wait(10)
    continue_download = driver.find_element_by_css_selector('div.actions > button.ui.small.primary.button')
    continue_download.click()
    time.sleep(3)

    find_fringe=driver.find_element_by_css_selector('div.cell.body.text.name.editable.read-only > span[title="FICA 1"]')
    find_fringe.click()
    # x = driver.find_element_by_css_selector('div:nth-child(2) > div.cell.body.text.name.editable.read-only > span')
    # y = x.text
    # x1 = driver.find_element_by_css_selector('div:nth-child(1) > div.cell.body.text.name.editable.read-only > span')
    # y1 = x1.text
    #
    # if y == find_fringe:
    #    x.click()
    # elif y1 == find_fringe:
    #    x1.click()

    time.sleep(3)
    click_delete1 = driver.find_element_by_css_selector('div.tools-actions > div > a:nth-child(2) > i')
    click_delete1.click()
    driver.implicitly_wait(10)
    delete_fringe_library1 = driver.find_element_by_css_selector('div:nth-child(1) > div.cell.body.text.name.editable.read-only > span')
    delete_fringe_library1.click()
    driver.implicitly_wait(5)
    click_delete1.click()
    driver.implicitly_wait(10)

    switch_to_budget_library = driver.find_element_by_css_selector('div.cloud-libs-switch.no-select > span.budget-library > span')
    switch_to_budget_library.click()
    time.sleep(3)

    select_downloaded_fringe=driver.find_element_by_css_selector('div:nth-child(42) > div.cell.body.text.name.editable.read-only > span')
    select_downloaded_fringe.click()
    driver.implicitly_wait(5)
    click_delete1=driver.find_element_by_css_selector('div.tools-actions > div > a:nth-child(2) > i')
    click_delete1.click()
    driver.implicitly_wait(15)

    close_setup = driver.find_element_by_css_selector('div.action > button')
    close_setup.click()
    time.sleep(2)






