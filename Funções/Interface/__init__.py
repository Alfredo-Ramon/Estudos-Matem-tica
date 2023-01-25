class Menus:
    def MenuBemVindo():
        print('\33[35m_\33[m'*100)
        print(F'\33[41m{"BEM VINDO AO APLICATIVO: Respota Rápida".center(100)}\33[m')
        print(f'{"Use a vontade :)".center(100)}')
        print('\33[35m_\33[m'*100)
    
    def MenuEscolhas():
        print(f'[1]: Adição')
        print(f'[2]: Subtração')
        print(f'[3]: Multiplicação')
        print(f'[4]: Divisão ')
        print(f'[5]: Finalizar')
        print('\33[35m_\33[m'*100)
    
        
    def Escolha(numero = 0):
        if numero == 0:
            print(f'\33[31mPor favor escolha umas das opções [1,2,3,4,5]\33[m')
        
        
        

if __name__ == '__main__' :
    Menus.MenuBemVindo()
    Menus.MenuEscolhas()
    Menus.Escolha(1)

        