from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 
import os
import time

def startBot(username, password, url):	
	# Create a Service object, WebDriver instance and Chrome Options
	service = Service()
	chrome_options = webdriver.ChromeOptions()
	driver = webdriver.Chrome(service=service, options=chrome_options)
	chrome_options.add_argument("--start-maximized") # [Optional] Launchs a maximized webpage

	# Perform actions on the browser using WebDriver methods get which opens the website in chrome.
	driver.get(url)
	
	# Find the id or name or class of
	# username by inspecting on username input. The example below :
	# driver.find_element_by_name("id/class/name of username").send_keys(username)
	print("Filling in username field...")
	driver.find_element(By.ID,"login_field").send_keys(username)

	# Find the password by inspecting on password input. . Example below:
	#driver.find_element_by_name("id/class/name of password").send_keys(password)
	print("Filling in password field...")
	driver.find_element(By.ID,"password").send_keys(password)

	# Click on submit/login button. Example below:
	# driver.find_element_by_css_selector("id/class/name/css selector of login button").click()
	driver.find_element(By.NAME,"commit").click()
	
	print("Login started...")
	time.sleep(20) # sleep for 5 seconds
	
	driver.quit()

# Driver Code
# Enter your login credentials below:
username = "Enter your username"
password = "Enter your password"

# URL of the login page of site
# where you want to automate login.
url = "https://github.com/login"

# Call the function
startBot(username,password,url)