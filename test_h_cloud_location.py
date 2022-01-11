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
    # field_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    edit_field.send_keys(input)
    time.sleep(2)
    edit_field.send_keys(Keys.TAB)
    time.sleep(2)

def test_cloud_setup_location(driver):
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(3)
    # select_locations_setup = driver.find_element_by_xpath('//span[contains(@class,"tools-alt") and '
    #                                                            'contains(text(),"locations")]')
    select_locations_setup = driver.find_element_by_css_selector('div.actions.tools-setup > button:nth-child(1) >'
                                                                 ' span.tools-alt')
    select_locations_setup.click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    location_budget_highlighted = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/'
                                                                    'div[4]/div/div[2]/div[2]/div[1]/div[3]')
    location = location_budget_highlighted.text
    select_upload_to_cloud = driver.find_element_by_xpath('//a[@class="ui basic label"]'
                                                               '//i[@class="sign-in horizontally flipped icon"]')
    select_upload_to_cloud.click()
    time.sleep(2)
    upload_continue_button = driver.find_element_by_xpath('//button[text()="Copy & continue"]')
    upload_continue_button.click()
    time.sleep(2)
    select_cloud_library = driver.find_element_by_xpath('//span[contains(text(),"Library")]')
    select_cloud_library.click()
    time.sleep(2)
    location_moved_to_cloud = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]'
                                                                '/div/div[2]/div[2]/div/div[2]')
    location_moved_to_cloud.click()
    assert location_moved_to_cloud.text == location
    add_category_cloud_location = driver.find_element_by_xpath('//a[@class="ui basic label"]'
                                                                    '//i[@class="add square icon"]')
    add_category_cloud_location.click()
    time.sleep(2)
    select_added_category = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[1]'
                                                              '/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]')
    select_added_category.click()
    time.sleep(2)
    category_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    edit_field(driver, select_added_category, category_string)
    # time.sleep(2)
    add_cloud_location = driver.find_element_by_xpath('//a[contains(@class,"ui basic label") and '
                                                           'contains(text(),"Add Location")]'
                                                           '//i[@class="add square icon"]')
    add_cloud_location.click()
    time.sleep(2)
    cloud_location_field = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/'
                                                             'div[2]/div[2]/div/div[2]')
    cloud_location_field.click()
    time.sleep(1)
    location_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    edit_field(driver, cloud_location_field, location_string)
    time.sleep(1)
    # cloud_location_field.send_keys(Keys.TAB)
    cloud_location_city_field = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]'
                                                                  '/div/div[2]/div[2]/div/div[3]')
    cloud_location_city_field.click()
    time.sleep(1)
    city_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    edit_field(driver, cloud_location_city_field, city_string)
    time.sleep(1)
    # cloud_location_city_field.send_keys(Keys.TAB)
    cloud_location_state_field = driver.find_element_by_xpath(
        '//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]'
        '/div/div[2]/div[2]/div/div[4]')
    cloud_location_state_field.click()
    time.sleep(1)
    state_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    edit_field(driver, cloud_location_state_field, state_string)
    time.sleep(1)
    cloud_location_country_field = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/'
                                                                     'div[4]/div/div[2]/div[2]/div/div[5]')
    cloud_location_country_field.click()
    time.sleep(1)
    # country_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    # self.edit_field(cloud_location_country_field, country_string)
    # time.sleep(1)

    # move_to_category_dropdown_icon = self.driver.find_element_by_xpath('//span[contains(text(),"MOVE TO CATEGORY")]'
    #                                                                     '//i[@class="sign-in horizontally flipped icon"]')
    move_to_category_dropdown_icon = driver.find_element_by_xpath('//div[contains(@class,"ui inline dropdown '
                                                                       'move-to-category dropdown-action")]'
                                                                       '//i[contains(@class,"dropdown icon")]')
    move_to_category_dropdown_icon.click()
    time.sleep(2)
    # select_uncategorized_from_dropdown = self.driver.find_element_by_xpath('//div[contains(@class,"item")]'
    #                                                                        '//span[contains(text(),"Uncategorized")]')
    select_uncategorized_from_dropdown = driver.find_element_by_xpath(
        '//div[contains(@class,"scrolling menu transition")]'
        '//div[contains(@class,"item")]//span[contains(text(),'
        '"Uncategorized")]')
    select_uncategorized_from_dropdown.click()
    time.sleep(2)
    category_uncategorized = driver.find_element_by_xpath('//span[contains(@class,"ellip no-select pre-span") '
                                                               'and contains(text(), "Uncategorized")]')
    category_uncategorized.click()
    location_moved_uncategorized = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/'
                                                                     'div[4]/div/div[2]/div[2]/div[1]/div[2]')
    assert location_moved_uncategorized.text == location_string
    time.sleep(2)
    # download_budget = self.driver.find_element_by_xpath('//a[contains(@class,"ui basic label") and '
    #                                                      '(text(),"Download to Budget")]'
    #                                                      '//i[contains(@class,"download icon")]')
    download_budget = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/'
                                                        'div[1]/div/a[3]/i')
    download_budget.click()
    time.sleep(2)
    continue_download = driver.find_element_by_xpath('//button[text()="Copy & continue"]')
    continue_download.click()
    time.sleep(2)
    # switch_to_budget_library = self.driver.find_element_by_xpath('//span[contains(@class,"budget-library active") '
    #                                                              'and contains(text(),"Budget")]')
    switch_to_budget_library = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[1]/'
                                                                 'div/div[1]/span[2]')
    switch_to_budget_library.click()
    time.sleep(2)
    location_downloaded = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/'
                                                            'div[2]/div[2]/div[2]/div[3]')
    assert location_downloaded.text == location_string
    time.sleep(1)
    select_dowloaded_location = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/'
                                                             'div[2]/div[2]/div[2]/div[1]')
    select_dowloaded_location.click()
    time.sleep(2)
    delete_downloaded_loc = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[1]/'
                                                         'div/a[2]')
    delete_downloaded_loc.click()
    time.sleep(2)
    # select_delete = driver.find_element_by_xpath('//button[@class = "ui basic button" and contains(text(),"Delete")]')
    # select_delete.click()
    # time.sleep(2)
    select_cloud_library.click()
    time.sleep(2)
    delete_location = driver.find_element_by_xpath('//a[contains(@class,"ui basic label") and contains(text(),'
                                                        '"Delete Location")]//i[@class="trash alternate icon"]')
    delete_location.click()
    time.sleep(2)
    select_category_be_deleted = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/'
                                                                   'div[1]/div/div[2]/div/div[2]/div[2]/div/'
                                                                   'div[2]/div[2]')
    select_category_be_deleted.click()
    time.sleep(2)
    delete_selected_category = driver.find_element_by_xpath('//a[contains(@class,"ui basic label") and '
                                                                 'contains(text(), "Delete") ]'
                                                                 '//i[contains(@class,"trash alternate icon")]')
    delete_selected_category.click()
    time.sleep(2)
    select_lib_loc = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[2]/div[2]/'
                                                  'div/div[2]')
    select_lib_loc.click()
    time.sleep(2)
    delete_lib_loc = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[1]/div/a[2]')
    delete_lib_loc.click()
    time.sleep(2)

    close_setup = driver.find_element_by_xpath('//button[contains(@class,"ui small primary button") '
                                                    'and contains(text(), "Close")]')
    close_setup.click()
    time.sleep(2)