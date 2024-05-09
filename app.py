import requests
import random
import os

# Definindo a URL da API que contém as palavras secretas
url = 'https://raw.githubusercontent.com/guilhermeonrails/api-imersao-ia/main/words.json'

# Limpando a tela antes de iniciar o jogo
os.system('clear'or'cls')

# Requisição HTTP para obter os dados da API
resposta = requests.get(url)

# Convertendo o JSON da resposta em um dicionário Python
data = resposta.json()

# Selecionando uma palavra aleatória da lista de palavras
valor_secreto = random.choice(data)

# Extraindo a palavra secreta e a dica do dicionário
palavra_secreta = valor_secreto['palavra']
dica = valor_secreto['dica']

# Exibindo a mensagem inicial do jogo
print(f'A palavra secreta possui {len(palavra_secreta)} letras --> Dica: {dica}')

# Solicitando o palpite do jogador
chute = input('Qual é a palavra secreta? ').lower()

# Verificando se o palpite está correto
if chute == palavra_secreta:
    print('Acerto mizeravi')
else:
    print(f'Eroooouu. a Resposta era {palavra_secreta}')
