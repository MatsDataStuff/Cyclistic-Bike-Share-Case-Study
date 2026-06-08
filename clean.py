import pandas as pd
import os
import glob

# grab all csvs from the same folder as this script
folder = os.path.dirname(os.path.abspath(__file__))
files = glob.glob(os.path.join(folder, "*.csv"))

print("files found:", files)

df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
print(f"rows loaded: {len(df)}")

# parse timestamps
df['started_at'] = pd.to_datetime(df['started_at'])
df['ended_at'] = pd.to_datetime(df['ended_at'])

# ride length in minutes
df['ride_length'] = (df['ended_at'] - df['started_at']).dt.total_seconds() / 60

# day, month, hour
day_map = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday',
           4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
month_map = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
             7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}

df['day_of_week'] = df['started_at'].dt.dayofweek.map(day_map)
df['month'] = df['started_at'].dt.month.map(month_map)
df['hour'] = df['started_at'].dt.hour

# drop bad rides (under 1 min or over 24 hrs)
df = df[df['ride_length'].between(1, 1440)]

# drop rows missing key fields
df = df.dropna(subset=['start_station_name', 'end_station_name', 'member_casual'])

# keep only valid user types
df = df[df['member_casual'].isin(['member', 'casual'])]

print(f"rows after cleaning: {len(df)}")
print(df.head())

# save
out = os.path.join(folder, "cyclistic_clean.csv")
df.to_csv(out, index=False)
print(f"saved to: {out}")
