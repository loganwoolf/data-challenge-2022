import pandas as pd
df = pd.read_csv('aus_weather.csv')
seasons = df[(df['season'] == 'summer') | (df['season'] == 'winter')]

grouped = seasons.groupby(['Location', 'season'])[['Temp9am']].mean()
semi = grouped.unstack(level=1)
semi['range'] = semi['Temp9am']['summer'] - semi['Temp9am']['winter']
semi.head(3)