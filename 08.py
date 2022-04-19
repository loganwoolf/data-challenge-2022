import pandas as pd

df = pd.read_csv('paris_landmarks.csv')
print(df.sort_values(by='price').tail())

print(df['queue_time'].mean())