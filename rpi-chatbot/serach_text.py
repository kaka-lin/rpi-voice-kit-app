import numpy as np
import pandas as pd

def search_text(text, path='data/data.csv'):
    df = pd.read_csv(path, index_col=['Item', 'Brand'])
    sorted_df = df.sort_index()

    try:
        result = sorted_df.loc[text,:].values # list of list of opinion
        result = result.reshape(-1) # flatten the list of list of opinion into a list
        result = '。'.join(result)  # join every opinion with '。'
    except:
        try:
            result = sorted_df.loc[(slice(None),slice(text, text)),:].values
        except:
            print('%s is not in the data.'%(text))
        else:
            return result[0][0]
    else:
        return result
