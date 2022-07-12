#!/usr/bin/env python
# coding: utf-8

# In[40]:


def last(n): return n[-1]

def sorted_tupple(tupples):
    return sorted(tupples, key=last , reverse = True)


# In[41]:


sorted_tupple([('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')])


# In[ ]:




