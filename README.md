# Automação de Relatórios de Vendas

Projeto em Python que automatiza a leitura e análise de dados de vendas a partir de arquivos CSV, gerando métricas de faturamento automaticamente — um processo que normalmente seria feito manualmente em planilhas.

## Funcionalidades

- Leitura de arquivos CSV
- Cálculo de faturamento total
- Faturamento por produto
- Cálculo de ticket médio
- Geração automática de relatório CSV

## Exemplo de saída

```
==========RELATÓRIO DE VENDAS==========
         data    produto  quantidade  preco  total
0  01/05/2024  Produto A           3     20     60
1  01/05/2024  Produto B           1     50     50
2  02/05/2024  Produto A           2     20     40
3  03/05/2024  Produto C           5     10     50

O faturamento total foi de R$200.00

Faturamento por produto:
- Produto A: R$100.00
- Produto B: R$50.00
- Produto C: R$50.00

Ticket médio: R$50.00
```

## Tecnologias utilizadas

- Python
- Pandas

## Estrutura do projeto

```
automacao-relatorios-python/
│
├── data_raw/       # dados de entrada (CSV)
├── data_output/    # relatórios gerados
├── docs/
├── src/
│   └── main.py
```

## Como executar

```bash
pip install pandas
cd src
python main.py
```