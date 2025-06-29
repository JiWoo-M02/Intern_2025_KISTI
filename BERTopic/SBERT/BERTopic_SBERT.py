# %%
from bertopic import BERTopic
import pandas as pd
import hdbscan
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

# === 데이터 불러오기 ===
file_path = r"C:\Users\MaengJiwoo\.vscode\KISTI-intern\2025_KISTI-intern\BERTopic\FA_entities.csv"
df = pd.read_csv(file_path, encoding="utf-8")

label_to_process = 'problem'
# label_to_process = 'solution'
# label_to_process = 'target'

df_filtered = df[df['entity_label'] == label_to_process].copy()
unique_texts = df_filtered['entity_text'].drop_duplicates().tolist()

# === SBERT ===
sbert_model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
embeddings = sbert_model.encode(unique_texts, show_progress_bar=True)

# === HDBSCAN ===
hdbscan_model = hdbscan.HDBSCAN(
    min_cluster_size=2,
    metric="euclidean",
    cluster_selection_method='eom',
    prediction_data=True
)

# === BERTopic ===
topic_model = BERTopic(
    embedding_model=None,
    hdbscan_model=hdbscan_model,
    min_topic_size=1,
    nr_topics="auto",
    verbose=True
)
topics, probs = topic_model.fit_transform(unique_texts, embeddings)
text2topic = dict(zip(unique_texts, topics))


# === 토픽 결과를 원본 데이터에 매핑 및 저장 ===
num = 2  # 파일 넘버
df_filtered['topic'] = df_filtered['entity_text'].map(text2topic)
df_filtered.to_csv(
    f"C:/Users/MaengJiwoo/.vscode/KISTI-intern/2025_KISTI-intern/BERTopic/SBERT/entity_topic_{label_to_process}_{num}.csv",
    index=False
)

# === 토픽 정보 집계 및 저장 ===
topic_info_df = topic_model.get_topic_info().set_index('Topic')
topic_counts = df_filtered['topic'].value_counts().sort_index()
topic_info_df['Count'] = topic_counts
topic_info_df['Count'] = topic_info_df['Count'].fillna(0).astype(int)
topic_info_df = topic_info_df.reset_index()

topic_info_df.to_csv(
    f"C:/Users/MaengJiwoo/.vscode/KISTI-intern/2025_KISTI-intern/BERTopic/SBERT/entity_topic_info_{label_to_process}_{num}.csv",
    index=False
)

# 모델 저장
topic_model.save(f"C:/Users/MaengJiwoo/.vscode/KISTI-intern/2025_KISTI-intern/BERTopic/SBERT/my_model_{label_to_process}_{num}")

# 결과 출력
print(topic_info_df)

# %%
# --- BERTopic과는 별개로, HDBSCAN 결과만으로 키워드 추출 ---
cluster_labels = hdbscan_model.fit_predict(embeddings)
df_cluster = pd.DataFrame({
    'entity_text': unique_texts,
    'topic': cluster_labels
})

num_keywords = 5
tfidf_results = []

for topic_num in sorted(df_cluster['topic'].unique()):
    if topic_num == -1:
        continue
    topic_texts = df_cluster[df_cluster['topic'] == topic_num]['entity_text'].tolist()
    if not topic_texts:
        continue
    vectorizer = TfidfVectorizer(max_features=num_keywords, stop_words='english')
    X = vectorizer.fit_transform(topic_texts)
    keywords = vectorizer.get_feature_names_out()
    tfidf_results.append({
        'topic': topic_num,
        'keywords': ', '.join(keywords),
        'count': len(topic_texts)
    })

df_tfidf_keywords = pd.DataFrame(tfidf_results)
df_tfidf_keywords = df_tfidf_keywords.sort_values(by='topic').reset_index(drop=True)
tfidf_save_path = f"C:/Users/MaengJiwoo/.vscode/KISTI-intern/2025_KISTI-intern/BERTopic/SBERT/entity_topic_keywords_tfidf_{label_to_process}_{num}_hdbscan_only.csv"
df_tfidf_keywords.to_csv(tfidf_save_path, index=False)
print("\n[HDBSCAN-only TF-IDF 기반 토픽별 대표 키워드]")
print(df_tfidf_keywords)

# %%
topic_model.visualize_barchart()

