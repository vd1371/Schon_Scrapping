from datetime import date, timedelta
import holidays

def _get_dates_for_scraping():

    def daterange(start_date, end_date):
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)

    hk_holidays = list(holidays.HongKong(years = 2022).keys())

    start_date = date(2022, 1, 1)
    end_date = date(2022, 8, 13)

    dates_for_scrapping = []

    for single_date in daterange(start_date, end_date):
        if not single_date in hk_holidays and single_date.weekday() < 5:
            dates_for_scrapping.append(single_date.strftime("%Y/%m/%d"))

    return dates_for_scrapping