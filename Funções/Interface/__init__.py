class Menus:
    def MenuBemVindo():
        print('_'*100)
        print(F'{"BEM VINDO AO APLICATIVO: Respota Rápida".center(100)}')
        print(f'{"Use a vontade :)".center(100)}')
        print('_'*100)
    
    def MenuEscolhas():
        print(f'[1]: Adição')
        print(f'[2]: Subtração')
        print(f'[3]: Multiplicação')
        print(f'[4]: Divisão ')
        print(f'[5]: Finalizar')
        print('_'*100)
    
        
    def Escolha(numero = 0):
        if numero == 0:
            print(f'Por favor escolha umas das opções [1,2,3,4,5]')
        
        
        

if __name__ == '__main__' :
    Menus.MenuBemVindo()
    Menus.MenuEscolhas()
    Menus.Escolha(1)

        