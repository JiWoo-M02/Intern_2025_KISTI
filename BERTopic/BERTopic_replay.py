import pandas as pd
from bertopic import BERTopic
import hdbscan
from sentence_transformers import SentenceTransformer

# 1. 파일 불러오기 & topic 0만 추출
file_path = r"C:\Users\MaengJiwoo\.vscode\KISTI-intern\2025_KISTI-intern\BERTopic\SBERT\entity_topic_problem_1.csv"
df = pd.read_csv(file_path, encoding="utf-8")
df_topic0 = df[df['topic'] == 0].copy()
unique_texts_0 = df_topic0['entity_text'].drop_duplicates().tolist()

# 2. SBERT 임베딩
sbert_model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
embeddings_0 = sbert_model.encode(unique_texts_0, show_progress_bar=True)

# 3. BERTopic 다시 돌리기
hdbscan_model = hdbscan.HDBSCAN(min_cluster_size=2, metric="euclidean", cluster_selection_method='eom', prediction_data=True)
topic_model_0 = BERTopic(embedding_model=None, hdbscan_model=hdbscan_model, min_topic_size=1, nr_topics="auto", verbose=True)
topics_0, probs_0 = topic_model_0.fit_transform(unique_texts_0, embeddings_0)

# 4. 다시 할당된 topic 저장
text2topic_0 = dict(zip(unique_texts_0, topics_0))
df_topic0['new_topic'] = df_topic0['entity_text'].map(text2topic_0)
df_topic0.to_csv(r"C:\Users\MaengJiwoo\.vscode\KISTI-intern\2025_KISTI-intern\BERTopic\SBERT\topic0_reclustered.csv", index=False)

# 5. 새 topic info도 저장
topic_info_0 = topic_model_0.get_topic_info()
topic_info_0.to_csv(r"C:\Users\MaengJiwoo\.vscode\KISTI-intern\2025_KISTI-intern\BERTopic\SBERT\info_topic0_reclustered.csv", index=False)

# 결과 출력
print(topic_info_0)
