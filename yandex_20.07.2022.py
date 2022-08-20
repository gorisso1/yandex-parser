#! /usr/bin/env python
# -*- coding: utf-8 -*-




from multiprocessing.sharedctypes import Value

from time import sleep
import time
import json

from unicodedata import category
import undetected_chromedriver
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import sys,os
from datetime import datetime
import re
from urllib.parse import urlparse
import sys
import os
import undetected_chromedriver as uc
from selenium.common.exceptions import NoSuchElementException 
from twocaptcha import TwoCaptcha
#безголовый запуск
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')

dev_arr = [] 
deb_arr = []

df = pd.read_excel('festivalnew.xlsx')
#массивы которые будут загружаться данными для переноса на новый прайс лист#_________________________
name_arr = []
price_arr=[]
link_arr = []
categories_arr = []
Description_arr=[]
price_market_arr = []
sex_arr = []
name_arr_market = []
family_arr = []
tip_arr = []

#загружаем последние данные если они есть если нет то выбросит исключение_______________



try: 
  nb = pd.read_excel('festival_parsnew.xlsx')
  num_rown_who = nb.count()[0]
  i = 0 
  while num_rown_who>i:
    name_arr.append(nb['Product Name'].iloc[i])
    price_arr.append(nb['Price list'].iloc[i])
    link_arr.append(nb['photo'].iloc[i])
    Description_arr.append(nb['Description'].iloc[i])
    categories_arr.append(nb['Categories'].iloc[i])
    price_market_arr.append(nb['Market price'].iloc[i])
    name_arr_market.append(nb['Product_name_ya'].iloc[i])
    sex_arr.append(nb['sex'].iloc[i])
    family_arr.append(nb['Family'].iloc[i])
    tip_arr.append(nb['TIP'].iloc[i])
    i = i+1
  
except Exception as ex:
  print(ex)
  name_arr = []
  price_arr=[]
  link_arr = []
  categories_arr = []
  Description_arr=[]
  price_market_arr = []
  sex_arr = []
  name_arr_market = []
  family_arr = []
  tip_arr = []



#______________________________________________________________________________

def captcha():
  try:
     
     driver.execute_script('''document.querySelector("#root > div > div > form > div.Spacer.Spacer_auto-gap_bottom > div > div > div.CheckboxCaptcha-Anchor > input").click()''')
     time.sleep(5)
     img =driver.find_elements(by=By.CSS_SELECTOR, value = 'img.AdvancedCaptcha-Image')[0].get_attribute('src')
     print(img)
     sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

      

     api_key = os.getenv('APIKEY_2CAPTCHA', '434a29710a6d779ab77cf72c27d4352f')

     solver = TwoCaptcha(api_key)

        
     result = solver.normal(img)
     result = result["code"]
     print(result)
     driver.find_elements(by=By.CSS_SELECTOR, value = 'input.Textinput-Control')[0].send_keys('{}'.format(result))
     driver.execute_script('''document.querySelector("#advanced-captcha-form > div > div.AdvancedCaptcha-FormActions > button.Button2.Button2_size_l.Button2_view_action").click()''')
    


                
            

        
  except Exception as ex:
    
    print('нет капчи')
    

def verification():#Функция последний товар по индексу__________________________________
  try:
    table= nb.count()[0]
    item = 0
    while num_rown_who>item:
      item = item + 1
    if item == num_rown_who:
      return item
  except Exception:
    return 0
#_____________________________________________________________________________________
#Читаем прайс лист который нужен нам



def open_ex():
  
  
  
  num_rows = 1973
  
  i =  verification()
  
  while i<num_rows:
   name = df['Название товара'].iloc[i]
   price = df['Цена товара'].iloc[i]
   dev_arr = [] 
   deb_arr = []
   
 
   print(name)
   

   print(price)
   
   i = i +1
 
   driver_market(name,price)
#------------------------------------------------------------------------------------------------

