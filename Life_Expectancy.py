#!/usr/bin/env python
# coding: utf-8

# # Life Expectancy
# [Data Source](https://data.worldbank.org/indicator/SP.DYN.LE00.IN)
# 

# In[20]:


get_ipython().run_line_magic('matplotlib', 'inline')

import pandas as pd
import numpy as np


# In[21]:


get_ipython().system(' head data/Life_Expectancy/API_SP.DYN.LE00.IN_DS2_en_csv_v2_713010.csv')


# In[23]:


df = pd.read_csv("data/Life_Expectancy/API_SP.DYN.LE00.IN_DS2_en_csv_v2_713010.csv", header=2, index_col=[0,1,2,3])
df.head()


# In[33]:


Life_Expectancy = df.groupby(level=0).first().transpose()
Life_Expectancy.head()


# In[34]:


list (Life_Expectancy.columns)


# In[39]:


Life_Expectancy_subset = Life_Expectancy[['United States', 'China', 'Japan', 'Russian Federation', 'United Kingdom']]


# In[41]:


Life_Expectancy_subset.plot()


# In[ ]:




