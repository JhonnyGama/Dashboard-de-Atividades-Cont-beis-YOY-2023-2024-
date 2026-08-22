# Databricks notebook source
# MAGIC %md
# MAGIC # Dashboard de Eficiência Contábil — ETL Medalhão
# MAGIC
# MAGIC Notebook responsável por gerar os dados sintéticos e organizá-los nas
# MAGIC camadas Bronze, Silver e Gold para consumo pelo dashboard.

# COMMAND ----------

import numpy as np
import pandas as pd

rng = np.random.default_rng(42)

atividades_base = [
    "Provisão de Notas",
    "Reclassificação Contábil",
    "Conciliação de Contas",
    "Análise de Variáveis",
    "Fechamento Mensal",
    "Validação de Lançamentos",
    "Ajustes Contábeis",
    "Importação de Dados do ERP",
    "Geração de Relatórios",
    "Revisão de Categorias",
]

categorias_base = [
    "Provisões",
    "Reclassificações",
    "Conciliações",
    "Fechamento",
    "Lançamentos",
    "Ajustes",
    "Controles",
    "Importações",
    "Relatórios",
    "Revisões",
]


def gerar_dados_ano(ano, multiplicador_automacao=1.0, n=100):
    atividades = []
    categorias = []

    for _ in range(n):
        idx = rng.integers(0, len(atividades_base))
        atividades.append(atividades_base[idx])
        categorias.append(categorias_base[idx])

    horas_totais = rng.integers(low=2, high=10, size=n)
    horas_economizadas = [
        int(rng.integers(0, horas_totais[i]) * multiplicador_automacao)
        for i in range(n)
    ]

    return pd.DataFrame(
        {
            "ano": ano,
            "atividade": atividades,
            "categoria": categorias,
            "horas_totais": horas_totais,
            "horas_economizadas": horas_economizadas,
        }
    )


df_2023 = gerar_dados_ano(2023, multiplicador_automacao=0.4, n=100)
df_2024 = gerar_dados_ano(2024, multiplicador_automacao=1.0, n=100)
df_final = pd.concat([df_2023, df_2024], ignore_index=True)

# COMMAND ----------
# MAGIC %md
# MAGIC ## Bronze — dados brutos

# COMMAND ----------

df_bronze_spark = spark.createDataFrame(df_final)

(
    df_bronze_spark.write
    .format("delta")
    .mode("overwrite")
    .saveAsTable("workspace.default.atividades_contabeis_bronze")
)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM workspace.default.atividades_contabeis_bronze;

# COMMAND ----------
# MAGIC %md
# MAGIC ## Silver — dados tratados e enriquecidos

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE workspace.default.atividades_contabeis_silver AS
# MAGIC SELECT
# MAGIC     ano,
# MAGIC     atividade,
# MAGIC     categoria,
# MAGIC     horas_totais,
# MAGIC     horas_economizadas,
# MAGIC     ROUND(horas_economizadas / horas_totais * 100, 2)
# MAGIC         AS impacto_percentual,
# MAGIC     CASE
# MAGIC         WHEN horas_economizadas > 0 THEN 'Automatizada'
# MAGIC         ELSE 'Manual'
# MAGIC     END AS status
# MAGIC FROM workspace.default.atividades_contabeis_bronze;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM workspace.default.atividades_contabeis_silver;

# COMMAND ----------
# MAGIC %md
# MAGIC ## Gold — indicadores anuais do dashboard

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE workspace.default.atividades_contabeis_gold AS
# MAGIC WITH resumo AS (
# MAGIC     SELECT
# MAGIC         ano,
# MAGIC         SUM(horas_totais) AS horas_totais,
# MAGIC         SUM(horas_economizadas) AS horas_economizadas,
# MAGIC         ROUND(
# MAGIC             SUM(horas_economizadas) / SUM(horas_totais) * 100,
# MAGIC             2
# MAGIC         ) AS percentual_economia
# MAGIC     FROM workspace.default.atividades_contabeis_silver
# MAGIC     GROUP BY ano
# MAGIC ),
# MAGIC comparacao AS (
# MAGIC     SELECT
# MAGIC         ano,
# MAGIC         horas_totais,
# MAGIC         horas_economizadas,
# MAGIC         percentual_economia,
# MAGIC         LAG(horas_economizadas) OVER (ORDER BY ano)
# MAGIC             AS horas_ano_anterior
# MAGIC     FROM resumo
# MAGIC )
# MAGIC SELECT
# MAGIC     ano,
# MAGIC     horas_totais,
# MAGIC     horas_economizadas,
# MAGIC     horas_totais - horas_economizadas AS horas_restantes,
# MAGIC     percentual_economia,
# MAGIC     ROUND(
# MAGIC         (horas_economizadas - horas_ano_anterior)
# MAGIC         / horas_ano_anterior * 100,
# MAGIC         2
# MAGIC     ) AS crescimento_yoy
# MAGIC FROM comparacao
# MAGIC ORDER BY ano;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM workspace.default.atividades_contabeis_gold
# MAGIC ORDER BY ano;
