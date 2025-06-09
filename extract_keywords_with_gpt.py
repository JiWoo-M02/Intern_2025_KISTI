import pandas as pd
from tqdm import tqdm
from openai import OpenAI

# OpenAI 클라이언트 초기화
client = OpenAI(api_key="sk-proj-39MAIAVyfnn1oYMs7fCuT3BlbkFJS3JKP12jYFCwXacyAdyY")

# Prompt 템플릿
keyword_system_prompt = """You are a keyword extraction model.

[Objective]
Extract the 3 to 5 most important noun-based keywords from a given text.

[Task Instructions]
- Only extract nouns or noun phrases that capture the core concepts.
- Output as a **comma-separated list**.
- Do not include any explanations or sentences.
- If no valid keywords, output an empty list.

[Format Example]
Input: "Artificial intelligence is transforming the healthcare industry with diagnostic tools."
Output: artificial intelligence, healthcare industry, diagnostic tools
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
            model="gpt-4.1-mini",   # gpt-4o 사용 추천
            messages=messages,
            temperature=0.3
        )
        content = response.choices[0].message.content.strip()
        keywords = [kw.strip() for kw in content.split(",") if kw.strip()]
        
        cost = calculate_cost_of_openai_api(response.usage.prompt_tokens, response.usage.completion_tokens)

        return keywords, cost
    except Exception as e:
        print(f"Error extracting keywords: {e}")
        return [], 0.0

# 키워드 포함 여부 확인
def keyword_in_text(keywords, text):
    return [kw for kw in keywords if kw.lower() in text.lower()]

# Main 처리
def main():
    total_cost = 0.0

    # CSV 로드
    file_path = "C:/Users/MaengJiwoo/.vscode/KISTI-intern/2025_KISTI-intern/overlapped_entities.csv"
    df = pd.read_csv(file_path, encoding="windows-1252")

    results = []

    for _, row in tqdm(df.iterrows(), total=len(df), desc="Processing rows"):
        entity = row['entity_text']
        abstract = str(row.get('abstract', ''))
        brfsum = str(row.get('brfsum', ''))

        keywords, cost = extract_keywords(entity)
        total_cost += cost

        in_abstract = keyword_in_text(keywords, abstract)
        in_brfsum = keyword_in_text(keywords, brfsum)

        results.append({
            "entity_text": entity,
            "keywords": ", ".join(keywords),
            "keywords_in_abstract": ", ".join(in_abstract),
            "keywords_in_brfsum": ", ".join(in_brfsum)
        })

    # 결과 저장
    results_df = pd.DataFrame(results)
    output_path = "C:/Users/MaengJiwoo/.vscode/KISTI-intern/2025_KISTI-intern/keyword_analysis_results.csv"
    results_df.to_csv(output_path, index=False)

    print(f"Keyword extraction complete. Result saved as '{output_path}'")
    print(f"Total API cost: ${total_cost:.6f}")

if __name__ == "__main__":
    main()
