import multiprocessing as mp
from multiprocessing import Process
from turtle import st

from ._save_list_of_all_stocks_to_csv import _save_list_of_all_stocks_to_csv
from ._scraper_process import _scrape_process

def scrape_all():

    stocks = _save_list_of_all_stocks_to_csv()

    n_cores = mp.cpu_count() - 1
    n_cores = 3
    len_batches = int(len(stocks)/n_cores) + 1
    
    workers = []
    for i in range(n_cores):
        stocks_slice = stocks.iloc[i*len_batches: min((i+1)*len_batches, len(stocks)), :]
        
        worker = Process(target= _scrape_process, args = (stocks_slice, i,))
        workers.append(worker)
        worker.start()

    print ("Workers started...")

    for worker in workers:
        worker.join()

    print ("Workers joined")