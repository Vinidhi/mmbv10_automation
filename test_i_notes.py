import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def add_open_reply_new_edit_delete_note(driver):
    edit_note = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/div/div/div[4]/'
                                                  'div/div/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div/textarea')
    edit_note.send_keys("TEST_NOTE")
    time.sleep(1)
    # self.driver.switch_to.active_element.click()
    save_note = driver.find_element_by_css_selector('.ui.small.primary.button')
    save_note.click()
    # save_note = self.driver.find_element_by_xpath('/*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/div/div/div[4]/'
    #                                              'div/div/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div/div/'
    #                                              'button[2]')
    # save_note.click()
    time.sleep(1)
    select_loc_tools = driver.find_element_by_xpath('//a[@class="item locations"and contains(text(), "Loc")]')
    select_loc_tools.click()
    time.sleep(4)
    icon_note = driver.find_element_by_xpath('//i[contains(@class,"sticky note icon grid-cell-icon")]')
    icon_note.click()
    time.sleep(2)
    notes = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/div/div/div[4]/'
                                              'div/div/div[1]/a[4]')
    assert 'active item notes' in notes.get_attribute("class")

    new_note = driver.find_element_by_xpath('//button[@class = "ui small primary button" and '
                                                       'contains(text(), "New Note")]')
    new_note.click()
    time.sleep(2)
    add_new_note = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/div/div/div[4]'
                                                     '/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div/'
                                                     'textarea')
    add_new_note.send_keys("TEST_NEW_NOTE")
    time.sleep(1)
    # self.driver.switch_to.active_element.click()
    save_note = driver.find_element_by_css_selector('.ui.small.primary.button')
    save_note.click()

    reply_note = driver.find_element_by_xpath('//i[contains(@class,"reply all icon")]')
    reply_note.click()
    time.sleep(2)
    add_reply_note = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/div/div/'
                                                       'div[4]/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/'
                                                       'div/textarea')
    add_reply_note.send_keys("Re_note")
    time.sleep(2)
    save_note = driver.find_element_by_css_selector('.ui.small.primary.button')
    save_note.click()
    time.sleep(2)
    edit_reply_note = driver.find_element_by_xpath('//i[contains(@class,"pencil alternate icon")]')
    edit_reply_note.click()
    time.sleep(2)
    add_edit_reply_note = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/div/'
                                                            'div/div[4]/div/div/div[2]/div/div[2]/div[2]/div[2]/div/'
                                                            'div[2]/div/textarea')
    add_edit_reply_note.clear()
    time.sleep(1)

    add_edit_reply_note.send_keys("editing Re_note")
    time.sleep(2)
    save_edit_note = driver.find_element_by_xpath('//button[@class = "ui small primary button" and '
                                                       'contains(text(), "Save Note")]')
    save_edit_note.click()
    time.sleep(2)
    delete_reply_note = driver.find_element_by_xpath('//i[@class = "trash alternate icon"]')
    delete_reply_note.click()
    time.sleep(2)
    delete_note = driver.find_element_by_xpath('//i[@class = "trash alternate icon"]')
    delete_note.click()
    time.sleep(2)

def test_add_note_topsheet(driver):
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    action = ActionChains(driver)
    right_click_row = driver.find_element_by_xpath('//span[@class = "no-select" and contains(text(),"1")]')
    action.context_click(right_click_row)
    action.perform()
    time.sleep(1)
    add_note = driver.find_element_by_xpath('//span[contains(text(),"Add Note")]')
    add_note.click()
    time.sleep(1)
    add_open_reply_new_edit_delete_note(driver)

def test_add_note_account(driver):
    action = ActionChains(driver)
    select_row = driver.find_element_by_xpath('//span[@class = "no-select" and contains(text(),"1")]')
    action.double_click(select_row)
    action.perform()
    time.sleep(2)
    # Open Notes
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).key_down(Keys.SHIFT).key_down(Keys.SPACE).key_up(Keys.SPACE).key_up(Keys.SHIFT). \
        key_up(Keys.CONTROL).perform()
    action.send_keys()
    time.sleep(2)
    add_open_reply_new_edit_delete_note(driver)

def test_add_note_detail(driver):
    action = ActionChains(driver)
    select_row = driver.find_element_by_xpath('//span[@class = "no-select" and contains(text(),"1")]')
    action.double_click(select_row)
    action.perform()
    time.sleep(2)
    # Open Notes
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).key_down(Keys.SHIFT).key_down(Keys.SPACE).key_up(Keys.SPACE).key_up(Keys.SHIFT). \
        key_up(Keys.CONTROL).perform()
    action.send_keys()
    time.sleep(2)
    add_open_reply_new_edit_delete_note(driver)

