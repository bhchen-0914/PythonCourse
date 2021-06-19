# -*- coding: UTF-8 -*-

str1 = '我想导航到'
f1 = open('poi.txt', 'r')
f2 = open('speech.txt', 'a')
for lines in f1.readlines():
    str2 = str1 + lines
    f2.write(str2)
f1.close()
f2.close()
