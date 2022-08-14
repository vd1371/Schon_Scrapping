import pandas as pd
from bs4 import BeautifulSoup

def _parse_table_to_df(page_html, stock_code, date_string):

    page_html = BeautifulSoup(page_html, "html.parser")

    table = page_html.find('div', {'class': 'table-scroller'})

    holder = []
    for i, row in enumerate(table.find_all("tr")):

        if i > 0:
            cols = row.find_all('td')

            row_values = []
            for ele in cols:
                val = ele.text.strip().split(":\n")

                if len(val) == 2:
                    row_values.append(val[1])
                else:
                    row_values.append(None)

            holder.append(row_values)

    column_names = [
        "Participant ID",
        "Name",
        "Address",
        "Shareholding",
        "percentage"]

    df = pd.DataFrame(holder, columns = column_names)
    df['percentage'] = df['percentage'].str.replace("%", "").astype(float)
    df['Shareholding'] = df['Shareholding'].str.replace(",", "").astype('int64')
    df['Date'] = date_string
    df['Stockcode'] = stock_code
    df['Stockcode'] = df['Stockcode'].astype('str')

    return df