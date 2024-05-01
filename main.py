import random
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

# genrand()
print(
    '''Websites Used: \nFor goods: Amazon and Flipkart, \nFor clothing: Ajio and Myntra, \nFor meds: Pharmeasy and 1MG''')
print('''Type reference: \n1 for goods \n2 for clothing \n3 for meds ''')
typeProd = input("Enter type: ")
product = input("Enter product: ")
# custom_website = input("Enter websit")
custom_website = input("Enter company name (if available else input 0): ")

goods_sites = [
    {"url": "https://www.amazon.in/",
     "search_bar": {"type": "xpath",
                    "value": "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input", },
     "sort_dd_present": "true",
     "sort_dd": {"type": "id", "value": "a-autoid-0-announce"},
     "low_to_high": {"type": "id", "value": "s-result-sort-select_1", },
     "search_res_container": {"type": "xpath", "value": "//*[@class='s-main-slot s-result-list s-search-results "
                                                        "sg-row']", },
     "search_results": {"type": "xpath", "value": "./div", },
     "name": "Amazon",
     },
    {"url": "https://flipkart.com/",
     "search_bar": {"type": "xpath",
                    "value": "/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input"},
     "sort_dd_present": "false",
     "low_to_high": {"type": "xpath",
                     "value": "/html/body/div[1]/div/div[3]/div[1]/div[2]/div[1]/div/div/div[2]/div[3]", },
     "search_res_container": {"type": "xpath", "value": "/html/body/div[1]/div/div[3]/div[1]/div[2]", },
     "search_results": {"type": "xpath", "value": "./div", },
     "name": "Flipkart",
     },
]

clothing_sites = [
    {
        "url": "https://myntra.com/",
        "search_bar": {
            "type": "xpath",
            "value": "/html/body/div[1]/div/div/header/div[2]/div[3]/input",
        },
        "sort_dd_present": "true",
        "sort_dd_click": "false",
        "sort_dd": {
            "type": "xpath", "value": "//*[@class='sort-sortBy']",
        },
        "low_to_high": {
            "type": "xpath",
            "value": "/html/body/div[2]/div/main/div[3]/div[2]/div/div[1]/section/div[1]/div[1]/div/div/div/ul/li[6]/label",
        },
        "enter_or_search_btn": "search_btn",
        "search_btn": {
            "type": "xpath", "value": "/html/body/div[1]/div/div/header/div[2]/div[3]/a",
        },
        "search_res_container": {
            "type": "xpath",
            "value": "/html/body/div[2]/div/main/div[3]/div[2]/div/div[2]",
        },
        "search_results": {
            "type": "xpath",
            "value": ".//li"
        },
        "name": "Myntra"

    }, {
        "url": "https://ajio.com/",
        "search_bar": {
            "type": "xpath",
            "value": "",
        },
        "sort_dd_present": "true",
        "sort_dd_click": "false",
        "sort_dd": {
            "type": "xpath", "value": "//*[@class='sort-sortBy']",
        },
        "low_to_high": {
            "type": "xpath",
            "value": "/html/body/div[2]/div/main/div[3]/div[2]/div/div[1]/section/div[1]/div[1]/div/div/div/ul/li[6]/label",
        },
        "enter_or_search_btn": "search_btn",
        "search_btn": {
            "type": "xpath", "value": "/html/body/div[1]/div/div/header/div[2]/div[3]/a",
        },
        "search_res_container": {
            "type": "xpath",
            "value": "/html/body/div[2]/div/main/div[3]/div[2]/div/div[2]",
        },
        "search_results": {
            "type": "xpath",
            "value": ".//li"
        },
        "name": "Ajio"
    }
]

meds_sites = [
    {
        "site": "",
        "search_bar": ""
    }, {
        "site": "",
        "search_bar": ""
    }, {
        "site": "",
        "search_bar": ""
    }
]

results = []

if typeProd == str(1):
    print("hi")

    for site in goods_sites:
        s = Service("C:/Users/hemal/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        driver.get(site["url"])
        time.sleep(1)

        search_bar = driver.find_element(site["search_bar"]["type"],
                                         site["search_bar"]["value"])

        search_bar.click()

        time.sleep(1)

        for c in product:
            time.sleep(random.randint(3, 5) / 10)
            search_bar.send_keys("" + c)

        search_bar.send_keys(Keys.ENTER)

        time.sleep(1)

        if site["sort_dd_present"] == "true":
            dd_sort = driver.find_element(site["sort_dd"]["type"], site["sort_dd"]["value"])
            dd_sort.click()

        time.sleep(0.5)

        driver.find_element(site["low_to_high"]["type"], site["low_to_high"]["value"]).click()

        time.sleep(1)

        search_res_container = driver.find_element(site["search_res_container"]["type"],
                                                   site["search_res_container"]["value"])
        search_results = search_res_container.find_elements(site["search_results"]["type"],
                                                            site["search_results"]["value"])

        print(len(search_results))

        for res in search_results:
            # first = driver.find_element("xpath", "/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[" + str(i) + "]")
            # print(res.text)
            if res.text.__contains__("Sponsored").__or__(res.text.__contains__("results")).__or__(
                    res.text.__contains__("Results")):
                continue
            else:
                results.append({"name": site["name"], "product": res.text})
                break

        driver.quit()
        time.sleep(1)

if typeProd == str(2):
    print("hiClothes")

    for site in clothing_sites:
        s = Service("C:/Users/hemal/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        driver.get(site["url"])
        time.sleep(1)

        search_bar = driver.find_element(site["search_bar"]["type"],
                                         site["search_bar"]["value"])

        search_bar.click()

        time.sleep(1)

        for c in product:
            time.sleep(random.randint(3, 5) / 10)
            search_bar.send_keys("" + c)

        if site["enter_or_search_btn"] == "search_btn":
            driver.find_element(site["search_btn"]["type"], site["search_btn"]["value"]).click()
        else:
            search_bar.send_keys(Keys.ENTER)

        time.sleep(1)

        if site["sort_dd_present"] == "true":
            dd_sort = driver.find_element(site["sort_dd"]["type"], site["sort_dd"]["value"])
            if site["sort_dd_click"] == "false":
                actions = ActionChains(driver)
                actions.move_to_element(dd_sort).perform()
            else:
                dd_sort.click()

        time.sleep(0.5)

        driver.find_element(site["low_to_high"]["type"], site["low_to_high"]["value"]).click()

        time.sleep(1)

        search_res_container = driver.find_element(site["search_res_container"]["type"],
                                                   site["search_res_container"]["value"])
        search_results = search_res_container.find_elements(site["search_results"]["type"],
                                                            site["search_results"]["value"])

        print(len(search_results))

        for res in search_results:
            # first = driver.find_element("xpath", "/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[" + str(i) + "]")
            # print(res.text)
            if res.text.__contains__("Sponsored").__or__(res.text.__contains__("results")).__or__(
                    res.text.__contains__("Results")):
                continue
            else:
                results.append({"name": site["name"], "product": res.text})
                break

        driver.quit()
        time.sleep(1)

print(results)
time.sleep(10)
# print(first.text)
