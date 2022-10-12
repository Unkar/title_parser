from concurrent import futures
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import config
import time
import datetime as dt
from concurrent.futures import ThreadPoolExecutor, wait
from source import get_driver, connect_to_page, parse_page, write_to_file


def add_to_log(log, file_path):
    with open(file_path, "a") as f:
        f.write(log)



def run_process(start_page, end_page, file_path):
    wait_time = 2
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    for i in range(start_page, end_page):
        file_path = f"{config.PATH_LOG}log_{start_page}-{end_page}.csv"
        driver.get(config.URL + str(i))
        if connect_to_page(driver, i, wait_time):
            output_dict = parse_page(driver, i)
            write_to_file(output_dict, file_path)
        # try:
        #     WebDriverWait(driver, wait_time).until(
        #         lambda driver: driver.find_element(By.CLASS_NAME, "CenterTitle")
        #         )
        #     print(f"""D{driver_count} : {str(i)} - {driver.find_element(By.CLASS_NAME, "CenterTitle").text}""")
        #     #add_to_log(f"""D{driver_count};{str(i)};{config.URL + str(i)};{driver.find_element(By.CLASS_NAME, "CenterTitle").text}\n""", file_path)
        # except:
        #     print(f"D{driver_count} : {str(i)} - Empty")
        #     #add_to_log(f"""D{driver_count};{str(i)};{config.URL + str(i)};Empty\n""", file_path)
    driver.quit()


def main():
    start_time = dt.datetime.now()
    begin_page = int(input("Введите стартовую страницу: "))
    page_step = 10
    step_numbers = int(input(f"Введите количество шагов по {page_step} страниц: "))
    stop_page = begin_page + page_step*step_numbers
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(run_process, i, i + page_step, f"{config.PATH_LOG}log_{i}-{i + page_step}.csv", (i - begin_page)//page_step) for i in range(begin_page, stop_page, page_step)]
        wait(futures)
    end_time = dt.datetime.now()
    print(f"Time taken: {end_time - start_time}")


if __name__ == "__main__":
    main()


# driver.get("https://forms.trimble.com/globalTRLTAB.aspx?nav=Collection-131398")
# filename = "ScanResults.png"
# element = driver.find_element(By.CLASS_NAME, "CenterTitle")
# print(element.text)
# driver.quit()
