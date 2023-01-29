def MenuDivisão():
    print()
    print()
    print(F'{"Divisão".center(100)}')
    print('_'*100)
    print(F'{"Escolha uma dificuldade".center(100)}')
    print('_'*100)
    
def MenuDivisãoEscolha():
    print(f'[1]: Fácil')
    print(f'[2]: Voltar para o Menu Principal')
    print('_'*100)
    
def DivisãoFacil():
    import random
    erros = 0
    print()
    print()
    print(F'{"Divisão".center(100)}')
    print('_'*100)
    print(F'{"Facil: O programa ira fazer 10 contas todas contendo só uma unidade".center(100)}')
    print('_'*100)
    print()
    print()
    for Conta in range(10):
            print('*'*100)
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
                            
            print(f'{Conta+1}: {Numero1}/{Numero2} = ?') 
            while True:
                try:
                    resposta = float(input('Resposta: ')) 
                except :
                    print('#'*100)
                    print(f'{Numero1}/{Numero2} = ?'.center(100))
                    print(f'{"Sixtaxe : Resposta com valor Inteiro X".center(100)} ')
                    print(f'{"Sixtaxe : Resposta com valor Decimal X.XX".center(100)} ')  
                    print(f'{"Por favor use só números [1|2|3|4|5|6|7|8|9|0]".center(100)}')
                    print(f'{"User . no lugar de ,".center(100)}')
                    print('#'*100)
                else:
                    if resposta == Numero1/Numero2:
                        print('Acertou')
                        print('*'*100)
                        print()
                        print()
                        break
                    else:
                        if resposta < Numero1/Numero2:
                            erros += 1
                            print()
                            print('#'*100)
                            print(f'{Numero1}/{Numero2} = ?'.center(100)) 
                            print('Mais + '.center(100))
                            print('#'*100)
                        elif resposta > Numero1/Numero2:
                            erros += 1
                            print()
                            print('#'*100)
                            print(f'{Numero1}/{Numero2} = ?'.center(100)) 
                            print('Menos - '.center(100))
                            print('#'*100)
    print(f'Você errou: {erros} vezes')
    

if __name__ == '__main__':
    DivisãoFacil()