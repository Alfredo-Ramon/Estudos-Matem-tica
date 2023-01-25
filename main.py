from Funções import Interface
import re

Interface.Menus.MenuBemVindo()
Interface.Menus.MenuEscolhas()


while True:
    while True:
        escolha = str(input('Digite uma opção: '))
        if re.fullmatch(re.compile('[1-5]'),escolha) == None:
            print('Erro')
        else:
            print('OK')
            break
    if escolha == '5' :
        break
             
    
Interface.Menus.Escolha(escolha)
