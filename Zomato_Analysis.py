# =================================================================
# SECTION A: IMPORTING LIBRARIES
# =================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
import os

# Start Timer
start = time.time()

# Output folder — Pydroid3 storage path
PATH = os.path.join("/sdcard", "Termux")

# Create folder if it does not exist (prevents save errors)
os.makedirs(PATH, exist_ok=True)

# Reading CSV File using OS Join for reliability
data = pd.read_csv(os.path.join(PATH, "zomato.csv"))


# =================================================================
# SECTION B: DATA_EXPLORATION
# =================================================================
print("<----------DATA_EXPLORATION---------->")

# Quick sanity check — shape and first few rows
head = data.head(10)
print("First 10 Rows of the DATA_SET\n", head)

# 2. Displaying Last 10 rows of the DATA_SET
tail = data.tail(10)
print("Last 10 Rows of the DATA_SET\n", tail)

# 3. Displaying Information of the DATA_SET
info = data.info()
print("Information of the DATA_SET\n", info)

# 4. Displaying Descriptive Statistics of the DATA_SET
describe = data.describe()
print('Descriptive Statistics of the DATA_SET\n', describe)

# 5. Displaying Shape of the DATA_SET (Rows, Columns)
shape = data.shape
print("Shape of the DATA_SET\n", shape)

# 6. Displaying Total Size of the DATA_SET (Total Elements)
size = data.size
print("Size of the DATA_SET\n", size)

# 7. Displaying Columns Names of the DATA_SET
columns = data.columns
print("Columns Names of the DATA_SET\n", columns)

# 8. Finding Null Value from the DATA_SET (True/False)
null = data.isnull()
print("Null values of the DATA_SET\n", null)

# 9. Displaying Sum of the null values of each Column
Sum_Of_the_Null_Values = data.isnull().sum()
print("The Sum of the Null values of the each Columns\n", Sum_Of_the_Null_Values)

# 10. Displaying Total Sum Of the Null Values
Total_Sum_Of_the_Null_Values = data.isnull().sum().sum()
print("Total Sum of the Null Values\n", Total_Sum_Of_the_Null_Values)

# 11. Displaying Percentage of Null Values of Each Column
null_percentage = data.isnull().mean() * 100
print("Percentage of Null Values", null_percentage)

# 12. Displaying Total Percentage Of the Null Values
Total_Percentage_of_Null_Values = (data.isnull().sum().sum() / data.size) * 100
print("Total Percentage of the Null Values", Total_Percentage_of_Null_Values)

# 13. Displaying Duplicated Values (Identification)
Duplicate_Values = data.duplicated()
print("Duplicate value of the DATA_SET", Duplicate_Values)

# 14. Displaying Sum of the Duplicate Values
Sum_of_the_Duplicate_Values = data.duplicated().sum()
print("Sum of the Duplicated Values", Sum_of_the_Duplicate_Values)

# 15. Displaying Unique Values Count
Unique_Values = data.nunique()
print("Unique values of the DATA_SET", Unique_Values)


# =================================================================
# SECTION C: DATA_CLEANING
# =================================================================
print("<----------DATA_CLEANING---------->")

# 1. Dropping Duplicates from the data
data.drop_duplicates(inplace=True)

# 2. Dropping unusable columns with high null counts
data.drop(['phone', 'dish_liked'], axis=1, inplace=True)

# 3. Dropping rows where critical info is missing
data.dropna(subset=['location', 'rest_type', 'cuisines', 'approx_cost(for two people)'], axis=0, inplace=True)

# 4. Remove '/5' from rate column
data['rate'] = data['rate'].apply(lambda x: str(x).split('/')[0])

# 5. Convert rate to numeric (handles 'NEW' or '-' as NaN)
data['rate'] = pd.to_numeric(data['rate'], errors='coerce')

# Strategic filling: Use median based on Restaurant Type and Location
data['rate'] = data['rate'].fillna(data.groupby(['rest_type', 'location'])['rate'].transform('median'))

