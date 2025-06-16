
# **keyword_analysis_results_4**
대체적으로 이전 prompt보다는 개선되어 keyword 추출이 된 것 같음.
<br> Total API cost: $0.049038
<br>

## 📌 문제점 및 수정 사항
| 문제            | prompt 수정                          |
| --------------- | ------------------------------------ |
| 키워드가 5단어 초과됨    | “Never return any keyword…” 문구 삽입    |
| 여러 키워드가 한 줄로 나옴 | “Each keyword on a separate line” 추가 |
| 원문 단어 아닌 표현 등장  | “Only use words from input text” 명시  |
<br>

## ✏️ examples
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
<br> 
<br> 

# **keyword_analysis_results_5**
대체적으로 이전 prompt보다는 개선되어 keyword 추출이 된 것 같음.
<br> Total API cost: $0.069472
<br>

## 📌 문제점 및 수정 사항
단어 낱개가 아닌, 의미 기반 결합을 위주로 추출할 수 있게 수정.
<br> ➡️ 중복되는 keyword 추출 문제 발생.
<br> ➡️ Objective에서 "Extract 3 to 5 of the most meaningful **noun phrases** from the input text." 부분 중, "3 to 5 of" 제거.
<br>

# **keyword_analysis_results_6**
"keyword_analysis_results_4"와 비슷한 데이터 추출 결과를 보임.
<br> Total API cost: $0.050155
<br>

<br> 
<br> 

# **keyword_analysis_results_7**

<br> Total API cost: $0.082579

## 📌 문제점 및 수정 사항
너무 키워드가 여러 개 뽑히는 것 같음.
<br>

## ✏️ examples
input: "challenging to find a lean-burn NOx catalyst that has the required activity, durability, and operating temperature range"
<br>output: lean-burn nox catalyst 
required activity	
durability	
operating temperature range 

✅ 핵심 키워드: "lean-burn NOx catalyst" (린번 질소산화물 촉매)  
이유: 이 문장은 특정 촉매를 찾는 데 어려움이 있다는 내용입니다.  
핵심 주제는 바로 "lean-burn NOx catalyst" 즉, 린번 엔진용 질소산화물 저감 촉매입니다.  
'required activity, durability, and operating temperature range'는 그 촉매가 만족해야 하는 조건(성능, 내구성, 온도 범위)을 설명하는 부가 정보입니다.

<br>
<br> 
<br> 

# **keyword_analysis_results_8**
Total API cost: $0.065808
<br> 

## 📌 문제점 및 수정 사항
<br> 빈 칸으로 반환된 keyword 존재.
<br> ➡️ Rules에서 "If no suitable noun phrase can be identified, return an empty list."를 지워줌.
<br>

## ✏️ examples
input: "to reach acceptably low levels of sulfur content"
<br>output: []