from time import sleep

from selenium import webdriver



driver = webdriver.Firefox()
url = "https://www.memrise.com/login/"
driver.get(url)

def Login():
    username = driver.find_element_by_name("username")
    username.send_keys(" ")

    password = driver.find_element_by_name("password")
    password.send_keys(" ")

# click login button
    button = driver.find_element_by_class_name("btn-success")
    button.click()


def AddLevel():
# open url
    url = "https://www.memrise.com/course/1570754/horizons-6th-edition/edit/"
    driver.get(url)

# click on Add button
    addbutton = driver.find_element_by_css_selector("div.add-level button")
    addbutton.click()
    sleep(1)

# choose French
    button = driver.find_element_by_xpath(".//a[@data-kind='things']")
    button.click()
    sleep(2)

# click on Level name, delete the default name and add custom name
    levelname = driver.find_element_by_xpath(".//div[@class='level']//h3[@class='level-name']")
    levelname.click()
    levelname.find_element_by_tag_name("input").clear()
    levelname.send_keys("leve1")

def AddWords():
# add words to 1st field
    word = driver.find_element_by_xpath(".//div[@class='level']//td[@data-key='1']//input[@type='text']")
    word.send_keys("hello")

# add words to 2nd field
    word1 = driver.find_element_by_xpath(".//div[@class='level']//td[@data-key='2']//input[@type='text']")
    word1.send_keys("hello")

# click add button
    add = driver.find_element_by_xpath(".//div[@class='level']//i[@class='ico ico-plus ico-blue']")
    add.click()

def Save():
    savebutton = driver.find_element_by_link_text("Save and continue")
    savebutton.click()

Login()
AddLevel()
AddWords()
Save()
# driver.quit()
