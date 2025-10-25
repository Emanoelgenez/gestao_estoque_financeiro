import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import streamlit as st

# Paleta aprimorada — daltônica e contrastiva
PALETTE = {
    "profit": "#004C91",
    "secondary": "#E89200",
    "loss": "#D55E00",
    "normal": "#007A5C",
    "critical": "#B14488",
    "neutral_bg": "#F9FAFB",
}


import streamlit as st

def base_layout(fig, title: str):
    # Detecta tema ativo (dark/light)
    theme = st.get_option("theme.base")

    if theme == "dark":
        text_color = "#F5F5F5"
        axis_color = "#E0E0E0"
        grid_color = "rgba(255,255,255,0.15)"
        paper_color = "#0E1117"
    else:
        text_color = "#1E1E1E"
        axis_color = "#333333"
        grid_color = "rgba(0,0,0,0.08)"
        paper_color = "white"

    fig.update_layout(
        title=dict(
            text=title,
            x=0.02,
            xanchor="left",
            font=dict(size=15, color=text_color)
        ),
        font=dict(family="Segoe UI, Roboto, sans-serif", size=12, color=text_color),
        plot_bgcolor=paper_color,
        paper_bgcolor=paper_color,
        margin=dict(l=40, r=40, t=60, b=40),
        yaxis=dict(
            showgrid=True,
            gridcolor=grid_color,
            zeroline=False,
            color=axis_color,
            title=dict(font=dict(color=axis_color)),
            tickfont=dict(color=axis_color)
        ),
        xaxis=dict(
            showgrid=False,
            color=axis_color,
            title=dict(font=dict(color=axis_color)),
            tickfont=dict(color=axis_color)
        ),
    )

    return fig


def plot_lucro_fornecedor(df, top_n=7):
    data = df.groupby("fornecedor")["lucro_liquido"].sum().sort_values(ascending=False).head(top_n).reset_index()
    fig = px.bar(data, x="fornecedor", y="lucro_liquido",
                 text=[f"R$ {v:,.0f}" for v in data["lucro_liquido"]],
                 color_discrete_sequence=[PALETTE["profit"]])
    fig.update_traces(textposition="outside", textfont_size=13)
    return base_layout(fig, f"Top {top_n} Fornecedores por Lucro Líquido")


def plot_margem_top_produtos(df, top_n=7):
    data = df.groupby("descricao")["margem_percentual"].mean().sort_values(ascending=False).head(top_n).reset_index()
    fig = px.bar(data, x="descricao", y="margem_percentual",
                 text=[f"{v:.1f}%" for v in data["margem_percentual"]],
                 color_discrete_sequence=[PALETTE["secondary"]])
    fig.update_traces(textposition="outside", textfont_size=13)
    return base_layout(fig, f"Top {top_n} Produtos por Margem Média (%)")


def plot_evolucao_mensal_lucro(df):
    data = df.groupby("mes")["lucro_liquido"].sum().reset_index()
    fig = px.line(data, x="mes", y="lucro_liquido", markers=True)
    fig.update_traces(line=dict(color=PALETTE["profit"], width=3))
    fig.add_trace(go.Scatter(
        x=data["mes"], y=data["lucro_liquido"],
        text=[f"R$ {v:,.0f}" for v in data["lucro_liquido"]],
        mode="text", textposition="top center", textfont=dict(size=12, color="#333"), showlegend=False
    ))
    return base_layout(fig, "Evolução Mensal do Lucro Líquido")


def plot_estoque_critico_donut(df):
    data = df["estoque_critico"].value_counts().rename_axis("status").reset_index(name="count")
    data["status"] = data["status"].map({True: "Crítico", False: "Normal"})
    fig = px.pie(data, names="status", values="count", hole=0.5,
                 color_discrete_map={"Normal": PALETTE["normal"], "Crítico": PALETTE["critical"]})
    fig.update_traces(textinfo="percent+label", textfont_size=13)
    return base_layout(fig, "Proporção de Itens em Estoque Crítico")


def plot_lucro_negativo_por_produto(df, top_n=7):
    data = df[df["lucro_negativo"]].groupby("descricao")["lucro_liquido"].sum().sort_values().head(top_n).reset_index()
    if data.empty:
        fig = go.Figure()
        fig.add_annotation(text="Nenhum produto com prejuízo", xref="paper", yref="paper", showarrow=False)
        return base_layout(fig, "Top Produtos com Maior Prejuízo")
    fig = px.bar(data, x="descricao", y="lucro_liquido",
                 text=[f"R$ {abs(v):,.0f}" for v in data["lucro_liquido"]],
                 color_discrete_sequence=[PALETTE["loss"]])
    fig.update_traces(textposition="outside", textfont_size=13)
    return base_layout(fig, f"Top {top_n} Produtos com Maior Prejuízo")