# Bug Fix: Fill any still-remaining NaNs with overall median BEFORE dtype conversion
# (float16 cast on NaN produces incorrect sentinel values on some platforms)
data['rate'] = data['rate'].fillna(data['rate'].median())

# Optimization: Rounding and memory reduction
data['rate'] = data['rate'].round(1).astype('float16')

data['votes'] = data['votes'].astype('int32')

data['online_order'] = data['online_order'].astype('category')

data['book_table'] = data['book_table'].astype('category')

# 6. Cleaning cost: Removing commas
data['approx_cost(for two people)'] = data['approx_cost(for two people)'].astype(str).str.replace(',', '')

# 7. Converting cost to float32 for performance
data['approx_cost(for two people)'] = pd.to_numeric(data['approx_cost(for two people)'], errors='coerce').astype('float32')

# 8. Rename long column name for cleaner code throughout
data.rename(columns={"approx_cost(for two people)": "cost_for_two"}, inplace=True)

print("<--- Dataset Summary after Cleaning --->")
After = data.info()
print(After)


# =================================================================
# SECTION D: SAVING PROCESSED FILES
# =================================================================
# Saving the cleaned data back to storage
data.to_csv(os.path.join(PATH, "zomato_cleaned.csv"), index=False)
print("Cleaned CSV_File Successfully saved in phone storage")


# =================================================================
# SECTION E: CREATING DATA SUBSET
# =================================================================
# Extracting specific columns for Insight Generation
sub_set = data[['name', 'online_order', 'book_table', 'rate', 'votes', 'location', 'cost_for_two']].copy()
print(sub_set.head())

sub_set.to_csv(os.path.join(PATH, "zomato_SubSet.csv"), index=False)
print("SubSet CSV_File Successfully Saved in Phone Storage")


# =================================================================
# SECTION F: INSIGHTS_OF_THE_DATA_SET
# =================================================================

# Que 1: Finding Value for Money Hotels (High Rating + Low Cost)
VFM = sub_set[(sub_set['rate'] > 4.0) & (sub_set['cost_for_two'] < 500)]
# Sort by votes — most popular VFM restaurants first (actionable recommendation)
VFM_top = VFM.sort_values('votes', ascending=False).head(10)
print("Value for Money Hotels (Top 10 by Votes)")
print(VFM_top[['name', 'location', 'rate', 'cost_for_two', 'votes']])

# Que 2: Top 10 Locations by Average rating
location_rating = sub_set.groupby('location')['rate'].mean()
print("Top 10 Locations by Average Rating: ")
top_10_locations = location_rating.sort_values(ascending=False).head(10)
print(top_10_locations)

# Que 3: Analyzing Impact of Online Order on Ratings
online_impact = sub_set.groupby('online_order')['rate'].mean()
print("Average Rating: Online_Order (Yes) vs Offline (No):")
print(online_impact)

# Que 4: Total Votes across all restaurants
total_votes = sub_set['votes'].sum()
print(total_votes)

# Que 5: Total Average Cost
avg_cost = sub_set['cost_for_two'].mean()

# Que 6: Which location has the best food?
# Grouping by location to see Average Rating and Cost
location_summery = sub_set.groupby('location').agg({'rate': 'mean', 'cost_for_two': 'mean', 'votes': 'sum'}).reset_index()
print(location_summery)


# =================================================================
# SECTION G: DATA_VISUALISATION
# =================================================================

# Que 1: Votes Distribution by Online Order & Table Booking

