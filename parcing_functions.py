"""шаблон парсера. Просто открывает страницу по url"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()

# disable webdriver mode
options.add_argument("--disable-blink-features=AutomationControlled")

# user agent
my_user_agent = "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)"
options.add_argument(f"user-agent={my_user_agent}")
driver = webdriver.Chrome(options=options)

url = 'https://ya.ru'

def open_page(url: str):
    "функция получает название модели и возвращает url с описанием этой модели на сайте производителя"
    print("открываю урл")
    driver.get(url)
    time.sleep(60)

open_page(url)
