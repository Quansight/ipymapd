
# Interactive tools for MapD

MapD is cool technology.  This tool bundles MapD technologies into a user friendly IPython API.


```python
    %reload_ext ipymapd
```

    c:\users\deathbeds\ibis\ibis\sql\postgres\compiler.py:223: UserWarning: locale specific date formats (%c, %x, %X) are not yet implemented for Windows
      'for %s' % platform.system()
    

## Connecting to a database

* List known connections

Return known MapD database connections using a configuration file.

    %mapd connect

Connect to a database connection.


```python
    %mapd connect metis
```

    <ibis.mapd.client.MapDClient object at 0x00000236D74E1940> contains the tables: ['flights_donotmodify', 'contributions_donotmodify', 'tweets_nov_feb', 'zipcodes_orig', 'zipcodes', 'demo_vote_clean']
    

List the tables in the connection.  This could return a sick widget to explore the data.

    %mapd table metis --interactive

Connect to a database using arguments

    %mapd connect \
    --user mapd \
    --password HyperInteractive \
    --host metis.mapd.com \
    --port 443 \
    --database mapd \
    --protocol https 

## Queries



```python
    %%mapd 
    SELECT goog_x as x, goog_y as y, tweets_nov_feb.rowid FROM tweets_nov_feb limit 10
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>x</th>
      <th>y</th>
      <th>rowid</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-6.494699e+06</td>
      <td>-4122946.500</td>
      <td>11232</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-4.279343e+05</td>
      <td>4904413.000</td>
      <td>11233</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-9.807124e+06</td>
      <td>5091781.500</td>
      <td>11234</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-1.316743e+07</td>
      <td>4024572.500</td>
      <td>11235</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-5.571405e+06</td>
      <td>-3475819.500</td>
      <td>11248</td>
    </tr>
    <tr>
      <th>5</th>
      <td>-4.337398e+06</td>
      <td>-1370884.875</td>
      <td>11249</td>
    </tr>
    <tr>
      <th>6</th>
      <td>4.758664e+06</td>
      <td>2412860.000</td>
      <td>11250</td>
    </tr>
    <tr>
      <th>7</th>
      <td>-1.024692e+07</td>
      <td>1706442.000</td>
      <td>11251</td>
    </tr>
    <tr>
      <th>8</th>
      <td>-1.080943e+07</td>
      <td>3844545.750</td>
      <td>5216</td>
    </tr>
    <tr>
      <th>9</th>
      <td>-6.514333e+06</td>
      <td>-4092641.750</td>
      <td>11236</td>
    </tr>
  </tbody>
</table>
</div>



## Visualization

The `mapd` magic may accept yaml in the body.  When `yaml` is used we return a visualization.


```python
    %%mapd
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
```




    <mapd_renderer.MapDBackendRenderer at 0x236d6129278>



Disconnect the last database that was created


```python
    %mapd disconnect 
```

## Completion

* Queries have completion
* The line magic has completion

## Alternatives

* ibis.mapd

## Assumptions

* A user will experiment with a query before visualizing it.
* Typing out the connection information in _unfun_


```python
if __name__ == '__main__':
    !jupyter nbconvert --to markdown readme.ipynb
```
