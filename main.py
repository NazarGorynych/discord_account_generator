import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from faker.providers import BaseProvider

from faker import Faker

# Faker settings
fakeEN = Faker('en_US')
fakeRU = Faker('ru_RU')
fakeEN.add_provider(BaseProvider)
fakeRU.add_provider(BaseProvider)

# Driver settings
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
actions = ActionChains(driver)
driver.get("https://discord.com/register")

# Data generation
email = fakeEN.email()
username = fakeEN.name()
password = fakeEN.password(length=12)

calendar_day = random.randint(1, 28)
month = fakeEN.month_name()
year = random.randint(1950, 2006)
# Find the email input field and type the email
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[1]/div/input').send_keys(email)

# Find the username input field and type the username
driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/form/div/div/div[2]/div/input').send_keys(username)

# Find the password input field and fill the password
driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/form/div/div/div[3]/div/input').send_keys(password)

# Find data of birth_date and fill in the fields
driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/form/div/div/div[4]/div[1]/div[1]/div/div/div/div[1]').click()

# Month
actions.send_keys(month)
actions.send_keys(Keys.ENTER)

# Day
actions.send_keys(calendar_day)
actions.send_keys(Keys.ENTER)

# Year
actions.send_keys(year)
actions.send_keys(Keys.ENTER)

actions.perform()
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[5]/button').click()    # Register button


input('hit ENTER if you have solved the CAPCHA and want auth token!')

token = driver.execute_script('location.reload();var i=document.createElement("iframe");document.body.appendChild(i);return i.contentWindow.localStorage.token').strip('"')

print(f'EMAIL -- PASSWORD -- AUTH_TOKEN:')
print(f'{email} -- {password} -- {token}')

driver.get("https://discord.com/login")

# driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[1]/div/input').send_keys(email)
# driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[2]/div/input').send_keys(password)
# driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[3]/button').click()

