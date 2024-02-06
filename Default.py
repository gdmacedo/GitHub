cBanko = 'DIO Bank '
cSlogan = 'More than a bank, your bank'
menu ='''         Seja bem-vindo ao DIO Bank!
[S] Sacar
[D] Depositar
[E] Consultar extrato
[Q] Sair

Selecione uma operação: '''

cOpcao = 'Início'
nQtd_Limite_Saque = 3
nValor_Limite_Saque = 500.0
nSaldo = 1500.0
nValor_Saque = nValor_Deposito = 0
lHistorico_Dpstos = []
lHistorico_Saques = []
lHistorico_Saldos = [nSaldo]

# Dando início ao menu
while True:
    print('-'*41)
    print(f'{cBanko:^41}'.upper())
    print(f'{cSlogan:^41}')
    print('-'*41)
    cOpcao = str(input(menu)).upper()
    print('-'*41)
    
    if cOpcao == 'S':
        # Lógica de realização do saque
        nValor_Saque = int(input('Valor do saque: R$ '))
        print()
        
        if nQtd_Limite_Saque > 0:
            if nValor_Saque <= nValor_Limite_Saque:
                if nValor_Saque <= nSaldo:
                    nQtd_Limite_Saque -= 1
                    nSaldo -= nValor_Saque
                    print('                SUCESSO!')
                    print(f'       Saque de R$ {nValor_Saque:.2f} realizado')
                    
                    # Lógica registro no extrato
                    lHistorico_Saques.append(nValor_Saque)
                       
                else:
                    print('                  ERRO!')
                    print('      Valor indisponível para saque')
            else:
                print('                  ERRO!')
                print('       Valor de saque indisponível')
        else:
            print('                  ERRO!')
            print('        Limite de saques atingido')
        
        print('\nRetornando ao menu...')
        

    elif cOpcao == 'D':
        # Lógica de realização do depósito
        nValor_Deposito = int(input('Valor do depósito: R$ '))
        if nValor_Deposito > 0:
            nSaldo += nValor_Deposito
            print('\n                SUCESSO!')
            print(f'      Depósito de R$ {nValor_Deposito:.2f} realizado')
        else:
            print('\nValor de depósito inválido')
            
        print('\nRetornando ao menu...')
        
        # Lógica registro no extrato
        lHistorico_Dpstos.append(nValor_Deposito)
    
    elif cOpcao == 'E':
        print(f'\n{cBanko:^41}'.upper())
        print(f'{cSlogan:^41}')
        print('-' * 41)
        print('\n            Extrato da conta\n')
        if len(lHistorico_Dpstos) == 0 and len(lHistorico_Saques) == 0:
            print('       Nenhuma operação realizada')
            print('-' * 41)
        else:
            print(f'nSaldo inicial: R$ {lHistorico_Saldos[0]:.2f}\n')
        if len(lHistorico_Dpstos) > 0:
            print('depósitos'.upper())
            for deposito in lHistorico_Dpstos:
                print(f'R$ {deposito:.2f}')
            print('-' * 41)
        if len(lHistorico_Saques) > 0:
            print('saques'.upper())
            for saque in lHistorico_Saques:
                print(f'R$ {saque:.2f}')
            print('-' * 41)
        print(f'nSaldo atual da conta: R$ {nSaldo:.2f}')
        print(f'Saques diários restantes: {nQtd_Limite_Saque}\n')
    
    elif cOpcao == 'Q':
        print('      O DIO Bank agradece a preferência!')
        print()
        break
    
    else:
        print('   Operação inválida. Tente novamente')
        print()
