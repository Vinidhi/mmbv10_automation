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

def test_add_fringes(driver):
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    #select_fringes_setup = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/button[2]')
    select_fringes_setup = driver.find_element_by_xpath('//*[text()[contains(.,"Fr")]]')
    select_fringes_setup.click()
    time.sleep(2)
    driver.implicitly_wait(2)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)
    add_fringe = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[1]/'
                                                   'div/a[1]')
    add_fringe.click()
    time.sleep(1)
    fringe_name = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[2]/'
                                                    'div[2]/div[1]/div[3]')
    fringe_name_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    edit_field(driver, fringe_name, fringe_name_string)
    time.sleep(1)
    fringe_desc = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[2]/'
                                                    'div[2]/div[1]/div[4]')
    fringe_desc_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    edit_field(driver, fringe_desc, fringe_desc_string)
    time.sleep(1)
    fringe_id = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[2]/'
                                                  'div[2]/div[1]/div[5]')
    fringe_id_string = ''.join(random.choices(string.digits, k=2))
    edit_field(driver, fringe_id, fringe_id_string)
    time.sleep(1)
    fringe_rate = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[2]/'
                                                    'div[2]/div[1]/div[6]')
    edit_field(driver, fringe_rate, 1)
    time.sleep(1)
    fringe_cutoff = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[2]/'
                                                      'div[2]/div[1]/div[8]')
    edit_field(driver, fringe_cutoff, 1)
    time.sleep(1)

    add_fringe.click()
    time.sleep(1)
    #
    # # delete_fringe = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[1]/'
    # #                                                   'div/a[2]')
    # # delete_fringe.click()
    # # time.sleep(2)
    #
    # # add_fringe = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[1]/'
    # #                                                'div/a[1]')
    # # add_fringe.click()
    # # time.sleep(1)
    fringe_name = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[2]/'
                                                    'div[2]/div[2]/div[3]')
    fringe_name_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    edit_field(driver, fringe_name, fringe_name_string)
    time.sleep(1)
    fringe_desc = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[2]/'
                                                    'div[2]/div[2]/div[4]')
    fringe_desc_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    edit_field(driver, fringe_desc, fringe_desc_string)
    time.sleep(1)
    fringe_id = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[2]/'
                                                  'div[2]/div[2]/div[5]')
    fringe_id_string = ''.join(random.choices(string.digits, k=2))
    edit_field(driver, fringe_id, fringe_id_string)
    time.sleep(1)
    fringe_rate = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[2]/'
                                                    'div[2]/div[2]/div[6]')
    edit_field(driver, fringe_rate, 1)
    time.sleep(1)
    fringe_unit = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[2]/'
                                                    'div[2]/div[2]/div[7]/div[1]')
    action = ActionChains(driver)
    action.double_click(fringe_unit)
    action.perform()
    edit_fringe_unit = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[2]/'
                                                         'div[2]/div[2]/div[7]/div[1]/input')
    edit_fringe_unit.clear()
    time.sleep(1)
    edit_fringe_unit.send_keys('Day')
    time.sleep(2)
    edit_fringe_unit.send_keys(Keys.TAB)
    time.sleep(2)
    fringe_cutoff = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[2]/'
                                                      'div[2]/div[2]/div[8]')
    edit_field(driver, fringe_cutoff, 1)
    time.sleep(1)

    add_fringe.click()
    time.sleep(1)

    close_fringe_setup = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]')
    close_fringe_setup.click()
    time.sleep(1)

def test_apply_fringes(driver):
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    drilldown_to_account_from_topsheet = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/'
                                                                           'div[1]/div[1]/div/div[2]/div/div[2]/'
                                                                           'div[1]/div[1]')
    action = ActionChains(driver)
    action.double_click(drilldown_to_account_from_topsheet)
    action.perform()
    time.sleep(2)
    drilldown_to_detail_from_account = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/'
                                                                         'div[1]/div[1]/div/div[2]/div/div[2]/'
                                                                         '/div[1]/div[1]')
    action = ActionChains(driver)
    action.double_click(drilldown_to_detail_from_account)
    action.perform()

    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)

    select_ellipsis_enable_columns_details = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/'
                                                                               'div[1]/div[1]/div/div[2]/div/div[1]/'
                                                                               'div[10]')
    select_ellipsis_enable_columns_details.click()
    time.sleep(1)
    select_fringes_column = driver.find_element_by_xpath('//div[@class="ui checkbox"]/label[text()="Fringes"]')
    select_fringes_column.click()
    time.sleep(1)

    select_tools_fringes_tab = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/'
                                                                 'div/div/div[1]/div/div[1]/div[1]/a[1]')
    select_tools_fringes_tab.click()
    time.sleep(1)

    ellipsis_tools_fringes = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/div/'
                                                               'div/div[1]/div/div/div[2]/div/div[3]/div[1]/div[6]')
    ellipsis_tools_fringes.click()
    time.sleep(1)
    enable_fringe_id_column = driver.find_element_by_xpath('/html/body/div[11]/div[2]/div')
    enable_fringe_id_column.click()
    time.sleep(1)

    enable_fringe_1 = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/div/div/'
                                                        'div[1]/div/div/div[2]/div/div[3]/div[2]/div[1]/div[2]')
    fringe_1_id = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/div/div/div[1]/'
                                                    'div/div/div[2]/div/div[3]/div[2]/div[1]/div[4]').text
    enable_setup_tool(enable_fringe_1)

    added_fringe_id = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/'
                                                     'div/div[2]/div[1]/div[3]')
    assert fringe_1_id in added_fringe_id.text

    enable_fringe_2 = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/div/div/'
                                                        'div[1]/div/div/div[2]/div/div[3]/div[2]/div[2]/div[2]')
    fringe_2_id = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/div/div/div[1]/'
                                                    'div/div/div[2]/div/div[3]/div[2]/div[2]/div[4]').text
    enable_setup_tool(enable_fringe_2)
    assert fringe_2_id in added_fringe_id.text

