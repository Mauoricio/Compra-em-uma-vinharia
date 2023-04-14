print("Bem-vindo ao cadastro de clientes!")

nome = input("Por favor, digite seu nome completo: ")
idade = int(input("Digite sua idade: "))
endereco = input("Digite seu endereço: ")
endereco_entrega = input("Digite o endereço de entrega: ")

if idade < 18:
    print("Desculpe, o comprador deve ser maior de idade.")
    print("O processo de compra foi encerrado.")
else:
    print("Obrigado pelo cadastro!")
    print("Nome: ", nome)
    print("Idade: ", idade)
    print("Endereço: ", endereco)
    print("Endereço de entrega: ", endereco_entrega)

    catalogo = {
        "Vinho 1": 50.00,
        "Vinho 2": 70.00,
        "Vinho 3": 60.00,
        "Vinho 4": 80.00,
        "Vinho 5": 65.00
    }

    valor_total = 0.0
    produtos_comprados = 0
    for vinho, preco in catalogo.items():
        qtd = int(input("Digite a quantidade de {0} que deseja comprar: ".format(vinho)))
        valor_total += qtd * preco
        produtos_comprados += qtd

    if valor_total < 100:
        print("Desculpe, o valor mínimo para compra é de R$ 100,00.")
    else:
        if valor_total > 200:
            frete = 0
            print("Parabéns! Frete Grátis!")
        else:
            frete = 20
            print("O valor do frete é R$ 20,00.")

        valor_total += frete
        print("Você comprou {0} produtos, com valor total de R$ {1:.2f}".format(produtos_comprados, valor_total))
        print("O pedido será entregue no endereço {0}.".format(endereco_entrega))
        print("Obrigado por comprar conosco!")
