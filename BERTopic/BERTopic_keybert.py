# %% 전체 파이프라인
from bertopic import BERTopic
from keybert import KeyBERT
import pandas as pd
import umap
import hdbscan
import plotly.io as pio

# 1. CSV 파일 불러오기
file_path = r"C:\Users\MaengJiwoo\.vscode\KISTI-intern\2025_KISTI-intern\overlapped_entities.csv"
df = pd.read_csv(file_path, encoding="windows-1252")
#df = pd.read_csv(file_path, encoding="ISO-8859-1")

# 1.1 "problem" 라벨 필터링
df_filtered = df[df['entity_label'] == 'problem'].copy()

# 2. KeyBERT 로딩 (같은 sentence-transformers 기반)
kw_model = KeyBERT(model="all-MiniLM-L6-v2")

# 3. 핵심 키워드 추출 함수
def extract_keywords(text):
    keywords = kw_model.extract_keywords(str(text), keyphrase_ngram_range=(1, 1), stop_words='english', top_n=5)
    return " ".join([kw for kw, _ in keywords])

# 핵심 키워드 문서 리스트 생성
reduced_docs = df_filtered['entity_text'].astype(str).apply(extract_keywords).tolist()


# 4. 차원축소 + 클러스터링 모델 정의
umap_model = umap.UMAP(
    n_neighbors=15, 
    n_components=5, 
    metric="cosine"
    )

hdbscan_model = hdbscan.HDBSCAN(
    min_cluster_size=15, 
    metric="euclidean", 
    cluster_selection_method='eom', 
    prediction_data=True
    )

# 5. BERTopic 모델 생성
topic_model = BERTopic(
    embedding_model="all-MiniLM-L6-v2",
    umap_model=umap_model,
    hdbscan_model=hdbscan_model,
    min_topic_size=10,
    nr_topics="auto",
    verbose=True
)

# 클러스터링 수행
topics, probs = topic_model.fit_transform(reduced_docs)

# 주제 정보 저장
topic_info_df = topic_model.get_topic_info()
topic_info_df.to_csv("entity_topic_info_HE1.csv", index=False)

# 필터링된 DataFrame에만 결과 저장
df_filtered['topic'] = topics
df_filtered.to_csv("entity_topics_keybert_HE1.csv", index=False)

# 모델 저장
topic_model.save("C:/Users/MaengJiwoo/.vscode/KISTI-intern/2025_KISTI-intern/BERTopic/my_keybert_model_HE1")

# 7. 결과 확인 및 저장
print(topic_model.get_topic_info())

# 8. 결과 시각화
pio.renderers.default = 'browser'
topic_model.visualize_topics()

# 9. 결과 저장
topic_info_df = topic_model.get_topic_info()
topic_info_df.to_csv("entity_topic_info_HE1.csv", index=False)
