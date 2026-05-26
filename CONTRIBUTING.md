# Contributing to Zomato Bangalore Restaurant EDA

> We appreciate your interest in contributing. This document outlines the standards, workflows, and expectations for all contributors. Please read it carefully before opening an issue or submitting a pull request.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Branch Naming Convention](#branch-naming-convention)
- [Commit Message Standards](#commit-message-standards)
- [Pull Request Process](#pull-request-process)
- [Project Structure](#project-structure)
- [Code Style Guidelines](#code-style-guidelines)
- [Contribution Ideas](#contribution-ideas)
- [Notes & Disclaimer](#notes--disclaimer)
- [Connect](#connect)

---

## Code of Conduct

This project follows a simple principle: be respectful, be constructive, be precise. Contributions that are vague, untested, or break existing functionality will be declined without exception.

---

## How to Contribute

There are several ways to contribute to this project:

- **Bug Reports** - Open an issue with a clear description and steps to reproduce
- **Feature Requests** - Open an issue tagged `enhancement` with a detailed use case
- **Code Contributions** - Fork the repo, make changes, and open a Pull Request
- **Documentation** - Improve clarity, fix typos, or expand existing sections
- **Analysis Extensions** - Add new insights, visualizations, or statistical methods

> **Important:** For significant changes, open an issue first to discuss the approach before writing code. This prevents wasted effort on contributions that may not align with the project direction.

---

## Getting Started

### Prerequisites

Ensure the following are installed before contributing:

| Tool | Minimum Version |
|------|----------------|
| Python | 3.13 |
| pip | Latest |
| Git | 2.30+ |

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/<your-username>/zomato-bangalore-restaurant-eda
cd zomato-bangalore-restaurant-eda

# Add the upstream remote
git remote add upstream https://github.com/Virajmore888/zomato-bangalore-restaurant-eda
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### 3. Add the Dataset

Download the dataset from Kaggle:

> **Zomato Bangalore Restaurants** by Himanshu Poddar
> https://www.kaggle.com/datasets/himanshupoddar/zomato-bangalore-restaurants

Place `zomato.csv` in the project root before running the pipeline.

### 4. Verify Setup

```bash
python Zomato_Analysis_Final.py
```

All 5 charts should generate without errors before you begin making changes.

---

## Development Workflow

```bash
# Sync with upstream before starting any work
git fetch upstream
git checkout main
git merge upstream/main

# Create a new branch for your contribution
git checkout -b feat/your-feature-name

# Make changes, then run the full pipeline to verify nothing is broken
python Zomato_Analysis_Final.py

# Stage and commit your changes
git add .
git commit -m "feat: add location-wise rating trend analysis"

# Push to your fork
git push origin feat/your-feature-name

# Open a Pull Request on GitHub
```

> All output files (cleaned CSVs + chart PNGs) are saved to the working directory automatically after running the pipeline.

---

## Branch Naming Convention

All branches must follow this naming pattern. PRs from branches that do not conform will not be reviewed.

| Type | Pattern | Example |
|------|---------|---------|
| Feature | `feat/<description>` | `feat/location-rating-trends` |
| Bug Fix | `fix/<description>` | `fix/cost-column-parsing` |
| New Chart | `viz/<description>` | `viz/top-locations-barplot` |
| Data Update | `data/<description>` | `data/add-cleaned-subset` |
| Documentation | `docs/<description>` | `docs/update-readme` |
| Refactor | `refactor/<description>` | `refactor/cleaning-pipeline` |

---

## Commit Message Standards

This project follows a simplified version of the [Conventional Commits](https://www.conventionalcommits.org/) specification.

**Format:**
```
<type>: <short description>

<optional body explaining what and why>
```

**Types:**

| Type | When to Use |
|------|------------|
| `feat` | New feature or analysis |
| `fix` | Bug fix |
| `viz` | New or updated chart |
| `docs` | Documentation only |
| `refactor` | Code restructure with no behavior change |
| `data` | Dataset or cleaning changes |
| `chore` | Maintenance tasks |

**Examples:**
```
feat: add KMeans restaurant segmentation to Section F
fix: correct groupby median imputation for edge case locations
viz: add choropleth map of Bangalore restaurant density
docs: expand README with cost bracket analysis section
```

---

## Pull Request Process

1. Ensure your branch is up to date with `upstream/main` before opening a PR
2. Fill in the PR template completely - incomplete PRs will not be reviewed
3. All 5 visualizations must regenerate without errors after your changes
4. At least one reviewer must approve before merging
5. Squash commits before merging if the branch has more than 3 commits

### PR Checklist

Before submitting, verify every item below:

- [ ] Pipeline runs end-to-end without errors (`python Zomato_Analysis_Final.py`)
- [ ] All 5 visualizations regenerate correctly as `.png` files
- [ ] No hardcoded absolute file paths - use `os.path.join()` with relative paths only
- [ ] Every new function includes a docstring explaining its analytical purpose
- [ ] No new null values introduced after any data transformation
- [ ] No increase in memory footprint without justification
- [ ] `README.md` updated if new charts, datasets, or sections are added
- [ ] Code follows the existing Section A through H structure

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
├── votes_online-order_booktable.png          # Viz 1 - Votes by Online Order & Table Booking
├── ratings_distribution_onlineorder.png      # Viz 2 - Ratings Benchmarking by Online Order
├── votes_vs_ratings_scatter.png              # Viz 3 - Correlation: Votes vs Ratings
├── cuisine_distribution_onlineorder.png      # Viz 4 - Cuisine Distribution by Online Order
├── correlation_heatmap.png                   # Viz 5 - Feature Correlation Heatmap
│
├── Zomato_Analysis_Report.pdf                # Full EDA report (25 pages)
├── Zomato_Presentation.pdf                   # Slide deck (14 slides)
│
├── CONTRIBUTING.md                           # Contribution guidelines (this file)
└── README.md                                 # Project overview and documentation
```

---

## Code Style Guidelines

### General

- Follow the existing **Section A through H** structure for all additions
- Variable names must be descriptive - avoid single-letter names outside loops
- Add section header comments (`# ===...===`) to separate logical blocks
- No commented-out dead code in PRs

### Visualization Standards

- Use **object-oriented matplotlib** (`fig, ax = plt.subplots()`) for all charts - never use `plt.xxx()` directly on new charts
- All chart functions must begin with `sns.set_theme()` and end with `plt.savefig()` and `plt.close()`
- Every chart must be saved to `PATH` using `os.path.join(PATH, "filename.png")`
- Use `dpi=150` minimum for all saved charts
- Chart titles must use `loc='left'`, `fontsize=20`, `fontweight='bold'`

### Data Handling

- Never use `inplace=True` on new data transformations - assign explicitly
- All new columns must be downcasted to the most memory-efficient dtype
- Smart imputation only - no blind `fillna(0)` or `dropna()` without justification

---

## Contribution Ideas

Looking for ways to contribute? Here are high-value open directions:

| Priority | Area | Idea |
|----------|------|------|
| High | Analysis | Location-wise rating trend analysis across Bangalore zones |
| High | Feature | Value Score metric combining rating and cost bracket |
| Medium | Machine Learning | Restaurant clustering using KMeans segmentation |
| Medium | Dashboard | Streamlit dashboard for interactive EDA exploration |
| Medium | Statistical | Normality tests (Shapiro-Wilk) on rating and cost distributions |
| Low | Visualisation | Choropleth or folium map of Bangalore restaurant density |
| Low | Deep Dive | Cuisine-wise profitability analysis using cost and votes data |

---

## Notes & Disclaimer

- **Dataset:** Zomato Bangalore Restaurants by Himanshu Poddar - sourced from Kaggle
- **Data Age:** Collected circa 2017-2018, approximately 7-8 years old. May not reflect current restaurant availability, ratings, or pricing
- **Purpose:** This project is for **educational and analytical purposes only** - not intended for commercial use
- **Environment:** Originally developed on Android using Termux + Acode / Pydroid3
- **Confidence Range:** Insights operate within a 90-95% confidence range due to smart imputation methodology

---

## Connect

- 🔗 **LinkedIn:** [Viraj More](https://www.linkedin.com/in/viraj-uttam-more-a24a80391)
- 📓 **Kaggle:** [virajmore111](https://www.kaggle.com/virajmore111)
- 💻 **GitHub:** [Virajmore888](https://github.com/Virajmore888)

---

*Prepared by Viraj More | virajmore.data888@gmail.com | May 2026*
