def MenuSubtração():
    print()
    print()
    print(F'{"Subtração".center(100)}')
    print('_'*100)
    print(F'{"Escolha uma dificuldade".center(100)}')
    print('_'*100)
    
def MenuSubtraçãoEscolha():
    print(f'[1]: Fácil')
    print(f'[2]: Fácil(Negativos)')
    print(f'[3]: Médio')
    print(f'[4]: Médio(Negativos)')
    print(f'[5]: Finalizar')
    print('_'*100)
    
def SubtraçãoFacil():
    import random
    erros = 0
    print()
    print()
    print(F'{"Multiplicação".center(100)}')
    print('_'*100)
    print(F'{"Facil: O programa ira fazer 10 contas todas contendo só uma unidade".center(100)}')
    print('_'*100)
    print()
    print()
    for Conta in range(10):
            print('*'*100)
            Numero1 = random.randint(1,9)
            Numero2 = random.randint(1,8)
            while Numero1 < Numero2:
                Numero2 = random.randint(1,8)
            print(f'{Conta+1}: {Numero1}-{Numero2} = ?') 
            while True:
                try:
                    resposta = int(input('Resposta: ')) 
                except :
                    print('#'*100)
                    print(f'{Numero1}-{Numero2} = ?'.center(100)) 
                    print(f'{"Por favor use só números [1|2|3|4|5|6|7|8|9|0]".center(100)}')
                    print('#'*100)
                else:
                    if resposta == Numero1-Numero2:
                        print('Acertou')
                        print('*'*100)
                        print()
                        print()
                        break
                    else:
                        if resposta < Numero1-Numero2:
                            erros += 1
                            print()
                            print('#'*100)
                            print(f'{Numero1}-{Numero2} = ?'.center(100)) 
                            print('Mais'.center(100))
                            print('#'*100)
                        elif resposta > Numero1-Numero2:
                            erros += 1
                            print()
                            print('#'*100)
                            print(f'{Numero1}-{Numero2} = ?'.center(100)) 
                            print('Menos'.center(100))
                            print('#'*100)
    print(f'Você errou: {erros} vezes')

def SubtraçãoFacilNegativo():
    import random
    erros = 0
    print()
    print()
    print(F'{"Multiplicação".center(100)}')
    print('_'*100)
    print(F'{"Facil: O programa ira fazer 10 contas todas contendo só uma unidade (O resultado pode ser negativo)".center(100)}')
    print('_'*100)
    print()
    print()
    for Conta in range(10):
                print('*'*100)
                Numero1 = random.randint(1,9)
                Numero2 = random.randint(1,9)
                print(f'{Conta+1}: {Numero1}-{Numero2} = ?') 
                while True:
                    try:
                        resposta = int(input('Resposta: ')) 
                    except :
                        print('#'*100)
                        print(f'{Numero1}-{Numero2} = ?'.center(100)) 
                        print(f'{"Por favor use só números [1|2|3|4|5|6|7|8|9|0]".center(100)}')
                        print('#'*100)
                    else:
                        if resposta == Numero1-Numero2:
                            print('Acertou')
                            print('*'*100)
                            print()
                            print()
                            break
                        else:
                            if resposta < Numero1-Numero2:
                                erros += 1
                                print()
                                print('#'*100)
                                print(f'{Numero1}-{Numero2} = ?'.center(100)) 
                                print('Mais'.center(100))
                                print('#'*100)
                            elif resposta > Numero1-Numero2:
                                erros += 1
                                print()
                                print('#'*100)
                                print(f'{Numero1}-{Numero2} = ?'.center(100)) 
                                print('Menos'.center(100))
                                print('#'*100)
    print(f'Você errou: {erros} vezes')
    
def SubtraçãoMédio():
    import random
    erros = 0
    print()
    print()
    print(F'{"Multiplicação".center(100)}')
    print('_'*100)
    print(F'{"Médio: O programa ira fazer 10 contas, contendo dezena e unidade".center(100)}')
    print('_'*100)
    print()
    print()
    for Conta in range(10):
                print('*'*100)
                Numero1 = random.randint(1,99)
                Numero2 = random.randint(1,98)
                while Numero1 < Numero2 :
                    Numero2 = random.randint(1,98)
                print(f'{Conta+1}: {Numero1}-{Numero2} = ?') 
                while True:
                    try:
                        resposta = int(input('Resposta: ')) 
                    except :
                        print('#'*100)
                        print(f'{Numero1}-{Numero2} = ?'.center(100)) 
                        print(f'{"Por favor use só números [1|2|3|4|5|6|7|8|9|0]".center(100)}')
                        print('#'*100)
                    else:
                        if resposta == Numero1-Numero2:
                            print('Acertou')
                            print('*'*100)
                            print()
                            print()
                            break
                        else:
                            if resposta < Numero1-Numero2:
                                erros += 1
                                print()
                                print('#'*100)
                                print(f'{Numero1}-{Numero2} = ?'.center(100)) 
                                print('Mais'.center(100))
                                print('#'*100)
                            elif resposta > Numero1-Numero2:
                                erros += 1
                                print()
                                print('#'*100)
                                print(f'{Numero1}-{Numero2} = ?'.center(100)) 
                                print('Menos'.center(100))
                                print('#'*100)
    print(f'Você errou: {erros} vezes')
    
def SubtraçãoMédioNegativo():
    import random
    erros = 0
    print()
    print()
    print(F'{"Multiplicação".center(100)}')
    print('_'*100)
    print(F'{"Médio: O programa ira fazer 10 contas, contendo dezena e unidade (O resultado pode ser negativo)  ".center(100)}')
    print('_'*100)
    print()
    print()
    for Conta in range(10):
                print('*'*100)
                Numero1 = random.randint(1,99)
                Numero2 = random.randint(1,98)
                print(f'{Conta+1}: {Numero1}-{Numero2} = ?') 
                while True:
                    try:
                        resposta = int(input('Resposta: ')) 
                    except :
                        print('#'*100)
                        print(f'{Numero1}-{Numero2} = ?'.center(100)) 
                        print(f'{"Por favor use só números [1|2|3|4|5|6|7|8|9|0]".center(100)}')
                        print('#'*100)
                    else:
                        if resposta == Numero1-Numero2:
                            print('Acertou')
                            print('*'*100)
                            print()
                            print()
                            break
                        else:
                            if resposta < Numero1-Numero2:
                                erros += 1
                                print()
                                print('#'*100)
                                print(f'{Numero1}-{Numero2} = ?'.center(100)) 
                                print('Mais'.center(100))
                                print('#'*100)
                            elif resposta > Numero1-Numero2:
                                erros += 1
                                print()
                                print('#'*100)
                                print(f'{Numero1}-{Numero2} = ?'.center(100)) 
                                print('Menos'.center(100))
                                print('#'*100)
    print(f'Você errou: {erros} vezes')    

if __name__ == '__main__':
    SubtraçãoFacil()