#!/usr/bin/env python
# coding: utf-8

# In[72]:


import pandas as pd

x = pd.read_excel (r'C:/Users/Anindita/Desktop/X.xlsx',index_col=0)['Chicken']
y = pd.read_excel (r'C:/Users/Anindita/Desktop/Y.xlsx',index_col=0)['Egg']
df = pd.concat([y,x],axis=1)
df.columns = ['Y','X']
df.head(14)               


# In[73]:


# Plot the time series
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
df.Y.plot(figsize=(8,4))
df.X.plot(figsize=(8,4))
plt.show()


# In[74]:


import pandas as pd

x = pd.read_excel (r'C:/Users/Anindita/Desktop/X.xlsx',index_col=0)['Chicken_Difference']
y = pd.read_excel (r'C:/Users/Anindita/Desktop/Y.xlsx',index_col=0)['Egg_Difference']
df = pd.concat([y,x],axis=1)
df.columns = ['Y','X']
df.head(14)


# In[75]:


# Plot the time series
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
df.Y.plot(figsize=(8,4))
df.X.plot(figsize=(8,4))
plt.show()


# In[76]:


plt.scatter(df.Y,df.X)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()


# In[77]:


#Hedge Ratio
import statsmodels.api as sm
model = sm.OLS(df.Y, df.X)
model = model.fit() 
print(model.params[0])


# In[80]:


#Spread
df['spread'] = df.Y - model.params[0] * df.X
# Plot the spread
df.spread.plot(figsize=(8,4))
plt.ylabel("Spread")
plt.show()


# In[94]:


# To perform ADF Test
from statsmodels.tsa.stattools import adfuller
# Compute ADF test statistics
adf = adfuller(df.spread, maxlag = 1)
adf[0]


# In[90]:


adf[4]


# In[ ]:


Conclusion: Since -2.64 ~ -2.72, Time series is Stationarity and X & Y is cointegrated with 90% certainty

