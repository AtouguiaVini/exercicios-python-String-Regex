# Você trabalha em uma biblioteca e está organizando os títulos de livros no sistema. Você precisa identificar todos os títulos que possuem palavras iniciadas por uma determinada letra, para criar coleções temáticas baseadas em letras específicas. Por exemplo, você poderia usar isso para agrupar livros com palavras que começam com a mesma letra, ajudando na organização ou em campanhas como “Livros com A para você!”.

# Como você criaria um programa que solicita um texto e uma letra inicial e retorna todas as palavras do texto que começam com essa letra?

# Exemplo de Entrada:

# Digite o título dos livro: As Aventuras de Alice no País das Maravilhas Digite a letra inicial para pesquisa: A

# Saída esperada:

# ["As", "Aventuras", "Alice"]

import re
import os

os.system('cls')

biblioteca = [
    "4 Horas para o Corpo",
    "Dom Casmurro",
    "Os Três Mosqueteiros",
    "Crime e Castigo",
    "1984",
    "2.001: Uma Odisseia no Espaço",
    "O Nome da Rosa",
    "Jane Eyre",
    "3 Sombras",
    "Noite na Taverna",
    "5 Dias no Umbral",
    "As Aventuras de Sherlock Holmes",
    "1Q84",
    "Coração das Trevas",
    "O Senhor dos Anéis",
    "Jogador Número 1",
    "Grande Sertão: Veredas",
    "O Estrangeiro",
    "Xadrez, de Stefan Zweig",
    "A Revolução dos Bichos",
    "O Conde de Monte Cristo",
    "Orgulho e Preconceito",
    "Lolita",
    "Frankenstein",
    "5 Minutos",
    "Harry Potter e a Pedra Filosofal",
    "A Cor Púrpura",
    "Memórias Póstumas de Brás Cubas",
    "Drácula",
    "Fahrenheit 451",
    "Cem Anos de Solidão",
    "A Divina Comédia",
    "Zorba, o Grego",
    "2 Irmãos",
    "1 Página de Cada Vez",
    "Ulysses",
    "Romeu e Julieta",
    "Laranja Mecânica",
    "Inferno",
    "Wuthering Heights",
    "Admirável Mundo Novo",
    "E o Vento Levou",
    "Ilíada",
    "Kafka à Beira-Mar",
    "História da Riqueza do Homem",
    "Percy Jackson e o Ladrão de Raios",
    "3 Desejos",
    "Ensaio Sobre a Cegueira",
    "Guerra e Paz",
    "Os Miseráveis",
    "10 Negrinhos",
    "Quincas Borba",
    "7 Habits of Highly Effective People",
    "A Metamorfose",
    "4 Estações",
    "Vidas Secas",
    "Y: O Último Homem",
    "O Hobbit",
    "O Apanhador no Campo de Centeio"
]
 
alfanumerico = input('Informe um alfanumérico para pesquisa: ')

while len(alfanumerico) > 1 or re.match(r'^\s+',alfanumerico):
    print('Pesquisa inválida! Por favor, informe apenas um alfanumérico.')
    alfanumerico = input('Informe um alfanumérico para pesquisa: ')

verificacao_regex = rf'^{alfanumerico}'

resultado = [livro for livro in biblioteca if re.search(verificacao_regex, livro, re.IGNORECASE)]

if resultado:
    print(f'Lista de livros disponíveis com iniciais com o alfanumérico {alfanumerico}:')
    resultado_ordem = sorted(resultado)
    print(resultado_ordem)
else:
    print(f'Não foi encontrado livros com o alfanumérico: {alfanumerico}')


