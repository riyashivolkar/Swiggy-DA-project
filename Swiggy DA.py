#!/usr/bin/env python
# coding: utf-8

# In[93]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[94]:


df=pd.read_csv(r"C:\Users\Ri\Downloads\ETL\DATA/Swiggy Bangalore Outlet Details.csv")
df.head()


# In[95]:


df.columns


# In[96]:


df.dtypes


# In[97]:


df.isnull().sum()


# In[98]:


df['Rating'].unique()


# In[99]:


df.replace('--',0,inplace=True)


# In[100]:


df['Rating'].unique()


# In[101]:


df['Rating'].dtype


# In[102]:


df['Rating']=df['Rating'].astype(float)


# In[103]:


df['Rating'].dtype


# In[104]:


df.head()


# In[105]:


df_rate=df.groupby('Shop_Name')['Rating'].mean().to_frame().reset_index()
df_rate.columns=['restaurant','avg_rating']
df_rate.head(20)


# In[106]:


sns.distplot(df_rate['avg_rating'])


# In[107]:


chains=df['Shop_Name'].value_counts()[0:20]
sns.barplot(x=chains,y=chains.index)
plt.title('Most famous Restaurant chains in Bangalore')
plt.xlabel('Number of outlets')


# In[108]:


df.head()


# In[109]:


restaurant=[]
location=[]
for key,location_df in df.groupby('Location'):
    location.append(key)
    restaurant.append(len(location_df['Shop_Name'].unique()))


# In[110]:


df_total=pd.DataFrame(zip(location,restaurant))
df_total.columns=['Location','Shop_Name']
df_total.head()


# In[111]:


df_total.set_index('Location',inplace=True)
df_total.head()


# In[112]:


df_total.sort_values(by='Shop_Name').tail(10).plot.bar()


# In[113]:


df.head()


# In[114]:


Cuisine=df['Cuisine'].value_counts()[0:10]
Cuisine


# In[115]:


import plotly.graph_objs as go
from plotly.offline import iplot


# In[116]:


trace1=go.Bar(
x=df['Cuisine'].value_counts()[0:10].index,
y=df['Cuisine'].value_counts()[0:10])


# In[117]:


iplot([trace1])


# In[118]:


df.columns


# In[31]:


df['Cost_for_Two'].isna().sum()


# In[32]:


df['Cost_for_Two'].dtype


# In[34]:


df['Cost_for_Two'].unique()


# In[35]:


df['Cost_for_Two']=df['Cost_for_Two'].apply(lambda x: x.replace('₹ ',''))


# In[36]:


df['Cost_for_Two'].unique()


# In[37]:


df['Cost_for_Two']=df['Cost_for_Two'].astype(int)


# In[38]:


df['Cost_for_Two'].dtype


# In[39]:


df.head()


# In[40]:


sns.scatterplot(x='Rating',y='Cost_for_Two',data=df)


# In[41]:


df['Cost_for_Two'].min()


# In[42]:


df['Cost_for_Two'].max()


# In[45]:


df[df['Cost_for_Two']==800]['Shop_Name']


# In[46]:


data=df.copy()


# In[47]:


data.set_index('Shop_Name',inplace=True)


# In[48]:


data.head()


# In[52]:


data['Cost_for_Two'].nlargest(10).plot.bar()


# In[54]:


data[data['Cost_for_Two']<=500]


# In[57]:


df_budget=data[data['Cost_for_Two']<=500].loc[:,('Cost_for_Two')]
df_budget=df_budget.reset_index()
df_budget.head()


# In[59]:


df[(df['Rating']>4)& (df['Cost_for_Two']<=500)].shape


# In[62]:


len(df[(df['Rating']>4)& (df['Cost_for_Two']<=500)]['Shop_Name'].unique())


# In[64]:


df_new=df[(df['Rating']>4 )& (df['Cost_for_Two']<=500)]
df_new.head()


# In[65]:


location=[]
total=[]



for loc,location_df in df_new.groupby('Location'):
    location.append(loc)
    total.append(len(location_df['Shop_Name'].unique()))


# In[66]:


location_df=pd.DataFrame(zip(location,total))
location_df.head()


# In[67]:


location_df.columns=['location','restaurant']


# In[68]:


location_df.head()

