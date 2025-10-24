import streamlit as st


def format_currency(value: float) -> str:
    """Formata valores em reais com vírgulas e pontos corretos."""
    try:
        return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except Exception:
        return "R$ 0,00"


def get_stock_alert(count: int) -> tuple:
    """Retorna mensagem e cor de alerta conforme número de itens críticos."""
    if count == 0:
        return "Estoque adequado", "success"
    elif count <= 5:
        return f"Atenção: {count} item com estoque baixo", "warning"
    else:
        return f"Urgente: {count} itens com estoque crítico", "error"


def add_spacing(rem: float = 1.0):
    """Adiciona espaçamento vertical (respiro visual)."""
    st.markdown(f"<div style='margin:{rem}rem 0'></div>", unsafe_allow_html=True)


def insight_card(title: str, body_html: str, tone: str = "info"):
    """Exibe um card de insight estilizado com tons acessíveis."""
    tones = {
        "info": ("#E9F5FF", "#004C91"),
        "warning": ("#FFF3CD", "#856404"),
        "danger": ("#F8D7DA", "#842029"),
    }
    bg, color = tones.get(tone, tones["info"])
    st.markdown(
        f"""
        <div style='background:{bg};padding:1rem 1.2rem;border-left:6px solid {color};
                    border-radius:10px;box-shadow:0 2px 6px rgba(0,0,0,0.05);'>
            <h4 style='color:{color};margin-bottom:0.5rem;'>{title}</h4>
            <div style='color:#333;font-size:15px;'>{body_html}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
