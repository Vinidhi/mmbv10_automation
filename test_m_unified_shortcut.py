import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller



def test_create_shortcut(driver, drilling_down_from_topsheet_to_detail, enabling_disabling_columns):
    shortcut_tool = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/div/div/'
                                                      'div[4]/div/div/div[1]/a[5]')
    shortcut_tool.click()
    time.sleep(2)
    new_shortcut = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/div/div/'
                                                     'div[4]/div/div/div[2]/div/div[1]/button')
    new_shortcut.click()
    time.sleep(2)
    next_tab = driver.find_element_by_xpath('/html/body/div[11]/div/div[3]/button[2]')
    next_tab.click()
    time.sleep(2)
    create_shortcut_tab = driver.find_element_by_xpath('/html/body/div[11]/div/div[3]/button[3]')
    create_shortcut_tab.click()
    time.sleep(4)
    created_shortcut = driver.find_element_by_xpath('//span[contains(@class,"ellip no-select pre-span") '
                                                         'and contains(text(),"SHORTCUT 1")]')
    assert created_shortcut.text == 'SHORTCUT 1'
    select_row = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/'
                                                   'div[2]/div[1]/div[1]')
    select_row.click()
    time.sleep(2)
    select_row_detail = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/'
                                                          'div[2]/div/div[2]/div[5]/div[1]')
    select_row_detail.click()
    shortcut_tool.click()
    time.sleep(4)

    select_shortcut_1 = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/div/div/'
                                                          'div[4]/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/'
                                                          'span')
    select_shortcut_1.click()
    time.sleep(2)
    select_action_add = driver.find_element_by_xpath('//button[text()="Add"]')
    select_action_add.click()
    time.sleep(2)
    action = ActionChains(driver)
    action.double_click(created_shortcut)
    action.perform()
    edit_shortcut_1_field = driver.find_element_by_class_name('grid-input-cell')
    edit_shortcut_1_field.clear()
    time.sleep(2)

    edit_shortcut_1_field.send_keys("test_SH1")
    driver.implicitly_wait(10)
    edit_shortcut_1_field.send_keys(Keys.TAB)
    time.sleep(2)
    select_row_detail = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/'
                                                          'div[2]/div/div[2]/div[8]/div[1]')
    select_row_detail.click()
    time.sleep(4)

    shortcut_tool.click()
    time.sleep(2)
    select_shortcut_1 = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/div/div/'
                                                          'div[4]/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/'
                                                          'span')
    select_shortcut_1.click()
    time.sleep(2)
    select_action_replace = driver.find_element_by_xpath('//button[text()="Replace"]')
    select_action_replace.click()
    time.sleep(2)


    shortcut_hotkey = driver.find_element_by_xpath('//div[contains(@class,"cell body custom magic_key")]'
                                                        '//i[@class="caret down icon magic-popup-handler"]')
    shortcut_hotkey.click()
    time.sleep(2)
    select_key_1 = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/div/div/div[4]'
                                                     '/div/div/div[2]/div/div[1]/div[3]/ul[2]/li[1]')
    select_key_1.click()
    time.sleep(3)

    select_row_detail_to_apply_sh = driver.find_element_by_xpath('//div[contains(@class,"cell body index")]'
                                                                      '//span[contains(@class,"no-select") and '
                                                                      'contains(text(),"11")]')
    select_row_detail_to_apply_sh.click()
    time.sleep(2)
    keyboard = Controller()
    keyboard.press(Key.alt)
    keyboard.press(Key.ctrl)
    keyboard.press('1')
    keyboard.release('1')
    keyboard.release(Key.ctrl)
    keyboard.release(Key.alt)
    time.sleep(4)

    shortcuts_setup = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/div/div/'
                                                        'div[4]/div/div/div[2]/div/div[1]/div[2]')
    shortcuts_setup.click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    listed_shortcut = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[1]/div/div/'
                                                        'div/div[2]/div[2]/div/div[2]/div/div/span')
    assert listed_shortcut.text == "test_SH1"
    delete_shortcut = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[1]/div/div/'
                                                        'div/div[2]/div[2]/div/div[1]/a')
    delete_shortcut.click()
    time.sleep(2)
    close_shortcut_setup = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/button')
    close_shortcut_setup.click()
    time.sleep(2)

