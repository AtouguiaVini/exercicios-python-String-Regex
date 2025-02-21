# Imagine que você precisa criar uma funcionalidade para um jogo, onde os jogadores recebem dicas baseadas em partes específicas de uma palavra-chave. Sua missão é desenvolver um programa que extraia trechos importantes de qualquer palavra digitada.

# Escreva um programa que solicite ao usuário uma palavra e exiba as três primeiras e as três últimas letras.

# Exemplo de Entrada:

# Digite a palavra-chave: Misterioso

# Saída esperada:

# Primeiras: Mis
# Últimas: oso

import re

palavra_chave = input('Digite a palavra chave: ')
print('')

primeiras = palavra_chave[:3]
ultimas = palavra_chave[-3:]

print(primeiras)
print(ultimas)