# **BERTopic**
BERT기반 embeddings + 클래스 기반(class-based) TF-IDF
<br>➜ 주제 설명에서 중요한 단어를 유지하면서도 쉽게 해석할 수 있는 조밀한 클러스터를 만드는 토픽 모델링 기술
<br>
<br>
<br>
<br>
<br>

# **Objective**
problem 개체가 대략 10만개 있다고 한다면, 3~5만개 내외로 묶는다고 생각하면 됨.
<br>BERTopic git은 docs형식이라 국내 블로그나 해외 블로그 참고해서 해보라고 하심.
<br>
<br>

## example
아래와 같이 과일 하나로 묶을 수 있도록. 대신 유니크한 것들은 따로 제외
<br> Topic: 과일
<br> - 열대 과일
<br> - 사과 나무
<br> - 배
<br>
<br>
<br>
<br>
<br>

# **TimeLINE**
NO.1. BERTopic_1은 git에서 Quick Start 참고하여 돌려본 것.
<br>  ➜ 아무것도 모르는 상태에서 감 잡기로 해본 것.(= 무시해도 무관)
<br>  해당 링크: https://maartengr.github.io/BERTopic/index.html
<br>
<br>
  
**NO.2. BERTopic_2는 해당 링크 참고** (https://mz-moonzoo.tistory.com/23)
<br>

| 토픽 번호    | 문서 수 | 주요 키워드                                 | 주제                                           |
| ------------ | ---- | -------------------------------------------- | --------------------------------------------------- |
| -1    | 105  | combustion, internal, engine, carbon, and...        | 내연기관/연소 관련 문서이나 군집되지 않은 문서 <br> (키워드 다양도 높음, 방향성 모호) |
| 0     | 75   | filter, particulate, honeycomb, filtration, ceramic | DPF 및 미세입자 필터링 (허니컴 구조, 세라믹 필터 등)               |
| 1     | 61   | exhaust, gas, temperature, pressure, engine         | 배기 가스 및 온도/압력 제어 시스템 (센서 기반 엔진 제어 가능성)          |
| 2     | 50   | vehicles, equipment, automobiles, buildings         | 차량 및 장비 관련 일반 문서 (구체 주제 없음, 외연 넓음)              |
| 3     | 49   | nox, reduction, emissions, burn, lean               | 질소산화물(NOx) 저감 (연소 최적화, lean burn 등 포함)          |
| 4     | 36   | catalyst, catalytic, oxidation, deterioration       | 촉매 반응 및 열화 (산화 촉매의 열화 또는 수명 관련)                 |
| 5     | 32   | sulfur, removal, hydrogen, sulfide                  | 황 제거 및 황화수소 처리 기술 (탈황 공정)                       |
| 6     | 27   | effects, harmful, environment, pollution            | 대기오염 및 환경 영향 분석 (건강 영향, 유해성 중심)                 |
| 7     | 25   | fuel, engines, engine, diesel, lean                 | 연료 소비 및 디젤 엔진 운용 (연비, lean mixture 등)           |
| 8     | 19   | nitrogen, oxides, removing, oxide                   | 질소산화물 제거 기술 (SCR 등) (촉매제 중심)                    |
| 9     | 12   | ammonia, infrastructure, distribution, possible     | 암모니아 기반 인프라 시스템 (분산 및 저장 기술 포함)                 |

<br>
<br>
  
**NO.3. BERTopic_3**
<br>entity_text에서 추출한 핵심 키워드를 중심으로 비슷한 것끼리 묶어보는 걸 목표로 실행
<br>➜ KeyBERT 기반으로 entity_text를 핵심 키워드 중심으로 재구성하고, BERTopic으로 클러스터링
<br>

| 토픽 번호 | 문서 수 | 주요 키워드                                     | 주제                                  |
| -------- | ---- | ------------------------------------------------- | -------------------------------------------- |
| -1       | 112  | increase, carbon, diesel, denitration, soot, ... | 키워드가 흩어져 있거나 의미적으로 고립된 경우 (노이즈) |
| 0        | 145  | engine, combustion, exhaust, catalyst, diesel    | 엔진 연소 및 배기가스 관련 기술 (내연기관, 촉매 반응 등)       |
| 1        | 65   | nox, nitrogen, oxides, reduction, catalyst       | 질소산화물(NOx) 저감 관련 기술 (촉매 환원 등)            |
| 2        | 63   | filter, honeycomb, filtration, particulate       | DPF/PM 필터링 구조 (허니컴 필터, 세라믹 입자 제거 등)      |
| 3        | 32   | sulfur, removal, hydrogen sulfide                | 황 제거 기술 (H₂S 제거, 황화물 처리 등)               |
| 4        | 27   | harmful, environment, pollution, air             | 환경 유해성 및 대기오염 영향 분석 (오염원, 건강 영향)         |
| 5        | 20   | vehicles, automobiles, military, equipment       | 차량/군용 장비 관련 문서 (배기 관련보다 차량 자체에 초점)       |
| 6        | 14   | ammonia, infrastructure, release, precursor      | 암모니아 기반 배출 시스템 및 인프라 구축 논의               |
| 7        | 13   | manufacturers, researchers, commercially         | 제조사/연구자 중심의 연구 동향 또는 기술 상용화 문서           |

<br>
<br>

**NO.4. BERTopic_4 version은 기존 'top_n=3'에서 'top_n=5'로 증가시켜 진행.**
<br>➜ 비슷한 개념끼리 더 세분화되게 묶어보는 것을 목표로 실행.
<br>KeyBERT에서 top_n 파라미터는 각 문서에서 의미적으로 가장 중요한 키워드를 몇 개 추출할지를 설정하는 값
<br>KeyBERT 기반으로 문장에서 top 5 핵심 키워드를 추출해 문서를 재구성하고, 이를 BERTopic에 입력하여 의미 표현을 확장한 상태에서 클러스터링 수행.
<br>

| 토픽 번호  | 문서 수 | 대표 키워드                    | 주제                         |
| -- | ---- | --------------------------------------- | ------------------------------- |
| -1 | 96   | soot, carbon, denitration, regeneration | 탈질·탄소 관련 문서 중 노이즈 처리된 문서들   |
| 0  | 69   | filter, particulate, honeycomb, ceramic | DPF/미세먼지 필터링 및 허니컴 세라믹 구조   |
| 1  | 60   | exhaust, gas, temperature, flow         | 배기 가스 온도·유량 제어 및 정화 장치      |
| 2  | 47   | nox, reduction, adsorber, emissions     | 질소산화물(NOx) 흡착·저감 시스템        |
| 3  | 39   | catalyst, oxidation, deterioration      | 산화 촉매 및 열화 현상               |
| 4  | 33   | engine, fuel, diesel, lean              | 연료소모, 디젤엔진, 희박연소(lean burn) |
| 5  | 30   | effects, harmful, environmental         | 환경유해성 및 공해 영향 분석            |
| 6  | 30   | sulfur, hydrogen, sulfide, removal      | 황 제거 및 황화수소 처리 단계           |
| 7  | 20   | nitrogen, oxides, gases, reduction      | 질소산화물 제거/환원 (SCR 포함 가능)     |
| 8  | 19   | vehicles, automobiles, owner, military  | 차량 및 군수 장비 관련 문서            |
| 9  | 19   | internal, combustion, engine            | 내연기관 기술 및 연소 원리             |
| 10 | 16   | manufacturers, researchers, commercial  | 산업계 및 연구기관 관련 기술 동향      |
| 11 | 13   | ammonia, infrastructure, distribution   | 암모니아 기반 연료 인프라 및 배포 문제     |

<br>
<br>
<br>

## parameter 조절

| 파라미터               | 설명                                   | 클러스터 크기/수에 미치는 영향                                              |
| ---------------------- | ------------------------------------ | ------------------------------------------------------------------- |
| `top_n` | KeyBERT에서 한 문장당 추출할 핵심 키워드 수 | 높일수록 문서 표현이 풍부해져 더 세분화된 클러스터 생성 가능. <br>하지만 너무 높으면 잡음 증가 가능성 |
| `n_neighbors` | UMAP에서 이웃으로 간주할 포인트 수 → 지역 밀도 기준 | 작게 설정하면 작은/조밀한 클러스터 증가, 크게 설정하면 더 큰 범위로 군집하려 함    |
| `n_components` | UMAP의 차원 축소 결과 차원 수  | 높일수록 정보 손실이 줄어 클러스터 분해가 섬세해질 수 있음. <br>하지만 시각화에는 2\~5차원 정도 권장  |
| `min_cluster_size` | HDBSCAN에서 하나의 클러스터로 인정되는 최소 문서 수 | 클러스터 수 감소 ↔ 노이즈 증가 감소, 작게 하면 더 많은 소형 클러스터 생성됨  |
| `min_topic_size`  | BERTopic 내에서 최종 토픽으로 인정될 최소 문서 수| 이보다 작은 클러스터는 주제 축소(nr\_topics) 과정에서 병합됨, 낮출수록 더 많은 토픽 유지 가능 |

<br>

| 목표                          | 조정 추천                                                     |
| ----------------------------- | --------------------------------------------------------- |
| 더 작은 클러스터도 포착하고 싶다 | `min_cluster_size ↓`, `min_topic_size ↓`, `n_neighbors ↓` |
| 더 큰 주제 단위로 묶고 싶다      | `min_cluster_size ↑`, `min_topic_size ↑`, `n_neighbors ↑` |
| 노이즈(-1)가 너무 많다          | `min_cluster_size ↑` 또는 `top_n ↓`                         |
| 토픽 수가 너무 적다             | `min_topic_size ↓`, `nr_topics=None` 지정                   |
| 토픽 수가 너무 많다             | `min_topic_size ↑` 또는 `nr_topics="auto"` 유지               |
<br>
<br>
  
**NO.1. entity_topics_keybert_FA1**
<br>topic의 개수 6개
<br>📌 **NO.2**부터는 'min_cluster_size'를 2로 조정.

| parameter          | size |
| ------------------ | ---- |
| top_n              | 5    |
| n_neighbors        | 15   |
| n_components       | 5    |
| min_cluster_size   | 15   |
| min_topic_size     | 10   |
<br>
<br>
  
**NO.2. entity_topics_keybert_FA2**
<br>topic의 개수 314개
<br>📌 **NO.3**부터는 'min_topic_size'를 2로 조정.

| parameter          | size |
| ------------------ | ---- |
| top_n              | 5    |
| n_neighbors        | 15   |
| n_components       | 5    |
| min_cluster_size   | 2    |
| min_topic_size     | 10   |

<br>
<br>
  
**NO.3. entity_topics_keybert_FA3**
<br>topic의 개수 321개
<br>📌 **NO.4**에서는 'n_neighbors'를 30으로, 'min_topic_size'를 10으로 조정.

| parameter          | size |
| ------------------ | ---- |
| top_n              | 5    |
| n_neighbors        | 15   |
| n_components       | 5    |
| min_cluster_size   | 2    |
| min_topic_size     | 2    |

<br>
<br>
  
**NO.4. entity_topics_keybert_FA4**
<br>topic의 개수 309개
<br>📌 **NO.5**에서는 'n_neighbors'를 50으로, 'min_topic_size'를 20으로 조정.

| parameter          | size |
| ------------------ | ---- |
| top_n              | 5    |
| n_neighbors        | 30   |
| n_components       | 5    |
| min_cluster_size   | 2    |
| min_topic_size     | 10   |

<br>
<br>
  
**NO.5. entity_topics_keybert_FA5**
<br>topic의 개수 312개
<br>📌 **NO.6**에서는 'n_neighbors'를 100으로 조정.

| parameter          | size |
| ------------------ | ---- |
| top_n              | 5    |
| n_neighbors        | 50   |
| n_components       | 5    |
| min_cluster_size   | 2    |
| min_topic_size     | 20   |

<br>
<br>
  
**NO.6. entity_topics_keybert_FA6**
<br>topic의 개수 284개
<br>📌1. topic의 갯수는 전과 다르게 줄어듦.
<br>📌2. 같은 entity_text인데, 다른 topic으로 표기됨.
| entity_text                                                   | topic                                                                      |
| ------------------------------------------------------------- | -------------------------------------------------------------------------- |
| being alone might be a problem when faced with an emergency   | -1_systems_person_elderly_patient <br>4_care_caregivers_general_caregiver  |        

| parameter          | size |
| ------------------ | ---- |
| top_n              | 5    |
| n_neighbors        | 100  |
| n_components       | 5    |
| min_cluster_size   | 2    |
| min_topic_size     | 20   |
<br>
<br>
  
**NO.7. entity_topics_keybert_FA7**
<br>topic의 개수 79개
<br>

| parameter          | size |
| ------------------ | ---- |
| top_n              | 5    |
| n_neighbors        | 100  |
| n_components       | 5    |
| min_cluster_size   | 5    |
| min_topic_size     | 20   |
<br>
<br>
<br>

## keyword 제외. BERTopic만.
2025-06-23 회의 결과, keyword를 기반으로 진행했던 부분을 제외.
<br>➜ entity_text가 바로 클러스터링 될 수 있도록 진행.
<br>

**NO.1.**
- 차원을 100으로 지정하고 진행 (최대 768) 
<br> ➜ n_components = 100

- 적어도 Keyword 기반보다 오래 걸릴 것이라고 예상했는데, 2분 미만으로 진행됨.
<br> ➜ `FA_entities` 데이터에서, problem의 개수는 3,582개로 양이 적어서 시간이 많이 걸리지 않는 것으로 예상.

- 위에서 언급한 것처럼, 시간이 오래 걸리지 않아 768 차원으로 해도 될 거 같음.
- 결과 데이터: entity_topic_problem_1, entity_topic_info_problem_1
<br>
<br>

**NO.2.**
- min topic = 1 (최소)
- min cluster = 2
- components = 50
- 결과 데이터: entity_topic_problem_2, entity_topic_info_problem_2
<br>
<br>

**NO.3.**
- components를 0.1로 진행하면 오류가 남. 정수로만 지정 가능한 듯.
<br> ➜ 1로 설정.

- hdbscan_model와 umap_model 모두 `metric="euclidean"`으로 진행.
<br> ➜ topic 339개(노이즈 -1 포함) 나옴.

- hdbscan_model에서 metric을 `cosine`으로 사용하려면, `algorithm='generic'`으로 바꾸어야 함.
<br> ➜ 해보았는데 오류 발생. ValueError: Buffer dtype mismatch, expected 'double_t' but got 'float'
<br> ➜ 타입의 문제인데, 일단 보류.

- 결과 데이터: entity_topic_problem_3, entity_topic_info_problem_3
<br>📌 topic이 중복되는 의미들이 보임.
<br>    ➜ 분류를 하기 전, topic이 만들어지고 나서 클러스터링 중복 제거 시도.
<br>
<br>

## 전반적인 코드 수정
### **Objective**
1. 차원 축소하지 않고, 그대로 진행
- umap_model 말고 SBERT 사용
- 이전 코드에서는 umap_model을 통한 차원 축소 후, hdbscan_model을 사용하여 클러스터링을 진행함.
- 수정 코드에서는 SBERT 모델로 임베딩하고, 클러스터링은 동일하게 hdbscan_model으로 진행.
- 먼저, SBERT 모델 중 `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`로 임베딩 진행.
<br>
<br>

2. 중복 제거
- 모양이 똑같은 것 중복 제거
- 1. 임베딩 전, 완전히 동일한 문장(중복 문장)을 **하나만 남기고** 제거. 
- 2. 토핑이 끝난 후, 할당된 토픽 번호를 다시 중복 포함 원본 데이터에 매핑.
- 3. 모든 텍스트(중복 포함)의 토픽 정보 저장.

- 아래와 같이 publication number가 달라도 entity text가 똑같으면 topic이 동일하게 나올 수 있어야 함. 
<br>  ➜ US09838861 : higher risk of being alone and experiencing an emergency
<br>  ➜ US09811998 : higher risk of being alone and experiencing an emergency
<br>  ➜ US09338627 : higher risk of being alone and experiencing an emergency
<br>
<br>

### **Process**
1. 데이터 불러오기
- CSV 파일에서 데이터를 읽어옴.
- 원하는 entity_label만 필터링.
<br>

2. 임베딩(SBERT(Sentence-BERT) 사용)
- 중복 제거된 entity_text만 추출.
<br>

3. 클러스터링(HDBSCAN 사용)
- 이 클러스터링을 BERTopic 프레임워크 내부에서 사용함.
    ➜ 클러스터 label 결과만 따로 계산해서 BERTopic에 넘기는 것은 불가능.
    ➜ 즉, BERTopic 내부에서 hdbscan_model을 fit하는 과정을 거치지 않고 label만 주는 방식은 없음.
    ➜ BERTopic을 쓴 이유: 각 토픽별로 Name(토픽 이름), Representation(대표 단어), Representative_Docs(토픽을 잘 보여주는 실제 예시 문장)와 같이 요약을 해주기 때문.
<br>

4. BERTopic으로 토픽 할당
- entity_text 데이터에 topic 할당
    ➜ 주제별 대표 단어 추출 기능을 제공하는 라이브러리.
- 임베딩+클러스터링 결과를 활용해 각 문장에 토픽을 부여.
<br>

5. 결과 저장
- topic 분류된 것과 topic info 내용 저장
- topic info 항목 설명
- - Topic : 토픽(군집) 번호
- - Count : 각 토픽에 포함된 문장 개수
- - Name : 토픽 이름 (대표 단어 등으로 자동 생성)
- - Representation : 토픽의 주요 키워드(대표 단어)
- - Representative_Docs : 토픽을 잘 보여주는 실제 예시 문장
<br>
<br>

### **ETC**
1. HDBSCAN 단독 사용 (임베딩 + HDBSCAN + TF-IDF)
- SBERT로 텍스트 임베딩을 수행한 뒤, HDBSCAN으로 클러스터링을 직접 진행.
- 각 문장에 군집(label)을 할당하고, 각 군집별로 TF-IDF를 이용해 대표 키워드를 추출.
- 전체 3,582개 中 2,608개의 노이즈.
- 노이즈(-1) 제외 총 220개의 topic 추출.
- 실제로 토픽으로 분류되는 데이터가 적음.
- 결과 데이터: (전체결과_problem sheet 中) entity_topic_info_problem_3_tf, entity_topic_problem_3_tf

2. BERTopic
- 외부에서 미리 계산한 SBERT 임베딩을 입력받아, BERTopic에서 HDBSCAN 클러스터링과 토픽 수 자동 조정, 대표 키워드, 대표 문장 추출까지 한 번에 처리.
- 토픽별로 대표 키워드와 대표 문장 등 다양한 분석 결과를 함께 제공.
- 전체 3,582개 中 623개의 노이즈.
- 노이즈(-1) 제외 총 180개의 topic 추출.
- 결과 데이터: (전체결과_problem sheet 中) entity_topic_info_problem_1, entity_topic_problem_1
<br>
<br>

### **이전과의 결과 비교**

| entity_text         | 기존.ver 결과                            | 수정.ver 결과                                      |
| ------------------- | --------------------------------------- | -------------------------------------------------- |
| embarrassing        | 20_themselves_living_individuals_alone  | 25_discomfort_psychologically_distress_traumatic   |
| humiliating         | 20_themselves_living_individuals_alone  | 44_violence_domestic_assault_abuse                 |
| physical discomfort | 20_themselves_living_individuals_alone  | 138_ulcers_pressure_sores_painful                  |



walking impediment due to weakened muscle resulting from aging



