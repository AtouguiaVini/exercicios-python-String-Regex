# Sara trabalha no setor de atendimento de uma empresa e precisa verificar rapidamente se os clientes estão digitando seus números de CPF no formato correto antes de registrar os dados no sistema.

# O formato esperado do CPF é: três blocos de 3 dígitos separados por pontos (.), seguidos por um bloco de 2 dígitos separados por um traço (-).

# Ajude Sara a criar um programa que solicite o CPF de um cliente e verifica se ele está no formato correto.

# Exemplo de Entrada:

# Digite o CPF no formato XXX.XXX.XXX-XX: 123.456.789-00

# Saída esperada:

# O CPF está no formato correto.

import re

cpf = input('Digite o CPF no formato XXX.XXX.XXX-XX: ')
validador_regex = r'\d{3}\.\d{3}\.\d{3}\-\d{2}'

if re.search(validador_regex,cpf):
    print('O CPF está no formato correto')
else:
    print('O CPF não está no formato correto')