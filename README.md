
## **keyword_analysis_results_4**
대체적으로 이전 prompt보다는 개선되어 keyword 추출이 된 것 같음.
<br> Total API cost: $0.049038
<br>

### 📌 문제점 및 수정 사항
| 문제            | prompt 수정                          |
| --------------- | ------------------------------------ |
| 키워드가 5단어 초과됨    | “Never return any keyword…” 문구 삽입    |
| 여러 키워드가 한 줄로 나옴 | “Each keyword on a separate line” 추가 |
| 원문 단어 아닌 표현 등장  | “Only use words from input text” 명시  |
<br>

### ✏️ examples
ex1. harmful effects on the environment
<br> 환경에 미치는 해로운 영향
| keyword  | eng | kor |
| -------- | --- | --- |
| keyword1 | harmful effects | 해로운 영향 |
| keyword2 | environment | 환경 |
<br>

ex2. clogging of the pores by soot
<br> 그을음으로 인한 모공 막힘
| keyword  | eng | kor |
| -------- | --- | --- |
| keyword1 | clogging | 막힘 |
| keyword2 | pores | 모공 |
| keyword3 | soot | 그을음 |
<br>
<br> ➡️ 단어 단위로 키워드가 쪼개짐. 즉, 문맥적 정보가 손실된 게 많음.
<br> ➡️ 낱개 단위로 나오지 않도록 "keyword_analysis_results_5"에 반영.
<br>

## **keyword_analysis_results_5**
대체적으로 이전 prompt보다는 개선되어 keyword 추출이 된 것 같음.
<br> Total API cost: $0.069472
<br>

### 📌 문제점 및 수정 사항
단어 낱개가 아닌, 의미 기반 결합을 위주로 추출할 수 있게 수정.
<br>
<br> ➡️ 중복되는 keyword 추출 문제 발생.
<br> ➡️ Objective에서 "Extract 3 to 5 of the most meaningful **noun phrases** from the input text." 부분 중, "3 to 5 of" 제거.
<br>


## **keyword_analysis_results_6**
"keyword_analysis_results_4"와 비슷한 데이터 추출 결과를 보임.
<br> Total API cost: $0.050155
<br>
