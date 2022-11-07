import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


PATH = "vk23-9sek.htm"


def get_dataframe(PATH):
    with open(PATH, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    tables = soup.find_all("table")
    table = tables[1]
    rows = table.find_all("tr")
    data = []
    for row in rows:
        cols = row.find_all("td")
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    return pd.DataFrame(data)








