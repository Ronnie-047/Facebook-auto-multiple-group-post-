from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> WELCOME >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#


def facebook():
    usr = ""                              # Type your USERNAME
    pwd = ""                              # Type your PASSWORD
    # PHOTO Path (Example "C:\\Users\\Ronnie\\Desktop\\1.jpg")
    photo = ""
    text = ""                             # Type your MESSAGE
    # Paste your GROUPS full URL in (m.facebook.com) format
    groups = [
        "",
        "",
    ]


# Opening Facebook for LOGIN >>>>
    # Change  Your CHROMEDRIVE.EXE file path in DRIVER Variable
    driver = webdriver.Chrome(
        "C:\\Users\\Ronnie\\Desktop\\Hello World\\chromedriver.exe")
    driver.get("https://m.facebook.com")
    driver.maximize_window()
    time.sleep(5)

# Login >>>>
    user = driver.find_element_by_name("email")
    user.send_keys(usr)
    password = driver.find_element_by_name("pass")
    password.send_keys(pwd)
    driver.find_element_by_name("login").click()
    time.sleep(3)

# Opening Groups One by One >>>>
    for group in groups:
        driver.get(group)
        time.sleep(3)

    # CLICK on Write Something
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[4]/div/div[1]/div/div[3]/div/div[1]/div[2]/div").click()
        time.sleep(3)

    # New POP UP window for posting ( Send msg & Add photo )
        # Send messge >>>>
        msg = driver.find_element_by_xpath("//*[@id='uniqid_1']")
        msg.send_keys(text)
        time.sleep(3)
        # Add photo >>>>
        image = driver.find_element_by_name("file1")
        image.send_keys(photo)
        time.sleep(5)

    # ALL DONE ! Post >>>>
        driver.find_element_by_xpath(
            "//*[@id='composer-main-view-id']/div[3]/div/div/button").click()

        print(f"{group} : DONE")

        time.sleep(5)


facebook()
