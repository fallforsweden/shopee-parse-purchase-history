from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import random

profile_path = r"C:\Users\danube_stream\AppData\Roaming\Mozilla\Firefox\Profiles\e2cxz3e6.x"

geckodriver_path = r"D:\course\Selenium\geckodriver.exe"

options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

options.add_argument("-profile")
options.add_argument(profile_path)
options.add_argument('--headless')

service = Service(executable_path=geckodriver_path)

print(f"Launching Firefox with profile: {profile_path}")

driver = webdriver.Firefox(service=service, options=options)

driver.get("https://shopee.co.id/user/purchase/")

try :
    time.sleep(random.uniform(1.6, 7))

    element_list = driver.find_element(By.CSS_SELECTOR, ".ashFMQ") #container all element

    time.sleep(random.uniform(1.6, 5))

    items = element_list.find_elements(By.CSS_SELECTOR, ".YL_VlX") # kotak kotak content

    time.sleep(random.uniform(1.6, 6))

    for item in items :
        nama_barang = item.find_element(By.CLASS_NAME, 'DWVWOJ').text
        harga = item.find_element(By.CLASS_NAME,'nW_6Oi').text
        
        # click_tanggal = item.find_element(By.CLASS_NAME, 'shopee-svg-icon').click()
        # tanggal_produk = item.find_element(By.CLASS_NAME, 'wUGCua').text

        print(f'nama barang : {nama_barang}')
        print(f'Harga Produk : {harga} ')
        # print(f'tanggal : {tanggal_produk} \n')
except Exception as e:
    print(e)
    pass

# ashFMQ all container
# J632se class name for container per product
# xpath container per product /html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/main/div[1]/div[4]/div[1]/div
# DWVWOJ class name for product title
# nW_6Oi PNlXhK class name for price per product

# 
# my_orders_button.click()
# time.sleep(random.uniform(1.6, 4.3)) # Pause before clicking

# exit
# print("Browser is open. Press Enter in this terminal to close it.")
# input()

# print("Closing the browser.")
# driver.quit()