import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from threading import Timer
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(chrome_options)
driver.get(url="https://orteil.dashnet.org/cookieclicker/")
minute_timeout = time.time() + 60*5

def buy_upgrade():
    try:
        cookie_count = int(driver.find_element(By.ID, value="cookies").text.split(" ")[0])
    except ValueError:
        cookie_count = int(driver.find_element(By.ID, value="cookies").text.replace(',', '').split(" ")[0])
    print(cookie_count)
    try:
        avail_upgrade = driver.find_element(By.XPATH,value='//*[@id="upgrade0"]')
        avail_upgrade.click()
    except selenium.common.exceptions.NoSuchElementException:
        pass
    avail_building = driver.find_elements(By.XPATH,value='//*[@id="products"]/div[@class="product unlocked enabled"]')
    for x in avail_building[::-1]:
        x.click()

def start_game():
    cookie_click = driver.find_element(By.ID,value="bigCookie")

    timeout = time.time() + 5
    while True:
        cookie_click.click()
        if time.time() > timeout:
            break
    if time.time() > minute_timeout:
        cps = driver.find_element(By.ID,value="cookiesPerSecond").text.split(":")[1]
        print(f"Cookies/Second: {cps}")
    buy_upgrade()
    start_game()
def cookie_and_english():
    accept_cookies = driver.find_element(By.XPATH, value='/html/body/div[1]/div/a[1]')
    accept_cookies.click()
    english_language = driver.find_element(By.XPATH, value='//*[@id="langSelect-EN"]')
    english_language.click()
    game_timer = Timer(2,start_game)
    game_timer.start()

start_flag = driver.find_element(By.XPATH,value='//*[@id="topBar"]/div[1]/b')
timer = Timer(2,cookie_and_english)
timer.start()


