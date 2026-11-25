# GeoPulse – Retail & Mobility Analytics

## Final Project Report

### 1. Project Overview

GeoPulse is a data analytics project that explores the relationship between retail locations and nearby public transportation facilities across 10 major Indian cities.

The project analyzes retail locations, mobility facilities, simulated daily visitor counts, simulated passenger counts, and geographical distances to understand retail accessibility.

The project uses Python, Pandas, NumPy, Matplotlib, Seaborn, Folium, and Jupyter Notebook.

**Important:** This project uses synthetic datasets generated for analytical demonstration. The results do not represent actual retail or public transportation conditions in the selected cities.

### 2. Project Objectives

- Analyze retail store distributions across 10 Indian cities.
- Examine the distribution of different retail categories.
- Analyze public transportation facility types.
- Calculate the nearest mobility facility for each retail location.
- Classify retail locations based on their distance from the nearest mobility facility.
- Compare retail accessibility across cities.
- Visualize retail and mobility locations using interactive geographical maps.
- Generate meaningful business insights from the analysis.

### 3. Dataset Description

The project contains two primary datasets.

#### 3.1 Retail Dataset

| Attribute | Details |
|---|---|
| Total records | 3,500 |
| Number of cities | 10 |
| Records per city | 350 |
| Main categories | Grocery, Clothing, Convenience, Supermarket |

Important columns:

- `retail_id`
- `city`
- `state`
- `store_name`
- `category`
- `latitude`
- `longitude`
- `simulated_daily_visitors`
- `data_source`
- `is_synthetic`

#### 3.2 Mobility Dataset

| Attribute | Details |
|---|---|
| Total records | 1,500 |
| Number of cities | 10 |
| Records per city | 150 |
| Main facility types | Bus Stop, Metro Station, Railway Station, Public Transport Platform |

Important columns:

- `mobility_id`
- `city`
- `state`
- `location_name`
- `mobility_type`
- `latitude`
- `longitude`
- `simulated_daily_passengers`
- `data_source`
- `is_synthetic`

#### 3.3 Cities Covered

1. Hyderabad
2. Bengaluru
3. Chennai
4. Mumbai
5. Delhi
6. Kolkata
7. Pune
8. Ahmedabad
9. Jaipur
10. Lucknow

### 4. Tools and Technologies

| Tool / Technology | Purpose |
|---|---|
| Python | Data analysis |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Jupyter Notebook | Analysis environment |
| Folium | Interactive geographical maps |
| Scikit-learn | Haversine distance calculation |
| Git and GitHub | Version control and project management |

### 5. Data Cleaning and Preparation

Both datasets were examined and cleaned before analysis.

The following operations were performed:

- Inspected dataset structure and data types.
- Checked missing values.
- Checked duplicate records.
- Removed duplicate records where applicable.
- Trimmed unnecessary whitespace from text columns.
- Validated latitude and longitude values.
- Checked invalid or non-positive visitor and passenger counts.
- Saved the cleaned datasets into the processed data directory.

The validation checks found no missing values, duplicate records, invalid coordinates, or invalid visitor/passenger counts in the datasets.

### 6. Exploratory Data Analysis

#### 6.1 Retail Analysis

Analyzed:

- Retail store distribution by city.
- Retail category distribution.
- Simulated daily visitor counts.
- Category-wise and city-wise summaries.

The analysis covered 3,500 retail records across 10 cities.

#### 6.2 Mobility Analysis

Analyzed:

- Mobility facility distribution.
- Mobility type distribution.
- Simulated daily passenger counts.
- City-wise mobility summaries.

The analysis covered 1,500 mobility records across 10 cities.

### 7. Retail–Mobility Integration

The retail and mobility datasets were integrated to identify the nearest mobility facility for every retail location.

The Haversine formula was used to calculate geographical distances between latitude and longitude coordinates.

The calculation was performed separately for each city to avoid matching retail locations with mobility facilities from other cities.

**Distance classification used in this project:**

| Distance | Accessibility classification |
|---|---|
| 0–0.5 km | High |
| 0.5–1 km | Moderate |
| More than 1 km | Low |

These thresholds are project-defined demonstration thresholds, not official accessibility standards.

#### 7.1 Overall Accessibility Results

Total retail locations analyzed: 3,500.

| Accessibility | Stores | Percentage |
|---|---:|---:|
| High | 419 | 11.97% |
| Moderate | 977 | 27.91% |
| Low | 2,104 | 60.11% |

The mean nearest-mobility distance was approximately 1.29 km.

