#!/usr/bin/env python
# coding: utf-8

"""    %%mapd metis
    select * from zipcodes limit 10
"""

# In[34]:


@λ.dataclasses.dataclass()
class f():...


# In[10]:


from .connection import MapDConfig


# In[2]:


mapd = MapDConfig('config.ini')['metis'].connect()


"""Create a magic class that stores the current connection info.
"""

# In[9]:


def mapd_query(line, cell):
    return mapd.raw_sql(line, results=True).to_df()


# In[8]:


mapd_query(mapd.table('flights_donotmodify').limit(10).compile())


# In[19]:


import argparse


"""This is shit
"""

# In[29]:


parser = argparse.ArgumentParser('mapd', '')
parser.add_argument('--alias', help='An alias in the configuration file.')
parser.add_argument('--config')
# add the other database params
parser.set_defaults(config='config.ini')

