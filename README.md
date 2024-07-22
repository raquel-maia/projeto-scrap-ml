# Projeto Scraping Mercado Livre 🦖

 Scraping de Tênis Esportivos do Mercado Livre

## Descrição do Projeto 📊

Este projeto realiza a extração de dados dos principais tênis esportivos disponíveis no Mercado Livre, transformando esses dados em informações úteis através de KPIs (Key Performance Indicators) e exibindo-os em um dashboard interativo usando Streamlit.

Além disso, ele abrange várias etapas do processo de engenharia de dados, incluindo a coleta, transformação e visualização dos dados. Aqui estão as partes específicas da engenharia de dados que o projeto envolve:

1. **Coleta de Dados (Data Ingestion):**
   - **Ferramenta Utilizada:** Scrapy
   - **Descrição:** Coleta de dados de tênis esportivos no Mercado Livre através da instalação do scraping (install scrapy). 

2. **Transformação de Dados (Data Transformation):**
   - **Ferramenta Utilizada:** Pandas
   - **Descrição:** Transformação e análise dos dados coletados para gerar KPIs e preparar os dados para visualização.

3. **Visualização de Dados (Data Visualization):**
   - **Ferramenta Utilizada:** Streamlit
   - **Descrição:** Criação de um dashboard interativo para visualizar os KPIs e outras métricas relevantes de maneira clara e acessível.

## Siga o passo a passo para rodar o projeto:

- Como rodar o web scraping?

        🎯 ```bash
    scrapy crawl mercadolivre -o ../../data/data.jsonl
    ```
- Como rodar o pandas?

        '''bash

        🎯 python transformacao/main.py
        ```
- Como rodar o streamlit 

        ```bash
        🎯 streamlit run dashboard/app.py 
        ```
## Veja o projeto Finalizado 🔍

![img](/src/scraping.png)