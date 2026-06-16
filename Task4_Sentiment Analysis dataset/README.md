![Stars](https://img.shields.io/github/stars/Rithika04-create/OasisInfobyte-Task4-SentimentAnalysis?style=social)
![Forks](https://img.shields.io/github/forks/Rithika04-create/OasisInfobyte-Task4-SentimentAnalysis?style=social)
![Issues](https://img.shields.io/github/issues/Rithika04-create/OasisInfobyte-Task4-SentimentAnalysis)

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
git clone https://github.com/Rithika04-create/OasisInfobyte-Task4-SentimentAnalysis.git
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

## 🎥 Live Demo

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Q0NXh_SanSi8I3CbmAS-IYaKSqdUqgEZ#scrollTo=Ii8_jR1C61eN)

Click the badge above to run the entire project in your browser – no installation required! 🚀

---

## 📈 Sample Visualizations

| Neon KPI Dashboard | Heart & Skull Word Clouds |
|:------------------:|:-------------------------:|
|<img width="1201" height="377" alt="image" src="https://github.com/user-attachments/assets/fe78ced4-dddb-477c-a831-4a81171dc001" /> | <img width="1227" height="479" alt="image" src="https://github.com/user-attachments/assets/8f6e707a-c613-4ce2-a507-5e3274ec698e" /> |

| Chord Diagram | Confusion Matrix |
|:-------------:|:----------------:|
| <img width="1207" height="445" alt="image" src="https://github.com/user-attachments/assets/b61b551b-9f53-484b-afe5-4e0582bb352b" /> | <img width="1183" height="398" alt="image" src="https://github.com/user-attachments/assets/0ac03a07-7f90-4582-8b78-e040585f09a9" /> |

| Sunburst Chart | Treemap |
|:--------------:|:-------:|
| <img width="1143" height="400" alt="image" src="https://github.com/user-attachments/assets/01252bc3-9a59-4eb0-a37d-d3fe77613ebe" /> | <img width="1185" height="406" alt="image" src="https://github.com/user-attachments/assets/336279dc-88f8-4d58-aa47-d4a1089042d8" /> |

| Network Graph | Sentiment Trend |
|:-------------:|:---------------:|
|<img width="1188" height="496" alt="image" src="https://github.com/user-attachments/assets/9f381dec-0379-48a6-91a0-cdd760e2444c" /> | <img width="1200" height="365" alt="image" src="https://github.com/user-attachments/assets/65e0e702-b73f-4f1a-9fed-dfcba05b2fbc" /> |

---

## 📊 Model Performance

| Model | Accuracy | 95% CI |
|-------|----------|--------|
| Logistic Regression | 85.2% | ±2.1% |
| Naive Bayes | 82.7% | ±1.9% |
| **Linear SVM** | **88.3%** | **±1.8%** |

> 🏆 **Best Model:** Linear SVM

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

# ✅ Dataset Section

```markdown id="5ijh8f"
## 📁 Dataset

- **Dataset Name:** `Twitter_Data.csv`
- **Type:** Twitter sentiment dataset
- **Records:** 160,000+ tweets
- **Classes:** Positive, Negative, Neutral
- **Purpose:** Sentiment classification using NLP and Machine Learning
```

---

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

## 🔗 Connect With Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Rithika-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/rithika-s-318694339)

[![GitHub](https://img.shields.io/badge/GitHub-Rithika04-black?style=for-the-badge&logo=github)](https://github.com/Rithika04-create)

[![Gmail](https://img.shields.io/badge/Gmail-Contact%20Me-red?style=for-the-badge&logo=gmail)](mailto:rithikasanthanam0406@gmail.com)

---

📝 Hashtags

#oasisinfobyte #oasisinfobytefamily #internship #python #DataScience #NLP #MachineLearning #SentimentAnalysis #AI

---

📄 License

MIT License – feel free to use, learn, and improve!

---

## ⭐ If You Like This Project

Give this repository a star and feel free to fork it for learning purposes.


