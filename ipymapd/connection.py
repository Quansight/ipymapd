#!/usr/bin/env python
# coding: utf-8

"""# connection files

One of the least interactive steps in using pymapd is creating a connection, but it requires a considerable amount of text.  

Placing connections in configuration files could make it easier for folks to connect the mapd database.

    pymapd
"""

# In[2]:


## A Connection Manager


"""* is docker a default?
"""

# In[3]:


import ibis.mapd
import configparser
from collections import UserDict
from pathlib import Path
from pandas import DataFrame

__all__ = 'MapDConfig',


"""`MapDConfig` establishes an API to ease the creation of a MapD Ibis instances.

    >>> manager = MapDConfig('config.ini')
    >>> assert manager.list(), "There is no connection information in the database"
    >>> assert manager._repr_html_().startswith('<table'), "There is no html representation"
    >>> assert isinstance(manager['metis'], MapdConnectionDict)
"""

# In[4]:


class MapDConfig(configparser.ConfigParser):
    def __init__(self, *files):
        super().__init__(), list(map(self.read, files))
                
    def _repr_html_(self):
        sections = self.sections()
        return DataFrame([
            self[object] for object in sections
        ], sections).to_html()


"""The dictionary should likely be a namespace instead.
"""

# In[5]:


class MapdConnectionDict(UserDict):
    def connect(self): return ibis.mapd.connect(**self)


# In[6]:


if __name__ == '__main__': 
    mapd = manager['metis'].connect()