def plot_pro_bar(df, x_col="online_order", y_col="votes", hue_col="book_table", title="Votes Distribution by Online Order & Table Booking"):
    # 1. Global Professional Setup
    sns.set_theme(
        context='talk',
        style='white',
        palette='viridis',
        rc={"axes.spines.right": False, "axes.spines.top": False}
    )
    
    plt.rcParams['figure.dpi'] = 100

    # 2. Object-Oriented Initialization
    fig, ax = plt.subplots(figsize=(12, 8), dpi=100)

    # 3. Core Barplot (mean votes with confidence intervals)
    sns.barplot(
        data=df,
        x=x_col,
        y=y_col,
        hue=hue_col,
        estimator='mean',
        errorbar=('ci', 95),
        capsize=0.1,
        alpha=0.85,
        ax=ax
    )

    # 4. Professional Data Labels
    for container in ax.containers:
        ax.bar_label(container, fmt='%.1f', padding=6, fontsize=10, fontweight='medium')
    ax.set_ylim(0, ax.get_ylim()[1] * 1.15)

    # 5. Global Average Line
    overall_avg = df[y_col].mean()
    ax.axhline(overall_avg, color='#e74c3c', linestyle='--', linewidth=1.5, label='Global Avg', alpha=0.7)

    # 6. Professional Labeling
    ax.set_title(title, loc='left', fontsize=20, pad=20, fontweight='bold')
    ax.set_xlabel("Online Order", fontsize=12, labelpad=10)
    ax.set_ylabel("Mean Votes", fontsize=12, labelpad=10)

    # 7. Legend Fine-tuning
    ax.legend(title="Book Table", frameon=False, loc='best')

    # 8. Aesthetic Polish
    plt.grid(axis='y', linestyle=':', alpha=0.5)
    plt.tight_layout()

    # 9. Save chart to Termux folder
    plt.savefig(
        os.path.join(PATH, "votes_online-order_booktable.png"),
        dpi=500,
        transparent=False,
        bbox_inches="tight"
    )
    print("Chart saved: votes_online-order_booktable.png")

    # 10. Show chart on screen
    plt.show()

    # 11. Close figure to free memory (prevents overlap in next chart)
    plt.close()

    # 12. Return plt
    return plt


# Question 2: How are ratings distributed across restaurants?

def plot_pro_hist(df, x_col="rate", hue_col="online_order", title="Ratings Benchmarking by Online Order"):
    # 1. Global Professional Setup
    sns.set_theme(
        style="white",
        context="talk",
        rc={"axes.spines.right": False, "axes.spines.top": False}
    )
    
    plt.rcParams['figure.dpi'] = 100

    # 2. Object-Oriented Initialization
    fig, ax = plt.subplots(figsize=(12, 7), dpi=100)

    # 3. Enhanced Histplot (with KDE for trend visualization)
    sns.histplot(
        data=df,
        x=x_col,
        hue=hue_col,
        bins=25,
        multiple='dodge',
        stat='percent',
        common_norm=False,
        kde=True,
        palette='viridis',
        shrink=0.8,
        alpha=0.6,
        ax=ax
    )

    # 4. Professional Data Labels — only label bar containers, not KDE line
    for container in ax.containers:
        if hasattr(container, '__iter__'):  # Bug Fix: skip non-bar containers (KDE artists)
            ax.bar_label(container, fmt='%.0f%%', padding=3, fontsize=9, fontweight='semibold')

    # 5. Reference Line (average rating)
    mean_val = df[x_col].mean()
    ax.axvline(mean_val, color='#d35400', linestyle='--', linewidth=2, alpha=0.8)
    # Bug Fix: use fixed offset (0.05) instead of mean_val * 1.02 for x label placement
    # mean_val * 1.02 gives only ~0.07 gap when mean~3.7, barely readable
    ax.text(mean_val + 0.05, ax.get_ylim()[1] * 0.9, "Avg: {:.2f}".format(mean_val),
            color='#d35400', fontweight='bold', fontsize=11)

    # 6. Labeling & Typography
    ax.set_title(title, loc='left', fontsize=20, pad=25, fontweight='bold')
    ax.set_xlabel("Rating", fontsize=13, labelpad=12)
    ax.set_ylabel("Proportion of Restaurants (%)", fontsize=13, labelpad=12)

    # 7. Legend & Grid Polish
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles=handles, labels=labels, title="Online Order",
              loc='best', frameon=False)
    ax.grid(axis='y', linestyle='-', alpha=0.1)

    plt.tight_layout()

    # 8. Save chart to Termux folder
    plt.savefig(
        os.path.join(PATH, "ratings_distribution_onlineorder.png"),
        dpi=500,
        transparent=False,
        bbox_inches="tight"
    )
    print("Chart saved: ratings_distribution_onlineorder.png")

    # 9. Show chart on screen
    plt.show()

    # 10. Close figure to free memory (prevents overlap in next chart)
    plt.close()

    # 11. Return plt
    return plt


