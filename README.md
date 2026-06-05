# Cyclistic Bike-Share Case Study
### Google Data Analytics Professional Certificate — Capstone Project

## Introduction
The **Cyclistic Bike-Share Case Study** is a capstone project for the **Google Data Analytics Professional Certificate**. Following the data analysis process — **Ask, Prepare, Process, Analyze, Share, and Act** — this project analyzes real-world bike-share data to develop marketing strategies aimed at converting casual riders into annual members.

---

## Background
Cyclistic is a bike-share company based in Chicago with a fleet of 5,824 bicycles across 692 geotracked stations. Customers can rent bikes from one station and return them to any other station in the network at their convenience.

Cyclistic offers three pricing plans: single-ride passes, full-day passes, and annual memberships. Customers who purchase single-ride or full-day passes are referred to as **casual riders**, while customers who purchase annual memberships are **Cyclistic members**.

The company's finance team has concluded that annual members are significantly more profitable than casual riders. The director of marketing believes the key to future growth is maximizing the number of annual memberships by converting existing casual riders into members.

---

## Approach

### 1. Ask
**Business Task:** Analyze how annual members and casual riders use Cyclistic bikes differently in order to design data-driven marketing strategies that convert casual riders into annual members.

> **Guiding Question:** How do annual members and casual riders use Cyclistic bikes differently?

---

### 2. Prepare

