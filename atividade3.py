# CONSTRUA A TABUADA DE UM NÚMERO. (EX: 1X1=1, 1X2=2,...,1X10=10);

while True:
    numeral = int(input("\033[32mDigite aqui o numeral de sua tubuada ou '0' para sair do programa: \033[m"))
    print('=' * 65)
    if numeral == 0:
        break
    for count in range(1, 11):
        print(f'\033[34m{numeral} X {count} = {numeral*count}\033[m')
    print('=' * 65)
print('\033[33mPrograma Tabuada encerrado. Obrigado e até a próxima vez!\033[m')
print('=' * 65)