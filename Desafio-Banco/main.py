print('=-=' * 10)
print(' '* 8 + 'Sejá bem vindo')
print('=-='* 10)
menu ='''Escolha uma das opções:
   [1] Depositar
   [2] Sacar
   [3] Extrato
   [4] Sair
'''

saldo = 0
limite = 500
extrato = ''
numero_saques =0
limite_saques = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input('Informe um valor para Saldo : '))
        if valor > 0:
            saldo += valor
            extrato += 'Depósito: R$ {:.2f}\n'.format(valor)

        else:
            print('Operação falhou!O valor informado é inválido')

    elif opcao == 2:
        valor = float(input('Informe o valor de saque: '))

        excedeu_saldo = valor > valor

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print('Operação falhou! Não tem saldo suficiente.')

        elif excedeu_limite:
            print('Operação falhou! O valor de saque excede o limite.')

        elif excedeu_saques:
            print('Operação falhou! Número máximo de saque excedido.')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1

        else:
            print('Operação falhou!O valor informado é inválido. ')

    elif opcao == 3:
        print('=' *15 +' EXTRATO '+ '='* 15)
        print('Não foram realizados movimentações.'if not extrato else extrato)
        print(f'\nSaldo: R${saldo:.2f}')
        print('='*40)

    elif opcao == 4:
        print('=-='*12)
        print('Obrigado por utlizar nossos serviços')
        print('=-=' * 12)
        break
    else:
        print('Operação inválida ,por favor selecione novamente a operação desejada.')

