"""Pipeline wrapper for the sentence classification model.

"""
import nltk
nltk.download('punkt')

from claim import get_claim
import pandas as pd


def pipeline(abstract=""):

    # removing unnecessary punctuation because problems in tokenization
    punctuation = '!"#$%&\'()*+-/:;?@[\]^_`{|}~'

    for c in punctuation:
        if c in abstract:
            abstract = abstract.replace(c, ' ')
    
    result = get_claim(abstract)

    df = pd.DataFrame({'label': result['labels'], 
                   'sentence': result['sents'], 
                   'score': result['scores']})

    return df
