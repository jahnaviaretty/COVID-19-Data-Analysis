
# COVID-19 Data Analysis and Visualization Using Python

## Project Overview

This project focuses on analyzing COVID-19 data using Python to understand the spread of the pandemic, daily case trends, and reported deaths in India.

The project uses data analysis and visualization libraries to explore real-world COVID-19 data and present meaningful insights through charts.

## Objectives

- Analyze COVID-19 cases and deaths in India.
- Study daily new cases and daily new deaths.
- Understand cumulative case and death trends over time.
- Explore global COVID-19 data.
- Create visualizations to communicate findings.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Dataset

The dataset is sourced from Our World in Data (OWID).

Dataset source:
https://ourworldindata.org/coronavirus

The dataset contains information such as:
- Country
- Date
- Total cases
- New cases
- Total deaths
- New deaths
- Vaccination information
- Population

## Project Structure

```text
COVID-19-Data-Analysis/
│
├── data/
│   └── covid_data.csv
│
├── notebooks/
│   └── covid_analysis.py
│
├── reports/
│   ├── india_covid_cases_trend.png
│   ├── india_daily_new_cases.png
│   ├── india_covid_deaths_trend.png
│   ├── india_daily_new_deaths.png
│   └── top_10_countries_cases.png
│
├── requirements.txt
└── README.md
```

## Analysis and Visualizations

The project generates visualizations covering:

1. Total COVID-19 cases in India over time.
2. Daily new COVID-19 cases in India.
3. Total COVID-19 deaths in India over time.
4. Daily new COVID-19 deaths in India.
5. Comparison of the highest reported case counts in the dataset.

## Key Findings

- India recorded approximately 45 million cumulative COVID-19 cases in the dataset.
- Reported cumulative deaths reached approximately 534,000.
- Daily case and death trends show changes in the intensity of the pandemic over time.
- Visualizations make it easier to understand trends in the data.

*Note: These figures reflect the downloaded dataset and its reporting methodology.*

## How to Run the Project

1. Clone or download this repository.
2. Install Python.
3. Install the required libraries:

```bash
pip install -r requirements.txt
```

4. Download the COVID-19 dataset from Our World in Data.
5. Place the downloaded CSV file inside the `data` folder with the filename `covid_data.csv`.
6. Run the analysis script:

```bash
python notebooks/covid_analysis.py
```

7. Find the generated charts inside the `reports` folder.

## Skills Demonstrated

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Data manipulation using Pandas
- Statistical analysis
- Data visualization
- Python programming
- Working with real-world datasets

## Author

Aretty Jahnavi

GitHub: https://github.com/jahnaviaretty
