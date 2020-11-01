# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 16:22:23 2020

@author: nik25
"""

import logging

logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = u'loger.log')

def sapros(ogranbas,watt,par_1,par_2): #фунция запроса и проверки значения ответа 
    go = True
    while go == True:
        ye = 0     
        bas = [1,0]
        if ogranbas == True: print('----------\n'+watt+':\n0 - '+par_1+'\n1 - '+par_2)
        else: print('----------\n'+watt)
        vosvrat = input(':')
        if  vosvrat.isdigit() == True:
            vosvrat = int(vosvrat)
            go = False
            logging.debug(u"число введено в правильном формате")
        else:
            go = True
            print('необходимо целое число')
            logging.debug(u"выбран неверный формат")
        if ogranbas != True: continue
        for i in bas:
            if vosvrat == i: ye +=1 
        if ye == 1: go = False 
        else:
            print('Введеное значение не совпадает с возможными')
            logging.debug(u"Введеное значение не совпадает с возможными")
            go = True
    return vosvrat 

cezar = True
while cezar == True:
    
    ho = sapros(True,'Режим работы','расшифровать','шифровать')
    logging.info(u"сделан выбор режима работы")
    r = sapros(True,'Алфавит ввода','латинский','русский') #выбр алфавита шифрования 
    logging.info(u"сделан выбор используемого алфавита")
    if r == 0: ALF = 'abcdefghijklmnopqrstuvwxyz'
    else: ALF = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    n = sapros(False,'Число символов смещения','','') #обозначение кол-ва знаков смещения 
    logging.info(u"сделан выбор числа смещения")
    if ho == 0: n = -n

    go = True
    while go == True:
        print('----------\nЦифры, знаки препинания и специальные символы не шифруются!')
        S = str(input('текст: ').lower()) #ввод строки 
        for i in S: 
            if i.isalpha() != True: continue #правильный ввод
            if ALF.count(i) != 0:
                go = False
                continue
            else: #неправильный ввод
                print('символы не соответствуют выбранному алфавиту')
                go = True
                break
            
    fr = str()
    for i in S:
        if i.isalpha() != True:
            fr += i
            continue 
        fr += ALF[(ALF.index(i) + n) % len(ALF)] #шифрование-расшифрование
    
    print('\nполучено: '+fr)
    
    progon = sapros(True,'Ещё разок?','да','нет') #повтро программы
    logging.info(u"сделан выбор запуска программы повторно")
    if progon == 1: cezar = False