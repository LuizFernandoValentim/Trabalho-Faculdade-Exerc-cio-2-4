print('Bem-vindo a Pizzaria do Luiz Fernando Valentim (RU: 4173542)')

print('-----------------------Cardápio----------------------')
print('| Código | Descrição   | Pizza Média | Pizza Grande |')
print('|   21   | Napolitana  |    R$ 20,00 |     R$ 26,00 |')
print('|   22   | Margherita  |    R$ 20,00 |     R$ 26,00 |')
print('|   23   | Calabresa   |    R$ 25,00 |     R$ 32,50 |')
print('|   24   | Toscana     |    R$ 30,00 |     R$ 39,00 |')
print('|   25   | Portuguesa  |    R$ 30,00 |     R$ 39,00 |')
print('-----------------------------------------------------')

subtotalfinal = 0
# Inicio do laço de repetição para verificação das informações que o cliente escolheu
while True:
    tamanhopizza = input('Qual tamanho da pizza que deseja (M/G): ')

    if (tamanhopizza == 'M'):
        pass

    elif (tamanhopizza == 'G'):
        pass

    else:
        print('Código inválido. Tente novamente!')

    while True:
        subtotal = 0
        codproduto = (input('Entre com o código do sabor desejado: '))

        if (codproduto == '21'):
            print('Você pediu uma pizza sabor Napolitana')
            subtotal += 20

        elif (codproduto == '22'):
            print('Você pediu uma pizza sabor Margherita')
            subtotal += 20

        elif (codproduto == '23'):
            print('Você pediu uma pizza sabor Calabresa')
            subtotal += 25

        elif (codproduto == '24'):
            print('Você pediu uma pizza sabor Toscana')
            subtotal += 30

        elif (codproduto == '25'):
            print('Você pediu uma pizza sabor Portuguesa')
            subtotal += 30

        else:
            print('Código inválido. Tente novamente!')
            continue

        if (tamanhopizza == 'G'):
            subtotal = subtotal + (subtotal * 30/100)

        else:
            pass

        subtotalfinal += subtotal
# Fim do laço de repetição para verificação das informações que o cliente escolheu

# Inicio do processo final de interação com cliente e laço de repetição para vereficar se o cliente que ralizar
#um novo pedido ou encerrar a conta
        while True:
            resposta = input('Deseja pedir mais alguma coisa? \n1 - Sim  \n2 - Não\n')

            if (resposta == '1') or (resposta == 'Sim'):
                break

            elif (resposta == '2') or (resposta == 'Não'):
                print('O total a ser pago é de: {:.2f}'.format(subtotalfinal))
                exit()

