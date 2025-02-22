# Carlos é analista de dados em um hospital e está organizando informações de pacientes em um banco de dados. Ele recebe os dados no formato: "PrimeiroNome Sobrenome - Ano". Por exemplo, “Monalisa Silva - 1994”.

# Carlos precisa de um programa que leia as informações, capture cada parte separadamente, nome, o sobrenome e o ano de nascimento para preencher os campos do sistema.

# Ajude Carlos criando um programa que solicite o nome completo e o ano de nascimento de um paciente e exiba-os separadamente.

# Exemplo de Entrada:

# Digite o nome completo e o ano de nascimento do paciente: Ana Silva - 1990

# Saída esperada:

# Primeiro Nome: Ana
# Sobrenome: Silva
# Ano de Nascimento: 1990
import re

nomes = [
    "Lucas de Almeida - 1995",
    "Mariana Souza - 1987",
    "João Pedro de Lima - 2003",
    "Fernanda Costa da Silva - 1990",
    "Rafael de Oliveira Santos - 1995",
    "Camila da Rocha - 1982",
    "Camila Vienna - 1987",
    "Gustavo Nogueira de Pereira - 2001",
    "Beatriz Mendes - 1997",
    "Eduardo Teixeira Ramos - 1985",
    "Larissa da Fernandes - 2000",
    "Thiago Moreira Duarte - 1993",
    "Aline de Castro - 1989",
    "Bruno Henrique Vasconcelos - 1995",
    "Vanessa Martins da Costa - 2004",
    "Felipe Cardoso de Barbosa - 1998"
]


regex = r'^(\w+)\s(.+)\s-\s(\d{4})'

lista_nomes = []
lista_sobrenome = []
lista_ano = []

for nome in nomes:
    analise = re.match(regex, nome)
    if analise:
        lista_nomes.append(analise.group(1))
        lista_sobrenome.append(analise.group(2))
        lista_ano.append(analise.group(3))


print(lista_nomes)
print(lista_sobrenome)
print(lista_ano)

def pesquisar_nomes(nome_procurado):
    resultados = []
    for posicao, nome in enumerate(lista_nomes):
        if nome == nome_procurado:
            resultados.append({
                'Nome': lista_nomes[posicao],
                'Sobrenome': lista_sobrenome[posicao],
                'Nascimento': lista_ano[posicao]
            })
    return resultados if resultados else 'Nome não encontrado.'


nome_digitado = input('Digite um nome procurado: ')
resultado_final = pesquisar_nomes(nome_digitado)

if isinstance(resultado_final,list):
    for i, res in enumerate(resultado_final, start= 1):
        print(f'Resuntado: {i}: {res}')
else:
    print(resultado_final)


