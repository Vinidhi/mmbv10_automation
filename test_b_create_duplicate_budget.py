import pytest
import time
from selenium.webdriver.common.action_chains import ActionChains


@pytest.mark.smoke
def test_create_duplicate_budget(driver):
    """Create duplicate budget from existing budget"""
    driver.switch_to.window(driver.window_handles[0])
    driver.implicitly_wait(5)
    select_project = driver.find_element_by_xpath('//span[contains(@class,"ellip no-select pre-span") and '
                                                       'contains(text(),"TEMP_PROJ")]')
    select_project.click()
    driver.implicitly_wait(2)
    select_budget = driver.find_element_by_xpath('//span[contains(@class,"ellip no-select pre-span") and '
                                                      'contains(text(),"Nashville Pattern & Amort v1")]')
    select_budget.click()
    driver.implicitly_wait(2)

    duplicate_budget = driver.find_element_by_xpath('//div[@class="action-buttons no-select "]'
                                                         '//a[@class="ui basic label"]//i[@class="copy icon"]')

    duplicate_budget.click()
    driver.implicitly_wait(5)

    add_project = driver.find_element_by_xpath('//*[text()[contains(.,"Add Project")]]')
    add_project.click()
    driver.implicitly_wait(5)
    select_new_project = driver.find_element_by_xpath('//span[contains(@class,"ellip no-select pre-span") '
                                                           'and contains(text(),"New Folder")]')
    select_new_project.click()
    driver.implicitly_wait(5)
    action = ActionChains(driver)
    action.double_click(select_new_project)
    action.perform()
    driver.implicitly_wait(5)
    new_project_name = driver.find_element_by_class_name('grid-input-cell')
    new_project_name.clear()
    driver.implicitly_wait(5)
    new_project_name_string = "TEST"
    new_project_name.send_keys(new_project_name_string)
    driver.implicitly_wait(5)
    select_uncategorized = driver.find_element_by_xpath(('//span[contains(@class,"ellip no-select pre-span") '
                                                              'and contains(text(),"TEMP_PROJ")]'))
    select_uncategorized.click()
    driver.implicitly_wait(5)
    select_duplicate_budget = driver.find_element_by_xpath('//span[contains(@class,"ellip no-select pre-span") and '
                                                      'contains(text(),"Nashville Pattern & Amort v1_1")]')
    select_duplicate_budget.click()
    driver.implicitly_wait(5)
    move_to_project_dropdown = driver.find_element_by_xpath('//div[@class="ui inline dropdown move-to-category'
                                                                  ' dropdown-action"]//i[@class="dropdown icon"]')
    move_to_project_dropdown.click()
    driver.implicitly_wait(5)

    # select_project_from_dropdown = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/'
    #                                                                  'div[4]/div/div[1]/div[2]/div/div[3]')
    select_project_from_dropdown = driver.find_element_by_css_selector('div.ui.active.visible.inline.dropdown.move-to-category.'
                                                        'dropdown-action > div > div:nth-child(3)')
    select_project_from_dropdown.click()
    driver.implicitly_wait(5)
    switch_to_selected_project = driver.find_element_by_xpath('//span[contains(@class,"ellip no-select pre-span") '
                                                              'and contains(text(),"TEST")]')

    switch_to_selected_project.click()
    driver.implicitly_wait(5)

    # select_budget = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[2]/'
    #                                                   'div/div[2]/div/div[1]/span')
    select_budget = driver.find_element_by_css_selector('div:nth-child(1) > div.cell.body.text.name.editable.read-only')
    select_budget.click()
    time.sleep(2)
    open_selected_budget = driver.find_element_by_xpath('//button[text()="Open Budget"]')
    open_selected_budget.click()
    time.sleep(2)
