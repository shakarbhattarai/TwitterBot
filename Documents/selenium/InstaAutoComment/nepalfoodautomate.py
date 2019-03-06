# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import random
import time
commentxpath='span[aria-label="Comment"]'
driver = webdriver.Chrome('./chromedriver')
def navigate(username,passowrd,url):
	
	driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
	driver.find_element_by_css_selector('input[name=username]').send_keys(username)
	driver.find_element_by_css_selector('input[name=password]').send_keys(passowrd)
	driver.find_element_by_css_selector('input[name=password]').send_keys(Keys.RETURN)
	time.sleep(5)
	driver.get(url)
	
def comment(text):
	wait = WebDriverWait(driver, 8)
	
	confirm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, commentxpath)))
	element = driver.find_elements_by_css_selector(commentxpath)
	element[0].click()
	ActionChains(driver).move_to_element(confirm).perform()
	element[0].send_keys(text)
	element[0].send_keys(Keys.RETURN)
	time.sleep(15)
	

	
navigate("shakarbhattarai","shakarbhattaraijaynepal","https://www.instagram.com/p/BfyBxRAHOXG")
comment("Hello world")
	
	
	
	
	
	
	
	
	

