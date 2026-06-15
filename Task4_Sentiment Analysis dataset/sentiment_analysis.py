
!pip install wordcloud networkx plotly --quiet

from google.colab import files
uploaded = files.upload()
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt

import re
import nltk
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from wordcloud import WordCloud
import networkx as nx
from collections import Counter
from itertools import combinations

df = pd.read_csv('/content/Twitter_Data.csv')
df = df.dropna()
df.columns = ['clean_text', 'category']
df['category'] = df['category'].replace({-1:'Negative', 0:'Neutral', 1:'Positive'})

print("="*70)
print("💎 RECRUITER WOW EDITION – AI SENTIMENT INTELLIGENCE")
print("="*70)
print(f"✅ Loaded {len(df)} tweets | Sentiment distribution:\n{df['category'].value_counts()}")

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#", "", text)
    text = re.sub(r"[^a-zA-Z ]", "", text)
    words = text.split()
    words = [lemmatizer.lemmatize(w) for w in words if w not in stop_words]
    return " ".join(words)

df['processed_text'] = df['clean_text'].apply(clean_text)
total = len(df)
pos_pct = (df['category']=='Positive').mean()*100
neg_pct = (df['category']=='Negative').mean()*100
neu_pct = (df['category']=='Neutral').mean()*100
avg_len = df['processed_text'].str.len().mean()
sentiment_score = pos_pct - neg_pct

fig_kpi = make_subplots(
    rows=2, cols=3,
    specs=[[{'type':'indicator'}, {'type':'indicator'}, {'type':'indicator'}],
           [{'type':'indicator'}, {'type':'indicator'}, {'type':'indicator'}]],
    subplot_titles=("📊 Total Tweets", "😊 Positive %", "😡 Negative %",
                    "😐 Neutral %", "📝 Avg Words", "🔥 Net Sentiment")
)

fig_kpi.add_trace(go.Indicator(mode="number", value=total, title={"text":"Tweets"}, number_font_size=40), row=1, col=1)

fig_kpi.add_trace(go.Indicator(mode="number", value=pos_pct, title={"text":"Positive"}, number_suffix="%", number_font_color="#00FFAA"), row=1, col=2)

fig_kpi.add_trace(go.Indicator(mode="number", value=neg_pct, title={"text":"Negative"}, number_suffix="%", number_font_color="#FF3366"), row=1, col=3)

fig_kpi.add_trace(go.Indicator(mode="number", value=neu_pct, title={"text":"Neutral"}, number_suffix="%", number_font_color="#FFD700"), row=2, col=1)

fig_kpi.add_trace(go.Indicator(mode="number", value=round(avg_len,1), title={"text":"Words"}, number_font_size=35), row=2, col=2)

fig_kpi.add_trace(go.Indicator(
    mode="gauge+number",
    value=sentiment_score,
    title={"text":""},
    gauge={
        'axis':{'range':[-100,100]},
        'bar':{'color':'#FF66CC'},
        'steps':[
            {'range':[-100,0], 'color':'#FF3366'},
            {'range':[0,100], 'color':'#00FFAA'}
        ]
    }),
    row=2, col=3
)

fig_kpi.update_layout(template="plotly_dark", height=500, title="✨ NEON EXECUTIVE DASHBOARD")
fig_kpi.show()

df['word_bin'] = pd.cut(df['processed_text'].str.split().str.len(), bins=[0,5,10,20,50], labels=['short','medium','long','very long'])
sunburst_data = df.groupby(['category','word_bin']).size().reset_index(name='count')

fig_sun = px.sunburst(sunburst_data, path=['category','word_bin'], values='count',
                      color='category', color_discrete_map={'Positive':'#00FFAA','Negative':'#FF3366','Neutral':'#FFD700'},
                      title="🌀 SUNBURST: Sentiment + Tweet Length", template="plotly_dark")
fig_sun.show()

fig_tree = px.treemap(sunburst_data, path=['category','word_bin'], values='count',
                      color='count', color_continuous_scale='Plasma', title="🌳 TREEMAP OF SENTIMENT VOLUME")
fig_tree.update_layout(template="plotly_dark")
fig_tree.show()

def create_heart_mask(size=(800, 600)):
    """Create a heart-shaped mask. Size is (width, height)."""
    width, height = size
    x = np.linspace(-1.5, 1.5, width)
    y = np.linspace(-1.5, 1.5, height)
    X, Y = np.meshgrid(x, y)
    heart = (X**2 + (9/4)*Y**2 - 1)**3 - X**2 * (0.5*Y)**3
    mask = heart <= 0
    img_mask = np.zeros((height, width), dtype=np.uint8)
    img_mask[mask] = 255
    return img_mask

