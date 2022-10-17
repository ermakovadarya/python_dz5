# 34. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# README учитываются отрицательные и положительные цифры
#       учитывается если степени и множетели состоят из нескольких разрядов
#       Но! реализовано только с наличием свободного множителя, без него не придумала

import re
import collections
def open_file(k):
    with open(k, 'r') as fh:  
        str=fh.readline()
    return str


x='mn1.txt'
y='mn2.txt'
str1=open_file(x)
str2=open_file(y)
print(str1)
print(str2)

def res_str(str):
    res1=re.split('[*+^x=]',str)    #разделяем строку 
    print(res1)
    res2=[]
    for i in res1:                   #Создаем новую без пустых элементов
        try:
            res2.append(int(i))
        except:
            res1.remove(i)
    # res2.pop(-1)
    dict1={}                        #создаем словарь из пар(степень/значение)
    for x in range(0,len(res2)-1,2):
        dict1[res2[x+1]]=res2[x]
    # dict['0']=int(res2[-2])
    return dict1


dict1=res_str(str1)
dict2=res_str(str2)
print (dict1)
print(dict2)


dict_res={}                         #создаем итоговый словарь из элементов, которые есть в обоих словарях и суммируем их элементы
for x,y in dict1.items():
    flag=False
    for a,b in dict2.items():
        if x==a:
            dict_res[x]=(y+b)
            flag=True
            break
    if flag==False:
        dict_res[x]=y               #Добавляем в итоговый словарь элементы 1 строки если они не встретились во втором словаре

for x,y in dict2.items():           #Проверяем 2 словарь. если там есть элементы, которые не добавились в ходе цикла выше то добавляем их в итоговый словарь
    flag=False
    for a,b in dict_res.items():
        if x==a:
            flag=True
            break
    if flag==False:
        dict_res[x]=y

print(dict_res)
sortedDict=collections.OrderedDict(sorted(dict_res.items(), reverse=True)) #Сортируем итоговый словарь по убыванию ключей

print(sortedDict)                   #Печатаем по форме многочлена
for i,j in sortedDict.items():
    print(f'{j}*x^{i}',end='+')
print (f'{sortedDict[0]}=0')



    



