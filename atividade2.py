# DEFINIR A IDADE DE UMA PESSOA E VERIFICAR SE ELA É MAIOR DE IDADE OU NÃO;

from datetime import datetime

data_atual = datetime.now()
data_formatada = data_atual.strftime("%d/%m/%Y")
data_nascimento_str = input("Informe aqui a sua data de nascimento:  ")
data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")
idade = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day))

if idade >= 18:
        print("Você é maior de idade.", end=" ")
else:
        print("Você é menor de idade.", end=" ")

print(f"E de acordo com a data de nascimento informada {data_nascimento_str},\nsua idade nesta data ({data_formatada}) é de {idade} anos.")




