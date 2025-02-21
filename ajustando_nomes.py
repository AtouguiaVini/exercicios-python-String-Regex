# Victor trabalha em um sistema de e-commerce e precisa organizar os nomes dos produtos que estão sendo cadastrados pelos lojistas. Esses nomes geralmente vêm com letras misturadas entre maiúsculas e minúsculas, além de espaços desnecessários no início e no final.

# Ajude Victor a criar um programa que receba um nome de produto e o padronize, deixando todas as letras minúsculas e removendo os espaços extras.

# Exemplo de Entrada:

# Digite o nome do produto: ChocoLAte Branco

# Saída esperada:

# chocolate branco

import re

def conversor_de_txt(txt: str) -> str:
    reduzir_letras = txt.lower()
    texto_sem_espacos = re.sub(r'\s{2,}',' ',reduzir_letras)
    return texto_sem_espacos.strip()

nome_produto = str(input('Digite o nome do produto: '))

resultado = conversor_de_txt(nome_produto)

print(resultado)