import time
from selenium.webdriver.common.action_chains import ActionChains
import lib.config as config


def test_budget_share(driver):
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
   # share_budget = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/button[2]')
    share_budget = driver.find_element_by_xpath('//button[@class = "ui button" and contains(text(),"Send")]')
    share_budget.click()
    # self.driver.implicitly_wait(10)
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    add_recipient = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[1]/a[1]')
    add_recipient.click()
    time.sleep(5)
    select_recipient_field = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[2]/div/div[2]/'
                                                               'div/div[1]')
    action = ActionChains(driver)
    action.double_click(select_recipient_field)
    action.perform()
    edit_email_field = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div/'
                                                         'div[1]/input')
    edit_email_field.send_keys(config.email_id)
    time.sleep(5)
    name_recipient_field = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[2]/div/div[2]/'
                                                             'div/div[2]')
    action = ActionChains(driver)
    action.double_click(name_recipient_field)
    action.perform()
    # assert self.driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[2]/div/div[2]/'
    #                                          'div/div/div[2]/span').text == 'vinaya.parvatikar@accionlabs.com'
    send_tab = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div/div[5]/button')
    send_tab.click()
    time.sleep(2)
    delete_recipient = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[1]/a[2]')
    delete_recipient.click()
    time.sleep(2)
    delete_tab = driver.find_element_by_xpath('/html/body/div[5]/div/div[3]/button[1]')
    delete_tab.click()
    time.sleep(2)
    close_share_window = driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div/button')
    close_share_window.click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
