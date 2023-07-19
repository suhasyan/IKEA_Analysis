#!/usr/bin/env python
# coding: utf-8

# In[33]:


# import python libraries

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt # visualizing data
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[34]:


#import csv file
df = pd.read_csv(r"C:\Users\saikr\\IKEA_Sales in (2022)_Analysis data.csv",encoding= 'unicode_escape')


# In[3]:


df.shape


# In[4]:


df.head()


# In[5]:


df.info()


# In[6]:


#drop unrelated/blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)


# In[7]:


#check for null values
df.isnull().sum()


# In[8]:


#drop null values
df.dropna(inplace=True)


# In[9]:


#change the type of data
df['Amount'] = df['Amount'].astype(int)


# In[10]:


df['Amount'].dtype


# In[11]:


df.columns


# In[12]:


#rename Column
df.rename(columns={'Marital_Status':'Shaadi'})


# In[13]:


# describe() method returns description of the data in the DataFrame (i.e. count, mean, std, etc)
df.describe()


# In[14]:


#use describe for specific columns
df[['Age', 'Orders', 'Amount']].describe()


# # Exploratory Data Analysis [EDA]
# Gender

# In[15]:


# plotting a bar chart for Gender and it's count
ax = sns.countplot(x = 'Gender', data=df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[16]:


# plotting a bar chart for gender vs total amount
sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x='Gender', y='Amount', data=sales_gen);


# From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men

# # Age

# In[17]:


ax = sns.countplot(data=df, x = 'Age Group', hue='Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[18]:


# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x='Age Group', y='Amount', data=sales_age)


# From above graphs we can see that most of the buyers are of age group between 26-35 yrs female

# # State

# In[19]:


# total number of orders from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values('Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(x='State', y='Orders', data=sales_state)


# In[20]:


# total amount/sales from top 10 states
sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values('Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(x='State', y='Amount', data=sales_state)


# From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively

# # Maritial Status

# In[24]:


ax = sns.countplot(data = df, x = 'Marital_Status')

for bars in ax.containers:
    ax.bar_label(bars)


# In[25]:


sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values('Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(x='Marital_Status', y='Amount', data=sales_state, hue='Gender')


# From above graphs we can see that most of the buyers are married (women) and they have high purchasing power

# # Occupation

# In[26]:


sns.set(rc={'figure.figsize':(20, 5)})
ax = sns.countplot(data=df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[27]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values('Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_state, x='Occupation', y='Amount')


# # Product Category

# In[28]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data=df, x='Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[29]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values('Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_state, x='Product_Category', y='Amount')


# # Product Id

# In[30]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Amount'].sum().sort_values('Amount', ascending = False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(x='Product_ID', y='Amount', data=sales_state)


# In[32]:


#top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# # Conclusion:

# Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category
# 
# 

# My Github profile:https://github.com/suhasyan

# # Thank you

# In[ ]:




