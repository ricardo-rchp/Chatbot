import google.generativeai as genai
import time
from dotenv import load_dotenv
import os

load_dotenv()

my_api_key = os.getenv('API_KEY')

GOOGLE_API_KEY = my_api_key
genai.configure(api_key=GOOGLE_API_KEY)

# for modelo in genai.list_models():
#   if 'generateContent' in modelo.supported_generation_methods:
#     print(modelo.name)

model = genai.GenerativeModel('gemini-pro')

# response = model.generate_content("Cite funções dentro da biblioteca google.generativeai")
# print(response.text)

chat = model.start_chat(history=[])
prompt = input('Digite sua mensagem: ')

while prompt != 'fim':
  response = chat.send_message(prompt)
  print('\nResposta: '+response.text+'\n')
  prompt = input('Digite sua mensagem: ')

while True:
    resposta = input('Deseja Exportar o chat para um arquivo .txt? [Y] para Sim [N] para não: ').lower()
    if resposta == 'y':
        nome_arquivo = f'Chat_{int(time.time())}.txt'
        with open(nome_arquivo,'w') as arquivo:
            for parte in chat.history:
                arquivo.write(parte.role+': '+parte.parts[0].text+'\n\n')
        break
    elif resposta == 'n':
        break
    else:
        print('Digite Y ou N: ')
