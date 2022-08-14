from cmath import isnan
import os
import pandas as pd
from bs4 import BeautifulSoup

def _save_list_of_all_stocks_to_csv():

    with open ("ListofStocks.html", encoding= 'utf-8') as fp:
        page_html = BeautifulSoup(fp.read(), "html.parser")

    holder = []
    for i, row in enumerate(page_html.find_all('tr')):
        row_holder = []
        for col in row.find_all("td"):
            if col.text:
                row_holder.append(col.text)
        holder.append(row_holder)

    df = pd.DataFrame(holder, columns = ['stock_id', 'stock_name'])
    df = df[~df['stock_id'].isna()]
    df.to_csv(os.path.join("Database", "ListofStocks.csv"))

    return df