import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
username = input("Kullanıcı Adı: ")
password = input("Sifre: ")

driver = webdriver.Chrome(".../chromedriver.exe")
url = "https://www.instagram.com/accounts/login/"
driver.get(url)

giris = driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input")
giris.send_keys(username)

sifre = driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input")
sifre.send_keys(password)

ok = driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]")
ok.click()

time.sleep(1)
driver.maximize_window()

input("Programın kapatılması için bir tuşa basın...")
driver.close()
