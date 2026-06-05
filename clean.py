import pandas as pd
import os
import glob

# Automatically use the folder where clean.py is located
folder_path = os.path.dirname(os.path.abspath(__file__))

# DEBUG - show what files are found
all_files = glob.glob(os.path.join(folder_path, "*.csv"))
print("Files found:", all_files)

# Load all CSV files and combine into one dataframe
df = pd.concat([pd.read_csv(f) for f in all_files], ignore_index=True)

print(f"Total rows loaded: {len(df)}")

# Convert datetime columns
df['started_at'] = pd.to_datetime(df['started_at'])
df['ended_at'] = pd.to_datetime(df['ended_at'])

# Add ride_length in minutes
df['ride_length'] = (df['ended_at'] - df['started_at']).dt.total_seconds() / 60

# Add day_of_week as actual day names
days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday',
        4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
df['day_of_week'] = df['started_at'].dt.dayofweek.map(days)

# Add month as actual month names
months = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
          7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
df['month'] = df['started_at'].dt.month.map(months)

# Add hour column (useful for analysis later)
df['hour'] = df['started_at'].dt.hour

# ---- CLEAN ----
# Remove rides under 1 minute or over 24 hours (bad data)
df = df[df['ride_length'] >= 1]
df = df[df['ride_length'] <= 1440]

# Remove rows missing station names or user type
df = df.dropna(subset=['start_station_name', 'end_station_name', 'member_casual'])

# Confirm only valid user types
df = df[df['member_casual'].isin(['member', 'casual'])]

print(f"Total rows after cleaning: {len(df)}")
print(df.head())

# ---- EXPORT ----
output_path = os.path.join(folder_path, "cyclistic_clean.csv")
df.to_csv(output_path, index=False)
print(f"Clean file saved to: {output_path}")