# **BERTopic**
<br>BERT기반 embeddings + 클래스 기반(class-based) TF-IDF
<br>➡️ 주제 설명에서 중요한 단어를 유지하면서도 쉽게 해석할 수 있는 조밀한 클러스터를 만드는 토픽 모델링 기술
<br>
<br>


# **Plan**
2025.06.17.Tue 회의: 하고 있는 거 정리 + BERTopic 사용해서 결과
<br>2025.06.18-20  팀장님 및 현호선생님 출장
<br>
<br>



# **Objective**
problem 개체가 대략 10만개 있다고 한다면, 3~5만개 내외로 묶는다고 생각하면 됨.
BERTopic git은 docs형식이라 국내 블로그나 해외 블로그 참고해서 해보라고 하심.
<br>

## EX
아래와 같이 과일 하나로 묶을 수 있도록. 대신 유니크한 것들은 따로 제외
<br> 과일
<br> - 열대 과일
<br> - 사과
<br> - 배



# **TimeLINE**
BERTopic_1은 git에서 Quick Start 참고하여 돌려본 것.
<br>➡️ 아무것도 모르는 상태에서 감 잡기로 해본 것이라 무시해도 됨.
<br>
<br>BERTopic_2는 해당 링크 참고 (https://mz-moonzoo.tistory.com/23)
| 토픽 번호 | 원래 이름                                   | 주제             |
| ----- | ---------------------------------------------- | --------------------- |
| -1    | `-1_combustion_internal_engine_of`             | 내연기관 및 연소 기술      |
| 0     | `0_filter_particulate_honeycomb_filtration`    | 입자 필터 및 허니컴 여과 기술 |
| 1     | `1_exhaust_gas_the_temperature`                | 배기가스 온도 및 특성     |
| 2     | `2_vehicles_equipment_automobiles_buildings`   | 자동차 및 관련 장비      |
| 3     | `3_nox_reduction_emissions_burn`               | NOx 저감 및 배출 제어   |
| 4     | `4_catalyst_catalytic_oxidation_deterioration` | 촉매 산화 및 열화 현상    |
| 5     | `5_sulfur_removal_hydrogen_sulfide`            | 황 제거 및 황화수소 처리    |
| 6     | `6_effects_harmful_environment_pollution`      | 유해 물질 및 환경 영향    |
| 7     | `7_fuel_engines_engine_diesel`                 | 디젤 연료 및 엔진 효율     |
| 8     | `8_nitrogen_oxides_removing_oxide`             | 질소산화물 제거 기술       |
| 9     | `9_ammonia_into_infrastructure_possible`       | 암모니아 기반 인프라 가능성   |
<br>
<br>BERTopic_3 version은 entity_text에서 추출한 핵심 키워드를 중심으로 비슷한 것끼리 묶어보는 걸 목표로 실행.
<br>➡️ KeyBERT 기반으로 entity_text를 핵심 키워드 중심으로 재구성하고, BERTopic으로 클러스터링

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
