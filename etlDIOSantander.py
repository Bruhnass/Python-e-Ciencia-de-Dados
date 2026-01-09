# Explorando IA Generativa com ETL em Python

# Primeiro: importar a biblioteca pandas para extrair os dados.
# Segundo: fazer upload de arquivo .csv com dados de clientes fictícios e converter para uma lista de dicionários.

import pandas as pd

users = pd.read_csv('SDW2023.csv').to_dict(orient='records')

# Insere um atributo novo para a etapa de Transformação
for user in users:
    user['news'] = []


# Transformação: gerar mensagem de marketing personalizada para cada cliente utilizando a IA Generativa GPT
# Para isso, instalar o openai.

!pip install openai

openai_api_key = 'inclua-APIkey-aqui' # inserir a sua chave de API do Chat GPT

import openai

openai.api_key = openai_api_key

def generate_ai_news(user):
  completion = openai.chat.completions.create(
    model="gpt-5.2",
    messages=[
      {
          "role": "system",
          "content": "Você é um gerente com conhecimento em marketing bancário."
      },
      {
          "role": "user",
          "content": f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos no planejamento financeiro, em no máximo 100 caracteres"
      }
    ]
  )
  return completion.choices[0].message.content.strip('\"')

for user in users:
  news = generate_ai_news(user)
  print(news)
  user['news'].append({
      "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
      "description": news
  })

# Simulação da etapa de Carregamento com o salvamento dos dados manipulados em arquivo csv.

df = pd.DataFrame(users)

nome_arquivo = 'SDW2023.csv'
df.to_csv(nome_arquivo, index=False, encoding='utf-8')

print(f"Dados salvos com sucesso em '{nome_arquivo}'")