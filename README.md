# RENAEST — Dashboard de Análise de Acidentes de Trânsito

Dashboard analítica interativa desenvolvida para o **Checkpoint 3 — Desenvolvimento da Dashboard**, da disciplina de **Data Science and Analytics**.

O projeto reúne os resultados obtidos nos Checkpoints 1 e 2, apresentando indicadores, visualizações e resultados da análise preditiva aplicada aos dados do **RENAEST — Registro Nacional de Sinistros e Estatísticas de Trânsito**.

---

## 1. Sobre o projeto

O projeto tem como objetivo desenvolver uma aplicação analítica interativa capaz de apresentar os principais resultados da análise dos acidentes de trânsito registrados no RENAEST.

A dashboard permite:

- visualizar indicadores gerais dos acidentes;
- explorar a distribuição de acidentes por estado;
- visualizar dados relacionados aos anos analisados;
- analisar a distribuição dos acidentes segundo condições meteorológicas;
- comparar os modelos de Machine Learning desenvolvidos no Checkpoint 2;
- visualizar o desempenho dos modelos por meio de métricas;
- utilizar filtros para exploração dos dados;
- apresentar uma visão preditiva complementar à análise exploratória realizada no Checkpoint 1.

A aplicação foi desenvolvida utilizando **Python, Streamlit e Plotly**.

---

## 2. Fonte dos dados

Os dados utilizados no projeto são provenientes do **RENAEST — Registro Nacional de Sinistros e Estatísticas de Trânsito**, disponibilizado pelo Ministério dos Transportes.

### Fonte oficial

https://dados.transportes.gov.br/dataset/renaest

Os dados utilizados nos Checkpoints 1 e 2 incluem informações relacionadas aos acidentes de trânsito, como:

- estado da ocorrência;
- ano e mês do acidente;
- dia da semana;
- fase do dia;
- tipo de acidente;
- condições meteorológicas;
- tipo de rodovia;
- condições da pista;
- tipo de cruzamento;
- tipo de pavimento;
- tipo de curva;
- limite de velocidade;
- tipo de pista;
- presença de guard-rail;
- presença de canteiro central;
- presença de acostamento;
- quantidade de óbitos.

---

## 3. Problema analisado

O projeto busca analisar os acidentes de trânsito e identificar características associadas à ocorrência de acidentes com óbitos.

A tarefa de Machine Learning desenvolvida no Checkpoint 2 foi definida como um problema de **classificação binária**.

### Variável alvo

A variável `obito` indica se o acidente apresentou pelo menos um óbito:

- `0` — acidente sem óbito;
- `1` — acidente com óbito.

### Variáveis preditoras

Foram utilizadas características relacionadas ao contexto do acidente, incluindo:

- UF;
- ano;
- mês;
- dia da semana;
- fase do dia;
- tipo de acidente;
- condição meteorológica;
- tipo de rodovia;
- condição da pista;
- tipo de cruzamento;
- tipo de pavimento;
- tipo de curva;
- limite de velocidade;
- tipo de pista;
- presença de guard-rail;
- presença de canteiro central;
- presença de acostamento.

Variáveis diretamente relacionadas ao resultado do acidente foram excluídas das features para evitar vazamento de informação (*data leakage*).

---

## 4. Checkpoint 1 — Análise exploratória

Na análise exploratória realizada no Checkpoint 1, foram identificados os seguintes indicadores principais:

| Indicador | Resultado |
|---|---:|
| Total de acidentes analisados | 8.371.800 |
| Acidentes com óbitos | 176.534 |
| Percentual de acidentes com óbitos | 2,11% |
| Estado com maior volume entre os estados apresentados | MG |
| Acidentes em MG | 2.152.175 |
| Ano com maior volume entre os anos preservados na análise | 2023 |
| Acidentes em 2023 | 1.185.420 |

Os estados apresentados na dashboard correspondem aos cinco estados com maior volume de acidentes identificado no levantamento utilizado no projeto:

- MG;
- SP;
- SC;
- PR;
- GO.

---

## 5. Checkpoint 2 — Modelagem preditiva

Foram desenvolvidos três modelos de Machine Learning:

1. Regressão Logística;
2. XGBoost;
3. Rede Neural Profunda.

Os modelos foram avaliados utilizando:

- Acurácia;
- Precisão;
- Recall;
- F1-score;
- ROC-AUC.

### Resultados

| Modelo | Acurácia | Precisão | Recall | F1-score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Regressão Logística | 69,83% | 12,20% | 74,82% | 20,98% | 79,39% |
| XGBoost | 72,85% | 13,74% | 77,12% | 23,32% | 83,20% |
| Rede Neural | 71,16% | 13,06% | 77,60% | 22,36% | 82,72% |

O XGBoost apresentou ROC-AUC de aproximadamente **0,832**, sendo utilizado como referência principal para a apresentação do desempenho preditivo na dashboard.

A Rede Neural apresentou o maior Recall entre os três modelos, enquanto o XGBoost apresentou o maior valor de ROC-AUC e F1-score.

---

