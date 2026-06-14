># 🧹 Task 3: Data Cleaning – Airbnb Dataset  

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Cleaning-orange)
![Plotly](https://img.shields.io/badge/Visualization-Interactive-success)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)
![NumPy](https://img.shields.io/badge/NumPy-1.21+-lightblue)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-teal)
![License](https://img.shields.io/badge/License-MIT-yellow)  

## 🎯 Objective  
Clean a real-world Airbnb dataset by handling missing values, removing duplicates, detecting outliers, and preparing it for analysis.  
  
## 📌 Project Background  
Raw data is rarely clean. This project simulates a real industry task where messy data is transformed into an analysis-ready format using Python.  
  
## 🛠️ Tech Stack  
- **Language:** Python  
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Plotly  
- **Environment:** Google Colab / Jupyter Notebook  
  
## 📁 Dataset

- **Dataset Name:** `Airbnb_Open_Data.csv`
- **Source:** Airbnb Open Dataset
- **Records:** ~48,000+ rows
- **Purpose:** Used for data cleaning, preprocessing, outlier detection, and visualization tasks.
  
## ✅ Steps Performed  
  
### 1. Data Loading & Inspection  
- Loaded dataset using Pandas  
- Checked shape, info, describe, and sample rows  
- Identified data quality issues  
  
### 2. Missing Value Treatment  
- Analyzed missing percentage per column  
- Used mean/median imputation for numerical columns  
- Used mode imputation for categorical columns  
- Dropped columns with >50% missing values  
  
### 3. Duplicate Removal  
- Identified duplicate rows  
- Removed ~15% duplicate records  
- Kept first occurrence only  
  
### 4. Outlier Detection & Removal  
- Used **IQR (Interquartile Range)** method  
- Calculated Q1, Q3, and IQR  
- Removed values outside [Q1 - 1.5*IQR, Q3 + 1.5*IQR]  
- Focused on price column anomalies  
  
### 5. Data Type Standardization  
- Converted price to numeric  
- Standardized date formats  
- Fixed categorical inconsistencies  
  
### 6. Feature Engineering (Optional)  
- Extracted neighbourhood groups  
- Created price brackets (Low/Medium/High)  
  
### 7. Visualization  
- Missing values heatmap  
- Boxplots for outlier detection  
- Price distribution (before vs after)  
- Correlation heatmap  
- Interactive Plotly dashboard  
  
### 8. Export Cleaned Data  
- Saved as `cleaned_data.csv`  
- Generated cleaning summary report  
  
## 📊 Key Insights After Cleaning  
  
| Insight | Finding |  
|---------|---------|  
| Top Neighbourhoods | 3 neighbourhoods drive 60% of high-value listings |  
| Room Type Popularity | Entire homes/apts are most common after outlier removal |  
| Price Range | Most listings between $50-$350 after cleaning |  
| Data Quality | 0 missing values, 0 duplicates, outliers removed |  

## 💼 Business Impact

This cleaned dataset can now be used for:

| Business Use Case | Application |
|-------------------|-------------|
| 💰 *Pricing Analysis* | Identify optimal price points by neighbourhood & room type |
| 👥 *Customer Behavior Analytics* | Understand booking patterns & preferences |
| 🎯 *Recommendation Systems* | Suggest similar listings based on cleaned features |
| 📈 *Predictive Modeling* | Forecast demand, occupancy rates & revenue |
| 📊 *Market Trend Analysis* | Track seasonal trends & emerging hotspots |

> 🚀 *Real-world value:* Clean data = Better business decisions. This dataset is now *production-ready* for dashboards, ML models, and strategic planning.
  
## 📈 Before vs After Comparison  
  
| Metric | Before | After |  
|--------|--------|-------|  
| Total Rows | 48,895 | ~41,500 |  
| Missing Values | 12 columns | 0 |  
| Duplicates | ~7,000 rows | 0 |  
| Price Outliers | 847 removed | Clean distribution |  
| Dataset Quality | Poor | Production-ready |  

---

## 📊 Dashboard Preview

### 🏠 Neighbourhood Analysis
- **Top revenue zones identified**
- 🔥 **3 neighbourhoods drive 60%** of high-value listings

### 🎛️ Interactive Dashboard (Plotly HTML)
> 🔗 **[Open Interactive Dashboard](visualizations/cleaning_dashboard.html)**

The HTML dashboard allows you to:
- ✅ Hover over data points for exact values
- ✅ Filter by neighbourhood & room type
- ✅ Zoom into specific price ranges
- ✅ Export filtered views

---

### 🖼️ Preview Images

<img width="856" height="523" alt="image" src="https://github.com/user-attachments/assets/cf63872b-bc19-4849-80c5-026483cc14c9" />

*Figure 1: Missing values heatmap showing data quality issues before cleaning*

<img width="846" height="325" alt="image" src="https://github.com/user-attachments/assets/07a7d9ba-34a0-440b-b5f8-d4b4721a964c" />

*Figure 2: Boxplot showing price outliers removed using IQR method*

<img width="1235" height="395" alt="image" src="https://github.com/user-attachments/assets/455e81b0-2008-45e7-821a-60dfe958ffe4" />

*Figure 3: Price distribution before vs after outlier removal*

---

### 📸 Screenshot Preview

<img width="385" height="425" alt="Executive Data Cleaning Report" src="https://github.com/user-attachments/assets/58c44540-38fa-4fe8-b43d-f1ebbb9bd698" />

*Figure 4: Final cleaned data output preview*

---

> 💡 **Note:** If images don't load, please check the `visualizations/` and `screenshots/` folders in this repository.

## 🚀 How to Run

```bash
# 1. Clone repository
git clone https://github.com/Rithika04-create/OIBSIP.git

# 2. Navigate to Task 3 folder
cd OIBSIP/Task3_Cleaning_Data

# 3. Install dependencies
pip install -r requirements.txt

# 4. Open notebook
jupyter notebook notebooks/data_cleaning.ipynb
```

📂 Files in This Repository

```
Task3_Cleaning_Data/
│
├── README.md                    # This file
├── requirements.txt             # Dependencies
│
├── data/
│   ├── raw_data.csv            # Original messy data
│   └── cleaned_data.csv        # Cleaned output
│
├── notebooks/
│   └── data_cleaning.ipynb     # Complete code
│
├── visualizations/
│   ├── missing_values_heatmap.png
│   ├── outlier_detection.png
│   ├── price_distribution.png
│   └── cleaning_dashboard.html
│
├── outputs/
│   └── cleaning_summary_report.txt
│
└── screenshots/
    └── final_output.png
```

## 💡 Key Learnings

- Data cleaning takes **60-80% of analysis time** in real industry
- **IQR method** is effective for price outlier detection
- **Interactive visualizations** help stakeholders understand data quality
- Clean data leads to **accurate business insights**

## ✅ Task Completion Checklist

- [x] Load and inspect data
- [x] Handle missing values
- [x] Remove duplicates
- [x] Detect and remove outliers (IQR)
- [x] Standardize data types
- [x] Create visualizations
- [x] Export cleaned dataset
- [x] Generate summary report

## 🔗 Connect With Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Rithika-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/rithika-s-318694339)
[![GitHub](https://img.shields.io/badge/GitHub-Rithika04-black?style=for-the-badge&logo=github)](https://github.com/Rithika04-create)
[![Gmail](https://img.shields.io/badge/Gmail-Contact%20Me-red?style=for-the-badge&logo=gmail)](mailto:rithikasanthanam0406@gmail.com)

## 📜 License

This project is submitted as part of the **Oasis Infobyte Data Analytics Internship**.

---

**#OasisInfobyte #Task3 #DataCleaning #Python #AirbnbAnalytics #Plotly #DataScience**
