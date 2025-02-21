import os
os.system('cls')


teste = 'sou um texto'
print(teste[1:6])
print(teste[-1])
print(len(teste))
print()

# Método IN - verifica se existe um trecho específico em uma string
print('Método IN')
print('um' in teste) 
print('zero' in teste)
print()

# Método startswith() - Verifica inicio da string
print('Método startswith()')
print(teste.startswith('sou'))
print(teste.startswith('SOU'))
print()
# Método endswith() - Verifica final da string
print('Método endswith()')
print(teste.endswith('xto'))
print(teste.endswith('xtO'))
print()

# Expressões regulares (Regex)
# Caracteres Literais
import re

