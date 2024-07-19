import pandas as pd
#import sqlite3
#import datetime


""" abs_json_file = os.path.abspath(json_file)
print(f'Caminho absoluto do arquivo JSON: {abs_json_file}') """

# Tentativa de leitura do arquivo JSON
df = pd.read_json('../data/data.jsonl', lines=True)

print(df)