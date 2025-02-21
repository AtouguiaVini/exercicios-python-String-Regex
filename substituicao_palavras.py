# Nathalia é uma escritora que está revisando um texto para publicação. Durante o processo, ela percebeu que usou a palavra "bom" repetidamente, quando queria expressar algo mais forte, como "ótimo". Para economizar tempo, Nathalia quer substituir automaticamente todas as ocorrências da palavra "bom" por "ótimo" no texto.

# Ajude Nathalia a criar um programa que solicite um texto, a palavra que será substituída e a nova palavra. O programa deve exibir o texto com as alterações aplicadas.

# Exemplo de Entrada:

# Digite o texto a ser revisado: O dia está bom, tudo está bom.`
# Qual palavra deseja substituir? bom
# Qual a nova palavra? ótimo
# 
# Saída esperada:

# O dia está ótimo, tudo está ótimo

import re

print('Editor de texto\n')

texto = input('Insira o texto: ')
palavra_substituida = input('Insira a palara que será substituida: ' )
nova_palavra = input('Insira a nova palavra: ' )
print()

substituicao_texto = re.sub(rf'\b{palavra_substituida}\b', nova_palavra, texto)

print(f'Resultado: "{substituicao_texto}"')

