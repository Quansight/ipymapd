#!/usr/bin/env python
# coding: utf-8

"""# `ipymapd` argparsing
"""

# In[39]:


import pytest


# In[5]:


from argparse import ArgumentParser
parser = ArgumentParser()
subparser = parser.add_subparsers()
# need to add a file input for the configuration.

connect = subparser.add_parser('connect')
connect.add_argument('name', nargs='?')
connect.add_argument('--user')
connect.add_argument('--password', default="HyperInteractive")
connect.add_argument('--host')
connect.add_argument('--port', type=int)
connect.add_argument('--database')
connect.add_argument('--protocol')

disconnect = subparser.add_parser(
    'disconnect', help="Disconnect from the current database,"
)
disconnect.add_argument('--disconnect', action='store_false')


   
table = subparser.add_parser('table')
table.add_argument('name')
table.add_argument('--interactive', action='store_true')
None


# In[2]:


def parse(cmd):
    return vars(parser.parse_args(cmd.split()))


# In[42]:


def test_nada():
    assert not parse("")


# In[43]:


def test_connect():
    assert parse("connect")['name'] == None
    assert parse("connect metis")['name'] == 'metis'
    bespoke =  parse("""connect --user mapd --password HyperInteractive --host metis.mapd.com --port 443 --database mapd --protocol https """)
    assert bespoke == {'name': None,
     'user': 'mapd',
     'password': 'HyperInteractive',
     'host': 'metis.mapd.com',
     'port': 443,
     'database': 'mapd',
     'protocol': 'https'}

    


# In[44]:


def test_disconnect():
    assert parse('disconnect')['disconnect'] is True


# In[45]:


def test_table():
    with pytest.raises(SystemExit): 
        parse("table")
    assert parse("table metis") == {'name': 'metis', 'interactive': False}


# In[7]:


if __name__ == '__main__':
    get_ipython().system('ipython -m pytest -- arguments.ipynb')

