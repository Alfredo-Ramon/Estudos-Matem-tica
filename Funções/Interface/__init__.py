class Interface:
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
        
    def Escolha(numero):
        pass
        
        

if __name__ == '__main__' :
    Interface.MenuBemVindo()
    Interface.MenuEscolhas()

        