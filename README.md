# Dashboard de Eficiência Contábil | YOY 2023–2024

Projeto de dados criado para analisar a evolução da eficiência em atividades contábeis entre 2023 e 2024, com foco em horas economizadas, redução de esforço manual e impacto das automações.

Este repositório registra duas etapas do mesmo projeto. A primeira versão foi construída no Looker Studio; a segunda concentra preparação, análise e visualização no Databricks, tornando a evolução técnica visível no próprio portfólio.

A V2 também foi conduzida como um projeto de aprendizagem prática: os dados foram gerados diretamente em Python no Databricks e organizados com a arquitetura Medalhão para compreender o papel das camadas Bronze, Silver e Gold. A IA generativa foi utilizada como apoio durante o estudo e o desenvolvimento.

## Acesse o projeto

- [Dashboard V2 publicado no Databricks](https://dbc-cab2dac6-3287.cloud.databricks.com/dashboardsv3/01f19e65b1a11877a1941640dec970c5/published?o=7474652829983420)
- [Dashboard V1 no Looker Studio](https://lookerstudio.google.com/reporting/6f13e190-cc9b-44b3-8044-c603cfb119cc)

## Evolução do projeto

| Aspecto | V1 — Looker Studio | V2 — Databricks |
| --- | --- | --- |
| Camada de visualização | Looker Studio | Databricks Dashboards |
| Fonte analítica | Google Sheets | Dataset no Databricks |
| Preparação dos dados | Python e CSV | Python, PySpark e SQL no Databricks |
| Arquitetura | Fluxo direto para o Google Sheets | Medalhão: Bronze, Silver e Gold |
| Abordagem visual | Visão operacional detalhada | Resumo executivo de eficiência |
| Principal aprendizado | Construção de métricas e narrativa visual | Centralização do fluxo analítico e evolução em SQL |

- [Documentação completa da V1](v1-looker-studio/README.md)
- [Documentação completa da V2](v2-databricks/README.md)

## Principais resultados

| Indicador | 2023 | 2024 |
| --- | ---: | ---: |
| Horas totais | 543 h | 558 h |
| Horas economizadas | 48 h | 238 h |
| Horas restantes | 495 h | 320 h |
| Taxa de economia | 8,84% | 42,65% |

Entre 2023 e 2024, as horas economizadas cresceram **395,83%**, passando de 48 para 238 horas. Em 2024, a taxa de economia chegou a **42,65%**.

## Dashboard V2

![Dashboard de Eficiência Contábil no Databricks](assets/dashboard-databricks-v2.png)

## Estrutura do repositório

```text
.
├── README.md
├── assets/
│   └── dashboard-databricks-v2.png
├── notebooks/
│   └── dashboard_atividades_contabeis_etl.py
├── src/
│   └── gerar_dados.py
├── v1-looker-studio/
│   └── README.md
└── v2-databricks/
    └── README.md
```

## Tecnologias

- Python
- Pandas e NumPy
- SQL
- Databricks
- Looker Studio
- Google Sheets

## Metodologia de desenvolvimento

A IA generativa foi utilizada como apoio ao aprendizado: ajudou a compreender recursos do Databricks, investigar erros, discutir a função de cada camada da arquitetura Medalhão e validar caminhos de implementação. As decisões sobre métricas, organização dos dados e apresentação do dashboard foram construídas e verificadas durante o desenvolvimento do projeto.

## Sobre os dados

Os dados são sintéticos e foram gerados em Python exclusivamente para fins de estudo e portfólio. Eles simulam atividades contábeis manuais e automatizadas sem representar informações reais de nenhuma empresa.

## Autor

[Jhonny Gama](https://github.com/JhonnyGama)
