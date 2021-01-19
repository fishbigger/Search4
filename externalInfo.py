import bs4
import requests
from selenium import webdriver
import os

def getExtraData(url, cssSelector):
	path = os.path.abspath('chromedriver')

	driver = webdriver.Chrome(executable_path=path)

	driver.get(url)
	soup = bs4.BeautifulSoup(driver.page_source,"html.parser")
	driver.quit()


	return soup.select_one(cssSelector).getText()