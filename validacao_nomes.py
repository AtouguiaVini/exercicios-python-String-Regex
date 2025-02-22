# Lorena trabalha no setor de cadastros de uma empresa e precisa garantir que os nomes inseridos pelos clientes estejam no formato correto. O padrão esperado é que os nomes comecem com uma letra maiúscula e contenham apenas letras (sem números ou caracteres especiais). Para facilitar o trabalho, ela quer um programa que valide automaticamente os nomes fornecidos.

# Ajude a Lorena criando um programa que solicite um nome ao usuário e verifique se ele atende às regras.

# Exemplo de Entrada:

# Digite o nome do cliente para validação: maria123

# Saída esperada:

# Nome inválido!

import re

nome = input('Digite o nome do cliente para validação: ')
validador_nome = r'\b[a-z]|[^a-zA-Z ]| {2,}'

if re.search(validador_nome,nome):
    print(f'O nome {nome} é um nome inválido!')
else:
    print(f'O nome {nome} é um nome válido!')