from bertopic import BERTopic
import pandas as pd
import hdbscan
from sentence_transformers import SentenceTransformer


# 1. CSV 파일 불러오기
file_path = r"C:\Users\MaengJiwoo\.vscode\KISTI-intern\2025_KISTI-intern\BERTopic\FA_entities.csv"
df = pd.read_csv(file_path, encoding="utf-8")


# 2. 원하는 entity_label 필터링
label_to_process = 'problem'
#label_to_process = 'solution'
#label_to_process = 'target'
df_filtered = df[df['entity_label'] == label_to_process].copy()


# 3. 중복 없이 unique entity_text만 추출 (클러스터링용)
unique_texts = df_filtered['entity_text'].drop_duplicates().tolist()


# 4. SBERT 임베딩
sbert_model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
embeddings = sbert_model.encode(unique_texts, show_progress_bar=True)


# 5. HDBSCAN 모델 정의
hdbscan_model = hdbscan.HDBSCAN(
    min_cluster_size=2, 
    metric="euclidean", 
    cluster_selection_method='eom', 
    prediction_data=True
)


# 6. BERTopic 모델 정의 및 클러스터링 수행
topic_model = BERTopic(
    embedding_model=None,
    hdbscan_model=hdbscan_model,
    min_topic_size=1,
    nr_topics="auto",
    verbose=True
)
topics, probs = topic_model.fit_transform(unique_texts, embeddings)


# 7. unique_texts와 topics로 딕셔너리 만들기
text2topic = dict(zip(unique_texts, topics))

# 8. 원본 df_filtered에서 entity_text 기준 topic 번호 붙이기
df_filtered['topic'] = df_filtered['entity_text'].map(text2topic)


# 9. 결과 저장/확인
num = 1
topic_info_df = topic_model.get_topic_info()
topic_info_df.to_csv(f"C:/Users/MaengJiwoo/.vscode/KISTI-intern/2025_KISTI-intern/BERTopic/SBERT/entity_topic_info_{label_to_process}_{num}.csv", index=False)

# 필터링된 DataFrame에만 결과 저장
df_filtered['topic'] = df_filtered['entity_text'].map(text2topic)
df_filtered.to_csv(f"C:/Users/MaengJiwoo/.vscode/KISTI-intern/2025_KISTI-intern/BERTopic/SBERT/entity_topic_{label_to_process}_{num}.csv", index=False)


# 모델 저장
# topic_model.save(f"C:/Users/MaengJiwoo/.vscode/KISTI-intern/2025_KISTI-intern/BERTopic/SBERT/my_model_{label_to_process}_{num}")


# 결과 출력
print(topic_model.get_topic_info())
pd.set_option('display.max_rows', None)
print(df_filtered.head(20))  # 일부 결과 미리 보기
