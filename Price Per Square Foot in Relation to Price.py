
# coding: utf-8

# In[4]:


import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
import pandas as pd


# In[41]:


df = pd.read_csv('train.csv')
df.head()


# In[42]:


print(df.shape)


# In[43]:


df = df[df.GarageArea != 0]
df = df[df.TotalBsmtSF != 0]
#remove outlier
df = df[df.TotalBsmtSF < 4000]
df.shape


# In[60]:


trace1 = go.Scatter(
    x = df['GarageArea'],
    y = df['SalePrice'],
    name = 'Garage Area',
    mode = 'markers',
    marker = dict(
        size = 10,
        color = 'rgba(65,105,225, .8)',
        line = dict(
            width = 2,
            color = 'rgb(0, 0, 0)',
        )
    )
)

trace2 = go.Scatter(
    x = df['TotalBsmtSF'],
    y = df['SalePrice'],
    name = 'Basement Area',
    mode = 'markers',
    marker = dict(
        size = 10,
        color = 'rgba(34,139,34, .9)',
        line = dict(
            width = 2,
        )
    )
)


# In[69]:


data = [trace1,trace2]

layout = dict(title = 'Correlation Between House Price ($) and Garage/Basement Area (sf)',
              yaxis = dict(zeroline = True, showgrid = False),
              xaxis = dict(zeroline = True, showgrid = False),
             )

fig = dict(data=data, layout=layout)
py.iplot(fig, filename='styled-scatter')