def create_skull_mask(size=(800, 600)):
    width, height = size
    mask = np.zeros((height, width), dtype=np.uint8)
    y, x = np.ogrid[:height, :width]
    center_x, center_y = width//2, height//2
    head = ((x - center_x) / (width*0.35))**2 + ((y - center_y) / (height*0.4))**2 <= 1
    left_eye = ((x - center_x + width*0.12) / (width*0.08))**2 + ((y - center_y - height*0.05) / (height*0.08))**2 <= 1
    right_eye = ((x - center_x - width*0.12) / (width*0.08))**2 + ((y - center_y - height*0.05) / (height*0.08))**2 <= 1
    nose = ((x - center_x) / (width*0.05))**2 + ((y - center_y + height*0.05) / (height*0.1))**2 <= 0.5
    mask[head] = 255
    mask[left_eye] = 0
    mask[right_eye] = 0
    mask[nose] = 0
    return mask

pos_words = " ".join(df[df['category']=='Positive']['processed_text'])
heart_mask = create_heart_mask((800, 600))
wc_pos = WordCloud(background_color='black', colormap='spring', mask=heart_mask, contour_width=1, contour_color='pink').generate(pos_words)

neg_words = " ".join(df[df['category']=='Negative']['processed_text'])
skull_mask = create_skull_mask((800, 600))
wc_neg = WordCloud(background_color='black', colormap='autumn', mask=skull_mask, contour_width=1, contour_color='red').generate(neg_words)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
ax1.imshow(wc_pos, interpolation='bilinear')
ax1.set_title("😊 POSITIVE – Heart of Joy", fontsize=18, color='#00FFAA')
ax1.axis('off')
ax2.imshow(wc_neg, interpolation='bilinear')
ax2.set_title("😡 NEGATIVE – Skull of Anger", fontsize=18, color='#FF3366')
ax2.axis('off')
plt.suptitle("☠️ CUSTOM-SHAPED WORD CLOUDS (No External Images)", fontsize=24, color='white')
plt.tight_layout()
plt.show()

all_words = " ".join(df['processed_text']).split()
top_words = [w for w, _ in Counter(all_words).most_common(15)]

co_occur = {}
for tweet in df['processed_text']:
    words = set(tweet.split())
    for w1, w2 in combinations(words, 2):
        if w1 in top_words and w2 in top_words:
            key = tuple(sorted([w1,w2]))
            co_occur[key] = co_occur.get(key, 0) + 1

chord_df = pd.DataFrame([(a,b,c) for (a,b),c in co_occur.items()], columns=['source','target','value'])
chord_df = chord_df.sort_values('value', ascending=False).head(30)

nodes = list(set(chord_df['source']).union(set(chord_df['target'])))
node_map = {n:i for i,n in enumerate(nodes)}
chord_df['source_idx'] = chord_df['source'].map(node_map)
chord_df['target_idx'] = chord_df['target'].map(node_map)

fig_chord = go.Figure(data=[go.Sankey(
    node=dict(pad=15, thickness=20, line=dict(color="black", width=0.5),
              label=nodes, color="cyan"),
    link=dict(source=chord_df['source_idx'], target=chord_df['target_idx'], value=chord_df['value']))
])
fig_chord.update_layout(title="🎵 WORD CO-OCCURRENCE CHORD DIAGRAM (Rare & Beautiful)", font_size=12, template='plotly_dark', height=600)
fig_chord.show()

X = df['processed_text']; y = df['category']
vectorizer = TfidfVectorizer(max_features=5000)
X_vec = vectorizer.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

models = {"Logistic Regression": LogisticRegression(), "Naive Bayes": MultinomialNB(), "Linear SVM": LinearSVC()}
results = []
for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    acc = accuracy_score(y_test, pred)
    results.append({'Model': name, 'Accuracy': acc})

best_model_name = max(results, key=lambda x: x['Accuracy'])['Model']
best_model = models[best_model_name]
y_pred = best_model.predict(X_test)

n_bootstrap = 100
boot_accs = []
y_test_array = y_test.to_numpy() if hasattr(y_test, 'to_numpy') else np.array(y_test)
for _ in range(n_bootstrap):
    idx = np.random.choice(len(y_test), len(y_test), replace=True)
    boot_accs.append(accuracy_score(y_test_array[idx], y_pred[idx]))
ci_low, ci_high = np.percentile(boot_accs, [2.5, 97.5])

results_df = pd.DataFrame(results)
fig_model = px.bar(results_df, x='Model', y='Accuracy', color='Accuracy', text='Accuracy',
                   color_continuous_scale='Rainbow', title="🏆 MODEL PERFORMANCE WITH CONFIDENCE INTERVALS")
fig_model.add_hrect(y0=ci_low, y1=ci_high, line_width=0, fillcolor="rgba(255,255,0,0.2)", annotation_text="95% CI of best model")
fig_model.update_traces(texttemplate='%{text:.2%}', textposition='outside')
fig_model.update_layout(template='plotly_dark', yaxis_tickformat='.0%', height=550)
fig_model.show()

