# Cyclistic Bike-Share Case Study
### Google Data Analytics Professional Certificate — Capstone Project

---

## Introduction

The Cyclistic Bike-Share Case Study is a capstone project for the Google Data Analytics Professional Certificate. Following the data analysis process — Ask, Prepare, Process, Analyze, Share, and Act — this project analyzes real-world bike-share data to develop marketing strategies aimed at converting casual riders into annual members.

---

## Background

Cyclistic is a bike-share company based in Chicago with a fleet of 5,824 bicycles across 692 geotracked stations. Customers can rent bikes from one station and return them to any other station in the network at their convenience.

Cyclistic offers three pricing plans: single-ride passes, full-day passes, and annual memberships. Customers who purchase single-ride or full-day passes are referred to as casual riders, while customers who purchase annual memberships are Cyclistic members.

The company's finance team has concluded that annual members are significantly more profitable than casual riders. The director of marketing believes the key to future growth is maximizing the number of annual memberships by converting existing casual riders into members.

---

## 1. Ask

**Business Task:** Analyze how annual members and casual riders use Cyclistic bikes differently in order to design data-driven marketing strategies that convert casual riders into annual members.

> **Guiding Question:** How do annual members and casual riders use Cyclistic bikes differently?

---

## 2. Prepare

**Data Source:** [Divvy Trip Data](https://divvy-tripdata.s3.amazonaws.com/index.html)
**Period:** May 2025 – April 2026 (12 months)
**License:** Made available by Motivate International Inc. under open license.
**Total Records:** 3,747,342 trips

### Tools Used

| Tool | Purpose |
|------|---------|
| Python (pandas) | Data cleaning, processing, and combining |
| SQL (Google BigQuery) | Data analysis and querying |
| Tableau Public | Data visualization and dashboard |
| GitHub | Portfolio and documentation |

### Data Structure

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

## 3. Process

Data was cleaned and processed using Python (pandas) and combined from 12 monthly CSV files into a single dataset.

### Steps Taken

**Data Combining**
12 CSV files covering May 2025 to April 2026 were merged into a single dataframe of 3,747,342 rows.

**Feature Engineering**
The following columns were added to support analysis:
- ride_length — trip duration in minutes
- day_of_week — day the ride started (Monday–Sunday)
- month — month the ride started (Jan–Dec)
- hour — hour the ride started (0–23)

**Data Verification**
Data was verified clean across all 3,747,342 records:
- No rides under 1 minute
- No rides over 24 hours
- No missing station names or user type values

No rows were removed. The dataset was confirmed ready for analysis.

### Tools
- Python (pandas) — combining and processing
- SQL (Google BigQuery) — analysis and querying
- Tableau Public — visualization

---

## 4. Analyze

The cleaned data was imported into Google BigQuery for SQL analysis.

### Total Rides by User Type

```sql
SELECT member_casual, COUNT(*) AS total_rides
FROM `cyclistic.trips`
GROUP BY member_casual;
```

| User Type | Total Rides | Percentage |
|-----------|-------------|------------|
| Member | 2,418,986 | 64.55% |
| Casual | 1,328,356 | 35.45% |

### Average Ride Length

```sql
SELECT member_casual, ROUND(AVG(ride_length), 2) AS avg_ride_minutes
FROM `cyclistic.trips`
GROUP BY member_casual;
```

| User Type | Avg Ride Length |
|-----------|----------------|
| Member | 13 minutes |
| Casual | 22 minutes |

### Rides by Day of Week

```sql
SELECT member_casual, day_of_week, COUNT(*) AS total_rides
FROM `cyclistic.trips`
GROUP BY member_casual, day_of_week
ORDER BY day_of_week;
```

### Rides by Month

```sql
SELECT member_casual, month, COUNT(*) AS total_rides
FROM `cyclistic.trips`
GROUP BY member_casual, month
ORDER BY month;
```

---

## 5. Share

[View Interactive Tableau Dashboard](https://public.tableau.com/app/profile/mathew.marrero.ahmad/viz/CyclisticBike-ShareAnalysis-MathewMarrero/Dashboard1?publish=yes)

### Key Findings

**Total Rides**
- Members account for 64.55% of all rides (2,418,986 trips)
- Casuals account for 35.45% (1,328,356 trips)
- Despite fewer rides, casuals ride 70% longer per trip (22 vs 13 minutes)

**Weekly Behavior**
- Members ride consistently Monday through Friday, suggesting commuter and purpose-driven use
- Casuals peak on Saturdays, suggesting leisure and recreational use
- Casual rides nearly double on weekends compared to weekdays

**Monthly/Seasonal Behavior**
- Both groups peak in July and August
- Casual ridership drops 93% from August to January
- Members drop only 73%, suggesting year-round reliance on bikes

**Similarities**
- Both groups prefer classic bikes over electric
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

## 6. Act

### Top 3 Recommendations

**1. Weekend Membership Campaign**
Casual riders are most active on weekends. Target them with in-app prompts and social media ads on Fridays and Saturdays offering a discounted annual membership. The pitch: you are already riding every weekend — a membership pays for itself.

**2. Summer Conversion Push (May–July)**
Casual ridership peaks in summer — this is the highest engagement window. Launch a limited-time summer membership discount or free first month trial during June–August to convert riders while they are most active.

**3. Cost Comparison Campaign**
Since casuals average 22 minutes per trip, they are likely paying significantly more per ride with single passes than they would with a membership. Show them a clear cost breakdown and make the financial benefit impossible to ignore.

---

## Conclusion

This analysis reveals that casual riders and members use Cyclistic bikes for fundamentally different purposes — members for daily commuting and casuals for weekend leisure. With 1.3 million casual riders already engaged with the platform, there is a significant opportunity to convert them into members through targeted weekend campaigns, seasonal promotions, and clear cost-value messaging.

---

## Repository Contents

| File | Description |
|------|-------------|
| clean.py | Python script for data cleaning and processing |
| README.md | Full project documentation |

---

*Data source: [Divvy Trip Data](https://divvy-tripdata.s3.amazonaws.com/index.html) provided by Motivate International Inc. under open license.*
