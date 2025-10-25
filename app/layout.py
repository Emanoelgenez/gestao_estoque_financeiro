import streamlit as st

def build_dashboard(df, kpis, plots):
    st.title("Dashboard de Estoque e Rentabilidade")
    st.markdown("Análise detalhada do desempenho financeiro e operacional dos produtos.")

    # KPIs em colunas
    cols = st.columns(4)
    kpi_keys = list(kpis.keys())
    for i, col in enumerate(cols):
        with col:
            key = kpi_keys[i]
            valor = kpis[key]
            if "R$" in key:
                st.metric(label=key, value=f"R$ {valor:,.2f}")
            elif "%" in key:
                st.metric(label=key, value=f"{valor:.2f}%")
            else:
                st.metric(label=key, value=f"{valor:,}")

    # Linha extra para KPIs restantes 
    if len(kpi_keys) > 4:
        cols2 = st.columns(len(kpi_keys) - 4)
        for i, col in enumerate(cols2):
            with col:
                key = kpi_keys[4 + i]
                valor = kpis[key]
                if "R$" in key:
                    st.metric(label=key, value=f"R$ {valor:,.2f}")
                elif "%" in key:
                    st.metric(label=key, value=f"{valor:.2f}%")
                else:
                    st.metric(label=key, value=f"{valor:,}")

    st.markdown("---")

    # Gráficos 
    st.subheader("Análises Visuais")
    st.plotly_chart(plots["lucro_fornecedor"], use_container_width=True)
    st.plotly_chart(plots["margem_top_produtos"], use_container_width=True)
    st.plotly_chart(plots["evolucao_mensal_lucro"], use_container_width=True)
    st.plotly_chart(plots["estoque_critico"], use_container_width=True)
    st.plotly_chart(plots["lucro_negativo_produtos"], use_container_width=True)

    st.markdown("---")

    # Tabela final para detalhamento
    st.subheader("Detalhamento do Estoque")
    st.dataframe(df.reset_index(drop=True))
