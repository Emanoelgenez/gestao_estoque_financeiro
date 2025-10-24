# Dashboard de Estoque e Rentabilidade  
**Monitoramento inteligente. Decisões em tempo real.**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-streamlit-app-url)  
![Python](https://img.shields.io/badge/Python-3.11-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-1.38-red) ![Plotly](https://img.shields.io/badge/Plotly-5.18-orange)  
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## O Problema

> **"Como saber onde estamos ganhando, perdendo e o que precisa de ação urgente — sem perder tempo em planilhas?"**

Empresas de varejo e distribuição lidam diariamente com:
- Estoque crítico não identificado
- Produtos com prejuízo mascarado
- Lucro volátil sem contexto temporal
- Dashboards genéricos, confusos e inacessíveis

---

## A Solução: Um Dashboard que **pensa como gestor**

```text
Insight → KPIs → Onde Ganha → Onde Perde → Tendência → Ação
```

### Destaques do Projeto

| Feature | Impacto |
|-------|--------|
| **Insight automático do período** | "Lucro subiu 4.8% vs anterior" — contexto imediato |
| **KPIs agrupados em cards com ícones** | Leitura em < 5 segundos |
| **Barras negativas em laranja** | Prejuízo visualmente inconfundível |
| **Donut chart com rótulos internos** | Proporção crítica clara (8.28%) |
| **Filtros dinâmicos (fornecedor, período, top N)** | Análise sob demanda |
| **Exportação CSV com 1 clique** | Dados nas mãos do time |
| **Dark/Light mode automático** | Experiência premium em qualquer dispositivo |
| **Glassmorphism + hover animations** | UI moderna, tech-savvy |

---

## Heurísticas de Nielsen (10/10 atendidas)

| # | Heurística | Como cumprimos |
|---|------------|----------------|
| 1 | **Visibilidade do status** | Timestamp + insight banner + "Atualizado em: 24/10/2025 10:12" |
| 2 | **Match com o mundo real** | Termos do varejo: "estoque crítico", "prejuízo", "giro" |
| 3 | **Controle do usuário** | Filtros, top N, exportação |
| 4 | **Consistência** | Ícones, cores, fontes, layout em grid |
| 5 | **Prevenção de erros** | Definições no glossário, tooltips implícitos |
| 6 | **Reconhecimento > memória** | Ícones (trophy, warning, chart), rótulos claros |
| 7 | **Flexibilidade** | Mobile-first, responsivo, expansível |
| 8 | **Minimalismo estético** | Apenas dados acionáveis, sem ruído |
| 9 | **Ajuda na recuperação** | Glossário expansível |
| 10 | **Documentação** | Este README + código comentado |

---

## Storytelling com Dados (Cole Nussbaumer Knaflic)

| Princípio | Aplicação no Dashboard |
|---------|------------------------|
| **Contexto primeiro** | Insight do período no topo |
| **Declutter** | Apenas 3 seções principais + tabela expansível |
| **Foco de atenção** | Títulos com ícones, cores contrastantes |
| **Narrativa clara** | Fluxo: Ganhando → Perdendo → Tendência |
| **Ação implícita** | "Urgente: 13 itens críticos" com warning icon |

> **"Não mostramos dados. Mostramos o que fazer com eles."**

---

## Acessibilidade & Inclusão

- **Paleta colorblind-safe**  
  ```python
  PROFIT   = "#00D4AA"  # teal
  LOSS     = "#FF6B6B"  # coral
  CRITICAL = "#9C27B0"  # purple
  ```
- **Contraste WCAG AA+** em light/dark mode
- **Rótulos em texto** (não só cor)
- **Donut > Pizza** (melhor legibilidade)
- **Fonte Inter (Google Fonts)** – alta legibilidade

---

## Arquitetura Técnica (Moderna & Escalável)

```
dashboard_estoque/
├── app/
│   ├── main.py          → UI + lógica de fluxo
│   ├── data_loader.py   → ETL + enriquecimento
│   ├── metrics.py       → Cálculo de KPIs
│   ├── visuals.py       → Gráficos Plotly (colorblind-safe)
│   ├── utils.py         → Formatação + alertas
│   └── __init__.py
├── assets/
│   └── logo.png
├── data/
│   └── df_estoque_st.csv
└── requirements.txt
```

### Tecnologias

| Camada | Ferramenta |
|-------|-----------|
| Frontend | Streamlit (`layout="wide"`, `st.plotly_chart`) |
| Visualização | Plotly Express + Graph Objects |
| Cache | `@st.cache_data(ttl=3600)` |
| Responsividade | CSS injetado + `use_container_width=True` |
| Export | `st.download_button` (CSV UTF-8) |

---

## Como Rodar

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/dashboard-estoque.git
cd dashboard-estoque

# 2. Crie ambiente
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 3. Instale dependências
pip install -r requirements.txt

# 4. Execute
streamlit run main.py
```

Acesse: `http://localhost:8501`

---

## Deploy (1 clique)

```yaml
# .streamlit/config.toml
[server]
enableCORS = false
```

[![Deploy](https://img.shields.io/badge/Deploy-Streamlit_Cloud-blue?logo=streamlit)](https://share.streamlit.io)

---

## Resultado Final (Visual)

```
Insight: Lucro subiu 4.8%
KPIs em cards com ícones
Onde Ganha (barras azuis)
Onde Perde (barras laranja + donut roxo)
Tendência (linha com rótulos)
Glossário + Tabela expansível
```

> **Um dashboard que não só informa — mas guia a ação.**

---

## Contribua

```bash
git checkout -b feature/nova-analise
# faça suas melhorias
git commit -m "feat: adiciona análise de sazonalidade"
git push origin feature/nova-analise
```

Pull Requests bem-vindos!

---

## Licença

[MIT License](LICENSE) – Use, modifique, implante.

---

**Feito para quem decide com dados, não com achismo.**

---
```

---

### Próximos Passos (opcional)

Se quiser, posso gerar:

- `LICENSE` (MIT)
- `.gitignore`
- `Dockerfile`
- `streamlit_app.py` para deploy
- PDF export com `pdfkit` ou `streamlit-pdf`

É só pedir

Agora é só criar o repositório no GitHub e fazer o upload!  
**Link sugerido:** `github.com/seu-empresa/dashboard-estoque-inteligente`
```

**Pronto para brilhar no GitHub**  
Este README transforma seu projeto em um **case de sucesso técnico e de UX**.
```