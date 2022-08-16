import os
import time

from Scraper import scrape_all

def run():

    start = time.time()
    scrape_all()
    print (time.time() - start)


if __name__ == "__main__":
    run()