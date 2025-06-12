import pandas as pd
from tqdm import tqdm
from openai import OpenAI

# OpenAI 클라이언트 초기화
client = OpenAI(api_key="sk-proj-39MAIAVyfnn1oYMs7fCuT3BlbkFJS3JKP12jYFCwXacyAdyY")

# Prompt 템플릿
keyword_system_prompt = """You are a strict keyword extraction model.

[Objective]  
Extract 3 to 5 of the most meaningful noun phrases from the input text.

[Rules]  
- Each keyword must be a noun or noun phrase with **no more than 5 words**. Do not exceed this limit.
- Only use words that are present in the original input text. Do not paraphrase or invent new terms.
- Remove generic terms like “method,” “system,” “use,” “apparatus,” etc.
- Normalize to lowercase and singular forms.
- Return each keyword on a **separate line** (one line = one keyword).
- If no suitable keywords exist, return an **empty list**.
- Strictly ensure: **each keyword contains 5 words or fewer.**
- Never return any keyword with more than 5 words.

[Example]  
Input: "Artificial intelligence is transforming the healthcare industry with diagnostic tools."  
Output:  
artificial intelligence  
healthcare industry  
diagnostic tools
"""

keyword_user_prompt = """Input text:
{text}

Keywords:"""

# 비용 계산 함수
def calculate_cost_of_openai_api(prompt_tokens, completion_tokens):
    input_cost_per_token = 0.40 / 1000000
    output_cost_per_token = 1.60 / 1000000

    input_cost = prompt_tokens * input_cost_per_token
    output_cost = completion_tokens * output_cost_per_token

    total_cost = input_cost + output_cost
    return total_cost

# 키워드 추출 함수
def extract_keywords(entity_text):
    messages = [
        {"role": "system", "content": keyword_system_prompt},
        {"role": "user", "content": keyword_user_prompt.format(text=entity_text)}
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=messages,
            temperature=0.0
        )
        content = response.choices[0].message.content.strip()

        keywords = [kw.strip() for kw in content.splitlines() if kw.strip()]

        cost = calculate_cost_of_openai_api(response.usage.prompt_tokens, response.usage.completion_tokens)

        return keywords, cost
    except Exception as e:
        print(f"Error extracting keywords: {e}")
        return [], 0.0


# Main 처리
def main():
    total_cost = 0.0

    # CSV 로드
    file_path = "C:/Users/MaengJiwoo/.vscode/KISTI-intern/2025_KISTI-intern/overlapped_entities.csv"
    df = pd.read_csv(file_path, encoding="windows-1252")

    results = []

    for _, row in tqdm(df.iterrows(), total=len(df), desc="Processing rows"):
        entity = row['entity_text']

        keywords, cost = extract_keywords(entity)
        total_cost += cost

        # 결과 dict 구성 (각 키워드를 별도 칼럼에 저장)
        result_row = {"entity_text": entity}
        for i, kw in enumerate(keywords):
            result_row[f"keyword_{i+1}"] = kw

        results.append(result_row)

    # 결과 DataFrame 생성
    results_df = pd.DataFrame(results)

    # 결과 저장 (CSV 혹은 XLSX 중 선택)
    output_path = "C:/Users/MaengJiwoo/.vscode/KISTI-intern/2025_KISTI-intern/keyword_analysis_results.csv"
    results_df.to_csv(output_path, index=False, encoding="utf-8-sig")  # 한글 깨짐 방지

    print(f"Keyword extraction complete. Result saved as '{output_path}'")
    print(f"Total API cost: ${total_cost:.6f}")

if __name__ == "__main__":
    main()
