
# Interactive tools for MapD

MapD is cool technology.  This tool bundles MapD technologies into a user friendly IPython API.


```python
%reload_ext ipymapd
```

## Connecting to a database

* List known connections

Return known MapD database connections using a configuration file.

    %mapd connect

Connect to a database connection.


```python
%mapd connect metis
```

    <ibis.mapd.client.MapDClient object at 0x113068f60> contains the tables: ['flights_donotmodify', 'contributions_donotmodify', 'tweets_nov_feb', 'zipcodes_orig', 'zipcodes', 'demo_vote_clean']


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
      <td>-13563874.0</td>
      <td>4.384050e+06</td>
      <td>4448</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-4913196.5</td>
      <td>-2.574509e+06</td>
      <td>10016</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-7009535.0</td>
      <td>-4.230903e+06</td>
      <td>4608</td>
    </tr>
    <tr>
      <th>3</th>
      <td>11907241.0</td>
      <td>-6.886003e+05</td>
      <td>4576</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-7630287.0</td>
      <td>-3.707356e+06</td>
      <td>9408</td>
    </tr>
    <tr>
      <th>5</th>
      <td>-8239380.0</td>
      <td>4.968139e+06</td>
      <td>9888</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-5436762.0</td>
      <td>-3.040998e+06</td>
      <td>4416</td>
    </tr>
    <tr>
      <th>7</th>
      <td>13476805.0</td>
      <td>1.632640e+06</td>
      <td>4960</td>
    </tr>
    <tr>
      <th>8</th>
      <td>-8241296.5</td>
      <td>4.973656e+06</td>
      <td>4449</td>
    </tr>
    <tr>
      <th>9</th>
      <td>-7277123.5</td>
      <td>-3.884417e+06</td>
      <td>9984</td>
    </tr>
  </tbody>
</table>
</div>



## Visualization

The `mapd` magic may accept yaml in the body.  When `yaml` is used we return a visualization.

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
    !jupyter nbconvert --to python ipymapd/*.ipynb
```
