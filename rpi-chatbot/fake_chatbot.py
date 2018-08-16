# Human Intelligence
from serach_text import *

FoodBubbleTea = [
    '珍珠奶茶'
]

BrandClass = [
    '五十嵐',
    'Coco', '口口', '扣扣'
    '一芳', '一方'
    '珍煮丹', '真主單'
    '老虎堂', '老虎糖'
]

def chatbot(sentence):
    for food in FoodBubbleTea:
        if food in sentence:
            return search_text(food)

    for brand in BrandClass:
        if brand in sentence:
            return search_text(brand)

    if "貝貝" in sentence or "寶貝" in sentence:
        return "情人節快樂"

    return "蛤，我不知道你在說什麼"

if __name__ == "__main__":
    question = '我超愛珍珠奶茶，請問有推薦的嗎'
    print('Qusetion: {}'.format(question))
    print(chatbot(question))
    print()

    question = '我超愛五十嵐'
    print('Qusetion: {}'.format(question))
    print(chatbot(question))
    print()
