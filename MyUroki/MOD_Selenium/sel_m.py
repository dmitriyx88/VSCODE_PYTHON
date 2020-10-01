from selenium import webdriver
import os
os.chdir(os.path.dirname(__file__))
browser= webdriver.Firefox()
browser.get("https://www.olx.ua/obyavlenie/zaschitnoe-5d-steklo-dlya-apple-watch-38-42-mm-apple-5-6-7-IDBqd9S.html")

tag_xx= browser.find_element_by_class_name('xx-large')
tag_xx.click()

print(tag_xx.text)  