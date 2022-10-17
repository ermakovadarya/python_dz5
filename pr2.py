# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.


def open_file(k):
    with open(k, 'r') as fh:  
        str1=fh.readline()
    return str1
def save(k,x):
    with open(k,'a') as fh:
        fh.write('\n'+x+' ')

str1=open_file('pr2.txt')
print (str1)
def rle_start(str1):
    res=[]
    i=0
    while i<len(str1)-1:
        temp=1
        fl=True
        try:
            while str1[i+1]==str1[i]:
                temp+=1
                i+=1
            else:
                res.append((str1[i],str(temp)))
                i+=1

        except:
            i=-1
            temp=1
            while str1[i]==str1[i-1]:
                temp+=1
                i-=1
            else:
                res.append((str1[i],str(temp)))
                i-=1
                fl=False
                break
        if fl and i==len(str1)-1:
            res.append((str1[-1],'1'))  
            # print('еще последний')
    return res
            
def rle_finish(res):
    res_str='Итоговая строка = '
    for i in res:
        for j in range(int(i[1])):
            res_str+=i[0]
    return res_str


            

res=rle_start(str1)
print(res)
res_str=rle_finish(res)
print(res_str)
for i in res:
    line=''.join(i)
    save('pr2.txt',line)
save('pr2.txt',res_str)
