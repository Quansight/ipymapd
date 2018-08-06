#!/usr/bin/env python
# coding: utf-8

"""# Magics to use MapD in the notebook.
"""

# In[14]:


from .arguments import parser
from .connection import MapDConfig
import mapd_renderer
import yaml, io
import ibis


# In[15]:


class NoConnectionException(BaseException): ...


# In[18]:


import importlib_resources


# In[2]:


from IPython.core.magic import (Magics, magics_class, line_magic, register_line_cell_magic,
                                cell_magic, line_cell_magic)

@magics_class
class MapD(Magics):
    def __init__(self, shell):
        super().__init__(shell)
        self.connections = MapDConfig()
        self.connections.read_string(importlib_resources.read_text('ipymapd', 'config.ini'))
        self.current = None
    
    @line_cell_magic
    def mapd(self, line, cell=None):
        line = vars(parser.parse_args(line.split()))
        
        if cell and not line:
            cell = yaml.load(io.StringIO(cell))
            if isinstance(cell, str):
                object = self.query
            if isinstance(cell, dict):
                object = self.view
            
            return object(cell)
        
        if line.pop('disconnect', None):
            object = self.disconnect

        elif 'interactive' in line:
            object = self.table
            del line['interactive']
        else:
            object = self.connect            
        return object(**line)
                
        
    def config(self, **object): 
        """Add a new database configuration"""

    def connect(self, **object):
        self.disconnect()
        name = object.pop('name')
        self.current = ibis.mapd.connect(**self.connections[name])
        print(f"{self.current} contains the tables: {self.current.list_tables()}")
    
    def disconnect(self, **object): 
        if self.current:
            self.current.close()

    def table(self, **object): 
        return 
    
    def query(self, object):
        if not self.current: raise NoConnectionException()
        return self.current.raw_sql(object, results=True).to_df()
    
    def view(self, object):
        return mapd_renderer.MapDBackendRenderer({
            'dbName' if 'database' == _0 else _0 : _1 
            for _0, _1 in  self.connections['metis'].items()
        }, object)


"""    mapd = ibis.mapd.connect(**MapD(get_ipython()).connections['metis'])

    query = mapd.table('tweets_nov_feb')

    q = query.projection([
        query['goog_x'].name('x'),
        query['goog_y'].name('y')
    ]).limit(10)
"""

# In[20]:


def load_ipython_extension(ip):
    ip.register_magics(MapD(get_ipython()))


"""    %mapd connect metis
"""

"""    %%mapd 
    SELECT goog_x as x, goog_y as y, tweets_nov_feb.rowid FROM tweets_nov_feb limit 10
"""

"""    %%mapd
    width: 384
    height: 564
    config: {ticks: false}
    data:
      - name: 'tweets'
        sql: 'SELECT goog_x as x, goog_y as y, tweets_nov_feb.rowid FROM tweets_nov_feb' 
    scales:
      - name: 'x'
        type: 'linear'
        domain: [3650484.1235206556, 7413325.514451755]
        range: 'width'
      - name: 'y'
        type: 'linear'
        domain: [5778161.9183506705, 10471808.487466192]
        range: 'height'
    marks:
      - type: 'points'
        from: {data: 'tweets'}
        properties:
          x: {scale: 'x', field: 'x'}
          y: {scale: 'y', field: 'y'}
          fillColor: 'green'
          size: {value: 1}
"""

"""    %mapd disconnect
"""
