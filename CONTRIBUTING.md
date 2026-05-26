# Contributing to Zomato Bangalore Restaurant EDA

> Thank you for your interest in contributing to this project.
> This repository contains a complete Exploratory Data Analysis pipeline for the Zomato Bangalore Restaurants dataset - covering data cleaning, insight generation, and professional visualizations.
> All contributions are welcome, whether it's a bug fix, a new chart, or an extended analysis.

---

## Table of Contents

- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Project Structure](#project-structure)
- [Branch Naming Convention](#branch-naming-convention)
- [Pull Request Checklist](#pull-request-checklist)
- [Contribution Ideas](#contribution-ideas)
- [Code Style Guidelines](#code-style-guidelines)
- [Notes & Disclaimer](#notes--disclaimer)

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Virajmore888/zomato-bangalore-restaurant-eda
cd zomato-bangalore-restaurant-eda
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install pandas numpy matplotlib seaborn
```

### 3. Add the Dataset

Download the dataset from Kaggle:
> **Zomato Bangalore Restaurants** by Himanshu Poddar
> https://www.kaggle.com/datasets/himanshupoddar/zomato-bangalore-restaurants

Place `zomato.csv` in the project root directory before running the pipeline.

---

## Development Workflow

```bash
# Run the full analysis pipeline (cleaning + insights + all 5 charts)
python Zomato_Analysis_Final.py

# Launch Jupyter Notebook for interactive section-wise EDA
jupyter notebook zomato-bangalore-analysis-eda.ipynb
```

> All output files (cleaned CSVs + chart PNGs) will be saved to the working directory automatically.

---

## Project Structure

```
zomato-bangalore-restaurant-eda/
│
├── Zomato_Analysis_Final.py                  # Main analysis & visualization pipeline
├── zomato-bangalore-analysis-eda.ipynb       # Jupyter Notebook (interactive EDA)
│
├── zomato_cleaned.csv                        # Cleaned dataset (post cleaning pipeline)
├── zomato_SubSet.csv                         # Subset used for insight generation
│
├── votes_online-order_booktable.png          # Viz 1 – Votes by Online Order & Table Booking
├── ratings_distribution_onlineorder.png      # Viz 2 – Ratings Benchmarking by Online Order
├── votes_vs_ratings_scatter.png              # Viz 3 – Correlation: Votes vs Ratings
├── cuisine_distribution_onlineorder.png      # Viz 4 – Cuisine Distribution by Online Order
├── correlation_heatmap.png                   # Viz 5 – Feature Correlation Heatmap
│
├── Zomato_Analysis_Report.pdf                # Full EDA report (25 pages)
├── Zomato_Presentation.pdf                   # Slide deck (14 slides)
│
├── CONTRIBUTING.md                           # Contribution guidelines (this file)
└── README.md                                 # Project overview and documentation
```

---

## Branch Naming Convention

All branches must follow this naming pattern before opening a Pull Request:

| Type          | Pattern                   | Example                          |
|---------------|---------------------------|----------------------------------|
| Feature       | `feat/<description>`      | `feat/location-rating-trends`    |
| Bug Fix       | `fix/<description>`       | `fix/cost-column-parsing`        |
| New Chart     | `viz/<description>`       | `viz/top-locations-barplot`      |
| Data Update   | `data/<description>`      | `data/add-cleaned-subset`        |
| Documentation | `docs/<description>`      | `docs/update-readme`             |

---

## Pull Request Checklist

Before submitting a Pull Request, verify the following:

- [ ] Script runs end-to-end without errors (`python Zomato_Analysis_Final.py`)
- [ ] All 5 visualizations regenerate correctly as `.png` files
- [ ] No hardcoded absolute file paths - use `os.path.join()` with relative paths only
- [ ] Every new function or analysis block includes a comment explaining its analytical purpose
- [ ] No new null values introduced after any data transformation
- [ ] `README.md` updated if new charts, datasets, or sections are added
- [ ] Code is clean, readable, and follows the existing section structure (A through H)

---

## Contribution Ideas

Looking for ways to contribute? Here are some open directions:

| Area              | Idea                                                                 |
|-------------------|----------------------------------------------------------------------|
| Analysis          | Add location-wise rating trend analysis across Bangalore zones       |
| Feature           | Build a Value Score metric combining rating and cost bracket         |
| Machine Learning  | Add restaurant clustering using KMeans segmentation                  |
| Dashboard         | Build a Streamlit dashboard for interactive EDA exploration           |
| Deep Dive         | Add cuisine-wise profitability analysis using cost and votes data     |
| Statistical       | Add normality tests (Shapiro-Wilk) on rating and cost distributions  |
| Visualisation     | Add a choropleth or folium map of Bangalore restaurant density        |

---

## Code Style Guidelines

- Follow the existing **Section A through H** structure for all additions
- Use **object-oriented matplotlib** (`fig, ax = plt.subplots()`) for all charts
- All chart functions must include `plt.savefig()` and `plt.close()` at the end
- Use `sns.set_theme()` at the start of every chart function
- Variable names should be descriptive - avoid single-letter names outside loops
- Add section header comments (`# ===...===`) to separate logical blocks

---

## Notes & Disclaimer

- **Dataset:** Zomato Bangalore Restaurants by Himanshu Poddar - sourced from Kaggle
- **Data Age:** The dataset is approximately 7-8 years old and may not reflect current restaurant availability, ratings, or pricing
- **Purpose:** This project is for **educational and analytical purposes only** - not intended for commercial use
- **Environment:** Originally developed on Android using Termux + Acode / Pydroid3

---

*Prepared by Viraj More | virajmore.data888@gmail.com | May 2026*
