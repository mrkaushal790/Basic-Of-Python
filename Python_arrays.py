#!/usr/bin/env python
# coding: utf-8

# In[2]:


import array as arr


# In[23]:


a=arr.array('i',[2,3,4,5])


# In[9]:


a[0]


# In[10]:


a[2]


# In[11]:


a[10]


# In[12]:


a[-1]


# In[13]:


a[-3]


# In[14]:


a[-6]


# In[16]:


a[0]=100
a


# In[18]:


a[2]=101
a


# In[19]:


a[3]=0
a


# In[25]:


a


# In[24]:


b=a[1:3]
b


# In[26]:


c=a[0:3]


# In[27]:


c


# In[28]:


d=a[2:4]
d


# In[29]:


e=a[0:10]
e


# In[30]:


a[10]
a


# In[31]:


f=a[3:100]


# In[32]:


f


# In[33]:


g=a[4:100]
g


# In[46]:


import array as arr
sample_array=arr.array('i',[4,9,12,2,6,100])
sample_array


# In[38]:


sample_array[0:4]


# In[47]:


del sample_array[2]
sample_array


# In[ ]:


### Concatenation


# In[48]:


a=arr.array('d',[1.1,2.2,3.1,4.4,7.8])
b=arr.array('d',[5.6,10.4])
c=arr.array('d')
c=a+b
c


# In[50]:


a=arr.array('d',[1.1,2.2,3.1,4.4,7.8])
b=arr.array('d',[5.6,10.4])
c=arr.array('d')
c=a*b
c


# In[59]:


a=arr.array('d',[1.1,2.2,3.1,4.4,7.8])
b=arr.array('d',[5.6,10.4])
c=arr.array('d')
c=b+a
c


# In[54]:


c[-1]


# In[55]:


c[1:3]


# In[61]:


c[-6:-4]


# In[ ]:




