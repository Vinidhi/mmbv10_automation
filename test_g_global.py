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
    # edit_field = self.driver.find_element_by_class_name(edit_field)
    # field_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    edit_field.send_keys(input)
    time.sleep(2)
    edit_field.send_keys(Keys.TAB)
    time.sleep(2)

def test_add_global(driver):
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    # global_setup = self.driver.find_element_by_xpath('//span[contains(@class,"tools-abbr") and contains(text(),"Gl")]')
    global_setup = driver.find_element_by_xpath('//*[text()[contains(.,"Gl")]]')
    global_setup.click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    add_global = driver.find_element_by_xpath('//*[text()[contains(.,"Add Global")]]')
    add_global.click()
    time.sleep(2)
    global_name = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[2]'
                                                    '/div[2]/div/div[5]')
    global_name_string = ''.join(random.choices(string.ascii_uppercase, k=3))
    # global_name.send_keys(global_name_string)
    edit_field(driver, global_name, global_name_string)
    time.sleep(2)
    global_desc = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[2]/'
                                                    'div[2]/div/div[6]')
    global_desc_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
    # global_name.send_keys(global_name_string)
    edit_field(driver, global_desc, global_desc_string)
    time.sleep(2)
    global_calc = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[2]/'
                                                    'div[2]/div[1]/div[7]')
    action = ActionChains(driver)
    action.double_click(global_calc)
    action.perform()
    global_calc_string = ''.join(random.choices(string.digits, k=2))
    edit_global_calc = driver.find_element_by_class_name('typeahead-input')
    edit_global_calc.send_keys(global_calc_string)
    # self.edit_field(global_calc, global_calc_string, 'cell body type_ahead_with_formula calculation editable ')

    time.sleep(2)
    global_unit = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[2]/'
                                                    'div[2]/div/div[8]')
    action = ActionChains(driver)
    action.double_click(global_unit)
    action.perform()
    # global_unit_string = 'D'
    global_unit_string = '%'
    edit_global_unit = driver.find_element_by_class_name('typeahead-input')
    time.sleep(2)
    edit_global_unit.send_keys(global_unit_string)
    time.sleep(1)
    edit_global_unit.send_keys(Keys.TAB)
    time.sleep(1)
    global_dec = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[2]/'
                                                   'div[2]/div/div[9]')
    global_dec_value = 2
    edit_field(driver, global_dec, global_dec_value)
    time.sleep(2)
    global_value = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/'
                                                            'div[2]/div[2]/div[1]/div[10]/span')
    assert global_value.text == global_calc_string + ".00"


    close_global_setup = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]')
    close_global_setup.click()
    time.sleep(1)

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

    # amt_field = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/'
    #                                               'div[2]/div[1]/div[4]')
    amt_field = driver.find_element_by_css_selector('div:nth-child(1) > div.cell.body.type_ahead_with_formula.amount.editable.read-only')
    action = ActionChains(driver)
    action.double_click(amt_field)
    action.perform()
    time.sleep(1)
    edit_amt_field = driver.find_element_by_class_name('typeahead-input')
    time.sleep(2)
    edit_amt_field.clear()
    time.sleep(1)
    edit_amt_field.send_keys(global_name_string)
    time.sleep(2)
    edit_amt_field.send_keys(Keys.TAB)
    time.sleep(2)
    assert amt_field.text == global_calc_string + ".00"

def test_delete_global(driver):
    select_global_setup = driver.find_element_by_css_selector('div.actions.tools-setup > button:nth-child(3)')
    select_global_setup.click()
    driver.implicitly_wait(5)
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(5)
    delete_global = driver.find_element_by_css_selector('div > div.tools-actions > div > a:nth-child(2) > i')
    delete_global.click()
    driver.implicitly_wait(5)
    select_delete_button = driver.find_element_by_css_selector('div > div.actions > button.ui.basic.button')
    select_delete_button.click()
    time.sleep(2)
    close_setup = driver.find_element_by_css_selector('.ui.small.primary.button')
    close_setup.click()
