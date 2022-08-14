from selenium.webdriver.common.by import By

def _get_html_page_of_stocks_per_date(driver, stock_code, date):

    inputElement = driver.find_element(By.ID, "txtShareholdingDate")
    inputElement.send_keys(date)

    inputElement = driver.find_element(By.ID, "txtStockCode")
    inputElement.send_keys(stock_code)

    driver.find_element(By.ID, "btnSearch").click()

    return driver.page_source