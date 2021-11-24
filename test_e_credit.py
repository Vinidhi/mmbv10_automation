import time
from selenium.webdriver.common.keys import Keys
import string
import random


def test_add_credit(driver):
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    credit_setup = driver.find_element_by_xpath('//*[text()[contains(.,"Cr")]]')
    credit_setup.click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)
    add_credit = driver.find_element_by_xpath(
        '//*[@id="root"]/div/div[1]/div[2]/div/div/div[1]/div/div/div/div[2]/div[2]/div/div[1]/a[1]')
    add_credit.click()
    time.sleep(1)
    credit_name = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[1]/'
                                                    'div[1]/div/div/input')
    credit_name.clear()
    time.sleep(1)
    credit_name_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
    credit_name.send_keys(credit_name_string)
    time.sleep(1)
    credit_name.send_keys(Keys.TAB)
    time.sleep(1)
    applied_credit_cap_number = random.choices(string.digits, k=3)
    applied_credit_cap = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/'
                                                           'div[1]/div[2]/div[1]/div/input')
    applied_credit_cap.send_keys(applied_credit_cap_number)
    time.sleep(1)
    applied_credit_cap.send_keys(Keys.TAB)
    time.sleep(1)
    discount =  driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[1]/'
                                                  'div[2]/div[2]/div/input')
    discount.send_keys('5')
    discount.send_keys(Keys.TAB)
    time.sleep(1)
    account_number = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[1]/'
                                                       'div[2]/div[3]/div/input')
    account_nuber_value = random.choices(string.digits, k=5)
    account_number.send_keys(account_nuber_value)
    time.sleep(1)
    add_row = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[2]/div/'
                                                'a[1]/i')
    add_row.click()
    time.sleep(2)
    user_name = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[3]/'
                                                  'div[2]/div/div[2]/input')
    user_name_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    user_name.send_keys(user_name_string)





        # apply_credit = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[1]/'
        #                                                  'div[1]/button')
        # apply_credit.click()
        # time.sleep(1)
        #
        # # delete_credit = self.driver.find_element_by_xpath(
        # #     '//*[@id="root"]/div/div[1]/div[2]/div/div/div[1]/div/div/div/'
        # #     'div[2]/div[2]/div/div[1]/a[2]')
        # # delete_credit.click()
        # # time.sleep(2)
        # close_credit_window = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]')
        # close_credit_window.click()
        # time.sleep(1)
