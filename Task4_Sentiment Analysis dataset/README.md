![Stars](https://img.shields.io/github/stars/yourusername/OasisInfobyte-Task4-SentimentAnalysis?style=social)
![Forks](https://img.shields.io/github/forks/yourusername/OasisInfobyte-Task4-SentimentAnalysis?style=social)
![Issues](https://img.shields.io/github/issues/yourusername/OasisInfobyte-Task4-SentimentAnalysis)

# 🚀 Sentiment Analysis 

## Oasis Infobyte Internship | Task 4

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![NLP](https://img.shields.io/badge/NLP-NLTK-green.svg)
![ML](https://img.shields.io/badge/Machine%20Learning-SVM%20%7C%20Logistic%20Regression%20%7C%20Naive%20Bayes-orange.svg)
![Plotly](https://img.shields.io/badge/Visualization-Plotly-purple.svg)
![License](https://img.shields.io/badge/License-MIT-red.svg)

> **"Most sentiment analysis projects look the same. I built one recruiters would actually remember."** 🎯

---

## 📌 Overview

This project performs **sentiment analysis on 160K+ tweets** using Natural Language Processing and Machine Learning. But unlike basic implementations, this version features **stunning, interactive visualizations** that tell a compelling story.

### ✨ What Makes This Unique?

| Feature | Typical Project | This Project |
|---------|----------------|--------------|
| Word Clouds | Basic circles | ❤️ Heart + 💀 Skull shapes |
| Model Comparison | Simple bar chart | + Confidence intervals (bootstrapping) |
| Word Relationships | Frequency bar | Chord diagram + Network graph |
| KPI Dashboard | Numbers only | Neon gauges + Sentiment meter |
| Hierarchy | None | Sunburst + Treemap |
| Trend Analysis | None | Rolling sentiment over tweets |

---

## 🔍 Key Features

✅ **Neon KPI Dashboard** – Live sentiment gauge with real-time metrics  
✅ **Heart‑shaped Word Cloud** – Positive tweets visualized beautifully ❤️  
✅ **Skull‑shaped Word Cloud** – Negative tweets with impact 💀  
✅ **Chord Diagram** – Word co‑occurrence relationships  
✅ **Network Graph** – Top 30 words & their connections  
✅ **Sunburst + Treemap** – Hierarchical sentiment analysis  
✅ **Model Confidence Intervals** – Bootstrapping for statistical rigor  
✅ **Rolling Sentiment Trend** – How emotions evolve over tweets  
✅ **Live Prediction Demo** – Test custom sentences instantly  
✅ **3 ML Models** – Logistic Regression, Naive Bayes, Linear SVM

---

## 📊 Tech Stack

```

┌─────────────────────────────────────────────────────┐
│  Python 3.9+                                        │
│  ├── NLP: NLTK, Regular Expressions                │
│  ├── ML: Scikit-learn (TF-IDF, SVM, Logistic Reg)  │
│  ├── Visualization: Plotly, Matplotlib, WordCloud  │
│  ├── Graph: NetworkX                               │
│  └── Data: Pandas, NumPy                           │
└─────────────────────────────────────────────────────┘

```

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/OasisInfobyte-Task4-SentimentAnalysis.git
cd OasisInfobyte-Task4-SentimentAnalysis
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Download NLTK data (automatically handled in script)

```python
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
```

4. Run the script

```bash
python sentiment_analysis.py
```

5. Upload your dataset

· The script will prompt you to upload Twitter_Data.csv
· Or place it in the same directory as Twitter_Data.csv

---

📈 Sample Visualizations

    Dashboard                      Word Clouds
images/dashboard.png           images/wordclouds.png

    Chord Diagram                 Confusion Matrix
images/chord_diagram.png      images/confusion_matrix.png

---

📊 Model Performance

Model Accuracy 95% CI
Logistic Regression ~85% ±2%
Naive Bayes ~83% ±2%
Linear SVM ~88% ±2%

🏆 Best Model: Linear SVM

---

## 🧠 Machine Learning Workflow

```text
Raw Tweets
   ↓
Text Cleaning
   ↓
Tokenization
   ↓
Stopword Removal
   ↓
Lemmatization
   ↓
TF-IDF Vectorization
   ↓
Model Training
   ↓
Prediction & Evaluation
```

This makes recruiters instantly understand your NLP pipeline.

---

# ✅ Add Dataset Section

```markdown id="5ijh8f"
## 📁 Dataset

- **Dataset Name:** `Twitter_Data.csv`
- **Type:** Twitter sentiment dataset
- **Records:** 160,000+ tweets
- **Classes:** Positive, Negative, Neutral
- **Purpose:** Sentiment classification using NLP and Machine Learning
```

📁 Project Structure

```
├── sentiment_analysis.py    # Main script (copy the final code)
├── requirements.txt         # Dependencies
├── Twitter_Data.csv         # Dataset (not included - upload manually)
├── images/                  # Screenshots for README
└── output/                  # Generated predictions
```

---

🎯 Key Takeaways for Recruiters

This project demonstrates:

· ✅ Advanced NLP – Text preprocessing, lemmatization, TF-IDF
· ✅ ML Mastery – Multiple models, hyperparameter tuning, bootstrapping
· ✅ Data Storytelling – Visualizations that drive insights
· ✅ Creative Problem Solving – Custom-shaped word clouds, chord diagrams
· ✅ Production Ready – Clean code, error handling, exports

---

💡 Real Experience

"It took 3 iterations to fix the heart-mask error and overlapping dashboard text. But that struggle taught me more than any perfect first run. Debugging = learning." 💪

---

🔗 Connect With Me

https://img.shields.io/badge/LinkedIn-Connect-blue
https://img.shields.io/badge/GitHub-Follow-black
https://img.shields.io/badge/Email-Contact-red

---

📝 Hashtags

#oasisinfobyte #oasisinfobytefamily #internship #python #DataScience #NLP #MachineLearning #SentimentAnalysis #AI

---

📄 License

MIT License – feel free to use, learn, and improve!

---

⭐ Star this repo if you found it useful!


