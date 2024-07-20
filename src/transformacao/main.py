import pandas as pd
import sqlite3
from datetime import datetime


""" abs_json_file = os.path.abspath(json_file)
print(f'Caminho absoluto do arquivo JSON: {abs_json_file}') """

# Tentativa de leitura do arquivo JSON
df = pd.read_json('../data/data.jsonl', lines=True)

#adicionar a coluna source

df['_source']="https://lista.mercadolivre.com.br/tenis-corrida-masculino"

# Adicionar a coluna _data_coleta e horas

df['_data_coleta'] = datetime.now()

#Tratar os valore nulos e colunas numericas e de texto

df['old_price_reais'] = df['old_price_reais'].fillna(0).astype(float)
df['old_price_centavos'] = df['old_price_centavos'].fillna(0).astype(float)
df['new_price_reais'] = df['new_price_reais'].fillna(0).astype(float)
df['new_price_centavos'] = df['new_price_centavos'].fillna(0).astype(float)
df['reviews_rating_number'] = df['reviews_rating_number'].fillna(0).astype(float)

pd.options.display.max_columns = None

# Remover os parênteses das colunas `reviews_amount`
df['reviews_amount'] = df['reviews_amount'].str.replace('[\(\)]', '', regex=True)
df['reviews_amount'] = df['reviews_amount'].fillna(0).astype(int)

# Tratar os preços como floats e calcular os valores totais
df['old_price'] = df['old_price_reais'] + df['old_price_centavos'] / 100
df['new_price'] = df['new_price_reais'] + df['new_price_centavos'] / 100

# Remover as colunas antigas de preços
df.drop(columns=['old_price_reais', 'old_price_centavos', 'new_price_reais', 'new_price_centavos'], inplace=True)

# Conectar ao banco de dados SQLite (ou criar um novo)
conn = sqlite3.connect('../data/quotes.db')

# Salvar o DataFrame no banco de dados SQLite
df.to_sql('mercadolivre_items', conn, if_exists='replace', index=False)

# Fechar a conexão com o banco de dados
conn.close()

print(df.head())