# Question 3: Do restaurants with more votes tend to have higher ratings?

def plot_pro_scatter(df, x_col="votes", y_col="rate", hue_col="online_order", size_col="book_table", title="Correlation: Votes vs. Ratings"):
    # 1. Professional Setup
    sns.set_theme(style="ticks", context="talk")
    
    plt.rcParams['figure.dpi'] = 100

    # 2. Object-Oriented Initialization
    fig, ax = plt.subplots(figsize=(12, 8), dpi=100)

    # 3. Core Scatter Plot
    sns.scatterplot(
        data=df,
        x=x_col,
        y=y_col,
        hue=hue_col,
        size=size_col,
        sizes=(40, 400),
        alpha=0.6,
        edgecolor='white',
        linewidth=0.5,
        palette='viridis',
        ax=ax
    )

    # 4. Log scale X-axis — dots spread ho jaenge, cluster nahi honge
    ax.set_xscale('log')
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))

    # 5. Quadrant Analysis
    mean_x = df[x_col].mean()
    mean_y = df[y_col].mean()
    ax.axvline(mean_x, color='grey', linestyle=':', alpha=0.6)
    ax.axhline(mean_y, color='grey', linestyle=':', alpha=0.6)
    ax.text(0.92, 0.95, 'Top Performers',
            transform=ax.transAxes,
            fontsize=12, fontweight='bold',
            color='#2c3e50', alpha=0.75, ha='right', va='top')

    # 6. Refined Labeling
    ax.set_title(title, loc='left', fontsize=20, pad=20, fontweight='bold')
    ax.set_xlabel("Votes", fontsize=14, labelpad=10)
    ax.set_ylabel("Ratings", fontsize=14, labelpad=10)

    # 7. Legend Polish
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles=handles, labels=labels,
              title="Online Order & Table Booking",
              loc='best',
              frameon=False, title_fontsize=11)

    # 8. Final Polish
    sns.despine()
    plt.tight_layout()

    # 9. Save chart to Termux folder
    plt.savefig(
        os.path.join(PATH, "votes_vs_ratings_scatter.png"),
        dpi=500,
        transparent=False,
        bbox_inches="tight"
    )
    print("Chart saved: votes_vs_ratings_scatter.png")

    # 10. Show chart on screen
    plt.show()

    # 11. Close figure to free memory (prevents overlap in next chart)
    plt.close()

    # 12. Return plt
    return plt


# Question 4: Which cuisines are most common among the restaurants?

