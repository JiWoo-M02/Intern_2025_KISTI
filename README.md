
## keyword_analysis_results_4.csv
대체적으로 이전 prompt보다는 개선되어 keyword 추출이 된 것 같음.

### 📌 prompt 수정
| 문제              | 해결 전략                                |
| --------------- | ------------------------------------ |
| 키워드가 5단어 초과됨    | “Never return any keyword…” 문구 삽입    |
| 여러 키워드가 한 줄로 나옴 | “Each keyword on a separate line” 추가 |
| 원문 단어 아닌 표현 등장  | “Only use words from input text” 명시  |

### examples
harmful effects on the environment
환경에 미치는 해로운 영향

keyword1 : harmful effects 해로운 영행
keyword2 : environment 환경



clogging of the pores by soot
그을음으로 인한 모공 막힘

keyword1 : clogging 막힘
keyword2 : pores 모공
keyword3 : soot 그을음