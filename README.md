# Chatbot Simples com Gemini

Este repositório contém o código para um chatbot simples utilizando a biblioteca google.generativeai. O modelo utilizado é o gemini-pro, que permite a geração de texto e interação por chat.

## Instalação

É necessário ter uma conta do Google e criar um projeto habilitado para a API Google Generative AI [Create API Key](https://aistudio.google.com/app/apikey).

**Instale as bibliotecas necessárias:**

```Bash
pip install google-generativeai python-dotenv
```

Crie um arquivo .env na raiz do projeto e adicione a sua chave de API:
`API_KEY=<sua_chave_de_API_generativeai>`

## Como rodar o código

Substitua `<sua_chave_de_API_generativeai>` no arquivo .env pela sua chave de API obtida no *Google AI Studio*.
Execute o script principal:
```Bash
python chatbot.py
```

Digite sua mensagem e pressione Enter para iniciar a conversa. O chatbot responderá e aguardará sua próxima mensagem.
Digite **fim** para encerrar a conversa.
Ao encerrar a conversa, será perguntado se deseja exportar o chat para um arquivo de texto. Digite **Y** para confirmar ou **N** para negar.

## Exportando o histórico da conversa

Após encerrar a conversa, você pode optar por exportar o histórico para um arquivo de texto. O arquivo será salvo no formato **Chat_[timestamp].txt** e conterá as mensagens trocadas entre você e o chatbot, identificando quem enviou cada mensagem.

# Linguagem Utilizada
![Static Badge](https://img.shields.io/badge/Python-v3.12-green?style=flat&logo=python&logoColor=green&color=green)
