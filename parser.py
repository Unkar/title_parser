from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import config


def add_to_log(log):
    with open(config.PATH_LOG, "a") as f:
        f.write(log)



def main():
    wait_time = 2
    start_page = 100086
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(wait_time)
    for i in range(start_page, start_page + 7):
        driver.get(config.URL + str(i))
        try:
            WebDriverWait(driver, wait_time).until(
                lambda driver: driver.find_element(By.CLASS_NAME, "CenterTitle")
                )
            print(str(i) + " - " + driver.find_element(By.CLASS_NAME, "CenterTitle").text)
            add_to_log(config.URL + str(i) + " - " + driver.find_element(By.CLASS_NAME, "CenterTitle").text + '\n')
        except:
            print(str(i) + " -  None")
            # add_to_log(config.URL + str(i) + " -  None"+"\n")
    driver.quit()


if __name__ == "__main__":
    main()


# driver.get("https://forms.trimble.com/globalTRLTAB.aspx?nav=Collection-131398")
# filename = "ScanResults.png"
# element = driver.find_element(By.CLASS_NAME, "CenterTitle")
# print(element.text)
# driver.quit()
