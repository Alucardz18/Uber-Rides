# :car: Uber Ride Data Analysis 🚙
This project performs exploratory data analysis (EDA) and visualization on a dataset of Uber rides. It includes data cleaning, feature engineering, categorical encoding, and a variety of plots to uncover insights about ride purpose, timing, and distance.

# Dataset Description 📋
A sample of Uber ride data with the following columns:
| Column Name  | Description                           | Type     | Nulls |
|--------------|----------------------------------------|----------|-------|
| START_DATE   | Ride start timestamp                  | object   | No    |
| END_DATE     | Ride end timestamp                    | object   | Yes   |
| CATEGORY     | Business or personal ride             | object   | Yes   |
| START        | Starting location                     | object   | Yes   |
| STOP         | Destination                           | object   | Yes   |
| MILES        | Distance of the ride in miles         | float64  | No    |
| PURPOSE      | Purpose of the ride (e.g., Meeting)   | object   | Yes   |

# Features Engineered :hammer_and_wrench:
- date and time extracted from START_DATE
- day-night: time-of-day classification (Morning, Afternoon, Evening, Night)
- MONTH: mapped month label from date
- DAYS: mapped weekday name from date

# Visualization :bar_chart:
1. Categorical Distributions
    * Count of rides by CATEGORY
    * Count of rides by PURPOSE
    * Count by Day vs Night
    * Cross-distribution of PURPOSE vs CATEGORY
      
2. Heatmap of Numeric Features
    - Correlation between MILES and encoded categorical features.

3. Monthly Trends
    - Line plot showing monthly ride frequency and max miles.

4. Day of Week
    - Bar plot: Number of rides per weekday.

5. Distance Insights
    - Boxplot: Ride distances (MILES)
    - Zoomed Boxplot: Miles under 100
    - Histogram: Miles under 40
  
# Insights & Observations 👀

- From Count Plots:
    - Most rides were booked for business purposes.
    - The most common purposes for booking were Meetings and Meal/Entertainment.
    - The majority of rides occurred between 10 AM – 5 PM (Afternoon).

- From Heatmap:
    - Business and Personal ride categories were highly negatively correlated, confirming earlier findings.
    - Other features did not show strong correlations with each other.

- From Monthly Trends:
    - Ride counts were irregular across months.
    - Fewer rides were observed in November, December, and January, likely due to winter in Florida, US.

- From Distance Analysis:
    - Most cabs were booked for short distances around 4–5 miles.
    - The majority of rides were within 0–20 miles.
    - Very few rides exceeded 20 miles.

# Data Preprocessing ⚙️
- Missing PURPOSE values replaced with 'Unknown'
- Converted START_DATE and END_DATE to datetime
- Dropped rows with nulls or duplicates

# Encoding 💻
Used OneHotEncoding to convert categorical variables CATEGORY and PURPOSE into numeric features for correlation analysis.

# License 📃
This project is for educational and personal learning purposes.
