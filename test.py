# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# from time import sleep
#
#
# driver = webdriver.Chrome()
#
# url = "https://www.letskodeit.com/courses"
#
# driver.get(url)
#
#
# element = driver.find_element(By.XPATH, "//a[@href='/courses/rest-assured-api-automation']")
#
# driver.execute_script("arguments[0].scrollIntoView(true);", element)
#
#
# sleep(3)
#
# driver.quit()

website = "https://vrii14.github.io/"

website_list = []

protocols = ("https", "http")
element = ["h", "t", "t", "p", "s"]


for digits in protocols:
    website_list.append(digits)
    print(digits)
website_result = website[:len(protocols[0])]


print(website_result)
assert  element is not None, 'Should not be NONE'



