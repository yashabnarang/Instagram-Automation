# Instagram Automater (BETA)
# By Yashab Narang

import time
from selenium import webdriver
from credentials import username, password

chromePath = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromePath)

# Open Instagram Website
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(4)

# Login
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input') \
    .send_keys(username)
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input') \
    .send_keys(password)
driver.find_element_by_css_selector('button[type=submit]').click()
time.sleep(4)

# Go To Giveaway Link
driver.get("https://www.instagram.com/p/B_sd6RWnfYb/")
time.sleep(4)

# Follow (Assumes Not Following, Need to Add Condition to check ifFollowing)
driver.find_element_by_css_selector('button[type=button]').click()
time.sleep(1)

# Like (Potential Issue, Uses Absolute Path, Consider changing to reduce risk of breaking)
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[1]/span[1]/button')\
    .click()
time.sleep(1)

# Comment


# Exit Driver
# driver.quit()
