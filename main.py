from email.quoprimime import quote
from turtle import back
from pandas import NA
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import csv 
def review(site):
    print(site)
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("--headless")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get(site)
    driver.implicitly_wait(10)
    def review_get(path):
        x = 9
        backupPath = '/html/body/div[1]/div/main/div/div[4]/section/div[' + str(x) + ']/article/section/div[2]/p'
        if len(driver.find_elements(By.XPATH, path))!= 0:
            a = driver.find_element(By.XPATH, path)     
            return a.text
        else:
            x+=1 
            return review_get(backupPath)
        
    review1 = review_get('/html/body/div[1]/div/main/div/div[4]/section/div[3]/article/section/div[2]/p')
    review2 = review_get('/html/body/div[1]/div/main/div/div[4]/section/div[5]/article/section/div[2]/p')
    review3 = review_get('/html/body/div[1]/div/main/div/div[4]/section/div[6]/article/section/div[2]/p')
    review4 = review_get('/html/body/div[1]/div/main/div/div[4]/section/div[7]/article/section/div[2]/p')
    review5 = review_get('/html/body/div[1]/div/main/div/div[4]/section/div[8]/article/section/div[2]/p')
    driver.close()
    driver.quit()
    return [ review1,review2,review3,review4,review5 ]
    

with open('trustpilot.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for i in spamreader:
        for j in i:
            if "https:" in j[0:-6]:
                row = review(j[0:-6])