# Открываем драйвер selenium
#________________________________________________________________________________________________
def driver_market(name,price):
 try:
    url = 'https://market.yandex.ru/'
    driver.get(url)
    time.sleep(2)
    captcha()
    time.sleep(3)
    

    search = driver.find_elements(by=By.CSS_SELECTOR, value = 'input#header-search')[0].send_keys('{}'.format(name))#фотка
    
      

    poisk = driver.execute_script('''document.querySelector("body > div._111XI.main > header > noindex > div > div > div._1GYM8 > div._2zPWB > div > div > form > div > button").click()''')
    
    time.sleep(5)
    captcha()
    len_products =  len(driver.find_elements(by=By.CSS_SELECTOR, value = 'a._2f75n._24Q6d.cia-cs'))
    if len_products > 0:
      click_product = driver.find_elements(by=By.CSS_SELECTOR, value = 'a._2f75n._24Q6d.cia-cs')[0].get_attribute('href')
      price_market = driver.find_elements(by=By.CSS_SELECTOR, value='div._3NaXx._33ZFz._2m5MZ')[0].text
      price_market = re.findall('\d', '{}'.format(price_market))
    
      driver.get(click_product)
      captcha()
      time.sleep(5)
      
     
    
    
      description = driver.find_elements(by=By.CSS_SELECTOR, value = 'div._1uLae')
      for i in description:
        description = i.text

      if len(description) ==0:
        description ='0'
    
      print(description)
      img = check_element()
      
      print(img)

      
      dev = driver.find_elements(by=By.CLASS_NAME, value = '_2TxqA')

      for i in dev:
        print(i.text)
        dev_arr.append(i.text)

      deb = driver.find_elements(by=By.CLASS_NAME, value = '_3PnEm')

      for i in deb:
        print('Вторая сторона')
        print(i.text)
              
        deb_arr.append(i.text)
      
      dic = dict(zip(dev_arr, deb_arr))
      print(dic)


      name_ya = driver.find_element(by=By.CSS_SELECTOR, value = 'h1._1BWd_').text
      

      
      
      

      categories =  driver.find_elements(by=By.CSS_SELECTOR, value = 'ul._2m7_o._1lmw2 >li')
      categori_arr = []
      for i in categories:
        categori_arr.append(i.text)

      sex  = driver.find_elements(by=By.CSS_SELECTOR, value = 'td._3M0mF > a')
      for i in sex:
        if i.text == 'женский':
          categori_arr.append('Женская парфюмерия')
        elif i.text == 'мужской':
          categori_arr.append('Мужская парфюмерия')
        elif i.text == 'унисекс':
          categori_arr.append('Унисекс')


      
      
      categories  = ",".join(categori_arr)
      
      price_ya = driver.find_element(by = By.CSS_SELECTOR, value = 'div._2NvRE>div.cia-vs').get_attribute('data-zone-data')
      price_ya  = json.loads(price_ya)
      print(price_ya['price'])

      
      name_arr.append(name)
      name_arr_market.append(name_ya)
      sex_arr.append(dic.get('Пол'))
      tip_arr.append(dic.get('Тип'))
      family_arr.append(dic.get('Семейство'))
      price_market_arr.append(price_ya['price'])
      price_arr.append(price)
      link_arr.append(img)
      Description_arr.append(description)
      categories_arr.append(categories)
      print(categories_arr)
      create_ex()

      time.sleep(5)
    else:
      name_arr.append(name)
      price_arr.append(price)
      price_market_arr.append(0)
      link_arr.append('https://image-cdn.kazanexpress.ru/bti8bhnqo07bc3qcner0/original.jpg')
      Description_arr.append(0)
      
      categories_arr.append('Без категории')
      sex_arr.append(0)
      tip_arr.append(0)
      family_arr.append(0)
      name_arr_market.append('нету')
      create_ex()
      

    


    
        
          
          
         

 

 except Exception as ex:
    print(ex)
    driver.close()
    driver.quit()
    from threading import Timer
    Timer(2.0, lambda: os.execv(sys.executable, [sys.executable] + sys.argv)).start()

#----------------------------------------------------------



def create_ex():
  try:
 #df.loc[len(df.index)] = [name_product, category, int(price_int), description_product, feature_product, img_product, dic.get('Артикул:'), dic.get('Бренд:'), dic.get('Вес, кг:'), dic.get('Вес брутто:'), dic.get('Вес брутто, кг:'), dic.get('Размеры, мм:'), dic.get('Страна-производитель:'), dic.get('Длина, мм:'), dic.get('Толщина, мм:'), dic.get('Высота:')]
    # cc.loc[len(cc.index)] = [name_arr,categories_arr, price_arr, Description_arr, link_arr ,price_market_arr, dic.get('Пол'), dic.get('Семейство'), dic.get('Тип')]
    # cc.to_excel('festival_pars.xlsx')
    cc = pd.DataFrame({
    'Product Name': name_arr,
    'Price list': price_arr,
    'photo': link_arr,    
    'Description':Description_arr,
    'Categories': categories_arr,
    'Product_name_ya': name_arr_market,
    'Market price': price_market_arr,
    'sex' : sex_arr,
    'Family': family_arr,
    'TIP': tip_arr
    

  #  
  #  
  #  
  #  
  #
   })       
    cc.to_excel('festival_parsnew.xlsx')
     
    

  except Exception as ex:
    print(ex)
    from threading import Timer
    Timer(2.0, lambda: os.execv(sys.executable, [sys.executable] + sys.argv)).start()

def check_element():
  try:
        img = driver.find_element(by=By.CLASS_NAME, value = '_3Wp6V').get_attribute('src')
        return img 
  except NoSuchElementException:
        img = 0
        return img
    

if __name__ == "__main__":
   # options = webdriver.ChromeOptions() # удалите комментария если вам нужен безголовый selenium
   # options.headless = True  #удалите комментария если вам нужен безголовый selenium
    
    driver = uc.Chrome()# options=options добавить если вы хотите безголовый запуск
    open_ex()
    