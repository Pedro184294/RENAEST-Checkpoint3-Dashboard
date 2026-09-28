
import streamlit as st
import pandas as pd
import plotly.express as px

# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="RENAEST - Dashboard",
    page_icon="🚗",
    layout="wide"
)

# ============================================================
# DADOS
# ============================================================

total_acidentes = 8371800
acidentes_com_obitos = 176534
percentual_obitos = 2.11

acidentes_por_uf = {
    "MG": 2152175,
    "SP": 1319805,
    "SC": 1241059,
    "PR": 769344,
    "GO": 741919
}

acidentes_por_ano = {
    2018: 749134,
    2023: 1185420
}

acidentes_meteorologia = {
    "NAO INFORMADO": 4432260,
    "CLARO": 1733663,
    "DESCONHECIDAS": 1322121,
    "OUTRAS CONDICOES": 692688,
    "CHUVA": 115800,
    "NUBLADO": 45053,
    "GAROACHUVISCO": 23484,
    "NEVOEIRO NEVOA OU FUMACA": 6484,
    "VENTOS FORTES": 220,
    "NEVE": 16
}

resultados_modelos = {
    "Modelo": [
        "Regressão Logística",
        "XGBoost",
        "Rede Neural V2"
    ],
    "Acurácia": [
        0.69825,
        0.72851,
        0.71160
    ],
    "Precisão": [
        0.121985,
        0.137362,
        0.130649
    ],
    "Recall": [
        0.748179,
        0.771156,
        0.776013
    ],
    "F1-score": [
        0.209768,
        0.233187,
        0.223646
    ],
    "ROC-AUC": [
        0.793921,
        0.832003,
        0.827179
    ]
}

# ============================================================
# DATAFRAMES
# ============================================================

df_uf = pd.DataFrame(
    list(acidentes_por_uf.items()),
    columns=["UF", "Acidentes"]
)

df_ano = pd.DataFrame(
    list(acidentes_por_ano.items()),
    columns=["Ano", "Acidentes"]
)

df_meteorologia = pd.DataFrame(
    list(acidentes_meteorologia.items()),
    columns=["Condicao_Meteorologica", "Acidentes"]
)

df_modelos = pd.DataFrame(resultados_modelos)

# ============================================================
# TÍTULO
# ============================================================

st.title("🚗 RENAEST — Dashboard de Acidentes de Trânsito")

st.markdown(
    """
    Dashboard desenvolvida a partir dos resultados dos Checkpoints 1 e 2.

    O objetivo é explorar indicadores dos acidentes registrados no RENAEST
    e apresentar os resultados da análise preditiva.
    """
)

st.divider()

# ============================================================
# FONTE DOS DADOS
# ============================================================

st.subheader("📚 Fonte dos dados")

st.markdown(
    "Os dados utilizados são provenientes do **RENAEST — Registro Nacional "
    "de Sinistros e Estatísticas de Trânsito**, disponibilizado pelo "
    "Ministério dos Transportes."
)

st.markdown(
    "[Acessar fonte oficial do RENAEST](https://dados.transportes.gov.br/dataset/renaest)"
)

st.divider()

# ============================================================
# KPIs
# ============================================================

st.subheader("📊 Indicadores principais")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total de acidentes",
    f"{total_acidentes:,}".replace(",", ".")
)

col2.metric(
    "Acidentes com óbitos",
    f"{acidentes_com_obitos:,}".replace(",", ".")
)

col3.metric(
    "Percentual com óbitos",
    f"{percentual_obitos:.2f}%"
)

col4.metric(
    "ROC-AUC — XGBoost",
    "0.832"
)

st.divider()

# ============================================================
# FILTRO POR ESTADO
# ============================================================

st.sidebar.header("🔎 Filtros")

ufs_disponiveis = ["Todos"] + list(df_uf["UF"])

uf_selecionada = st.sidebar.selectbox(
    "Estado",
    ufs_disponiveis
)

if uf_selecionada != "Todos":
    df_uf_exibicao = df_uf[
        df_uf["UF"] == uf_selecionada
    ]
else:
    df_uf_exibicao = df_uf

# ============================================================
# GRÁFICO ESTÁTICO
# ============================================================

st.subheader("📈 Visualização estática")

try:
    st.image(
        "grafico_acidentes_uf.png",
        caption="Acidentes registrados por estado"
    )
