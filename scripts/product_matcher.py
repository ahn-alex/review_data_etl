import pandas as pd
import numpy as np
from rapidfuzz import process, fuzz

# load the dataset
prod = pd.read_csv('product_reference.csv')
reviews = pd.read_csv('sample_reviews.csv')
ref_names = prod['product_name'].tolist()

# matching function
# 1. 완전 일치 먼저 매칭
reviews['matched_product'] = np.where(
    reviews['product_name'].isin(ref_names),
    reviews['product_name'],
    None
)

# 2. RapidFuzz 적용 (unmatched만)
def fuzzy_match(name):
    if pd.isna(name):
        return None
    match = process.extractOne(name, ref_names, scorer=fuzz.token_sort_ratio)
    return match[0] if match and match[1] >= 70 else None

# Apply fuzzy only to unmatched
mask = reviews['matched_product'].isna()
reviews.loc[mask, 'matched_product'] = reviews.loc[mask, 'product_name'].apply(fuzzy_match)

