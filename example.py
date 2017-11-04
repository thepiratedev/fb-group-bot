from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


rootUrl = 'https://mbasic.facebook.com'


groups = []
message = """Your Message Here"""
username = "Your username"
password = "Your password"

# start
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(30)
driver.set_window_size(400, 600)
driver.get(rootUrl)


print('Waiting for login elements')
wait.until(EC.presence_of_element_located(
    (By.XPATH, '//input[@type="password"]')))
print('Login Available')
inputUsername = driver.find_element_by_id('m_login_email')
inputPassword = driver.find_element_by_xpath('//input[@type="password"]')
inputUsername.send_keys(username)
inputPassword.send_keys(password)
inputPassword.send_keys(Keys.RETURN)
print('Successfully logged in.')

driver.get('https://mbasic.facebook.com/groups/?seemore&refid=27')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

for tag in soup.find_all('a', href=re.compile(r'groups/\d')):
    print('saving in fb-groups.txt: ' + tag.text)
    groups.append(rootUrl + tag['href'])
    # time.sleep(0.05)
for group in groups:
    link = rootUrl + group

print('Sucessfull wrote all group links to fb-groups.txt')
for group in groups:
    try:
        driver.get(group)
        wait.until(EC.presence_of_element_located(
            (By.XPATH, '//textarea[@name="xc_message"]')))
        textarea = driver.find_element_by_xpath(
            '//textarea[@name="xc_message"]')
        textarea.send_keys(message)
        print('YES')
    except NoSuchElementException:
        print('No text-area found skipping...')
        continue
