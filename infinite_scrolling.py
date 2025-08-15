from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

driver = webdriver.Firefox()
driver.get('https://intoli.com/blog/scrape-infinite-scroll/demo.html')

items = []
file = open("Employees.txt", "w") 

last_height = driver.execute_script("return document.body.scrollHeight") # ambil ukuran page

itemTargetCount = 30 #set target 

while itemTargetCount > len(items):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # scroll sampe bawah 

    time.sleep(1)

    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height: # kalo website stop showing more content
        break
    
    last_height = new_height

    judul = driver.find_elements(By.CLASS_NAME, 'box') #cari element JANGAN LUPA PAKE elementSSSSS
    elem_judul = [] 
    for x in judul:
        elem_judul.append(x.text) #masukkan konten ke array (text sebagai contoh) juga pilih tipe attribute, text / href etc
    
    items = elem_judul 
    

# Read from file and parse JSON

res = ' '.join(items)
print(res)

with open("scrap.json", "w") as f:
    data = json.dump(res, f, indent=2)


# import to text


# file.write(res) 
# file.write("\n") 

# file.close() 
