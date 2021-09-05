#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
url = BeautifulSoup('http://www.nepalstock.com/todaysprice', "html.parser")
response = requests.get(url)
response


# In[2]:


data = response.text
data


# In[3]:


soup = BeautifulSoup(data, 'lxml')
soup


# In[4]:


tag = soup.find_all('tr')
tag


# In[5]:


soup = soup.table
soup


# In[6]:


x = []
for i in tag:

   y =i.get_text()
   x.append(y)
print(x)


# In[7]:


x


# In[8]:


z = []
for i in x:
  a = i.split('\n')[1:10]
  z.append(a)
print(z)


# In[9]:


z


# In[12]:


del z[-4:-1]


# In[13]:


del z[-1]


# In[15]:


del z[0]


# In[16]:


z


# In[17]:


import csv
f = open('Nepalshare.csv','w')
write = csv.writer(f)
for i in z:
  write.writerow(i)
  
f.close()


# In[18]:


import pandas as pd
df = pd.read_csv('Nepalshare.csv',)
df


# In[20]:


import plotly.express as px

fig = px.bar(df.iloc[0:10], x='Traded Companies', y='Amount')
fig.show()


# In[23]:


import plotly.express as px



fig = px.bar(df.iloc[0:3], x="Traded Companies", y=["No. Of Transaction", "Traded Shares", "Amount"], title="Wide-Form Input")
fig.show()


# In[25]:



import plotly.express as px
df=df.iloc[0:10]
fig = px.pie(df, values='No. Of Transaction', names='Traded Companies',title='Nepal Share')
fig.show()


# In[ ]:




