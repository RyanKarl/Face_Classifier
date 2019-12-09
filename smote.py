#!/usr/bin/env python
# coding: utf-8

# In[61]:


import numpy as np
import random
import pickle
from imblearn.over_sampling import SMOTE


# In[62]:


with open('encodings.pickle', 'rb') as f:
    encodings = pickle.load(f, encoding='latin1')
len(encodings['encodings'])


# In[63]:


# sm = SMOTE(sampling_strategy='auto')
# sm


# In[57]:


# names_ryan = []
# names_pt = []

# enc_ryan = []
# enc_pt = []


# In[58]:


# for name, enc in zip(encodings['names'], encodings['encodings']):
#     if name == 'ryan_karl':
#         names_ryan.append('ryan_karl')
#         enc_ryan.append(enc)
#     else:
#         names_pt.append('patrick_tinsley')
#         enc_pt.append(enc)


# In[59]:


# encodings_ryan = {
#     'names':names_ryan,
#     'encodings':enc_ryan
# }
# encodings_pt = {
#     'names':names_pt,
#     'encodings':enc_pt
# }


# In[65]:


for i in range(6000-101):
    X, y = SMOTE().fit_resample(encodings['encodings'], encodings['names'])
    encodings['encodings'].append(X[-1])
    encodings['names'].append(y[-1])


# In[69]:


len(encodings['encodings'])


# In[70]:


with open('smoted_encodings.pickle', 'wb') as f:
    pickle.dump(encodings, f)


# In[ ]:




