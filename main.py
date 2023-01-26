from Funções import Interface
from Funções import Games
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
            Games.Soma.MenuSoma()
            Games.Soma.MenuSomaEscolha()
            escolhaSomaDificuldade = str(input('Digite uma opção: '))
            if re.fullmatch(re.compile('[1-4]'),escolhaSomaDificuldade) == None:
                print()
                print('#'*100)
                print(f'{"Por favor escolha umas das opções [1,2,3,4]".center(100)}')
                print('#'*100)
            if escolhaSomaDificuldade == '1' :
                 Games.Soma.SomaFacil()
            elif escolhaSomaDificuldade == '2':
                Games.Soma.SomaMédio()
            elif escolhaSomaDificuldade == '3':
                Games.Soma.SomaDificil()
            elif escolhaSomaDificuldade == '4' :
                 break
                      
    if escolhaMenuPrincipal == '5':
        break
             
    

