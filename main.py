import streamlit as st
from datetime import datetime
from app.data_loader import load_and_enrich_data
from app.metrics import calculate_kpis
from app.utils import format_currency, get_stock_alert, add_spacing, insight_card
from app.visuals import (
    plot_lucro_fornecedor,
    plot_margem_top_produtos,
    plot_evolucao_mensal_lucro,
    plot_estoque_critico_donut,
    plot_lucro_negativo_por_produto,
    PALETTE,
)

st.set_page_config(page_title="Dashboard de Estoque e Rentabilidade", layout="wide", page_icon="📊")

@st.cache_data(ttl=3600, show_spinner="Carregando dados…")
def get_data():
    return load_and_enrich_data()

df = get_data()

# SIDEBAR
with st.sidebar:
    st.image("assets/logo.png", width=160)
    st.markdown("## Filtros")
    fornecedores = ["Todos"] + sorted(df["fornecedor"].unique().tolist())
    fornecedor_selecionado = st.multiselect("Fornecedores", fornecedores, default=["Todos"])
    if "Todos" in fornecedor_selecionado:
        fornecedor_selecionado = df["fornecedor"].unique()

    data_min, data_max = df["data_entrada"].min().date(), df["data_entrada"].max().date()
    data_inicio, data_fim = st.date_input("Período de Entrada", [data_min, data_max])
    top_n = st.slider("Top N (Produtos/Fornecedores)", 5, 20, 7)

df_filtrado = df[
    (df["fornecedor"].isin(fornecedor_selecionado)) &
    (df["data_entrada"].dt.date >= data_inicio) &
    (df["data_entrada"].dt.date <= data_fim)
].copy()

kpis = calculate_kpis(df_filtrado)
kpis["Giro do Estoque (vezes)"] = round(kpis["Giro do Estoque (vezes)"], 4)

# HEADER
st.markdown(
    f"""
    <div style='text-align:center;padding:1rem;background:linear-gradient(80deg,#073252,#004C91);color:white;border-radius:10px;margin-bottom:1rem;'>
        <h2>Dashboard de Estoque e Rentabilidade</h2>
        <p><strong>Dados atualizados em:</strong> {datetime.now().strftime('%d/%m/%Y %H:%M')}</p>
    </div>
    """, unsafe_allow_html=True
)

# INSIGHT
lucro_atual = kpis["Lucro Líquido (R$)"]
lucro_anterior = df_filtrado[df_filtrado["mes"] < df_filtrado["mes"].max()]["lucro_liquido"].sum()
pct = ((lucro_atual - lucro_anterior) / lucro_anterior * 100) if lucro_anterior else 0
var = "subiu" if pct >= 0 else "caiu"
tone = "warning" if kpis["Itens em Estoque Crítico"] > 0 else "info"
insight_card("Insight do Período", f"O lucro líquido <strong>{var} {abs(pct):.1f}%</strong> em relação ao período anterior.<br>Estoque crítico: <strong>{kpis['Itens em Estoque Crítico']}</strong> itens.", tone)
add_spacing(0.8)

# KPIs
st.markdown("### 📈 Principais Indicadores")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Vendas Totais", format_currency(kpis["Vendas Totais (R$)"]))
    st.metric("Custo Total do Estoque", format_currency(kpis["Custo Total do Estoque (R$)"]))
with col2:
    st.metric("Lucro Líquido", format_currency(kpis["Lucro Líquido (R$)"]))
    st.metric("Margem Média", f"{kpis['Margem Média (%)']:.2f}%")
with col3:
    alerta, _ = get_stock_alert(kpis["Itens em Estoque Crítico"])
    st.metric("Itens em Estoque Crítico", kpis["Itens em Estoque Crítico"])
    st.markdown(f"<span style='color:#B14488;font-weight:600;'>⚠ {alerta}</span>", unsafe_allow_html=True)

add_spacing(0.6)
col4, col5, col6 = st.columns(3)
with col4:
    st.metric("Giro do Estoque (vezes)", f"{kpis['Giro do Estoque (vezes)']:.4f}")
with col5:
    st.metric("Ticket Médio", format_currency(kpis["Ticket Médio (R$)"]))
with col6:
    st.metric("Lucro / Faturamento (%)", f"{kpis['Percentual Lucro/Faturamento (%)']:.2f}%")

st.markdown("---")

# GRÁFICOS
st.markdown("### 🏆 Onde Estamos Ganhando")
colA, colB = st.columns(2)
with colA:
    st.plotly_chart(plot_lucro_fornecedor(df_filtrado, top_n), use_container_width=True)
with colB:
    st.plotly_chart(plot_margem_top_produtos(df_filtrado, top_n), use_container_width=True)

add_spacing(0.8)
st.markdown("### ⚠️ Onde Estamos Perdendo")
colC, colD = st.columns(2)
with colC:
    st.plotly_chart(plot_lucro_negativo_por_produto(df_filtrado, top_n), use_container_width=True)
with colD:
    st.plotly_chart(plot_estoque_critico_donut(df_filtrado), use_container_width=True)

add_spacing(0.8)
st.markdown("### 📈 Tendência Temporal")
st.plotly_chart(plot_evolucao_mensal_lucro(df_filtrado), use_container_width=True)

# DETALHES
st.markdown("---")
with st.expander("📘 Glossário de Indicadores"):
    st.markdown("""
    - **Estoque Crítico:** `estoque_atual < 50 unidades`
    - **Prejuízo:** `lucro_liquido < 0`
    - **Giro do Estoque:** `vendas_totais / custo_total_estoque`
    - **Ticket Médio:** `vendas_totais / número de itens vendidos`
    """)

with st.expander("📊 Detalhamento Completo do Estoque"):
    st.dataframe(df_filtrado, use_container_width=True, hide_index=True)
