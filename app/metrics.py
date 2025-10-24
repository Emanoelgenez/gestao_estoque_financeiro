import pandas as pd

def calculate_kpis(df: pd.DataFrame) -> dict:
    vendas_totais = df["vl_venda"].sum()
    custo_estoque = (df["estoque_atual"] * df["vl_custo"]).sum()
    lucro_liquido = df["lucro_liquido"].sum()
    margem_media = df["margem_percentual"].mean()
    itens_criticos = df[df["estoque_critico"]].shape[0]
    itens_negativos = df[df["lucro_negativo"]].shape[0]

    giro_estoque = vendas_totais / custo_estoque if custo_estoque else 0
    ticket_medio = vendas_totais / len(df) if len(df) else 0
    pct_lucro = (lucro_liquido / vendas_totais * 100) if vendas_totais else 0

    return {
        "Vendas Totais (R$)": vendas_totais,
        "Custo Total do Estoque (R$)": custo_estoque,
        "Lucro Líquido (R$)": lucro_liquido,
        "Margem Média (%)": margem_media,
        "Itens em Estoque Crítico": itens_criticos,
        "Itens com Prejuízo": itens_negativos,
        "Giro do Estoque (vezes)": giro_estoque,
        "Ticket Médio (R$)": ticket_medio,
        "Percentual Lucro/Faturamento (%)": pct_lucro,
    }
