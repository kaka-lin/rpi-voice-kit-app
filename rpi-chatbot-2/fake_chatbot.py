# Human Intelligence
from search_text import *

BubbleTeas = [
    '50嵐', '五十嵐',
    'CoCo',
    '一芳',
    '珍煮丹',
    '老虎堂',
]

NightMarkets = [
    '士林夜市',
    '饒河夜市',
    '通化夜市',
    '寧夏夜市'
]

TaipeiScenes = [
    '台北101',
    '中正紀念堂',
    '西門町',
    '九份'
]

def chatbot(sentence):
    for bubble_tea in BubbleTeas:
        if bubble_tea in sentence:
            return search_text(bubble_tea)
    if '珍珠奶茶' in sentence:
        return search_text('珍珠奶茶')

    for night_markets in NightMarkets:
        if night_markets in sentence:
            return search_text(night_markets)
    if '夜市' in sentence:
        return search_text('夜市')

    for taipei_scene in TaipeiScenes:
        if taipei_scene in sentence:
            return search_text(taipei_scene)
    if '台北' in sentence:
        return search_text('台北')

    return "蛤，我不知道你在說什麼，請再說一次"

if __name__ == "__main__":
    question = '我超愛珍珠奶茶，請問有推薦的嗎'
    print('Qusetion: {}'.format(question))
    print(chatbot(question))
    print()

    question = '我超愛50嵐'
    print('Qusetion: {}'.format(question))
    print(chatbot(question))
    print()

    question = '夜市，請推薦'
    print('Qusetion: {}'.format(question))
    print(chatbot(question))
    print()

    question = '士林夜市，請推薦'
    print('Qusetion: {}'.format(question))
    print(chatbot(question))
    print()

    question = '台北有什麼好玩的'
    print('Qusetion: {}'.format(question))
    print(chatbot(question))
    print()

    question = '西門町有什麼好玩好吃的'
    print('Qusetion: {}'.format(question))
    print(chatbot(question))
    print()
