import time


def test_report_setup(driver):
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    # select_reports_dropdown = self.driver.find_element_by_xpath('//div[contains(@class,"text") and '
    #                                                             'contains(text(), "Reports")]')
    select_reports_dropdown = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div/div[1]')
    select_reports_dropdown.click()
    time.sleep(2)
    select_report_setup = driver.find_element_by_xpath('//span[contains(@class, "text") and '
                                                            'contains(text(),"Report Setup")]')
    select_report_setup.click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)
    select_template_for_the_budget = driver.find_element_by_xpath('//span[contains(text(), '
                                                                       '"Templates for this Budget")]')
    select_template_for_the_budget.click()
    time.sleep(1)
    new_report_template = driver.find_element_by_xpath('//span[contains(@class,"text") and '
                                                            'contains(text(),"New Report Template")]')
    new_report_template.click()
    time.sleep(1)
    vert_lines_dropdown = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[7]/div[2]/i')
    # vert_lines_dropdown = self.driver.find_element_by_xpath('//i[contains(@class, "dropdown icon")]')
    vert_lines_dropdown.click()
    time.sleep(2)
    vert_lines_on = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[7]/div[2]/div/div[1]/span')
    vert_lines_on.click()
    time.sleep(2)
    font_size = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[6]/div[2]')
    font_size.click()
    time.sleep(1)
    select_font_size_10 = driver.find_element_by_xpath('//span[contains(text(), "10 pt")]')
    select_font_size_10.click()
    time.sleep(2)
    font_size.click()
    time.sleep(2)
    select_font_size_6 = driver.find_element_by_xpath('//span[contains(text(), "6 pt")]')
    select_font_size_6.click()
    time.sleep(1)
    select_orientation = driver.find_element_by_xpath('//span[contains(text(), "Portrait")]')
    select_orientation.click()
    select_landscape_orientation = driver.find_element_by_xpath('//span[contains(@class, "text") and '
                                                                     'contains(text(), "Landscape")]')
    select_landscape_orientation.click()
    time.sleep(1)
    report_shading = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[4]/div[2]')
    report_shading.click()
    time.sleep(1)
    select_report_shading = driver.find_element_by_xpath('//span[contains(@class, "text") and '
                                                              'contains(text(), "Off")]')
    select_report_shading.click()
    time.sleep(1)
    group_color = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[3]/div[2]')
    group_color.click()
    select_group_color = driver.find_element_by_xpath('//span[contains(@class, "text") and '
                                                           'contains(text(), "Color")]')
    select_group_color.click()
    time.sleep(1)
    included_sections = driver.find_element_by_xpath('//a[contains(@class, "ui basic label right-justify")]'
                                                          '//i[contains(@class,"checkmark box icon")]')
    included_sections.click()
    time.sleep(2)
    select_additional_reports_checkbox = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/'
                                                                           'div[3]/ul/li[4]/div')
    select_additional_reports_checkbox.click()
    time.sleep(2)
    select_apply_to_report = driver.find_element_by_xpath('//button[@class="ui small primary button" and '
                                                               'contains(text(),"Apply to Report")]')
    select_apply_to_report.click()
    time.sleep(2)



    select_new_template = driver.find_element_by_xpath('//span[contains(@class,"ui input") and '
                                                            'contains(text(),"NEW Untitled Print Template")]')
    select_new_template.click()
    time.sleep(1)

    close_report = driver.find_element_by_css_selector('button.ui.small.button.tertiary')
    close_report.click()
    time.sleep(1)

    # select_new_template.clear()
    # select_new_template.send_keys('temp1')
    # time.sleep(2)
    # header = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/div/div/div[3]/a[1]')
    # header.click()
    # time.sleep(1)
    # create_header = driver.find_element_by_xpath('//i[@class = "add square icon"]')
    # create_header.click()
    # time.sleep(1)
    # edit_name_header = driver.find_element_by_xpath('//i[@class = "pencil icon edit-button"]')
    # edit_name_header.click()
    # time.sleep(1)
    # # edit_header = driver.find_element_by_class_name('grid-input-cell')
    # # edit_header.clear()
    # # edit_header.send_keys('test')
    # # time.sleep(2)




    # budget_file_name_source = self.driver.find_element_by_xpath('//div[contains(@class,"options") and '
    #                                                              'contains(text(),"Budget File Name")]')
    # # destination = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[4]/div/div[2]/div/div[2]/'
    # #                                                 'div[2]/div/div/div/div/div/div/span')
    # # action = ActionChains(self.driver)
    # # action.drag_and_drop(budget_file_name_source, destination).perform()
    # # time.sleep(5)
    #
    # select_header_column = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[4]/div/div[2]/div/'
    #                                                          'div[2]/div[2]/div/div/div/div/div/div')
    # action = ActionChains(self.driver)
    # action.double_click(select_header_column)
    # action.perform()
    # time.sleep(2)
    # #select_header_cursor = self.driver.find_element_by_xpath('//span[contains(@data-offset-key,"7gofo-0-0")]')
    # select_header_cursor = self.driver.find_element_by_xpath('//span[data-offset-key="7gofo-0-0"]')
    # select_header_cursor.send_keys('test')
    # time.sleep(2)
    # action2 = ActionChains(self.driver)
    # action2.click_and_hold(budget_file_name_source).move_to_element(select_header_cursor).pause(2).\
    #     move_by_offset(20, 20).release().perform()
    # time.sleep(5)

