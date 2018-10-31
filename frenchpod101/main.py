from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()

urlHomePage = "https://www.frenchpod101.com/"
driver.get(urlHomePage)

signIn = driver.find_element_by_class_name("r101-sign-in--a__button")
signIn.click()

userName = driver.find_element_by_id("hm_amember_login")
userName.send_keys("rylie.mahrus@0ne0ut.com")

password = driver.find_element_by_id("hm_amember_pass")
password.send_keys("hM4A1KZYx$MU")

loginButton = driver.find_element_by_class_name("r101-sign-in--a__submit")
loginButton.click()

file = open("lessons.csv")

for string in file:
    string = string.rstrip()
    string = string.split(';')
    urlLesson = string[0]
    count = string[1]
    print(urlLesson)
    print(count)
    driver.get(urlLesson)

    script = "$('input[type=checkbox]').each(function(index, item) {" \
             "  if (index < %s && !item.hasAttribute('checked')) {" \
             "    item.click();" \
             "  }" \
             "})" % count
    driver.execute_script(script)
    sleep(1)

driver.quit()
