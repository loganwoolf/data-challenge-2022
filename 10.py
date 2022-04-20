""" Challenge
Which neighborhood has the highest average property price and the highest size_in_sqft? """

import pandas as pd
df = pd.read_csv('dubai_properties_data.csv')

""" 
We can specify the columns we want to group by:
df.groupby(['quality'])[['price','size_in_sqft','no_of_bedrooms']].mean()

Try this line of code below and see what it does:
df.groupby(['view_of_landmark','view_of_water'])[['price','no_of_bedrooms']].mean()
"""

df.groupby(['neighborhood'], sort=False)[['price']].mean().sort_values(by="price", ascending=False).head(1)
df.groupby(['neighborhood'], sort=False)[['size_in_sqft']].mean().sort_values(by="size_in_sqft", ascending=False).head(1)
