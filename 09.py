"""
#Example - Loading Data
user_filter = pd.read_csv('wine.csv')
df.head()

#Step 1: Create filter
user_filter = df['Alcohol'] >= 14

#Step 2: Feed the filter to the original DataFrame and store the result in a new variable
filtered_df = df[user_filter]

#Step 3: Display Variable
filtered_df

# Step 1 and 2
filtered_df_2 = df[df['Alcohol'] >= 14]
"""

import pandas as pd
df = pd.read_csv('wine.csv')
under_thirteen = df[df['Alcohol'] <= 13]
print(1, len(under_thirteen))

class_three = df[df['Class'] == 3]
print(2, len(class_three))