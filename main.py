# https://github.com/baptisteCanac
from selenium import webdriver
import pyperclip

website = input("website complete adress (ex:https://google.com) : ")

driver = webdriver.Edge(executable_path="msedgedriver.exe")
driver.get(website)

htmlSource = driver.page_source
print(htmlSource)
pyperclip.copy(htmlSource)

driver.close()

print("The text as been copied, you can paste it in a code or text editor")
