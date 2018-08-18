import numpy as np
import pandas as pd

'''
def search_text(text, path='../rpi-chatbot-2/data/data.csv'):
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
'''

def search_text(text, path='data/data.csv'):
    '''
    Search the text in the data and return a string.
    If nothing is found, then return an empty string.
    '''
    columns = ['Item', 'Brand']

    df = pd.read_csv(path)
    # text = word2zhuyin(text)          # transform to zhuyin
    # zhuyin_df = df.apply(word2zhuyin) # transform to zhuyin

    df = df.set_index(columns)
    # zhuyin_df = zhuyin_df.set_index(columns)

    result = []
    for i in range(len(df)):
        if text in df.index[i][0]:
            result.append(df.index[i][1])
        elif text in df.index[i][1]: # df.index[0] = ('珍珠奶茶', '50嵐')
            result += list(df.loc[df.index[i]].values)
    result = '。'.join(result)

    return result

if __name__ == "__main__":
    question = '我超愛珍珠奶茶，請問有推薦的嗎'
    print('Qusetion: {}'.format(question))
    print(search_text('珍珠奶茶'))
    print()

    question = '我超愛50嵐'
    print('Qusetion: {}'.format(question))
    print(search_text('50嵐'))
    print()

    question = '夜市，請推薦'
    print('Qusetion: {}'.format(question))
    print(search_text('夜市'))
    print()

    question = '士林夜市，請推薦'
    print('Qusetion: {}'.format(question))
    print(search_text('士林夜市'))
    print()

