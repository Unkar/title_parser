from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
from bs4 import BeautifulSoup


import config

# Функция включения и настройки драйвера


def get_driver(headless=True):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--log-level=OFF")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("--silent")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

# Функция проверки наличия элемента на странице. Элемент является маркером, что ссылка не битая.


def connect_to_page(driver, page_number, wait_time=2):
    driver.get(config.URL + str(page_number))
    # connection_attempts = 0
    # while connection_attempts < 3:
    try:
        WebDriverWait(driver, wait_time).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "CenterTitle"))
        )
        return True
    except Exception as e:
        # print(e)
        # connection_attempts += 1
        #print(f"Error connecting to {config.URL + page_number}.")
        # print(f"Attempt #{connection_attempts}.")
        return False

# Функция парсинга страницы. Парсим сначала маркер не пустой страницы attrs={"class": "CenterTitle"}. Затем парсим текст первой ссылки.


def parse_page(driver, page_number):
    soup = BeautifulSoup(driver.page_source, "html.parser")
    output_dict = {}
    title = soup.find(attrs={"class": "CenterTitle"}).text
    if title == "":
        title = "Empty"
    links = soup.find_all(attrs={"class": "CenterLink"})
    for link in links:
        if link.text == "":
            link_text = "Empty"
        else:
            link_text = link.text
            break
    output_dict["id"] = page_number
    output_dict["url"] = config.URL + str(page_number)
    output_dict["title"] = title
    output_dict['link'] = link_text
    return output_dict

# def write_to_file(output_dict, filename):
#     with open(filename, "a") as csvfile:
#         fieldnames = ["id", "url", "title"]
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writerow(output_dict)

# Функция записи в файл. Передаем словарь с данными и имя файла.

 
def write_to_file(output_dict, filename):
    with open(filename, "a") as file:
        file.write(f"{output_dict['id']};{output_dict['url']};{output_dict['title']};{output_dict['link']}\n")
