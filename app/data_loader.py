import pandas as pd
import os


def load_and_enrich_data(path: str = "data/df_estoque_st.csv") -> pd.DataFrame:
    """Carrega, limpa e enriquece os dados de estoque e rentabilidade."""
    full_path = os.path.join(os.path.dirname(__file__), "..", path)
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {full_path}")

    df = pd.read_csv(full_path, encoding="utf-8")

    # Normalizar colunas
    df.columns = [
        str(col).strip().lower()
        .replace("ç", "c").replace("ã", "a").replace("é", "e").replace(" ", "_")
        for col in df.columns
    ]

    # Ajustar tipos
    df["data_entrada"] = pd.to_datetime(df["data_entrada"], errors="coerce")
    numeric_cols = ["estoque_atual", "vl_custo", "vl_venda", "lucro_bruto", "lucro_liquido", "margem_percentual"]
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

    # Limpeza
    df = df.dropna(subset=numeric_cols + ["fornecedor", "descricao", "data_entrada"])

    # Enriquecimento
    df["valor_total_estoque"] = df["estoque_atual"] * df["vl_custo"]
    df["mes"] = df["data_entrada"].dt.to_period("M").astype(str)
    df["estoque_critico"] = df["estoque_atual"] < 50
    df["lucro_negativo"] = df["lucro_liquido"] < 0

    return df
