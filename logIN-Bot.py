# Used to import the webdriver from selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 
import os

# Get the path of chromedriver which you have install

def startBot(username, password, url):
	path = "/usr/local/bin/chromedriver.exe"
	
	# Create a Service object
	service = Service(path)

	# Setup Chrome option (optional)
	chrome_options = Options()
	chrome_options.add_argument("--start-maximized") # Launchs a maximized webpage

	# Initialize the Chrome browser with Serice and Options

	# Create a WebDriver instance and giving the path of chromedriver to the selenium webdriver
	driver = webdriver.Chrome(path)
	
	# Perform actions on the browser using WebDriver methods get which opens the website in chrome.
	driver.get(url)
	
	# Find the id or name or class of
	# username by inspecting on username input
	driver.find_element_by_name("id/class/name of username").send_keys(username)
	
	# Find the password by inspecting on password input
	driver.find_element_by_name("id/class/name of password").send_keys(password)
	
	# Click on submit
	driver.find_element_by_css_selector("id/class/name/css selector of login button").click()


# Driver Code
# Enter below your login credentials
username = "Enter your username"
password = "Enter your password"

# URL of the login page of site
# where you want to automate login.
url = "url"

# Call the function
startBot(username, password, url)
