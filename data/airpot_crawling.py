from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
import requests
import re
import pandas as pd
import numpy as np
import os

name = ['에어팟3세대']
category = ['별점']
air3 = 'https://search.shopping.naver.com/catalog/29413009627?query=%EC%97%90%EC%96%B4%ED%8C%9F3%EC%84%B8%EB%8C%80&NaPm=ct%3Dl2prqjgo%7Cci%3D346c848972d2ff51742b02bb6a112583a35555f1%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D90f8a4acc5dc0d84f7deb26543baab6b9b5fd55c'
shoppingmall_review = '//*[@id="section_review"]/div[2]/div[2]/ul/li[1]/a'

header = {'User_Agent':''}
driver = webdriver.Chrome(r'd:\sungil\popo\chromedriver.exe')
driver.implicitly_wait(3)
driver.get(air3)
req = requests.get(air3,verify=False)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
sleep(2)

driver.find_element_by_xpath(shoppingmall_review).click()
sleep(2)

element=driver.find_element_by_xpath(shoppingmall_review)
driver.execute_script('arguments[0].click();',element)
sleep(2)

def add_dataframe(name,category,reviews,stars,cnt):
    df1=pd.DataFrame(columns=['type','category','review','star'])
    n=1
    if (cnt>0):
        for i in range(0,cnt-1):
            df1.loc[n]=[name,category,reviews[i],stars[i]] 
            i+=1
            n+=1
    else:
        df1.loc[n]=[name,category,'null','null']
        n+=1    
    return df1

driver.find_element_by_xpath(shoppingmall_review).click() 
name_=name[0]
category_=category[0]
reviews=[]
stars=[]
cnt=1   
page=1

while True:
    j=1
    print ("페이지", page ,"\n") 
    sleep(2)
    while True: #한페이지에 20개의 리뷰, 마지막 리뷰에서 error발생
        try:
            star=driver.find_element_by_xpath('//*[@id="section_review"]/ul/li[1]/div[1]/span[1]').text
            stars.append(star)
            review=driver.find_element_by_xpath('//*[@id="section_review"]/ul/li['+str(j)+']/div[2]/div/p').text
            reviews.append(review)
            if j%2==0: #화면에 2개씩 보이도록 스크롤
                ELEMENT = driver.find_element_by_xpath('//*[@id="section_review"]/ul/li['+str(j)+']/div[2]/div/p')
                driver.execute_script("arguments[0].scrollIntoView(true);", ELEMENT)       
            j+=1
            print(cnt, review ,star, "\n")
            cnt+=1 
        except: break
            
    sleep(2)
    
    if page<11:#page10
        try: #리뷰의 마지막 페이지에서 error발생
            page +=1
            next_page=driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[6]/div[3]/a['+str(page)+']').click() 
            
        except: break #리뷰의 마지막 페이지에서 process 종료
        
    else : 
        try: #page11부터
            if page%10==0: driver.find_element(By.XPATH, '//*[@id="section_review"]/div[3]/a[12]').click()
            else : next_page=driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[6]/div[3]/a['+str(page%10+2)+']').click()
            page+=1
        except: break
            

df4=add_dataframe(name_,category_,reviews,stars,cnt)
#save()
df4.to_csv('air3_result.csv')
