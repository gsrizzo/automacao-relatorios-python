import pandas as pd

def main():
    print("Lendo arquivo CSV...")

    caminho_csv = "../data_raw/vendas.csv"

    try:
        dados = pd.read_csv(caminho_csv, sep=";")
    except FileNotFoundError:
        print("Arquivo CSV não encontrado.")
        return
           
    dados["total"] = dados["quantidade"] * dados["preco"]

    print("\n==========RELATÓRIO DE VENDAS==========")
    print(dados)

    #faturamento total
    faturamento_total = dados["total"].sum()
    print(f"\nO faturamento total foi de R${faturamento_total:.2f}")

    #faturamento por produto
    faturamento_produto = dados.groupby("produto")["total"].sum()
    print("\nFaturamento por produto:")
    for produto, valor in faturamento_produto.items():
        print(f"- {produto}: R${valor:.2f}")
        
    # exportar relatório
    faturamento_produto.to_csv("../data_output/relatorio_produtos.csv")

    #ticket medio
    ticket_medio = faturamento_total / len(dados)
    print(f"\nTicket médio: {ticket_medio:.2f}")

if __name__ == "__main__":
    main()



