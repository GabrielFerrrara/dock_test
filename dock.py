from conversor import Date

a = '31/01/2022'
b = '20220201'

a = Date(a)
b = Date(b)

print(f'Formatos convergidos: {a}, {b}')

if(a.getNumeric()>b.getNumeric()):
    print(f' Maior data: {a}\n Menor data: {b}')
elif(a.getNumeric()<b.getNumeric()):
    print(f' Maior data: {b}\n Menor data: {a}')
else:
    print('Datas iguais: ' + a)

    
