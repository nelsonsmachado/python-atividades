# LEIA UM NÚMERO ATÉ QUE O USUÁRIO DIGITE 10;

numeros_digitados = []

while True:
    numero = input("Digite um número inteiro qualquer ou '10' para sair do programa: ")

    if numero == '10':
        print("Programa encerrado. Obrigado e volte sempre!")
        break

    if numero in numeros_digitados:
        print("Número já informado anteriormente. Por favor, informe outro valor.")
    else:
        numeros_digitados.append(numero)

print("Números digitados:", numeros_digitados)
