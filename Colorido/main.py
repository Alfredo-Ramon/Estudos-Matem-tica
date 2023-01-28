from Funções import Interface
from Funções import Mais
from Funções import Menos
from Funções import Vezes
from Funções import Dividir
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
             
             
             
    elif escolhaMenuPrincipal == '2':
        while True:
            Menos.MenuSubtração()
            Menos.MenuSubtraçãoEscolha
            escolhaSubtraçãoDificuldade = str(input('Digite uma opção: '))
            if re.fullmatch(re.compile('[1-5]'),escolhaSubtraçãoDificuldade) == None:
                print()
                print('#'*100)
                print(f'{"Por favor escolha umas das opções [1,2,3,4,5]".center(100)}')
                print('#'*100)
                print()            
            if escolhaSubtraçãoDificuldade == '1':
                Menos.SubtraçãoFacil()
            elif escolhaSubtraçãoDificuldade == '2':
                Menos.SubtraçãoFacilNegativo()
            elif escolhaSubtraçãoDificuldade == '3':
                Menos.SubtraçãoMédio()
            elif escolhaSubtraçãoDificuldade == '4':
                Menos.SubtraçãoMédioNegativo()
            elif escolhaSubtraçãoDificuldade == '5':
                break
            

       
    elif escolhaMenuPrincipal == '3':
        while True:
            Vezes.MenuMultiplicação()
            Vezes.MenuMultiplicaçãoEscolha()
            escolhaMultiplicaçãoDificuldade = str(input('Digite uma opção: '))
            if re.fullmatch(re.compile('[1-3]'),escolhaMultiplicaçãoDificuldade) == None:
                print()
                print('#'*100)
                print(f'{"Por favor escolha umas das opções [1,2,3]".center(100)}')
                print('#'*100)
            if escolhaMultiplicaçãoDificuldade == '1' :
                Vezes.MultiplicaçãoFacil()
            elif escolhaMultiplicaçãoDificuldade == '2':
                Vezes.MultiplicaçãoDificil()
            elif escolhaMultiplicaçãoDificuldade == '3':
                break
    
    elif escolhaMenuPrincipal =='4':
        while True:
            Dividir.MenuDivisão()
            Dividir.MenuDivisãoEscolha()
            escolhaDivisãoDificuldade = str(input('Digite uma opção: '))
            if re.fullmatch(re.compile('[1-2]'),escolhaDivisãoDificuldade) == None :
                print()
                print('#'*100)
                print(f'{"Por favor escolha umas das opções [1,2]".center(100)}')
                print('#'*100)
            if escolhaDivisãoDificuldade == '1' :
                Dividir.DivisãoFacil()
            elif escolhaDivisãoDificuldade == '2':
                break
                
    
                
    elif escolhaMenuPrincipal == '5':
        break


    

