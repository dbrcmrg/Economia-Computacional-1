"""
Programa: busca_sequencial.py
Descrição: Este programa busca um valor em uma base de dados.
Autor: Débora Camargo Ferreira
Versão: 0.0.2
Correções realizadas: informação mais intuitiva ao usuário da posição em que seu CPF foi encontrado.
Data: 22/08/2024
"""

## Alocação de memória
lista = []
achou = False
posicao = 0
cpf = 0

# Leitura da base de dados de CPF
base = [11,5,2,87,31]
lista = base

# leitura de dados
cpf = int(input("Digite o valor a procurar:"))

# Processamento de dados
while posicao < len(lista):
    if lista[posicao] == cpf:
        achou = True
        break # interrompe a execução
    posicao+=1 # é a mesma coisa que posicao = posicao + 1

# Saída de dados
if achou:
    print(f'\nO valor {cpf} foi achado na posição {posicao + 1}.')
else:
    print(f'\nO valor {cpf} não foi achado.')