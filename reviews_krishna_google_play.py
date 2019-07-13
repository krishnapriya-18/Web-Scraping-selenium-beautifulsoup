#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from bs4 import BeautifulSoup
import time
import datetime


# In[2]:


browser = webdriver.Chrome()
url="https://play.google.com/store/apps/details?id=org.me.mobiexpensifyg&hl=en&showAllReviews=true"


# In[3]:


browser.maximize_window()
browser.get(url)
time.sleep(90)
html = browser.page_source.encode('utf-8').strip()
soup=BeautifulSoup(html,'html.parser')
reviews = soup.find_all('div', {"class":"d15Mdf bAhLNe"})


# In[4]:


# browser.maximize_window()
# browser.get(url)
# pause_time = 2
# last_height = browser.execute_script("return document.body.scrollHeight")
# start = datetime.datetime.now()
# while True:
#     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(pause_time)
#     new_height = browser.execute_script("return document.body.scrollHeight")  
#     if new_height == last_height:
#         break
#     else:
#         last_height = new_height
# end = datetime.datetime.now()
# delta = end-start
# print("[INFO] Total time taken to scroll till the end {}".format(delta))
# html = browser.page_source.encode('utf-8').strip()
# soup=BeautifulSoup(html,'html.parser')
# reviews = soup.find_all('div', {"class":"d15Mdf bAhLNe"})


# In[5]:


for tag in reviews:
    print(str(tag))
browser.quit()


# In[6]:


len(reviews)


# In[7]:


filename = "Expensify_reviews.csv"
f=open(filename,'w', encoding="utf-8")

headers = "reviewer_name, rating, review_date, upvote, review\n"

f.write(headers)

for review in reviews:
    title_reviewer=review.findAll('span',{'class':'X43Kjb'})
    reviewer_name=title_reviewer[0].text.strip()
    
    title_rating=review.find('div',{'class':'pf5lIe'})
    rating=title_rating.div['aria-label']
    
    title_date=review.findAll('span',{'class':'p2TkOb'})
    review_date=title_date[0].text.strip()
    
    title_upvote=review.findAll('div',{'class':'jUL89d y92BAb'})
    upvote=title_upvote[0].text.strip()
    
    title_review=review.findAll('span',{'jsname':'bN97Pc'})
    review=title_review[0].text.strip()
    
    f.write(reviewer_name.replace(","," ")+","+ rating+"," +review_date.replace(","," ")+","+ upvote+"," +review.replace(","," ")+ "\n")

f.close()


# In[ ]:




