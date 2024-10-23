a = input('ведите строку 1 ') 
b = input('ведите строку 2 ')
k =0
for i in a:
    if i in b:
        k += 1
print('Строки аннограммы' if k == len(a) else 'Строки не аннограммы')
