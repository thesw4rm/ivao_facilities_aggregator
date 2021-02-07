from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pprint import pprint
from bs4 import BeautifulSoup
import json
import time

with open("config.json", "r") as cred_file:
    creds = json.load(cred_file)


driver = webdriver.Firefox(firefox_binary="/usr/bin/firefox-developer-edition")
driver.get("https://ivao.aero/fras/list.asp?id=" + creds["region"].upper())
driver.find_elements_by_class_name("cc_b_ok")[0].click()

## Logging in
vid_input = driver.find_element_by_id("loginVID")
vid_input.send_keys(creds["user"])

pass_input = driver.find_element_by_id("ctl00_ContentPlaceHolder1_loginPassword")
pass_input.send_keys(creds["pass"])

login_btn = driver.find_element_by_id("ctl00_ContentPlaceHolder1_loginBtn")
login_btn.click()

time.sleep(3)  # Give time to load the ratings initially.

## Extracting rating requirements


def extract_entry_num_info(info_str):
    parts = info_str.split(" ")
    return [
        int(parts[1].replace(",", "")),
        int(parts[3].replace(",", "")),
        int(parts[5].replace(",", "")),
    ]


def extract_row(row_data):
    return {
        "airport": row_data[0].text,
        "start_time": row_data[1].text,
        "end_time": row_data[2].text,
        "days": [row_data[x].text for x in range(3, 10)],
        "date": row_data[10].text,
        "rating_num": row_data[11]
        .select_one("img")["src"]
        .split("/")[-1]
        .replace(".gif", ""),
    }


# entry_num_info_str = Showing X out of XX of XXX entries
entry_num_info_str = driver.find_element_by_id("frasTable_info").text


start_entry, end_entry, max_entries = extract_entry_num_info(entry_num_info_str)

data = {creds["region"].lower(): []}
while end_entry < max_entries:
    page = BeautifulSoup(driver.page_source, "html.parser")
    for aport_row in (
        page.select_one("table#frasTable").select_one("tbody").find_all("tr")
    ):
        data["xa"].append(extract_row(aport_row.find_all("td")))
    driver.find_element_by_id("frasTable_next").click()

    # entry_num_info_str = Showing X out of XX of XXX entries
    entry_num_info_str = driver.find_element_by_id("frasTable_info").text
    start_entry, end_entry, max_entries = extract_entry_num_info(entry_num_info_str)
    time.sleep(0.5)


with open("ext_data.json", "w") as w:
    json.dump(data, w, indent=8)
driver.close()
