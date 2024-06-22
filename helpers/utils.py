import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://ckan.pbh.gov.br/dataset/relacao-das-pessoas-envolvidas-nos-acidentes-de-transito-com-vitima"
DOWNLOAD_URL = "https://ckan.pbh.gov.br/dataset/b127c1d8-9e1b-4820-884a-8bd8129ba5e3/resource/{}/download/{}.csv"


def get_download_ids():
    browser = webdriver.Chrome()
    browser.get(URL)

    # pega a div dos datasets
    res_list = browser.find_element(By.CLASS_NAME, 'resource-list')

    # pega todas as divs com cada um dos datasets
    res_items = res_list.find_elements(By.CLASS_NAME, "resource-item")

    # form list of iterations to link
    download_ids = []
    for item in res_items:
        head = item.find_element(By.CLASS_NAME, "heading")
        if head.get_attribute("title").startswith("si_env-"):
            download_ids.append({"id": item.get_attribute("data-id"),
                                 "title": head.get_attribute("title")})

    browser.close()
    return download_ids


def get_data(ids: list):
    data = []
    storage_options = {'User-Agent': 'Mozilla/5.0'}
    for id in ids:
        url = DOWNLOAD_URL.format(id.get("id"), id.get("title"))
        df = pd.read_csv(url, storage_options=storage_options, sep=";",
                         encoding='latin-1')
        data.append({"id": id.get("title"), "data": df})
    return data
