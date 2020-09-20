# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 15:16:55 2020

@author: nik25
"""

alphabet1 = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
alphabet2 = ['А','Б','В','Г','Д','Е','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']
 
def encrypt(word, shift):
    per = ""
    for x in word:
        if x in alphabet1:
            ind = alphabet1.index(x)%len(alphabet1)
            per += alphabet1[(ind+shift)%len(alphabet1)]
        elif x in alphabet2:
            ind = alphabet2.index(x)%len(alphabet1)
            per += alphabet2[(ind+shift)%len(alphabet1)]
        else:
            per += x
    return per
 
def decrypt(word, shift):
    per = ""
    for x in word:
        if x in alphabet1:
            ind = alphabet1.index(x)
            per += alphabet1[ind]
        elif x in alphabet2:
            ind = alphabet2.index(x)
            per += alphabet2[ind]
        else:
            per += x
    return per

word1 = input("Ввелите фразу: ")
shift1 = int(input("Введите сдвиг: ")) 
print("")
print("закодированная фраза: ", encrypt(word1, shift1))
print("раскодированная фраза: ", decrypt(word1, shift1))