# Human Intelligence
from serach_text import *

class FoodClass:
    FOOD_BUBBLE_TEA = '珍珠奶茶'

class BrandClass:
    BRAND_1 = '50嵐'


def chatbot(sentence):
    if FoodClass.FOOD_BUBBLE_TEA in sentence:
        return search_text(FoodClass.FOOD_BUBBLE_TEA)

    if BrandClass.BRAND_1 in sentence:
        return search_text(BrandClass.BRAND_1)

if __name__ == "__main__":
    question = '我超愛珍珠奶茶，請問有推薦的嗎'
    print('Qusetion: {}'.format(question))
    print(chatbot(question))
    print()

    question = '我超愛50嵐'
    print('Qusetion: {}'.format(question))
    print(chatbot(question))
    print()
