import pytest
import time
from selenium.webdriver.common.action_chains import ActionChains
import lib.config as config
from selenium.webdriver.common.keys import Keys


# def test_open_first_budget(driver,open_budget):
#     driver.switch_to.window(driver.window_handles[1])
#     time.sleep(2)

@pytest.mark.parametrize('budget_file',[config.budget_1_selector,config.budget_2_selector,config.budget_3_selector,
                                        config.budget_4_selector, config.budget_5_selector])
def test_open_multipe_budgets(driver, budget_file):
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    open_new_button = driver.find_element_by_xpath('//button[text()="Open/New"]')
    open_new_button.click()
    driver.implicitly_wait(5)
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(10)
    select_budget = driver.find_element_by_css_selector(budget_file)
    select_budget.click()
    driver.implicitly_wait(10)
    action = ActionChains(driver)
    action.double_click(select_budget)
    action.perform()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)


def test_open_split_screen(driver):
    driver.switch_to_window(driver.window_handles[0])
    time.sleep(2)
    select_ellipsis_icon = driver.find_element_by_css_selector('div.ui.top.left.pointing.dropdown.ellipsis-menu > i')
    select_ellipsis_icon.click()
    time.sleep(2)
    dropdown_select_open_in_split_screen = driver.find_element_by_css_selector('div.ui.active.visible.top.left.pointing.'
                                                                               'dropdown.ellipsis-menu > div > '
                                                                               'div:nth-child(4) > span')
    dropdown_select_open_in_split_screen.click()
    time.sleep(2)
    select_second_budget = driver.find_element_by_css_selector('div.ui.attached.tabular.menu > a:nth-child(2) > div > '
                                                               'span')
    select_second_budget.click()
    time.sleep(2)
    select_ellipsis_icon = driver.find_element_by_css_selector('div.ui.top.left.pointing.dropdown.ellipsis-menu > i')
    select_ellipsis_icon.click()
    time.sleep(2)
    dropdown_select_move_to_right_pane = driver.find_element_by_css_selector('div.ui.active.visible.top.left.pointing.'
                                                                             'dropdown.ellipsis-menu > div > '
                                                                             'div:nth-child(4) > span')
    dropdown_select_move_to_right_pane.click()
    time.sleep(2)

def test_setup_tools_budget(driver):
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).send_keys('e').key_up(Keys.CONTROL).perform()
    action.send_keys()
    time.sleep(2)
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).send_keys('k').key_up(Keys.CONTROL).perform()
    action.send_keys()
    time.sleep(2)
    select_second_budget = driver.find_element_by_css_selector('div.budgets-container.horizontal.half-width.left > '
                                                               'div.ui.attached.tabular.menu > a:nth-child(2) > div')
    select_second_budget.click()
    time.sleep(2)
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).send_keys('e').key_up(Keys.CONTROL).perform()
    action.send_keys()
    time.sleep(2)
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).send_keys('k').key_up(Keys.CONTROL).perform()
    action.send_keys()
    time.sleep(2)

    tool_tab = driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div/div')
    tool_tab.click()
    time.sleep(2)

    apply_fringe = driver.find_element_by_css_selector('div.cell.body.custom.applied.non-editable.field-range.'
                                                       'field-range-top.field-range-bottom.read-only')
    # apply_fringe = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[2]/div[1]/div[4]/div/div/div/div[2]/div/'
    #                                             'div[3]/div[2]/div[1]/div[2]/div')
    apply_fringe.click()
    time.sleep(2)

    splitscreen3 = driver.find_element_by_xpath(
        '//div[@class="ui top left pointing dropdown ellipsis-menu"]//i[@class="ellipsis vertical icon"]')
    splitscreen3.click()
    time.sleep(1)

    splitscreen_close = driver.find_element_by_xpath('//*[text()[contains(.,"Exit Split-Screen")]]')
    splitscreen_close.click()
    time.sleep(3)
    driver.close()







'''
@pytest.mark.smoke
def test_act_budget(login_fix):
    """Going to Detail level of budget"""
    driver = login_fix.driver
    detail2 = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[7]/div[1]/span')
    action = ActionChains(driver)
    action.double_click(detail2)
    action.perform()
    time.sleep(2)

    detail3=driver.find_element_by_xpath(('//*[@id="root"]/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[1]/div[1]/span'))
    action = ActionChains(driver)
    action.double_click(detail3)
    action.perform()
    time.sleep(3)

    tool_tab=driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div/div')
    tool_tab.click()
    time.sleep(2)

    apply_fringe=driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[2]/div[1]/div[4]/div/div/div/div[2]/div/div[3]/div[2]/div[1]/div[2]')
    apply_fringe.click()
    time.sleep(2)

    splitscreen3=driver.find_element_by_xpath('//div[@class="ui top left pointing dropdown ellipsis-menu"]//i[@class="ellipsis vertical icon"]')
    splitscreen3.click()
    time.sleep(1)

    splitscreen_close=driver.find_element_by_xpath('//*[text()[contains(.,"Exit Split-Screen")]]')
    splitscreen_close.click()
    time.sleep(3)
    driver.close()
'''