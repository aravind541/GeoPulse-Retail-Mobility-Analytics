# GeoPulse – Retail & Mobility Analytics

**A Geospatial Data Analytics Project Exploring Retail Locations and Public Transportation Accessibility Across 10 Indian Cities**

## Project Overview

GeoPulse is a data analytics project that explores the geographical relationship between retail locations and nearby public transportation facilities.

The project analyzes retail and mobility datasets across 10 major Indian cities, calculates the nearest mobility facility for each retail location, classifies retail accessibility, and visualizes geographical distributions using interactive maps.

**Important:** This project uses synthetic data generated for analytical demonstration. It does not represent actual retail locations, transportation infrastructure, visitor counts, or passenger counts.

## Project Objectives

- Analyze retail distribution across 10 Indian cities.
- Explore retail categories and mobility facility types.
- Calculate the nearest public transportation facility for each retail location.
- Measure geographical distances using the Haversine formula.
- Classify retail locations based on nearest mobility distance.
- Compare accessibility across cities.
- Create interactive geographical maps.

## Cities Covered

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

## Dataset Overview

| Dataset | Records | Cities |
|---|---:|---:|
| Retail Locations | 3,500 | 10 |
| Mobility Locations | 1,500 | 10 |
| **Total** | **5,000** | **10** |

### Retail Dataset

Contains retail IDs, city, state, store name, category, geographical coordinates, and simulated daily visitors.

### Mobility Dataset

Contains mobility IDs, city, state, facility name, mobility type, geographical coordinates, and simulated daily passengers.

## Technologies Used

- **Python** – Programming and analysis
- **Pandas** – Data manipulation
- **NumPy** – Numerical operations
- **Matplotlib** – Data visualization
- **Seaborn** – Statistical visualization
- **Scikit-learn** – Haversine distance calculation
- **Folium** – Interactive geographical maps
- **Jupyter Notebook** – Analysis environment
- **Git & GitHub** – Version control

## Project Workflow

1. Synthetic dataset generation.
2. Data inspection and cleaning.
3. Exploratory Data Analysis (EDA).
4. Retail and mobility dataset integration.
5. Nearest mobility facility identification.
6. Geographical distance calculation.
7. Accessibility classification.
8. City-wise and category-wise analysis.
9. Interactive spatial visualization.
10. Final reporting and documentation.

## Accessibility Classification

Retail locations are classified using the distance to their nearest mobility facility.

| Distance | Classification |
|---|---|
| 0–0.5 km | High |
| 0.5–1 km | Moderate |
| More than 1 km | Low |

These are project-defined demonstration thresholds, not official accessibility standards.

## Key Analysis Results

### Overall Accessibility

| Classification | Retail Locations | Percentage |
|---|---:|---:|
| High | 419 | 11.97% |
| Moderate | 977 | 27.91% |
| Low | 2,104 | 60.11% |

- Total retail locations analyzed: 3,500.
- Average nearest mobility distance: approximately 1.29 km.
- Hyderabad Low accessibility percentage: 75.43%.
-Lucknow has the highest number of High-accessibility locations among the analyzed cities, with 59 stores.
These results describe the synthetic dataset only.

## Interactive Maps

Two interactive maps were developed using Folium:

- **India-wide map:** Displays retail and mobility locations across all 10 cities.
- **Hyderabad map:** Provides a focused geographical view of retail and mobility locations in Hyderabad.

Map files:

- `reports/geopulse_spatial_map.html`
- `reports/hyderabad_spatial_map.html`

Download or open the HTML files locally in a web browser to explore the maps.

## Project Structure

```text
GeoPulse-Retail-Mobility-Analytics/
│
├── dashboard/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── reports/
│   ├── eda_summary.csv
│   ├── GeoPulse_Final_Report.md
│   ├── geopulse_spatial_map.html
│   └── hyderabad_spatial_map.html
│
├── sql/
│
├── src/
│   └── collect_data.py
│
├── GeoPulse_EDA.ipynb
├── GeoPulse_Datasets.zip
├── README.md
└── .gitignore
```

## Limitations

- The datasets are synthetic, not real-world observations.
- Geographical coordinates are generated within approximate city boundaries.
- Visitor and passenger counts are simulated.
- Distances represent straight-line geographical distances, not actual road or walking distances.
- Traffic, travel time, transport frequency, and pedestrian infrastructure are not considered.

## Future Enhancements

- Integrate real-world retail and transportation datasets.
- Calculate road-network distances.
- Incorporate actual visitor and passenger statistics.
- Develop an interactive Power BI dashboard.
- Expand accessibility analysis using real geographical data.

## Final Report

For detailed methodology, analysis results, Hyderabad-specific findings, limitations, and conclusions, see:

`reports/GeoPulse_Final_Report.md`

## Conclusion

GeoPulse demonstrates an end-to-end data analytics workflow combining data cleaning, exploratory analysis, geographical distance calculations, retail–mobility integration, accessibility classification, and interactive spatial visualization.

The project provides practical experience in Python-based analytics and geospatial data analysis.

---

**Project:** GeoPulse – Retail & Mobility Analytics  
**Domain:** Data Analytics and Geospatial Analysis