#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd

x = pd.read_excel (r'C:/Users/Anindita/Desktop/X.xlsx',index_col=0)['Chicken']
y = pd.read_excel (r'C:/Users/Anindita/Desktop/Y.xlsx',index_col=0)['Egg']
df = pd.concat([y,x],axis=1)
df.columns = ['Y','X']
df.head(41)


# In[12]:


# Plot the time series
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
df.Y.plot(figsize=(8,4))
df.X.plot(figsize=(8,4))
plt.show()


# In[13]:


plt.scatter(df.Y,df.X)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()


# In[2]:


import pandas as pd

x = pd.read_excel (r'C:/Users/Anindita/Desktop/X1.xlsx',index_col=0)['Chicken_Difference']
y = pd.read_excel (r'C:/Users/Anindita/Desktop/Y1.xlsx',index_col=0)['Egg_Difference']
df = pd.concat([y,x],axis=1)
df.columns = ['Y','X']
df.head(40)


# In[3]:


# Plot the time series
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
df.Y.plot(figsize=(8,4))
df.X.plot(figsize=(8,4))
plt.show()


# In[4]:


plt.scatter(df.Y,df.X)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()


# In[5]:


#Hedge Ratio
import statsmodels.api as sm
model = sm.OLS(df.Y, df.X)
model = model.fit() 
print(model.params[0])


# In[6]:


#Spread
df['spread'] = df.Y - model.params[0] * df.X
# Plot the spread
df.spread.plot(figsize=(8,4))
plt.ylabel("Spread")
plt.show()


# In[10]:


# To perform ADF Test
from statsmodels.tsa.stattools import adfuller
# Compute ADF test statistics
adf = adfuller(df.spread, maxlag = 1)
adf[0]


# In[8]:


adf[4]


# In[ ]:


Conclusion: Since -4.05 < -3.61, Time series is Stationarity and X & Y is cointegrated with 99% certainty

