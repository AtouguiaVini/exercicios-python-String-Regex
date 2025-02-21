# Renan está desenvolvendo um sistema que verifica se os links de sites parceiros começam com https:// e terminam com .com. Esses critérios são obrigatórios para que o site seja aprovado no cadastro. Ajude Renan a criar um programa que realize essa validação de forma automática.

# Como você escreveria um programa que peça ao usuário uma URL e informe se ela é válida ou inválida?

# Exemplo de Entrada:

# Digite a URL para validação: https://monitorrenan.com

# Saída esperada:

# URL válida!
import re
import os


os.system('cls') 

endereco_url = input('Digite a URL para validação: ')

def validacao_url(url):
    inicio_url = re.search(r'^https?:\/\/', url)
    final_url = re.search(r'(\.com)$',url)

    if inicio_url and final_url:
        return f'URL "{endereco_url}" é válida!'
    else:
        return f'URL "{endereco_url}" não é válida!'
         
avaliacao_final = validacao_url(endereco_url)
print(avaliacao_final)