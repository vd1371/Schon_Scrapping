from selenium.webdriver.common.by import By

def _get_html_page_of_stocks_per_date(driver, stock_code, date):
    
    driver.execute_script(f"document.getElementById('txtShareholdingDate').value = '{date}'")

    inputElement = driver.find_element(By.ID, "txtStockCode")
    inputElement.send_keys(stock_code)

    driver.find_element(By.ID, "btnSearch").click()

    return driver.page_source