except:
    st.info(
        "O gráfico estático não foi encontrado. "
        "Os gráficos interativos continuam disponíveis abaixo."
    )

st.divider()

# ============================================================
# GRÁFICO INTERATIVO — ESTADOS
# ============================================================

st.subheader("🗺️ Acidentes por estado")

fig_uf = px.bar(
    df_uf_exibicao,
    x="UF",
    y="Acidentes",
    title="Quantidade de acidentes por estado",
    labels={
        "UF": "Estado",
        "Acidentes": "Quantidade de acidentes"
    },
    text="Acidentes"
)

fig_uf.update_traces(
    texttemplate="%{text:,}",
    textposition="outside"
)

st.plotly_chart(
    fig_uf,
    use_container_width=True
)

# ============================================================
# GRÁFICO — ANO
# ============================================================

st.subheader("📅 Acidentes por ano")

fig_ano = px.line(
    df_ano,
    x="Ano",
    y="Acidentes",
    markers=True,
    title="Acidentes registrados por ano",
    labels={
        "Ano": "Ano",
        "Acidentes": "Quantidade de acidentes"
    }
)

st.plotly_chart(
    fig_ano,
    use_container_width=True
)

# ============================================================
# GRÁFICO — METEOROLOGIA
# ============================================================

st.subheader("🌦️ Condições meteorológicas")

fig_meteorologia = px.bar(
    df_meteorologia.sort_values(
        "Acidentes",
        ascending=True
    ),
    x="Acidentes",
    y="Condicao_Meteorologica",
    orientation="h",
    title="Acidentes por condição meteorológica",
    labels={
        "Condicao_Meteorologica": "Condição meteorológica",
        "Acidentes": "Quantidade de acidentes"
    }
)

st.plotly_chart(
    fig_meteorologia,
    use_container_width=True
)

st.divider()

# ============================================================
# ANÁLISE PREDITIVA
# ============================================================

st.subheader("🤖 Análise preditiva")

st.markdown(
    """
    Foram avaliados três modelos de Machine Learning para estimar a
    ocorrência de acidentes com óbitos:
    
    - Regressão Logística;
    - XGBoost;
    - Rede Neural V2.
    """
)

st.dataframe(
    df_modelos.style.format({
        "Acurácia": "{:.2%}",
        "Precisão": "{:.2%}",
        "Recall": "{:.2%}",
        "F1-score": "{:.2%}",
        "ROC-AUC": "{:.3f}"
    }),
    use_container_width=True
)

# ============================================================
# COMPARAÇÃO ROC-AUC
# ============================================================

fig_modelos = px.bar(
    df_modelos,
    x="Modelo",
    y="ROC-AUC",
    title="Comparação dos modelos — ROC-AUC",
    labels={
        "Modelo": "Modelo",
        "ROC-AUC": "ROC-AUC"
    },
    text="ROC-AUC"
)

fig_modelos.update_traces(
    texttemplate="%{text:.3f}",
    textposition="outside"
)

fig_modelos.update_yaxes(
    range=[0, 1]
)

st.plotly_chart(
    fig_modelos,
    use_container_width=True
)

# ============================================================
# INTERPRETAÇÃO
# ============================================================

st.subheader("🔎 Interpretação dos resultados")

st.markdown(
    """
    Os resultados da modelagem complementam a análise exploratória
    apresentada no Checkpoint 1.

    A análise descritiva permite identificar padrões históricos nos
    registros de acidentes, enquanto os modelos de Machine Learning
    acrescentam uma perspectiva preditiva.

    Entre os modelos avaliados, o XGBoost apresentou ROC-AUC de 0,832,
    enquanto a Rede Neural V2 apresentou recall de 0,776.
    """
)

st.divider()

# ============================================================
# LIMITAÇÕES
# ============================================================

st.subheader("⚠️ Limitações")

st.markdown(
    """
    - Os indicadores apresentados foram obtidos a partir da análise
      realizada nos Checkpoints 1 e 2.
    - Parte dos registros possui informações ausentes ou não informadas.
    - A análise preditiva não deve ser interpretada como certeza sobre
      a ocorrência de um acidente.
    - Para utilização operacional, seria necessário validar o modelo
      com dados atualizados e integrar a solução a uma infraestrutura
      de processamento adequada.
    """
)

st.divider()

st.caption(
    "Projeto acadêmico — FIAP | Data Science and Analytics"
)
