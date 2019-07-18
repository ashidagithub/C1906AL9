# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   定义标准发牌机的动作函数
# ------------------------(max to 80 columns)-----------------------------------

# import some external moduls
import random
import codecs
import os
import csv


def create_deck_54(new_deck):
    '推出一副54张的新牌'
    print('\n -- debug: I made a new deck of 54.')

    # initialize var
    cardJokers = ('♞', '♘')
    cardMarks = ('♠', '♥', '♣', '♦')
    cardNumbers = ('2', '3', '4', '5', '6', '7', '8',
                   '9', '10', 'J', 'Q', 'K', 'A')

    for c in cardJokers:
        new_deck.append(c)

    # add 4x13 cards
    for cn in cardNumbers:
        for cm in cardMarks:
            #card = cm + cn
            card = cn + cm
            new_deck.append(card)

    return


def create_deck_52(new_deck):
    '推出一副52张的新牌'
    print('\n -- debug: I made a new deck of 52.')

    # initialize var
    #cardJokers = ('♞', '♘')
    # for c in cardJokers:
    #    new_deck.append(c)

    cardMarks = ('♠', '♥', '♣', '♦')
    cardNumbers = ('2', '3', '4', '5', '6', '7', '8',
                   '9', '10', 'J', 'Q', 'K', 'A')
    # add 4x13 cards
    for cn in cardNumbers:
        for cm in cardMarks:
            #card = cm + cn
            card = cn + cm
            new_deck.append(card)

    return


def shuffled_deck(deck_to_be_shuffled):
    '洗牌'
    print('\n -- debug: I shuffled a deck')

    random.shuffle(deck_to_be_shuffled)
    return


'''
def record_deck(deck_to_be_record, filename):
    '记录一副牌'
    print('\n -- debug: I record a deck')

    out_path = os.getcwd() + '\\OutputDecks\\' + filename
    #print(out_path)
    f = codecs.open(out_path, "w", "utf-8")
    for card in deck_to_be_record:
        f.write(card)
        f.write('\n')
    f.close

    return
'''

# ---- Poker 3.0 added
def make_deck_by_type(play_type, out_deck):
    '按要求制作各种扑克牌'
    if play_type == 1:  # 争上游的牌
        create_deck_54(out_deck)
        shuffled_deck(out_deck)
        record_deck(out_deck, '争上游-刚洗好的牌.txt')
    if play_type == 2:  # 桥牌
        create_deck_52(out_deck)
        shuffled_deck(out_deck)
        record_deck(out_deck, '桥牌-刚洗好的牌.txt')
    if play_type == 3:  # 三人斗地主的牌
        create_deck_54(out_deck)
        shuffled_deck(out_deck)
        record_deck(out_deck, '三人斗地主-刚洗好的牌.txt')
    if play_type == 4:  # 四人斗地主的牌
        # first deck
        deck_a = []
        create_deck_54(deck_a)
        out_deck.extend(deck_a)
        # second deck
        deck_b = []
        create_deck_54(deck_b)
        out_deck.extend(deck_b)
        # shuffled & record
        shuffled_deck(out_deck)
        record_deck(out_deck, '四人斗地主-刚洗好的牌.txt')

    return

# ---- Poker 4.0 added
def record_deck_csv(deck_to_be_record, csv_filename):
    '用CSV格式记录一副牌'
    print('\n -- debug: I record a deck')

    out_path = os.getcwd() + '\\out_decks_csv\\' + csv_filename

    with open(out_path, "w", encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(deck_to_be_record)

    return
