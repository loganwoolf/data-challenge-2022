"""

import pandas as pd
df = pd.read_csv('dubai_properties_data.csv')

# old way - averages of both columns were computed for each neighborhood
df.groupby(['neighborhood'])[["price","price_per_sqft"]].mean()

# new way - using the aggregate function .agg()
df.groupby(['neighborhood']).agg({'price' : 'mean', 'price_per_sqft' : 'max'})

# two aggregations in one column
df.groupby(['neighborhood']).agg({'price' : ['mean','max']})
"""

# Challenge
# Using the functions described above, which neighborhood has the biggest difference between maximum and minimum property price?

import pandas as pd
df = pd.read_csv('dubai_properties_data.csv')
minmax = df.groupby(['neighborhood']).agg({'price' : ['min', 'max']})
minmax['range'] = minmax['price']['max'] - minmax['price']['min']
minmax.sort_values('range', ascending=False).head()