#### Data Source
- **Source:** [Divvy Trip Data](https://divvy-tripdata.s3.amazonaws.com/index.html)
- **Period:** May 2025 – April 2026 (12 months)
- **License:** Made available by Motivate International Inc.
- **Rows:** 3,747,342 total trips

#### Tools Used
| Tool | Purpose |
|------|---------|
| Python (pandas) | Data cleaning, processing, and combining |
| SQL (Google BigQuery) | Data analysis and querying |
| Tableau Public | Data visualization and dashboard |
| GitHub | Portfolio and documentation |

#### Data Structure
| Column | Description |
|--------|-------------|
| ride_id | Unique ID for each ride |
| rideable_type | classic, electric, or docked bike |
| started_at | Date and time ride started |
| ended_at | Date and time ride ended |
| start_station_name | Name of starting station |
| end_station_name | Name of ending station |
| start_lat / start_lng | Starting coordinates |
| end_lat / end_lng | Ending coordinates |
| member_casual | Rider type: member or casual |

---

### 3. Process

Data was cleaned and processed using Python (pandas). The following steps were taken:

- Combined 12 monthly CSV files into a single dataframe (3,747,342 rows)
- Converted `started_at` and `ended_at` to datetime format
- Created `ride_length` column (duration in minutes)
- Created `day_of_week` column (Monday–Sunday)
- Created `month` column (Jan–Dec)
- Created `hour` column for time-of-day analysis
- Removed rides under 1 minute or over 24 hours (bad data)
- Removed rows with missing station names or user type
- Confirmed only valid user types (member/casual)

**Final clean dataset: 3,747,342 rows**

#### Python Cleaning Script
```python
import pandas as pd
import os
import glob

folder_path = os.path.dirname(os.path.abspath(__file__))
all_files = glob.glob(os.path.join(folder_path, "*.csv"))
df = pd.concat([pd.read_csv(f) for f in all_files], ignore_index=True)

df['started_at'] = pd.to_datetime(df['started_at'])
df['ended_at'] = pd.to_datetime(df['ended_at'])
df['ride_length'] = (df['ended_at'] - df['started_at']).dt.total_seconds() / 60

days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday',
        4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
df['day_of_week'] = df['started_at'].dt.dayofweek.map(days)

months = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
          7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
df['month'] = df['started_at'].dt.month.map(months)

df['hour'] = df['started_at'].dt.hour
df = df[df['ride_length'] >= 1]
df = df[df['ride_length'] <= 1440]
df = df.dropna(subset=['start_station_name', 'end_station_name', 'member_casual'])
df = df[df['member_casual'].isin(['member', 'casual'])]
df.to_csv(os.path.join(folder_path, "cyclistic_clean.csv"), index=False)
```

---

### 4. Analyze

The cleaned data was imported into Google BigQuery for SQL analysis.

#### Total Rides by User Type
```sql
SELECT member_casual, COUNT(*) AS total_rides
FROM `cyclistic.trips`
GROUP BY member_casual;
```
| User Type | Total Rides | Percentage |
|-----------|-------------|------------|
| Member | 2,418,986 | 64.55% |
| Casual | 1,328,356 | 35.45% |

#### Average Ride Length
```sql
SELECT member_casual, ROUND(AVG(ride_length), 2) AS avg_ride_minutes
FROM `cyclistic.trips`
GROUP BY member_casual;
```
| User Type | Avg Ride Length |
|-----------|----------------|
| Member | 13 minutes |
| Casual | 22 minutes |

#### Rides by Day of Week
```sql
SELECT member_casual, day_of_week, COUNT(*) AS total_rides
FROM `cyclistic.trips`
GROUP BY member_casual, day_of_week
ORDER BY day_of_week;
```

#### Rides by Month
```sql
SELECT member_casual, month, COUNT(*) AS total_rides
FROM `cyclistic.trips`
GROUP BY member_casual, month
ORDER BY month;
```

---

### 5. Share

**[View Interactive Tableau Dashboard](#)** ← *(replace with your Tableau Public link)*

#### Key Findings

**Total Rides**
- Members account for **64.55%** of all rides (2,418,986 trips)
- Casuals account for **35.45%** (1,328,356 trips)
- Despite fewer rides, casuals ride **70% longer** per trip (22 vs 13 mins)

**Weekly Behavior**
- Members ride consistently Monday–Friday → suggests **commuter/purpose-driven use**
- Casuals peak on Saturdays → suggests **leisure and recreational use**
- Casual rides nearly double on weekends compared to weekdays

**Monthly/Seasonal Behavior**
- Both groups peak in **July–August**
- Casual ridership drops **93% from August to January**
- Members drop only **73%** — suggesting year-round reliance on bikes

**Similarities**
- Both groups prefer **classic bikes** over electric
- Both groups ride longer on weekends than weekdays
- Both groups follow a similar seasonal curve peaking in summer

**Differences**
| | Members | Casuals |
|--|---------|---------|
| Avg ride length | 13 mins | 22 mins |
| Peak day | Thursday | Saturday |
| Peak month | September | August |
| Usage pattern | Commute/errands | Leisure/recreation |
| Seasonal consistency | More consistent | Highly seasonal |

---

### 6. Act

#### Top 3 Recommendations

**1. Weekend Membership Campaign**
Casual riders are most active on weekends. Target them with in-app prompts and social media ads on Fridays and Saturdays offering a discounted annual membership. The pitch: *"You're already riding every weekend — a membership pays for itself."*

**2. Summer Conversion Push (May–July)**
Casual ridership peaks in summer — this is the highest engagement window. Launch a limited-time summer membership discount or free first month trial during June–August to convert riders while they are most active.

**3. Cost Comparison Campaign**
Since casuals average 22 minutes per trip, they are likely paying significantly more per ride with single passes than they would with a membership. Show them a clear cost breakdown: *"Your average ride costs $X as a casual — but only $Y as a member."* Make the financial benefit impossible to ignore.

---

## Conclusion
This analysis reveals that casual riders and members use Cyclistic bikes for fundamentally different purposes — members for daily commuting and casuals for weekend leisure. With 1.3 million casual riders already engaged with the platform, there is a significant opportunity to convert them into members through targeted weekend campaigns, seasonal promotions, and clear cost-value messaging.

---

## Repository Contents
| File | Description |
|------|-------------|
| `clean.py` | Python script for data cleaning and processing |
| `README.md` | Full project documentation |

---

*Data source: [Divvy Trip Data](https://divvy-tripdata.s3.amazonaws.com/index.html) provided by Motivate International Inc. under open license.*