The results show that most generated retail locations fall into the Low accessibility category under the project's chosen thresholds.

#### 7.2 City-wise Accessibility

| City | High | Moderate | Low |
|---|---:|---:|---:|
| Hyderabad | 20 | 66 | 264 |
| Delhi | 28 | 69 | 253 |
| Bengaluru | 25 | 75 | 250 |
| Mumbai | 28 | 87 | 235 |
| Chennai | 50 | 96 | 204 |
| Pune | 49 | 104 | 197 |
| Jaipur | 49 | 107 | 194 |
| Ahmedabad | 57 | 121 | 172 |
| Lucknow | 59 | 122 | 169 |
| Kolkata | 54 | 130 | 166 |

Each city contains 350 generated retail records.

### 8. Hyderabad Spatial Analysis

A separate analysis was performed for Hyderabad.

#### 8.1 Retail Analysis

| Retail Category | Stores | Average Simulated Visitors |
|---|---:|---:|
| Grocery Store | 101 | 759.17 |
| Clothing Store | 85 | 779.35 |
| Convenience Store | 85 | 798.22 |
| Supermarket | 79 | 734.19 |

Key observations:

- Grocery stores have the highest store count.
- Grocery stores also have the highest total simulated visitors.
- Convenience stores have the highest average simulated visitors.

#### 8.2 Mobility Analysis

| Mobility Type | Facilities | Average Simulated Passengers |
|---|---:|---:|
| Bus Stop | 50 | 2,740.76 |
| Railway Station | 38 | 2,393.42 |
| Metro Station | 32 | 2,407.38 |
| Public Transport Platform | 30 | 2,449.17 |

Key observations:

- Bus stops have the highest facility count.
- Bus stops also have the highest average simulated passenger count.

#### 8.3 Hyderabad Accessibility Results

| Accessibility | Stores | Percentage |
|---|---:|---:|
| High | 20 | 5.71% |
| Moderate | 66 | 18.86% |
| Low | 264 | 75.43% |

The average nearest-mobility distance was approximately 1.60 km.

The analysis also compared accessibility classifications across retail categories using a heatmap.

### 9. Geographical Visualization

Interactive maps were created using Folium.

#### 9.1 India-wide Map

The India-wide map displays:

- 3,500 retail locations.
- 1,500 mobility locations.
- Separate marker layers for retail and mobility.
- Marker clusters.
- Interactive popups.
- Layer controls.

Output file: `reports/geopulse_spatial_map.html`

#### 9.2 Hyderabad Map

A separate interactive map was generated for Hyderabad, displaying retail and mobility locations with marker clusters and interactive information.

Output file: `reports/hyderabad_spatial_map.html`

### 10. Key Findings

1. The project analyzed 5,000 synthetic retail and mobility records across 10 Indian cities.
2. Grocery stores represented the largest retail category in the Hyderabad dataset.
3. Bus stops represented the largest mobility category in Hyderabad.
4. Approximately 60.11% of all generated retail locations were classified as having Low accessibility.
5. Hyderabad had 75.43% of its generated retail locations in the Low accessibility category.
6. Lucknow had the highest number of High-accessibility locations, with 59 out of 350 retail locations.
7. The project demonstrated how geographical distance calculations and interactive maps can support retail and mobility analysis.

These findings describe the generated datasets only. They should not be interpreted as real-world city rankings or evidence of actual transport accessibility.

### 11. Limitations

- The datasets are synthetic and not collected from actual city records.
- Latitude and longitude coordinates are generated within approximate city boundaries.
- Visitor and passenger counts are simulated.
- The nearest-facility distance does not represent actual road-network or walking distance.
- The project does not account for traffic, travel time, service frequency, transport capacity, or pedestrian infrastructure.
- The accessibility thresholds are demonstration choices.

### 12. Future Enhancements

- Integrate real retail location data.
- Collect real public transportation locations using reliable APIs or open datasets.
- Calculate road-network distances instead of straight-line distances.
- Incorporate actual visitor and passenger statistics where available.
- Build an interactive Power BI dashboard.
- Develop city-level retail accessibility comparisons using validated real-world data.

### 13. Conclusion

GeoPulse demonstrates an end-to-end data analytics workflow involving data preparation, exploratory analysis, geographical distance calculation, retail–mobility integration, accessibility classification, and interactive spatial visualization.

The project provides practical experience with Python-based data analytics and geographical analysis while demonstrating how retail and mobility datasets can be combined to explore location-based business questions.

Although the current results are based on synthetic data, the workflow can be extended using reliable real-world datasets to support more meaningful retail location and transportation accessibility studies.
