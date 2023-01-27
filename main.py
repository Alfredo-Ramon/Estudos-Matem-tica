from Funções import Interface
from Funções import Mais
from Funções import X
import re


Interface.Menus.MenuPrincipalBemVindo()
print()
print()

while True:
    while True:
        Interface.Menus.MenuPrincipalEscolhas()
        escolhaMenuPrincipal = str(input('Digite uma opção: '))
        if re.fullmatch(re.compile('[1-5]'),escolhaMenuPrincipal) == None:
            print()
            print('#'*100)
            print(f'{"Por favor escolha umas das opções [1,2,3,4,5]".center(100)}')
            print('#'*100)
            print()            
        else:
            break
    if escolhaMenuPrincipal == '1':
        while True:
            Mais.MenuSoma()
            Mais.MenuSomaEscolha()
            escolhaSomaDificuldade = str(input('Digite uma opção: '))
            if re.fullmatch(re.compile('[1-4]'),escolhaSomaDificuldade) == None:
                print()
                print('#'*100)
                print(f'{"Por favor escolha umas das opções [1,2,3,4]".center(100)}')
                print('#'*100)
            if escolhaSomaDificuldade == '1' :
                Mais.SomaFacil()
            elif escolhaSomaDificuldade == '2':
                Mais.SomaMédio()
            elif escolhaSomaDificuldade == '3':
                Mais.SomaDificil()
            elif escolhaSomaDificuldade == '4' :
                 break
    if escolhaMenuPrincipal == '3':
        while True:
            X.MenuMultiplicação()
            X.MenuMultiplicaçãoEscolha
            escolhaMultiplicaçãoDificuldade = str(input('Digite uma opção: '))
            if re.fullmatch(re.compile('[1-3]'),escolhaMultiplicaçãoDificuldade) == None:
                print()
                print('#'*100)
                print(f'{"Por favor escolha umas das opções [1,2,3]".center(100)}')
                print('#'*100)
            if escolhaMultiplicaçãoDificuldade == '1' :
                X.MultiplicaçãoFacil()
            elif escolhaMultiplicaçãoDificuldade == '2':
                X.MultiplicaçãoDificil()
            elif escolhaMultiplicaçãoDificuldade == '3':
                break
                
    if escolhaMenuPrincipal == '5':
        break


    

