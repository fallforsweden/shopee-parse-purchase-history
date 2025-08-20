import csv
import time
import random
import re
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

profile_path = r"ROOT DIRECTORY"
geckodriver_path = r"GECKO DRIVER"

options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
options.add_argument("-profile")
options.add_argument(profile_path)
options.add_argument("--headless")

service = Service(executable_path=geckodriver_path)
print(f"Launching Firefox with profile: {profile_path}")

driver = webdriver.Firefox(service=service, options=options)
driver.get("https://shopee.co.id/user/purchase/?type=3")
actions = ActionChains(driver)


try:
    time.sleep(random.uniform(2, 4))
    box_counter = []
    last_height = driver.execute_script("return document.body.scrollHeight")
    itemTargetCount = 400

    while itemTargetCount > len(box_counter):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.uniform(2, 4))

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

        box = driver.find_elements(By.CLASS_NAME, 'DWVWOJ')
        elem_judul = [x.text for x in box]
        box_counter = elem_judul

except Exception as e:
    print("Scrolling error:", e)

orders = []
try:
    time.sleep(random.uniform(2, 4))
    element_list = driver.find_element(By.CSS_SELECTOR, ".ashFMQ")
    items = element_list.find_elements(By.CSS_SELECTOR, ".YL_VlX")

    for i, item in enumerate(items):
        try:
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", item)
            time.sleep(0.7)

            
            drawers = item.find_elements(By.CSS_SELECTOR, ".shopee-drawer")

            tanggal = ""
            for drawer in drawers:
                try:
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", drawer)
                    actions.move_to_element(drawer).perform()

                    drawer_id = drawer.get_attribute("id")
                    content = WebDriverWait(driver, 3).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, f"#{drawer_id} .shopee-drawer__contents[aria-hidden='false']"))
                    )

                    cand = content.find_elements(By.XPATH, ".//*[contains(@class,'Rnz') and contains(@class,'5l')]//div[not(contains(@class,'wuCGUa'))]")
                    if cand:
                        tanggal = cand[-1].text
                        break
                except:
                    continue

            # regex
            m = re.search(r"\b\d{2}-\d{2}-\d{4}\s+\d{2}:\d{2}\b", tanggal)
            tanggal = m.group(0) if m else tanggal.strip()

            
            nama_barang = [x.text for x in item.find_elements(By.CLASS_NAME, 'DWVWOJ')]
            
            quantities = [q.text for q in item.find_elements(By.CLASS_NAME, 'j3I_Nh')]
            
            harga_list = [y.text for y in item.find_elements(By.CLASS_NAME, 'nW_6Oi')]

            # total
            try:
                total_pesanan = item.find_element(By.CLASS_NAME, 't7TQaf').text
            except Exception:
                total_pesanan = ""

            for idx, nama in enumerate(nama_barang):
                qty = quantities[idx] if idx < len(quantities) else ""
                harga = harga_list[idx] if idx < len(harga_list) else ""

                orders.append({
                    "tanggal": tanggal,
                    "nama_barang": nama,
                    "quantity": qty,
                    "harga": harga,
                    "total": total_pesanan
                })

        except Exception as a:
            print(f"[{i}] Gagal ambil data:", a)

except Exception as e:
    print("Extracting error:", e)

with open("shopee.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["tanggal", "nama_barang", "quantity", "harga", "total"])
    writer.writeheader()
    writer.writerows(orders)

print("data saved to shopee.csv")

driver.quit()
