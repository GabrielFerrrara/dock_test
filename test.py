from conversor import *

var1 = Date('12/03/2021')
var2 = Date('15/04/2022')
var3 = Date('20210506')
var4 = Date('20220208')

listaRetorno = []


def test1(data1, data2):
    descricao = f'Teste 1: Verificando se data {data1} é maior que a data {data2} (Ambas de mesmo formato)'
    if(data1.getNumeric()>data2.getNumeric()):
        return listaRetorno.append(descricao)

test1(var1,var2)
 

def test2(data1, data2):
    descricao = f'Teste 2: Verificando se data {data1} é maior que a data {data2} (Formatos distintos de entrada)'
    if(data1.getNumeric()<data2.getNumeric()):
        return listaRetorno.append(descricao)

test2(var1,var3)

def test3(data1, data2, data3):
    descricao = f'Teste 3: Verificando se data {data1} é maior que as datas {data2} e {data3} (As de comparacao com formatos distintos)'
    if(data1.getNumeric()<(data2.getNumeric() and data3.getNumeric())):
        return listaRetorno.append(descricao)

test3(var2,var1,var4)

def test4(data1):
    valorTeste = '20210312'
    descricao = f'Teste 4: Verificando se a formatação de {data1.getFormatInit()} ficou como {valorTeste}'
    if(data1.getFormat() != valorTeste):
        return listaRetorno.append(descricao)

test4(var1)

def test5(data1):
    valorTeste = '20220208'
    descricao = f'Teste 5: Verificando se a formatação de {data1.getFormatInit()} ficou como {valorTeste}'
    if(data1.getFormat() == valorTeste):
        return listaRetorno.append(descricao)
test5(var4)    


qntTeste = 5


if(len(listaRetorno) == 0):
    print(f'Sucesso! Todos os {qntTeste} casos passaram nos testes')
else:
    print(f'Falha! Os teste(s) a seguir falharam, sendo {len(listaRetorno)}/{qntTeste}')
    for teste in listaRetorno:
        print(teste)


