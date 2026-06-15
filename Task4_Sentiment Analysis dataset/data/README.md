# 📊 Dataset Information

## Twitter_Data.csv

This project uses a Twitter sentiment dataset provided by **Oasis Infobyte** for Task 4.

### Dataset Details

| Property | Value |
|----------|-------|
| **File Name** | `Twitter_Data.csv` |
| **Records** | 160,000+ tweets |
| **Format** | CSV (Comma Separated Values) |
| **Encoding** | UTF-8 |

### Columns

| Column | Description | Values |
|--------|-------------|--------|
| `clean_text` | Preprocessed tweet text | String |
| `category` | Sentiment label | -1 (Negative), 0 (Neutral), 1 (Positive) |

### Sentiment Distribution

After preprocessing, labels are mapped to:

| Original | Mapped |
|----------|--------|
| -1 | Negative |
| 0 | Neutral |
| 1 | Positive |

---

## 📥 How to Get the Dataset

### Option 1: From Oasis Infobyte (Recommended)
- Download from the internship portal
- Place `Twitter_Data.csv` in the root folder

### Option 2: Alternative Source
- Use any Twitter sentiment dataset from [Kaggle](https://www.kaggle.com/datasets)
- Rename it to `Twitter_Data.csv`

---

## 🚀 How to Use

### For Local Running:
```bash
# Place the file in the project root folder
OasisInfobyte-Task4-SentimentAnalysis/
└── Twitter_Data.csv    # ← Place here