def plot_pro_count(df, x_col="cuisines", hue_col="online_order", title="Cuisine Distribution by Online Order"):
    # 1. Professional Style Setup
    sns.set_theme(style="white", context="talk")
    
    plt.rcParams['figure.dpi'] = 100

    # 2. Object-Oriented Setup
    fig, ax = plt.subplots(figsize=(16, 8), dpi=100)

    # Top 15 cuisines only — chart readable rehta hai
    # Bug Fix: cuisines column has comma-separated values like "North Indian, Chinese"
    # value_counts() on raw column counts full strings not individual cuisines
    # Explode the column to count each cuisine individually
    cuisine_series = df[x_col].dropna().str.split(',').explode().str.strip()
    top_15_cuisines = cuisine_series.value_counts().head(15).index.tolist()
    df_filtered = df[df[x_col].isin(top_15_cuisines)].copy()
    # For rows with multiple cuisines, use only the primary (first) cuisine for charting
    df_filtered = df_filtered.copy()
    df_filtered[x_col] = df_filtered[x_col].str.split(',').str[0].str.strip()

    # 3. Core Countplot (sorted by frequency)
    sns.countplot(
        data=df_filtered,
        x=x_col,
        hue=hue_col,
        order=top_15_cuisines,
        palette='viridis',
        alpha=0.85,
        ax=ax
    )

    # 4. Professional Data Labels
    for container in ax.containers:
        ax.bar_label(container, padding=3, fontsize=9, fontweight='semibold')

    # 5. Labeling & Typography
    ax.set_title(title, loc='left', fontsize=20, pad=25, fontweight='bold')
    ax.set_xlabel("Cuisine Type", fontsize=14, labelpad=12)
    ax.set_ylabel("Number of Restaurants", fontsize=14, labelpad=12)

    # 6. Legend & Grid Polish
    plt.xticks(rotation=30, ha='right', fontsize=9)
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles=handles, labels=labels, title="Online Order", frameon=False, loc='upper right')
    ax.grid(axis='y', linestyle=':', alpha=0.5)
    sns.despine()

    plt.tight_layout()

    # 7. Save chart to Termux folder
    plt.savefig(
        os.path.join(PATH, "cuisine_distribution_onlineorder.png"),
        dpi=500,
        transparent=False,
        bbox_inches="tight"
    )
    print("Chart saved: cuisine_distribution_onlineorder.png")

    # 8. Show chart on screen
    plt.show()

    # 9. Close figure to free memory (prevents overlap in next chart)
    plt.close()

    # 10. Return plt
    return plt


# Question 5: What are the correlations among numeric variables?

def plot_pro_corr(df, title="Feature Correlation: Identifying Multi-collinearity"):
    # 1. Professional Style Setup
    sns.set_theme(style="white", context="talk")
    
    plt.rcParams['figure.dpi'] = 100

    # 2. Data Preparation: Numeric Correlation
    corr = df.corr(numeric_only=True)

    # 3. Mask Upper Triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 4. Core Heatmap Execution
    fig, ax = plt.subplots(figsize=(12, 10), dpi=100)
    sns.heatmap(
        corr,
        mask=mask,
        cmap='RdBu_r',
        vmax=1, vmin=-1, center=0,
        annot=True, fmt='.2f',
        square=True,
        linewidths=.8,
        cbar_kws={"shrink": .7, "label": "Pearson Correlation Coefficient"},
        ax=ax
    )

    # 5. Professional Polish
    ax.set_title(title, loc='left', fontsize=20, fontweight='bold', pad=30)
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.yticks(rotation=0, fontsize=12)

    # 6. Final Layout
    plt.tight_layout()

    # 7. Save chart to Termux folder
    plt.savefig(
        os.path.join(PATH, "correlation_heatmap.png"),
        dpi=500,
        transparent=False,
        bbox_inches="tight"
    )
    print("Chart saved: correlation_heatmap.png")

    # 8. Show chart on screen
    plt.show()

    # 9. Close figure to free memory (prevents overlap in next chart)
    plt.close()

    # 10. Return plt
    return plt


# =================================================================
# SECTION H: FINAL EXECUTION
# =================================================================
print("\n[PROCESS] Generating high-resolution insights...")

# 1. Analyzing impact of online orders on engagement
plot_pro_bar(sub_set)

# 2. Benchmarking the distribution of restaurant ratings
plot_pro_hist(sub_set)

# 3. Correlation analysis between votes and ratings
plot_pro_scatter(sub_set)

# 4. Visualizing frequency of top cuisines
plot_pro_count(data)

# 5. Multicollinearity check via Feature Correlation Heatmap
plot_pro_corr(sub_set)

print("[DONE] All 5 charts saved successfully!")

end = time.time()
print(f"-----Required Data Loading Time: {end - start:.4f} seconds------")