## 6. Dashboard

A aplicação reúne os resultados das etapas anteriores em uma interface interativa.

### Indicadores apresentados

A dashboard apresenta os seguintes KPIs:

- total de acidentes;
- total de acidentes com óbitos;
- percentual de acidentes com óbitos;
- ROC-AUC do modelo XGBoost.

### Visualizações

A aplicação apresenta gráficos estáticos e interativos.

#### Gráfico estático

É apresentado um gráfico estático utilizando **Matplotlib**, mostrando a quantidade de acidentes por estado.

#### Gráficos interativos

São utilizados gráficos interativos com **Plotly**, incluindo:

- acidentes por estado;
- acidentes por ano;
- acidentes por condição meteorológica;
- comparação do desempenho dos modelos de Machine Learning.

### Filtro

A dashboard disponibiliza um filtro de estado para permitir a exploração dos dados apresentados no gráfico de acidentes por estado.

---

## 7. Tecnologias utilizadas

- **Python**
- **Streamlit**
- **Pandas**
- **Plotly**
- **Matplotlib**
- **Scikit-learn**
- **XGBoost**

---

## 8. Estrutura do projeto

RENAEST-Checkpoint3-Dashboard/
│
├── app.py
├── grafico_acidentes_uf.png
├── requirements.txt
└── README.md

app.py

Arquivo principal da aplicação Streamlit.

Contém:

configuração da dashboard;
KPIs;
filtros;
gráficos interativos;
tabela de resultados dos modelos;
apresentação dos resultados da análise.
grafico_acidentes_uf.png

Gráfico estático utilizado na dashboard para representar os acidentes por estado.

requirements.txt

Arquivo contendo as dependências necessárias para executar a aplicação.

README.md

Documento com informações sobre o projeto, fonte dos dados e instruções para execução.

9. Como executar localmente

9.1. Pré-requisitos

É necessário possuir:

Python 3.9 ou superior;
Git;
acesso ao terminal ou prompt de comando.
9.2. Clonar o repositório

Execute:

git clone https://github.com/Pedro184294/RENAEST-Checkpoint3-Dashboard.git

Depois, entre na pasta:

cd RENAEST-Checkpoint3-Dashboard

9.3. Instalar as dependências

Execute:

pip install -r requirements.txt

9.4. Executar a aplicação

Execute:

streamlit run app.py

Após o comando, o Streamlit disponibilizará a aplicação localmente no navegador.

Normalmente, o endereço será:

http://localhost:8501

10. Aplicação hospedada

A aplicação foi disponibilizada publicamente por meio do Streamlit Community Cloud, permitindo o acesso à dashboard pela Internet sem necessidade de instalação ou execução de código pelo avaliador.

URL pública da aplicação

https://renaest-checkpoint3-dashboard-ysafgjxjoksqb4urm9q47y.streamlit.app

11. Repositório

O código-fonte do projeto está disponível no GitHub:

https://github.com/Pedro184294/RENAEST-Checkpoint3-Dashboard

12. Relação entre os Checkpoints
13. 
Checkpoint 1

Foi realizada a análise exploratória dos dados do RENAEST, identificando:

volume de acidentes;
distribuição por estado;
distribuição temporal;
condições meteorológicas;
ocorrência de acidentes com óbitos;
características e qualidade dos dados.
Checkpoint 2

Foi desenvolvida a etapa de modelagem preditiva, utilizando três modelos:

Regressão Logística;
XGBoost;
Rede Neural Profunda.

Os resultados foram avaliados por diferentes métricas de classificação.

Checkpoint 3

Os resultados das etapas anteriores foram reunidos em uma aplicação analítica interativa, permitindo:

consultar indicadores;
explorar visualizações;
comparar modelos;
observar resultados da análise preditiva;
apresentar os resultados de maneira organizada em uma dashboard.

13. Limitações

Os resultados apresentados na dashboard devem ser interpretados considerando algumas limitações do conjunto de dados.

Entre elas:

existência de registros com informações não preenchidas ou não informadas;
concentração de registros em determinadas categorias;
grande quantidade de valores classificados como NAO INFORMADO ou DESCONHECIDAS na condição meteorológica;
os dados apresentados na dashboard representam os resultados preservados das análises realizadas nos Checkpoints 1 e 2;
os gráficos de anos apresentados não representam necessariamente toda a série temporal disponível no RENAEST, mas os anos mantidos na análise utilizada neste projeto.

Além disso, o modelo preditivo deve ser utilizado como ferramenta de apoio à análise, e não como substituto da avaliação técnica dos dados.

14. Conclusão

A dashboard integra as etapas de análise exploratória e modelagem preditiva desenvolvidas nos Checkpoints anteriores.

A aplicação permite visualizar indicadores e padrões presentes nos dados do RENAEST e, ao mesmo tempo, apresentar uma perspectiva preditiva por meio dos modelos de Machine Learning.

Dessa forma, o projeto demonstra a utilização de dados, visualização e Machine Learning em uma aplicação analítica interativa voltada à análise de acidentes de trânsito.
