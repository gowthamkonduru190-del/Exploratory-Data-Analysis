# Exploratory-Data-Analysis
## 📌 Project Overview

This project performs **Exploratory Data Analysis (EDA)** on the Titanic dataset using Python. The main objective is to analyze passenger information, identify important patterns, clean the dataset, and visualize insights related to survival rates.

The project includes:

* Data Cleaning
* Missing Value Handling
* Outlier Detection
* Correlation Analysis
* Data Visualization
* Automated Data Profiling

---

# 📂 Dataset

The dataset contains passenger details such as:

* Passenger Class
* Name
* Gender
* Age
* Fare
* Cabin
* Embarked Location
* Survival Status

---

# 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* YData Profiling

---

# 📊 EDA Steps Performed

## 1. Data Loading

* Loaded the Titanic dataset using Pandas.

## 2. Data Understanding

* Checked dataset shape, columns, and data types.
* Generated statistical summaries.

## 3. Missing Value Analysis

* Identified missing values using heatmaps and summary functions.
* Filled missing values in:

  * `Age` using median
  * `Embarked` using mode
* Removed `Cabin` column due to excessive missing values.

## 4. Duplicate Value Check

* Verified duplicate records in the dataset.

## 5. Univariate Analysis

Performed visualization for:

* Survival Count
* Gender Distribution
* Passenger Class Distribution
* Age Distribution
* Fare Distribution

## 6. Bivariate Analysis

Analyzed relationships between:

* Survival vs Gender
* Survival vs Passenger Class
* Age vs Survival
* Fare vs Survival

## 7. Correlation Analysis

* Converted categorical features into numerical values.
* Generated correlation heatmaps.

## 8. Outlier Detection

* Detected outliers using boxplots for:

  * Age
  * Fare

## 9. Automated Profiling Report

* Generated a complete profiling report using YData Profiling.

---

# 📈 Key Insights

* Female passengers had higher survival rates.
* First-class passengers survived more frequently.
* Most passengers belonged to the age group of 20–40 years.
* Fare column contained significant outliers.
* Data cleaning improved dataset quality and analysis accuracy.

---

# 📷 Visualizations Included

* Count Plots
* Histograms
* Heatmaps
* Boxplots
* Pairplots
* Correlation Matrix

---

# 🚀 How to Run the Project

## Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn ydata-profiling
```

## Run the Notebook

```bash
jupyter notebook
```

Open the notebook and run all cells.

---

# 📁 Project Structure

```bash
Titanic-EDA/
│
├── titanic.csv
├── Titanic_EDA_Notebook.ipynb
├── titanic_report.html
└── README.md
```

---

# 🎯 Conclusion

This project demonstrates the importance of Exploratory Data Analysis in understanding datasets before building machine learning models. Through visualization and preprocessing, meaningful insights were extracted from the Titanic dataset.

---

# 👨‍💻 Author

Shaik Abid
