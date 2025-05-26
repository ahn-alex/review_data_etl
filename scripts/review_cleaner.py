# review_cleaner.py

import pandas as pd
import re

def clean_text(text):
    if not isinstance(text, str):
        return ''
    
    # 1. 앞뒤 공백 제거
    text = text.strip()

    # 2. 숫자, 영문, 한글, 공백만 남기고 나머지 제거
    text = re.sub(r'[^0-9a-zA-Zㄱ-ㅎ가-힣\s]', '', text)

    # 3. 여러 공백을 하나로
    text = re.sub(r'\s+', ' ', text)

    return text

def clean_reviews(input_path, output_path):
    df = pd.read_csv(input_path)

    # 정제 적용
    df['review'] = df['review'].apply(clean_text)

    # 빈 문자열 제거
    df = df[df['review'].str.strip().astype(bool)]

    # 중복 제거
    df = df.drop_duplicates(subset='review')

    df.to_csv(output_path, index=False)
    print(f"Cleaned reviews saved to {output_path}")

if __name__ == "__main__":
    input_file = "../data/scraped_reviews.csv"
    output_file = "../data/cleaned_reviews.csv"
    clean_reviews(input_file, output_file)
