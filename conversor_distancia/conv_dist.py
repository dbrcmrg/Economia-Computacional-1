"""
Progra conv_dist
Descrição: Este programa lê um valor em metros e o converte para milímetros.
Autor: Débora Camargo
Data: 06/08/2024
Versão: 0.0.1
"""

# Alocação de memória
metros: float =  0
milímetros: float = 0

# Entrada de dados

metros = float(input("Digite a distância em metros: "))

# Processamento de dados
milímetros = 1000 * metros

# Saída de dados
print(f'\nA distância em milímetros é igual a {milímetros}')
