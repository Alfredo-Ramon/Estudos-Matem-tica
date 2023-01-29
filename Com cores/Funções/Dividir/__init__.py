def MenuDivisão():
    print()
    print()
    print(F'\33[33m{"Divisão".center(100)}\33[m')
    print('\33[45m \33[m'*100)
    print(F'\33[33m{"Escolha uma dificuldade".center(100)}\33[m')
    print('\33[45m \33[m'*100)
    
def MenuDivisãoEscolha():
    print(f'\33[32m[1]: Fácil\33[m')
    print(f'\33[31m[2]: Voltar para o Menu Principal\33[m')
    print('\33[45m \33[m'*100)
    
def DivisãoFacil():
    import random
    erros = 0
    print()
    print()
    print(F'\33[33m{"Divisão".center(100)}\33[m')
    print('\33[45m \33[m'*100)
    print(F'\33[36m{"Facil: O programa ira fazer 10 contas todas contendo só uma unidade".center(100)}\33[m')
    print('\33[45m \33[m'*100)
    print()
    print()
    for Conta in range(10):
            print('\33[45m \33[m'*100)
            while True :
                while True:
                    Numero1 = random.randint(1,9)
                    Numero2 = random.randint(1,Numero1)
                    conta = Numero1/Numero2
                    conta = str(conta)
                    if len(conta) > 4:
                        Numero1 = random.randint(1,9)
                        Numero2 = random.randint(1,Numero1) 
                    else:
                        break
                if Numero1 == Numero2:
                    Numero1 = random.randint(1,9)
                    Numero2 = random.randint(1,Numero1)
                elif Numero2 == 1:
                    Numero2 = random.randint(1,Numero1)
                else:
                    if Conta == 0:
                        UltimaContaNumero1 = Numero1
                        UltimaContaNumero2 = Numero2
                        break
                    elif Conta > 0:
                        if UltimaContaNumero1 != Numero1 and UltimaContaNumero2 != Numero2 : 
                            UltimaContaNumero1 = Numero1
                            UltimaContaNumero2 = Numero2   
                            break

            print(f'\33[36m{Conta+1}:\33[m {Numero1}\33[33m/\33[m{Numero2} \33[36m=\33[m \33[31m?\33[m') 
            while True:
                try:
                    resposta = float(input('Resposta: ')) 
                except :
                    print('\33[41m \33[m'*100)
                    print(f'\33[31m{Numero1}/{Numero2} = ? \33[m'.center(100)) 
                    print(f'\33[31m{"Sixtaxe : Resposta com valor Inteiro X".center(100)} \33[m')
                    print(f'\33[31m{"Sixtaxe : Resposta com valor Decimal X.XX".center(100)} \33[m')  
                    print(f'\33[31m{"Por favor use só números [1|2|3|4|5|6|7|8|9|0]".center(100)}\33[m')
                    print(f'\33[31m{"User . no lugar de ,".center(100)}\33[m')
                    print('\33[41m \33[m'*100)
                else:
                    if resposta == Numero1/Numero2:
                        print('\33[32mAcertou\33[m')
                        print('\33[42m \33[m'*100)
                        print()
                        print()
                        break
                    else:
                        if resposta < Numero1/Numero2:
                            erros += 1
                            print()
                            print('\33[43m \33[m'*100)
                            print(f'\33[33m{Numero1}/{Numero2} = ? \33[m'.center(100))  
                            print('\33[33mMais + \33[m'.center(100))
                            print('\33[43m \33[m'*100)
                        elif resposta > Numero1/Numero2:
                            erros += 1
                            print()
                            print('\33[43m \33[m'*100)
                            print(f'\33[33m{Numero1}/{Numero2} = ? \33[m'.center(100))  
                            print('\33[33mMenos - \33[m'.center(100))
                            print('\33[43m \33[m'*100)
    print(f'Você errou: \33[31m{erros}\33[m vezes')
    

if __name__ == '__main__':
    DivisãoFacil()