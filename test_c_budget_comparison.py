import pytest
import time


@pytest.mark.smoke
def test_budget_compare(driver):
    driver.switch_to.window(driver.window_handles[1])
    select_budget_compare = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[3]/button[3]')
    #select_budget_compare = driver.find_element_by_css_selector('i.caret.down.icon')
    select_budget_compare.click()
    time.sleep(2)
    #driver.implicitly_wait(5)
    search_budget = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[3]/button[3]/div/div[2]/'
                                                 'div/div/input')
    #search_budget = driver.find_element_by_css_selector(' div.content.bottom > div > div > input[type=text]')
    search_budget.click()
    time.sleep(2)
    budget_name = 'test'
    search_budget.send_keys(budget_name)
    searched_budget = driver.find_element_by_xpath(
        '//*[@id="root"]/div/div[1]/div[3]/button[3]/div/div[2]/div/'
        'div/div/div[2]/div/div[2]/span')
    # searched_budget = driver.find_element_by_css_selector('div.content.bottom > div > div > div > div.grid-body.alt > '
    #                                                       'div:nth-child(1) > div.cell.body.text.name.non-editable.read-only')
    assert budget_name in searched_budget.get_attribute('title')
    link_budget = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[3]/button[3]/div/div[2]/div/'
                                               'div/div/div[2]/div/div[6]')
    link_budget.click()
    time.sleep(2)
    search_budget.clear()
    search_budget.send_keys('Nashville')
    link_budget_2 = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[3]/button[3]/div/div[2]/div/'
                                                 'div/div/div[2]/div[2]/div[6]')
    link_budget_2.click()
    time.sleep(2)
    link_budget_3 = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[3]/button[3]/div/div[2]/div/'
                                                 'div/div/div[2]/div[3]/div[6]')
    link_budget_3.click()
    time.sleep(2)
    move_to_topsheet_from_detail = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/'
                                                                'div[1]/div/div[1]/div[1]/div[1]')
    move_to_topsheet_from_detail.click()
    budget_a_column = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/'
                                                   'div[2]/div/div[1]/div[4]')
    assert 'total_a' in budget_a_column.get_attribute("class")
    # budget_this_column = self.driver.find_element_by_xpath()
    budget_b_column = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/'
                                                   'div[2]/div/div[1]/div[5]')
    assert 'total_b' in budget_b_column.get_attribute("class")
    budget_c_column = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/'
                                                   'div[2]/div/div[1]/div[6]')
    assert 'total_c' in budget_c_column.get_attribute("class")
    budget_column_4 = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/'
                                                   'div[2]/div/div[1]/div[7]')
    assert 'total_compared_budgets' in budget_column_4.get_attribute("class")
    budget_column_5 = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/'
                                                   'div[2]/div/div[1]/div[8]')
    assert 'average_compared_budgets' in budget_column_5.get_attribute("class")
    budget_column_6 = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/'
                                                   'div[2]/div/div[1]/div[9]')
    assert 'total_d' in budget_column_6.get_attribute("class")
    budget_column_7 = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/'
                                                   'div[2]/div/div[1]/div[10]')
    assert 'var' in budget_column_7.get_attribute("class")
    budget_column_8 = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/'
                                                   'div[2]/div/div[1]/div[11]')
    assert 'percent' in budget_column_8.get_attribute("class")
    select_reports = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div/div[1]')
    select_reports.click()
    time.sleep(2)
    budget_comparison_report = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div/'
                                                            'div[2]/div[4]')
    budget_comparison_report.click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    comparison_sheet = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/span')
    assert comparison_sheet.text == 'Quick Report: Budget Comparison'
    time.sleep(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    select_budget_compare.click()
    time.sleep(2)
    link_budget_3.click()
    time.sleep(2)
    link_budget_2.click()
    time.sleep(2)
    link_budget.click()
    time.sleep(2)
