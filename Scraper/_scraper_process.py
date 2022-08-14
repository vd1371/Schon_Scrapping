import os

from ._get_html_page_of_stocks_per_date import _get_html_page_of_stocks_per_date
from ._parse_table_to_df import _parse_table_to_df
from ._get_dates_for_scraping import _get_dates_for_scraping
from ._get_a_driver import _get_a_driver

def _scrape_process(stocks, worker_number):

    dates = _get_dates_for_scraping()
    driver = _get_a_driver()
    
    for j, stock_id in enumerate(stocks['stock_id']):

        print (f"Worker {worker_number} is about to work on {j}/{len(stocks)}")

        base_dir = os.path.join("Database", f"StockID-{stock_id}")
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)

        for date_string in dates:
            
            df_dir = os.path.join(
                    base_dir,
                    f"Stock-{stock_id}-{date_string.replace('/', '')}.csv"
                )

            if not os.path.exists(df_dir):

                page_html = _get_html_page_of_stocks_per_date(
                    driver,
                    stock_id,
                    date_string
                )
                df = _parse_table_to_df(page_html, stock_id, date_string)

                df.to_csv(df_dir, index= False)