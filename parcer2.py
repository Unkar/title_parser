import sys
from concurrent.futures import ThreadPoolExecutor, wait
from time import sleep, time
from datetime import datetime

from source import get_driver, connect_to_page, parse_page, write_to_file
import config


def run_process(page_number, filename):
    driver = get_driver()
    if connect_to_page(driver, page_number):
        # sleep(2)
        output_dict = parse_page(driver, page_number)
        write_to_file(output_dict, filename)
        time1 = time()
        print(f"Page {page_number} done, time: {time1}")
        driver.quit()
        time2 = time()
        print(f"Page {page_number} quit, time: {time2}")
    else:
        print(f"Error connecting to {config.URL + str(page_number)}")
        driver.quit()


def do_a_part(start_page, end_page):
    start_time = time()
    filename = f"log_{start_page}-{end_page}.csv"
    futures = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(run_process, page_number, filename)
                   for page_number in range(start_page, end_page)]
    wait(futures, timeout=2)
    end_time = time()
    print(f"Time start: {datetime.fromtimestamp(start_time).strftime('%H:%M:%S')}, time end: {datetime.fromtimestamp(end_time).strftime('%H:%M:%S')}, time spent: {end_time - start_time}")
    return


def main():
    start_page = int(input("Введите стартовую страницу: "))
    page_step = 500
    step_numbers = int(input(f"Введите количество шагов по {page_step} страниц: "))
    end_page = start_page + page_step*step_numbers
    for i in range(start_page, end_page, page_step):
        do_a_part(i, i + page_step)
        print(f"Done {i} - {i + page_step}")


if __name__ == "__main__":
    time_run = time()
    main()
    time_stop = time()
    print(f"Time run^ {datetime.fromtimestamp(time_run).strftime('%H:%M:%S')}, time stop: {datetime.fromtimestamp(time_stop).strftime('%H:%M:%S')}, time spent: {time_stop - time_run}")
