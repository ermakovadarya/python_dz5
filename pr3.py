# задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв". 
# Функции FIND и COUNT юзать нельзя.


sp='абв абвгд абвгдабв гдабв гбабвгб гбгб гдбв'
res=sp.split()
print(res)

def delete(x):
    i=0
    while i<=len(res)-1:
        flag=True
        while (flag):
            if x in res[i]:
                res.pop(i)
            else:
                i+=1
                flag=False
delete('абв')               
print(res)