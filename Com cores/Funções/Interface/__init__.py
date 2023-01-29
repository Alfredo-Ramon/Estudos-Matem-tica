class Menus:
    def MenuPrincipalBemVindo():
        print('\33[45m \33[m'*100)
        print(F'\33[36m{"BEM VINDO AO PROGRAMA: Resposta Rápida".center(100)}\33[m')
        print('\33[45m \33[m'*100)
    
    def MenuPrincipalEscolhas():
        print()
        print()
        print(f'\33[36m{"Menu Principal".center(100)}\33[m')
        print('\33[45m \33[m'*100)
        print(f'\33[36m{"Escolha uma opção".center(100)}\33[m')
        print('\33[32;45m \33[m'*100)
        print(f'\33[32m[1]: Adição\33[m')
        print(f'\33[35m[2]: Subtração\33[m')
        print(f'\33[34m[3]: Multiplicação\33[m')
        print(f'\33[33m[4]: Divisão \33[m')
        print(f'\33[31m[5]: Finalizar\33[m')
        print('\33[45m \33[m'*100)
    
        

        
        
        

if __name__ == '__main__' :
    Menus.MenuPrincipalBemVindo()
    Menus.MenuPrincipalEscolhas()

        