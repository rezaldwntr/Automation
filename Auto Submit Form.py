from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pandas as pd 

driver = webdriver.Edge("")

df = pd.read_excel(r'E:\REZAL\Automation\File Data.xlsx') # letak file

for index, row in df.iterrows(): # perulangan mengambil setiap baris data
    # inputan biasa
    driver.get("https://cloud.hsu.go.id/apps/forms/s/94L8acLygrpjEnBa8yq8YdWP") # web tujuan

    jp_input = driver.find_element(By.XPATH, '//*[@id="app-content-vue"]/form/ul/li[1]/div[2]/input')
    jp_input.send_keys(row['Jenis Pengadaan'])

    jju_input = driver.find_element(By.XPATH, '//*[@id="app-content-vue"]/form/ul/li[2]/div[2]/input')
    jju_input.send_keys(row['Jenis Jabatan Umum'])

    nama_input = driver.find_element(By.XPATH, '//*[@id="app-content-vue"]/form/ul/li[3]/div[2]/input')
    nama_input.send_keys(row['Nama Jabatan'])

    jj_input = driver.find_element(By.XPATH, '//*[@id="app-content-vue"]/form/ul/li[4]/div[2]/input')
    jj_input.send_keys(row['Jenis Jabatan'])

    jumlah_input = driver.find_element(By.XPATH, '//*[@id="app-content-vue"]/form/ul/li[5]/div[2]/input')
    jumlah_input.send_keys(row['Jumlah'])

    up_input = driver.find_element(By.XPATH, '//*[@id="app-content-vue"]/form/ul/li[6]/div[2]/textarea')
    up_input.send_keys(row['Unit Penempatan'])

    driver.find_element(By.XPATH, '//*[@id="app-content-vue"]/form/div/button[2]/span/span[2]').click() # autoklik tombol

# auto input dropdown
# dropdown_input = driver.find_element(By.XPATH, '')
# select = Select(selection_input)
# select.select_by_visible_text("Iten 3")

# auto input checkbox
# driver.find_element(By.XPATH, '').click()

# auto input tanggal
# tanggal_input = driver.find_element(By.XPATH, '')
# tanggal_input.click()
# tanggal_input.send_keys("26052025")

time.sleep(2)

driver.quit()