def test_shortcut_type_create_new_row(driver):
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    select_row = driver.find_element_by_xpath('//span[@class = "no-select" and contains(text(),"4")]')
    select_row.click()
    shortcut_tool = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/div/div/'
                                                       'div[4]/div/div/div[1]/a[5]')
    shortcut_tool.click()
    time.sleep(2)
    new_shortcut = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/div/div/'
                                                          'div[4]/div/div/div[2]/div/div[1]/button')
    new_shortcut.click()
    time.sleep(2)
    select_shortcut_type = driver.find_element_by_xpath('//span[contains(text(),"Create New Row(s)")]')
    select_shortcut_type.click()
    time.sleep(2)
    next_tab = driver.find_element_by_xpath('/html/body/div[11]/div/div[3]/button[2]')
    next_tab.click()
    time.sleep(2)
    create_shortcut_tab = driver.find_element_by_xpath('/html/body/div[11]/div/div[3]/button[3]')
    create_shortcut_tab.click()
    time.sleep(4)
    created_shortcut = driver.find_element_by_xpath('//span[contains(@class,"ellip no-select pre-span") '
                                                         'and contains(text(),"SHORTCUT 1")]')
    assert created_shortcut.text == 'SHORTCUT 1'
    select_row = driver.find_element_by_xpath('//span[@class = "no-select" and contains(text(),"1")]')
    select_row.click()
    time.sleep(1)
    shortcut_tool.click()
    time.sleep(2)
    #insert_shortcut_1 = self.driver.find_element_by_xpath('//button[contains(text(),"Insert")]')
    insert_shortcut_1 = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/div/div/'
                                                          'div[4]/div/div/div[2]/div/div[2]/div/div[2]/div/div[4]')
    insert_shortcut_1.click()
    time.sleep(2)
    shortcut_hotkey = driver.find_element_by_xpath('//div[contains(@class,"cell body custom magic_key")]'
                                                             '//i[@class="caret down icon magic-popup-handler"]')
    #     # # shortcut_hotkey = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/div/div/'
    #     # #                                                     'div[4]/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]')
    shortcut_hotkey.click()
    time.sleep(2)
    select_key_2 = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/div/div/div[4]'
                                                     '/div/div/div[2]/div/div[1]/div[2]/ul[2]/li[2]')
    select_key_2.click()
    time.sleep(2)
    select_row_detail_to_apply_sh = driver.find_element_by_xpath('//div[contains(@class,"cell body index")]'
                                                                          '//span[contains(@class,"no-select") and '
                                                                           'contains(text(),"11")]')
    select_row_detail_to_apply_sh.click()
    time.sleep(4)
    keyboard = Controller()
    keyboard.press(Key.alt)
    keyboard.press(Key.ctrl)
    keyboard.press('2')
    keyboard.release('2')
    keyboard.release(Key.ctrl)
    keyboard.release(Key.alt)
    # self.driver.implicitly_wait(5)
    time.sleep(4)

    shortcuts_setup = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/div/div/'
                                                        'div[4]/div/div/div[2]/div/div[1]/div[2]')
    shortcuts_setup.click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    listed_shortcut = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[1]/div/div/'
                                                        'div/div[2]/div[2]/div/div[2]/div/div/span')
    assert listed_shortcut.text == "SHORTCUT 1"
    delete_shortcut = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[1]/div/div/'
                                                        'div/div[2]/div[2]/div/div[1]/a')
    delete_shortcut.click()
    time.sleep(2)
    close_shortcut_setup = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/button')
    close_shortcut_setup.click()
    time.sleep(2)
    