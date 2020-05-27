""""Run the whole pipeline
"""

import pandas as pd
from pprint import pprint
from pipeline import pipeline

file_location = 'csv.pubmed19n1034.csv'
abstract_df = pd.read_csv(file_location)
abstract_df = abstract_df.dropna()

result_dict = dict()
for _, row in abstract_df.iterrows():
    temp_result = pipeline(row['abstract'])
    temp_title = row['title']
    result_dict[temp_title] = temp_result

# pprint(abstract_df.isnull())
