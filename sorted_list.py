#!/usr/bin/env python
# coding: utf-8

# In[6]:


def last(n): return n[-1]

def sorted_list(tupples):
    return sorted(tupples, key=last)


# In[7]:


sorted_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])


# In[ ]:





# In[ ]:




