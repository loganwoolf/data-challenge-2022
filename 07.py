import pandas as pd
df = pd.read_csv('fc_barcelona.csv')

games_played = pd.Series(df.MP)
print(1, games_played.max())

attendance = pd.Series(df.Attendance.dropna()) # skipping missing values (NaN) because there were no fans during 2020-2021 season because of COVID
print(2, attendance.mean())

wins = pd.Series(df.W)
losses = pd.Series(df.L)
diff = wins.median() - losses.median()
print(3, diff)
print(4, wins.min())

points = pd.Series(df.Pts)
range = points.max() - points.min()
print(5, range)