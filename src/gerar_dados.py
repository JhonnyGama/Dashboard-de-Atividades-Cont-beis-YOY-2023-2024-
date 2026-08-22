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

    impacto = [
        round((horas_economizadas[i] / horas_totais[i]) * 100, 2)
        if horas_economizadas[i] > 0
        else 0
        for i in range(n)
    ]

    status = [
        "Automatizada" if horas_economizadas[i] > 0 else "Manual"
        for i in range(n)
    ]

    return pd.DataFrame(
        {
            "ano": ano,
            "atividade": atividades,
            "categoria": categorias,
            "horas_totais": horas_totais,
            "horas_economizadas": horas_economizadas,
            "impacto_percentual": impacto,
            "status": status,
        }
    )


df_2023 = gerar_dados_ano(2023, multiplicador_automacao=0.4, n=100)
df_2024 = gerar_dados_ano(2024, multiplicador_automacao=1.0, n=100)

df_final = pd.concat([df_2023, df_2024], ignore_index=True)
df_final.to_csv(
    "relatorio_atividades_contabeis_YOY_100_linhas.csv",
    index=False,
)
