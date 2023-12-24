from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time

def main():
    options = webdriver.ChromeOptions()
    options.add_argument(
        "User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install(), options=options))
    driver.get("https://www.booking.com/searchresults.ru.html?ss=%D0%BF%D0%B0%D1%80%D0%B8%D0%B6&ssne=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0&ssne_untouched=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0&label=gog235jc-1DCAEoggI46AdIIVgDaE2IAQGYASG4ARjIAQzYAQPoAQH4AQKIAgGoAgS4ApHa0asGwAIB0gIkMTI3ZGU1YWYtOWVjNS00NzQ5LTgwNTQtN2VhMmUxZGM1ZjQ32AIE4AIB&aid=397594&lang=ru&sb=1&src_elem=sb&src=searchresults&dest_id=-1456928&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=ru&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=18795f91617001ef&ac_meta=GhAxODc5NWY5MTYxNzAwMWVmIAAoATICcnU6CtC%2F0LDRgNC40LZAAEoAUAA%3D&group_adults=2&no_rooms=1&group_children=0")
    time.sleep(10)
    titles = driver.find_elements(By.XPATH,"/html/body/div[4]/div/div[2]/div/div[2]/div[3]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/h3")
    true_titles =[]
    for title in titles:

        true_titles.append(title.text.replace("Откроется в новом окне","").replace(" ","+").replace("\n",""))
    print(true_titles)
    for final_title in true_titles:
        driver.get(f"https://www.google.com/maps/search/{final_title}/@48.8731503,2.3157361,15z?entry=ttu")
        time.sleep(10)
        try:
            driver.find_element(By.XPATH,"//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[1]/h1")
            try:
                driver.find_element(By.XPATH,"//*[contains(text(),'Booking')]")
                print('Есть на гугл картах, есть ссылка на букинг.')
            except NoSuchElementException:
                print('Есть на гугл картах, нет ссылки на букинг')
        except NoSuchElementException:
            print('такого Отеля нет')

if __name__ == '__main__':
    main()