class Menus:
    def MenuPrincipalBemVindo():
        print('#'*100)
        print(F'{"BEM VINDO AO PROGRAMA: Resposta Rápida".center(100)}')
        print('#'*100)
    
    def MenuPrincipalEscolhas():
        print()
        print()
        print(f'{"Menu Principal".center(100)}')
        print('-'*100)
        print(f'{"Escolha uma opção".center(100)}')
        print('-'*100)
        print(f'[1]: Adição')
        print(f'[2]: Subtração')
        print(f'[3]: Multiplicação')
        print(f'[4]: Divisão ')
        print(f'[5]: Finalizar')
        print('_'*100)
    
        

        
        
        

if __name__ == '__main__' :
    Menus.MenuPrincipalBemVindo()
    Menus.MenuPrincipalEscolhas()

        