cm = confusion_matrix(y_test, y_pred, labels=['Positive','Neutral','Negative'])
cm_norm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
annot = [[f"{val}\n({pct:.0%})" for val, pct in zip(row, row_norm)] for row, row_norm in zip(cm, cm_norm)]
fig_cm = px.imshow(cm, text_auto=False, labels=dict(x="Predicted", y="Actual"), color_continuous_scale='Turbo',
                   title=f"🎯 CONFUSION MATRIX – {best_model_name} (with %)")
for i in range(3):
    for j in range(3):
        fig_cm.add_annotation(x=j, y=i, text=annot[i][j], showarrow=False, font=dict(color='white'))
fig_cm.update_layout(template='plotly_dark', height=500)
fig_cm.show()

print("\n📋 CLASSIFICATION REPORT\n", classification_report(y_test, y_pred))

top30 = [w for w,_ in Counter(all_words).most_common(30)]
G = nx.Graph()
G.add_nodes_from(top30)
for tweet in df['processed_text']:
    words = set(tweet.split())
    for w1,w2 in combinations(words,2):
        if w1 in top30 and w2 in top30:
            if G.has_edge(w1,w2):
                G[w1][w2]['weight'] += 1
            else:
                G.add_edge(w1,w2,weight=1)

pos = nx.spring_layout(G, seed=42)
edge_trace = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_trace.append(go.Scatter(x=[x0,x1], y=[y0,y1], mode='lines', line=dict(width=G[edge[0]][edge[1]]['weight']/10, color='cyan'), hoverinfo='none'))

node_x, node_y = zip(*[pos[n] for n in G.nodes()])
node_trace = go.Scatter(x=node_x, y=node_y, mode='markers+text', text=list(G.nodes()), textposition="top center",
                        marker=dict(size=[G.degree(n)*2 for n in G.nodes()], color='#FF66CC', line_width=2))

fig_net = go.Figure(data=edge_trace + [node_trace])
fig_net.update_layout(title="🕸️ WORD NETWORK GRAPH (Size = Degree, Edge Width = Co-occurrence)",
                      showlegend=False, template='plotly_dark', height=700)
fig_net.show()

df['sentiment_num'] = df['category'].map({'Positive':1, 'Neutral':0, 'Negative':-1})
df['rolling_mean'] = df['sentiment_num'].rolling(50, center=True).mean()
fig_line = px.line(df, x=df.index, y='rolling_mean', title="📈 SENTIMENT TREND OVER TWEETS (Rolling avg 50)",
                   labels={'index':'Tweet Sequence', 'rolling_mean':'Sentiment Polarity'}, color_discrete_sequence=['#FFD700'])
fig_line.add_hline(y=0, line_dash="dash", line_color="white")
fig_line.update_layout(template='plotly_dark', height=500)
fig_line.show()

sample_texts = [
    "This product is absolutely amazing and wonderful!",
    "Worst experience ever, very disappointed.",
    "The service was okay and average."
]
sample_clean = [clean_text(t) for t in sample_texts]
sample_vec = vectorizer.transform(sample_clean)
preds = best_model.predict(sample_vec)

pred_df = pd.DataFrame({'Text': sample_texts, 'Predicted Sentiment': preds})
print("\n🤖 LIVE PREDICTION RESULTS\n", pred_df)

df['Predicted'] = best_model.predict(X_vec)
df.to_csv('Sentiment_Recruiter_Edition.csv', index=False)
files.download('Sentiment_Recruiter_Edition.csv')

print("\n" + "="*70)
print("🏆 RECRUITER WOW EDITION – FINAL INSIGHTS")
print("="*70)
print(f"✅ Total tweets analyzed : {total}")
print(f"😊 Positive : {pos_pct:.1f}%  |  😡 Negative : {neg_pct:.1f}%")
print(f"🔥 Net sentiment score : {sentiment_score:.1f}")
print(f"🤖 Best model : {best_model_name} with {results_df['Accuracy'].max():.1%} accuracy")
print(f"📊 95% confidence interval : [{ci_low:.1%}, {ci_high:.1%}]")
print("\n✨ UNIQUE FEATURES IN THIS WORK:")
print("✔ Heart-shaped & skull-shaped word clouds")
print("✔ Chord diagram for word co-occurrence")
print("✔ Sunburst + treemap hierarchy")
print("✔ Model confidence intervals (bootstrapping)")
print("✔ Network graph of top 30 words")
print("✔ Neon KPI dashboard with sentiment gauge")
print("✔ Rolling sentiment trend line")
print("\n💎 THIS IS NOT YOUR TYPICAL SENTIMENT ANALYSIS. RECRUITERS WILL REMEMBER THIS.")
print("="*70)
