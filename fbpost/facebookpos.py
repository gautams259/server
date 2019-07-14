from selenium import webdriver
from image_sheet import *
import sys
import pickle
import time
from datetime import datetime
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

options=Options()#
options.add_argument('-headless')#
driver=webdriver.Firefox(firefox_options=options)#
#driver=webdriver.Firefox()

def login_validation():
    driver.find_element(By.XPATH, "//a[@class='y r z']").click()

def download_cookies():
    pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

def load_cookies():
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    time.sleep(4)

def visitlink(link= 'https://m.facebook.com/'):
    driver.get(link)
    load_cookies()

    

def login(id, pwd):
    if id and pwd:
        print('logging to {} '.format('https://m.facebook.com/'))
        driver.find_element(By.XPATH, "//input[@id='m_login_email']").send_keys(id)
        driver.find_element(By.XPATH, "//input[@class='bl bm bo bp']").send_keys(pwd)
        driver.find_element(By.XPATH, "//input[@name='login' and @type='submit']").click()
        download_cookies()
    else:
        print("trying to login using cookies...")




def post_pic(image_path='~/data/practice/gitrepo/fbpost/images/'):
    driver.find_element(By.XPATH, "//input[@name='view_photo']").click()
    pub_data=get_images()
    if pub_data:
        print(pub_data)
        image_path=image_path+pub_data[0]
        print(image_path)
        file_upload = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "file1")))
        time.sleep(5)
        #file_upload.send_keys('~/data/practice/gitrepo/fbpost/images/dhoni.jpeg')
        file_upload.send_keys(image_path)
        driver.find_element(By.XPATH, "//input[@name='add_photo_done']").click()
        time.sleep(4)
        driver.find_element(By.XPATH, "//textarea[@class='bj bk bl']").send_keys(pub_data[1])
        driver.find_element(By.XPATH, "//input[@name='view_post']").click()
        driver.close()
        mark_cell_as_published(pub_data[2])
    else:
        print("no images availabel please update sheet")
        driver.close()

def main():
    id = pwd = None
    if len(sys.argv) == 3:
        id=sys.argv[1].strip()
        pwd=sys.argv[2].strip()
    visitlink()
    login(id,pwd)
    
    grouplink='https://m.facebook.com/tarkaexpress'
    visitlink(grouplink)
    post_pic()



if __name__ =='__main__':
    main()
    
