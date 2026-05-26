# 🍽️ Zomato Bangalore - Market Intelligence & Business Strategy Engine

<div align="center">

### *51,148 restaurants. 15 variables. 5 findings that can make or break a food business.*

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-1.3+-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Kaggle](https://img.shields.io/badge/Kaggle-Notebook-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white)](https://www.kaggle.com/code/virajmore111/zomato-bangalore-analysis-eda/notebook)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Viraj%20More-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/viraj-uttam-more-a24a80391)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](./LICENSE)

**[🚀 Live Kaggle Notebook](https://www.kaggle.com/code/virajmore111/zomato-bangalore-analysis-eda/notebook) · [📊 Presentation](https://github.com/Virajmore888/zomato-bangalore-restaurant-eda/blob/9991210ea27399f9f9fd8f3c05ed557638d5ed64/Zomato_Analysis_Presentation.pdf) · [📝 Full Report](https://github.com/Virajmore888/zomato-bangalore-restaurant-eda/blob/3cd1faa379ca89ea6cb2d998450525eb37b138bd/Zomato_Analysis_Report.pdf)**

*Tuesday, May 26, 2026*

</div>

---

## 👋 About This Project

Hi, I'm **Viraj More** - an aspiring Data Analyst with a passion for turning raw, messy data into decisions that actually matter. Currently expanding into Data Science and AI/ML - one project at a time.

This project is not just an EDA. It's an **end-to-end data analytics pipeline** - from a 51K-row raw dataset riddled with nulls and text anomalies, all the way to a stakeholder-ready report and presentation. Built entirely on **Android (Termux + Acode)** with zero cloud infrastructure.

> If you're a recruiter or fellow analyst - the TL;DR below tells you everything in 30 seconds. The rest of the README is for those who want to go deeper.

> ⚠️ **Data Confidence Note:** Real-world data is never 100% clean. This analysis operates within a **90-95% confidence range** - insights are data-driven and reliable, but acknowledge natural market variation. Blind deletion of nulls was avoided; smart imputation was used to preserve business integrity. See the [Full Report](https://github.com/Virajmore888/zomato-bangalore-restaurant-eda/blob/3cd1faa379ca89ea6cb2d998450525eb37b138bd/Zomato_Analysis_Report.pdf) for the complete Data Disclaimer.

> 📅 **Dataset Note:** This dataset is approximately 7-8 years old and sourced from Kaggle (by Himanshu Poddar). It may not reflect current restaurant availability, ratings, or pricing. This project is intended for analytical and educational purposes only.

---

## ⚡ TL;DR - 5 Findings That Change Restaurant Strategy

| # | Finding | Business Impact |
|---|---------|----------------|
| 1 | 🚀 Table booking → **7x more customer votes** | Highest-ROI growth lever available |
| 2 | 📦 Online delivery shifts ratings **3.4 → 3.9** | Digital presence = higher perceived quality |
| 3 | ⭐ Quality (r=0.44) beats Pricing (r=0.40) | Don't overprice - invest in quality instead |
| 4 | 🗺️ North Indian is **oversaturated** - Cafes & Desserts are wide open | Blue ocean opportunity for new entrants |
| 5 | 📱 Entire pipeline built on **Android (Termux)** - zero cloud cost | Reproducible anywhere, no infra needed |

---

## 🎯 What Makes This Project Different

Most EDA projects stop at charts. This one answers **"So what?"**

| Kaggle Beginner Notebooks | This Project |
|---|---|
| Shows rating distribution | Quantifies the exact business lift from going digital |
| Lists top cuisines | Identifies oversaturated vs. underserved market gaps |
| Computes correlations | Translates r-values into actionable pricing strategy |
| Runs on cloud/Colab | Built natively on **Android** - zero infrastructure cost |
| Static notebook | End-to-end delivery: pipeline → insights → report + presentation |

---

## 💡 Key Business Insights

### 1. 📈 The 7x Engagement Multiplier
**87.4% of restaurants (44,699 out of 51,148) don't offer table booking** - and they're leaving massive engagement on the table. Restaurants that do offer it see a **7x increase in mean customer votes** (1,147 vs 161 avg votes). This is not a luxury feature - it's the single highest-leverage action a restaurant owner can take.

<details>
<summary><b>🖼️ View Chart: Votes by Table Booking & Online Order</b></summary>
<br>
<img src="https://github.com/Virajmore888/zomato-bangalore-restaurant-eda/blob/ffb83f2bca513b4ca56be53ab6b6e1db6e3ef9c5/votes_online-order_booktable.png?raw=true" alt="Votes by Table Booking" width="800">
</details>

---

### 2. 📦 The Digital Delivery Benchmark
**20,837 restaurants** operate without online delivery and cluster around a **3.4-3.5 modal rating**. The moment delivery is enabled (30,311 restaurants), the entire distribution shifts right - peaking at **3.7-3.9**. Average rating jump: 3.63 (offline) vs 3.71 (online). Consumers don't just want food delivered - they reward the convenience with better ratings.

<details>
<summary><b>🖼️ View Chart: Ratings Distribution by Online Order</b></summary>
<br>
<img src="https://github.com/Virajmore888/zomato-bangalore-restaurant-eda/blob/0fabea674a68393ea6aeb300d336eeacd019c2de/ratings_distribution_onlineorder.png?raw=true" alt="Ratings Distribution" width="800">
</details>

---

### 3. 🌟 Quality Wins - Pricing Doesn't
The full correlation picture from the dataset:
- **Ratings vs Votes (r = 0.44)** - strongest link, quality drives engagement organically
- **Ratings vs Cost (r = 0.40)** - higher price tends to rate better, but gap is thin
- **Votes vs Cost (r = 0.38)** - premium price alone does not drive traffic, service does

All three correlations are moderate and below 0.50 - confirming **zero multicollinearity**. The data is clear: a restaurant charging Rs 1,000+ with poor service will still lose to a Rs 400 restaurant with consistent quality and table booking enabled.

<details>
<summary><b>🖼️ View Charts: Correlation Heatmap & Scatter Plot</b></summary>
<br>
<img src="https://github.com/Virajmore888/zomato-bangalore-restaurant-eda/blob/0fabea674a68393ea6aeb300d336eeacd019c2de/correlation_heatmap.png?raw=true" alt="Correlation Heatmap" width="400">
<img src="https://github.com/Virajmore888/zomato-bangalore-restaurant-eda/blob/0fabea674a68393ea6aeb300d336eeacd019c2de/votes_vs_ratings_scatter.png?raw=true" alt="Votes vs Ratings" width="400">
</details>

---

### 4. 🗺️ Where the Real Opportunity Is
North Indian cuisine dominates with 2,858 restaurants - which means hyper-competition for new entrants. The data points to a clear gap: **Cafes (406 offline vs 320 online) and Bakery (411 offline vs 238 online)** are digitally underserved. Digital-first cloud kitchens in these categories represent a significant untapped opportunity with lower competition.

<details>
<summary><b>🖼️ View Chart: Cuisine Distribution</b></summary>
<br>
<img src="https://github.com/Virajmore888/zomato-bangalore-restaurant-eda/blob/0fabea674a68393ea6aeb300d336eeacd019c2de/cuisine_distribution_onlineorder.png?raw=true" alt="Cuisine Distribution" width="800">
</details>

---

## ⚙️ Technical Architecture

This pipeline was engineered under **extreme resource constraints** - developed and executed entirely on **Android (Termux + Acode)**, with no cloud compute, no Colab, no shortcuts.

| Technique | Implementation Detail |
|---|---|
| **Smart Contextual Imputation** | 7,775 missing ratings filled using `groupby(['rest_type', 'location'])` median - no naive global averages that would distort local market signals |
| **Memory Optimization** | Binary columns → `category`, Floats → `float16`, Integers → `int32`. Result: dataset memory reduced from ~33MB to ~4.9MB (85% reduction) |
| **Data Purity** | Stripped text anomalies (`'4.2/5'`, `'NEW'`, `'-'`) and eliminated **38,045 nulls** across operational features before any analysis |
| **Pipeline Runtime** | Full pipeline (cleaning + 6 insights + 5 charts) completes in under 60 seconds on constrained Android hardware |

---

## 🛠️ Skills Demonstrated

`Python` · `Pandas` · `NumPy` · `Matplotlib` · `Seaborn` · `Exploratory Data Analysis` · `Data Cleaning & Imputation` · `Statistical Analysis` · `Pearson Correlation` · `Business Intelligence` · `Data Visualization` · `Memory Optimization` · `Mobile DevOps (Termux)`

---

## 🚀 Run This Project Locally

### Prerequisites
- Python 3.13
- pip
- Kaggle account (for dataset download)

### Step 1: Clone
```bash
git clone https://github.com/Virajmore888/zomato-bangalore-restaurant-eda.git
cd zomato-bangalore-restaurant-eda
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Download Dataset
```bash
# Setup Kaggle API credentials first: https://www.kaggle.com/settings
kaggle datasets download -d himanshupoddar/zomato-bangalore-restaurants
unzip zomato-bangalore-restaurants.zip
```
Or download manually from [Kaggle Dataset Page](https://www.kaggle.com/datasets/himanshupoddar/zomato-bangalore-restaurants) and place the CSV in the project root.

### Step 4: Run the Pipeline
```bash
python Zomato_Analysis.py
```
📄 [View Full Source Code](https://github.com/Virajmore888/zomato-bangalore-restaurant-eda/blob/87fef230507eb41f505a23f9c344989e94b612bb/Zomato_Analysis.py)

### Step 5: Explore the Notebook (Optional)
```bash
jupyter notebook zomato-bangalore-analysis-eda.ipynb
```
📓 [View Kaggle Notebook](https://www.kaggle.com/code/virajmore111/zomato-bangalore-analysis-eda/notebook) · [View GitHub Notebook](https://github.com/Virajmore888/zomato-bangalore-restaurant-eda/blob/3cd1faa379ca89ea6cb2d998450525eb37b138bd/zomato-bangalore-analysis-eda.ipynb)

### 📱 Mobile Setup (Termux)
```bash
pkg install python
pip install pandas numpy matplotlib seaborn jupyter
```

---

## 📦 Dependencies

```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
jupyter>=1.0.0
```

---

## 📊 Dataset at a Glance

| Attribute | Value |
|---|---|
| **Source** | Zomato Bangalore via Kaggle (Himanshu Poddar) |
| **Total Records** | 51,148 restaurants |
| **Features** | 17 raw → 15 after cleaning |
| **Nulls Eliminated** | 38,045 |
| **Ratings Imputed** | 7,775 records |
| **Dataset Age** | Collected circa 2017-2018, approximately 7-8 years old |

---

## 📂 Repository Structure

```
zomato-bangalore-restaurant-eda/
│
├── 📊 Zomato_Analysis_Presentation.pdf       # Stakeholder-ready visual summary
├── 📝 Zomato_Analysis_Report.pdf             # Deep-dive statistical consulting report
├── 💻 Zomato_Analysis.py                     # Production ETL & EDA pipeline
├── 📓 zomato-bangalore-analysis-eda.ipynb    # Jupyter Notebook (interactive EDA)
│
├── 📈 Charts
│   ├── votes_online-order_booktable.png
│   ├── ratings_distribution_onlineorder.png
│   ├── correlation_heatmap.png
│   ├── votes_vs_ratings_scatter.png
│   └── cuisine_distribution_onlineorder.png
│
├── CONTRIBUTING.md
└── README.md
```

---

## 🤝 Connect & Contribute

- 🔗 **LinkedIn:** [Viraj More](https://www.linkedin.com/in/viraj-uttam-more-a24a80391)
- 📓 **Kaggle Notebook:** [View Full Notebook](https://www.kaggle.com/code/virajmore111/zomato-bangalore-analysis-eda/notebook)
- 📊 **Kaggle Output:** [View Charts & Output](https://www.kaggle.com/code/virajmore111/zomato-bangalore-analysis-eda/output)
- 💻 **GitHub:** [zomato-bangalore-restaurant-eda](https://github.com/Virajmore888/zomato-bangalore-restaurant-eda)

Found something to improve? Open an **Issue** or submit a **Pull Request** - contributions are welcome!
Read the **[Contributing Guide](https://github.com/Virajmore888/zomato-bangalore-restaurant-eda/blob/1bb9dc3a459ddd034cffce091c6e78be042aa0e0/CONTRIBUTING.md)** before submitting.

---

## 📄 License

MIT License - see [LICENSE](./LICENSE) for details.

---

<div align="center">

**Built with ❤️ on Android · Termux + Acode · Zero Cloud Cost**

*Tuesday, May 26, 2026*

*If this project added value, consider leaving a ⭐ on the repo - it helps others find it too.*

</div>
