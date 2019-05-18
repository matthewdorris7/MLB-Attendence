
# coding: utf-8

# In[ ]:


import requests
import pandas as pd
import os
import datetime
import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import csv 

driver = webdriver.Chrome(executable_path=r"C:\\Users\\Matt\\Downloads\\chromedriver.exe")


# In[ ]:


counter = 0
for month in range(4, 10):
    for day in range(1,32):
        try:
            list = []
            month = int(month)
            day = int(day)
            month ="{0:0=2d}".format(month)
            day ="{0:0=2d}".format(day)

            url = "https://www.baseball-reference.com/boxes/WAS/WAS2011" + str(month) +  str(day) +"0.shtml"
            driver.get(url)


            #element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, """<a href="javascript:void(0)">MENU</a>""")))


            date = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div[3]/div[1]""")
            list.append(date.text)
            attendence = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div[3]/div[3]""")
            list.append(attendence.text)
            time = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div[3]/div[6]""")
            list.append(time.text)
            
            try:
                weather = driver.find_element_by_xpath("""//*[@id="div_1188334583"]/div[4]""")
                list.append(weather.text) 
            except:
                weather = driver.find_element_by_xpath("""//*[@id="div_6350237457"]/div[5]""")
                list.append(weather.text)

            with open('attendenceData.csv', 'a') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(list)
            csvFile.close()

            print("Game on " + str(month) + "/"+ str(day) )
            counter = counter + 1
        except:
            continue


# In[ ]:


counter


# In[ ]:


import requests
import pandas as pd
import os
import datetime
import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import csv 

driver = webdriver.Chrome(executable_path=r"C:\\Users\\Matt\\Downloads\\chromedriver.exe")


# In[ ]:


month = int(month)
day = int(day)
month ="{0:0=2d}".format(month)
day ="{0:0=2d}".format(day)

url = "https://www.baseball-reference.com/boxes/WAS/WAS201604220.shtml"
driver.get(url)


# In[ ]:


date = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div[3]/div[1]""")
print(date.text)
list.append(date.text)


# In[ ]:


attendence = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div[3]/div[3]""")
print(attendence.text)
list.append(attendence.text)


# In[ ]:


time = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div[3]/div[6]""")
print(time.text)
list.append(time.text)


# In[ ]:


weather = driver.find_element_by_xpath("""//*[@id="div_6350237457"]/div[5]""")
print(weather.text)
list.append(weather.text)


# In[ ]:


list


# In[ ]:


import csv 
with open('attendenceData.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(list)
csvFile.close()

