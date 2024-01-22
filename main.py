from selenium import webdriver
from selenium.webdriver.common.by import By
import threading
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from typing import Final

# form link
Form: Final = 'https://forms.gle/BfeWcU3eEixGvUaW7' # put your own link

# list of names, registration numbers and enrolled courses
names=["Joy", "Manish", "Asish"]
reg_no=['23bce112','23bce111','23bce110']
enrolled_courses=['MBBS','B.Tech','M.Tech']

# all the drivers
driver1=webdriver.Chrome()
driver2=webdriver.Chrome()
driver3=webdriver.Chrome()

def formFillup(index, driver):

    # link open
    driver.get(Form)

    name_space = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'))
    )
    name_space.send_keys(names[index])

    time.sleep(1)

    # reg no filling
    reg_space=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    reg_space.click()
    reg_space.send_keys(reg_no[index])

    time.sleep(1)

    # course filling
    course_space = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'))
    )
    course_space.send_keys(enrolled_courses[index])
    print('course filled')

    time.sleep(1)

    # submit button
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'))
    )

    submit_button.click()
    print(f'submitted for {names[index]}')
    time.sleep(3)

    # taking ss of submitting
    driver1.get_screenshot_as_file(f'{names[index]}.png')


# multiple threads to perform io tasks
th1=threading.Thread(target=formFillup,args=(0,driver1))
th2=threading.Thread(target=formFillup,args=(1,driver2))
th3=threading.Thread(target=formFillup,args=(2,driver3))

th1.start()
th2.start()
th3.start()

# Wait for all threads to finish
th1.join()
th2.join()
th3.join()

# final message of main thread
print("All the forms have been auto-filled successfully")


