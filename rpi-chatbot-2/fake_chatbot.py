# Human Intelligence
from search_text import *

FoodBubbleTea = [
    '珍珠奶茶'
]

BrandClass = [
    '50嵐', '五十嵐',
    'CoCo',
    '一芳',
    '珍煮丹',
    '老虎堂',
]

def chatbot(sentence):
    for food in FoodBubbleTea:
        if food in sentence:
            return search_text(food)

    for brand in BrandClass:
        if brand in sentence:
            return search_text(brand)

    return "蛤，我不知道你在說什麼"

if __name__ == "__main__":
    question = '我超愛珍珠奶茶，請問有推薦的嗎'
    print('Qusetion: {}'.format(question))
    print(chatbot(question))
    print()

    question = '我超愛50嵐'
    print('Qusetion: {}'.format(question))
    print(chatbot(question))
    print()
