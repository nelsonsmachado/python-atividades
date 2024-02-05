# GERE 10 NÚMEROS ALEATÓRIOS ENTRE 0 E 100; MOSTRE TODOS NA TELA (EM UMA ÚNICA LINHA);
# IDENTIFIQUE O MENOR E O MAIOR DELES;
from random import randint

numeros_aleatorios = (randint(1, 100, ), randint(1, 100, ), randint(1, 100, ),
                      randint(1, 100, ), randint(1, 100, ), randint(1, 100, ),
                      randint(1, 100, ), randint(1, 100, ),
                      randint(1, 100, ), randint(1, 100, ))

print('Os valores sorteados foram os números : ', end=" ")
for numeros in numeros_aleatorios:
    print(f" {numeros} ", end=' ')
print(f"\nO maior valor sorteado foi o número: {max(numeros_aleatorios)}")
print(f"O menor valor sorteado foi o número: {min(numeros_aleatorios)}\n")

print("=" * 70)
print("=" * 70)

numeros_aleatorios = [randint(0, 100) for numeros in range(10)]
print(f"\nOs valores sorteados foram os números: {numeros_aleatorios}")
print(f"O maior valor sorteado foi o número: {max(numeros_aleatorios)}")
print(f"O menor valor sorteado foi o número: {min(numeros_aleatorios)}")

