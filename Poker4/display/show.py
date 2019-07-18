# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   按金字塔形显示一副牌牌
# ------------------------(max to 80 columns)-----------------------------------

# 引用Python的模块
'''
import sys
import codecs
import os
'''

# 引用自己的模块
#sys.path.append('..')
#from display.menu import clear_menu


def show_deck_para(deck):
    '用并排的方式显示一副扑克牌（假设扑克牌已经排好序）'

    #clear_menu()

    print('**********************************')
    print('***       我挑的牌如下         ***')
    pre_card = ''
    cur_card = ''
    for card in deck:
        cur_card = card[:-1]
        if cur_card != pre_card:
            print('\n%s ' % (card), end='')
        else:
            print('%s ' % (card), end='')
        pre_card = cur_card

    print('\n\n**********************************')
    print('*****        总计 %d 张牌      ***' % (len(deck)))

    return
