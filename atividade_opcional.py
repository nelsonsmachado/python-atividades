# PARA CADA PRODUTO INFORMADO (NOME, PREÇO E QUANTIDADE), ESCREVA O NOME DO PRODUTO COMPRADO E O VALOR TOTAL A
# SER PAGO, CONSIDERANDO QUE SÃO OFERECIDOS DESCONTOS PELO NÚMERO DE UNIDADES COMPRADAS, SEGUNDO A TABELA ABAIXO:
# A. ATÉ 10 UNIDADES: VALOR TOTAL   -  B. DE 11 A 20 UNIDADES: 10% DE DESCONTO  -
# C. DE 21 A 50 UNIDADES: 20% DE    -  D. ACIMA DE 50 UNIDADES: 25% DE DESCONTO 3);

def calcular_valor_total(nome, preco, quantidade):
    valor_bruto = preco * quantidade

    if quantidade <= 10:
        abatimento = 0
    elif quantidade <= 20:
        abatimento = 0.1
    elif quantidade <= 50:
        abatimento = 0.2
    else:
        abatimento = 0.25

    valor_com_desconto = valor_bruto * (1 - abatimento)

    return nome, valor_bruto, abatimento, valor_com_desconto


produto_nome = input("Digite o nome do produto: ")
produto_preco = float(input("Digite o preço do produto: "))
produto_quantidade = int(input("Digite a quantidade comprada: "))

nome_produto, valor_total, desconto, valor_a_pagar = calcular_valor_total(produto_nome, produto_preco,
                                                                          produto_quantidade)
desconto_reais = valor_total - valor_a_pagar

print(f"Produto: {nome_produto}")
print(f"Valor total sem desconto: R${valor_total:.2f}")
print(f"Desconto aplicado: {desconto * 100:.2f}%")
print(f"Valor a ser pago com desconto: R${valor_a_pagar:.2f}")
print(f'Você economizou nesta compra R$ {desconto_reais:.2f}')
print('Obrigado e volte sempre!')
