def MenuMultiplicação():
    print()
    print()
    print(F'\33[34m{"Multiplicação".center(100)}\33[m')
    print('\33[45m \33[m'*100)
    print(F'\33[36m{"Escolha uma dificuldade".center(100)}\33[m')
    print('\33[45m \33[m'*100)

def MenuMultiplicaçãoEscolha():
    print(f'\33[32m[1]: Fáci\33[m')
    print(f'\33[35m[2]: Dificil\33[m')
    print(f'\33[31m[3]: Voltar ao Menu Principal\33[m ')
    print('\33[45m \33[m'*100)


def MultiplicaçãoFacil():
    import random
    erros = 0
    print()
    print()
    print(F'\33[34m{"Multiplicação".center(100)}\33[m')
    print('\33[45m \33[m'*100)
    print(F'\33[36m{"Facil: O programa ira fazer 10 contas todas contendo só uma unidade".center(100)}\33[m')
    print('\33[45m \33[m'*100)
    print()
    print()
    for Conta in range(10):
            print('\33[45m \33[m'*100)
            Numero1 = random.randint(1,9)
            Numero2 = random.randint(1,9)
            print(f'\33[36m{Conta+1}:\33[m {Numero1}\33[34mX\33[m{Numero2} \33[36m=\33[m \33[31m?\33[m')   
            while True:
                try:
                    resposta = int(input('Resposta: ')) 
                except :
                    print('\33[41m \33[m'*100)
                    print(f'\33[31m{Numero1}X{Numero2} = ?\33[m'.center(100)) 
                    print(f'\33[31m{"Por favor use só números [1|2|3|4|5|6|7|8|9|0]".center(100)}\33[m')
                    print('\33[41m \33[m'*100)
                else:
                    if resposta == Numero1*Numero2:
                        print('\33[32mAcertou\33[m')
                        print('\33[42m \33[m'*100)
                        print()
                        print()
                        break
                    else:
                        if resposta < Numero1*Numero2:
                            erros += 1
                            print()
                            print('\33[43m \33[m'*100)
                            print(f'\33[33m{Numero1}X{Numero2} = ?\33[m'.center(100)) 
                            print('\33[33mMais +\33[m'.center(100))
                            print('\33[43m \33[m'*100)
                        elif resposta > Numero1*Numero2:
                            erros += 1
                            print()
                            print('\33[43m \33[m'*100)
                            print(f'\33[33m{Numero1}X{Numero2} = ?\33[m'.center(100)) 
                            print('\33[33mMenos -\33[m'.center(100))
                            print('\33[43m \33[m'*100)
    print(f'Você errou: \33[31m{erros}\33[m vezes')

def MultiplicaçãoDificil():
    import random
    erros = 0
    print()
    print()
    print(F'\33[34m{"Multiplicação".center(100)}\33[m')
    print('\33[45m \33[m'*100)
    print(F'\33[36m{"Dificil: O programa ira fazer 10 contas, contendo dezena e unidade".center(100)}\33[m')
    print('\33[45m \33[m'*100)
    print()
    print()
    for Conta in range(10):
            print('\33[45m \33[m'*100)
            Numero1 = random.randint(1,99)
            Numero2 = random.randint(1,99)
            print(f'\33[36m{Conta+1}:\33[m {Numero1}\33[34mX\33[m{Numero2} \33[36m=\33[m \33[31m?\33[m') 
            while True:
                try:
                    resposta = int(input('Resposta: ')) 
                except :
                    print('\33[41m \33[m'*100)
                    print(f'\33[31m{Numero1}X{Numero2} = ?\33[m'.center(100)) 
                    print(f'\33[31m{"Por favor use só números [1|2|3|4|5|6|7|8|9|0]".center(100)}\33[m')
                    print('\33[41m \33[m'*100)
                else:
                    if resposta == Numero1*Numero2:
                        print('\33[32mAcertou\33[m')
                        print('\33[42m \33[m'*100)
                        print()
                        print()
                        break
                    else:
                        if resposta < Numero1*Numero2:
                            erros += 1
                            print()
                            print('\33[43m \33[m'*100)
                            print(f'\33[33m{Numero1}X{Numero2} = ?\33[m'.center(100)) 
                            print('\33[33mMais +\33[m'.center(100))
                            print('\33[43m \33[m'*100)
                        elif resposta > Numero1*Numero2:
                            erros += 1
                            print()
                            print('\33[43m \33[m'*100)
                            print(f'\33[33m{Numero1}X{Numero2} = ?\33[m'.center(100)) 
                            print('\33[33mMenos -\33[m'.center(100))
                            print('\33[43m \33[m'*100)
    print(f'Você errou: \33[31m{erros}\33[m vezes')
    
if __name__ == "__main__":
    MultiplicaçãoDificil()