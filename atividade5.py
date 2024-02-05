# IMPLEMENTE UM JOGO JOKENPO (PEDRA, PAPEL OU TESOURA).
# SERÁ O JOGADOR CONTRA A MÁQUINA. O CÓDIGO TEM QUE GERAR AS POSIÇÕES
# ALEATORIAMENTE E COMPARAR COM O QUE ESCOLHEMOS;

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Escolha sua jogada:
[0] PEDRA 
[1] PAPEL 
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))

print("\033[31mJAN...\033[m", end='')
sleep(0.5)
print("\033[34mKEN...\033[m", end='')
sleep(0.5)
print("\033[33mPÔO...\033[m\n", end='')
sleep(0.5)

print('=' * 45)
print(f'O computador jogou {itens[computador]}.')
print(f'Você jogou {itens[jogador]}')


if computador == 0:
    if jogador == 0:
        print('Jogada Empatada!')
        print('=' * 45)
    elif jogador == 1:
        print('Parabens! Você GANHOU esta jogada!')
        print('=' * 45)
        print('PAPEL ganha de PEDRA')
    elif jogador == 2:
        print('Que pena! Você PERDEU esta partida, TENTE OUTRA VEZ!')
        print('TESOURA perde de PEDRA')
        print('=' * 45)
    else:
        print('Jogada inválida. Escolha novamente.')
        print('=' * 45)

elif computador == 1:
    if jogador == 1:
        print('Jogada Empatada!')
        print('=' * 45)
    elif jogador == 2:
        print('Parabens! Você GANHOU esta jogada!')
        print('TESOURA ganha de PAPEL')
        print('=' * 45)
    elif jogador == 0:
        print('Que pena! Você PERDEU esta partida, TENTE OUTRA VEZ!')
        print('PEDRA perde de PAPEL')
        print('=' * 45)
    else:
        print('Jogada inválida. Escolha novamente.')
        print('=' * 45)

elif computador == 2:
    if jogador == 2:
        print('Jogada Empatada!')
        print('=' * 45)
    elif jogador == 0:
        print('Parabens! Você GANHOU esta jogada!')
        print('PEDRA ganha de TESOURA')
        print('=' * 45)
    elif jogador == 1:
        print('Que pena! Você PERDEU esta partida, TENTE OUTRA VEZ!')
        print('PAPEL perde de TESOURA')
        print('=' * 45)
    else:
        print('Jogada inválida. Escolha novamente.')
        print('=' * 45)
