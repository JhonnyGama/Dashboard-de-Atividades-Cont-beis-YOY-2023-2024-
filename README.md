# Documentação Completa — Dashboard de Atividades Contábeis YOY (2023–2024)

## 📌 1. Visão Geral do Projeto

Este projeto tem como objetivo criar um dashboard analítico no **Looker Studio**, comparando atividades contábeis entre os anos de **2023 e 2024**, incluindo métricas de produtividade, automação e impacto percentual.

Os dados são **artificiais**, gerados via Python, exportados em CSV, armazenados no **Google Sheets** e conectados ao Looker Studio para visualização.

---

## 📌 2. Arquitetura da Solução


<img width="344" height="373" alt="Arquitetura" src="https://github.com/user-attachments/assets/1826ea36-388f-4581-8ec5-9bdaf1098cd9"/>



---

## 📌 3. Estrutura do Dataset

O dataset final contém **200 linhas**, sendo:

* 100 linhas referentes a 2023
* 100 linhas referentes a 2024

### **Colunas do dataset**

| Coluna                 | Descrição                                                   |
| ---------------------- | ----------------------------------------------------------- |
| **ano**                | Ano da atividade (2023 ou 2024)                             |
| **atividade**          | Nome da atividade contábil realizada                        |
| **categoria**          | Categoria geral da atividade                                |
| **horas_totais**       | Horas necessárias para execução manual                      |
| **horas_economizadas** | Horas economizadas via automação                            |
| **impacto_percentual** | Percentual de economia: `horas_economizadas / horas_totais` |
| **status**             | "Automatizada" ou "Manual"                                  |

---

## 📌 4. Código Utilizado (Python)

O código gera dados sintéticos balanceados entre atividades manuais e automatizadas.
Inclui variação entre 2023 (menos automações) e 2024 (mais automações).

```python
import numpy as np
import pandas as pd

rng = np.random.default_rng()

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
    "Revisão de Categorias"
]

categorias_base = [
    "Provisões", "Reclassificações", "Conciliações", "Fechamento",
    "Lançamentos", "Ajustes", "Controles", "Importações",
    "Relatórios", "Revisões"
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
        if horas_economizadas[i] > 0 else 0
        for i in range(n)
    ]

    status = [
        "Automatizada" if horas_economizadas[i] > 0 else "Manual"
        for i in range(n)
    ]

    df = pd.DataFrame({
        "ano": ano,
        "atividade": atividades,
        "categoria": categorias,
        "horas_totais": horas_totais,
        "horas_economizadas": horas_economizadas,
        "impacto_percentual": impacto,
        "status": status
    })

    return df

# 2023 → menos automações
df_2023 = gerar_dados_ano(2023, multiplicador_automacao=0.4, n=100)

# 2024 → automações melhores
df_2024 = gerar_dados_ano(2024, multiplicador_automacao=1.0, n=100)

# Dataset final
df_final = pd.concat([df_2023, df_2024], ignore_index=True)

df_final.to_csv("relatorio_atividades_contabeis_YOY_100_linhas.csv", index=False)
```

---

## 📌 5. Estrutura no Google Sheets

Arquivo usado como intermediário:
**Aba "Dataset"**

### Boas práticas aplicadas:

* Cabeçalhos limpos e sem espaços especiais: (Ex: horas_totais, horas_economizadas).
* Colunas padronizadas em snake_case: (Ex: horas_totais em vez de Horas Totais).
* Tipos de dados validados: (Números como numéricos, textos como texto).
* Uso de filtros e congelamento da primeira linha: (Essencial para navegação e conexão com o Looker Studio).
* Atualização manual/automática do CSV quando necessário: (Garantindo que a fonte do dashboard esteja sempre fresca).

---

## 📌 6. Construção do Dashboard no Looker Studio

### Origens de dados:

* Conector: **Google Sheets**
* Atualização: automática a cada acesso

### **Visuais incluídos:**

* KPIs de Desempenho: Horas totais, Horas salvas (com variação percentual YOY) e % de Economia.
* Gráfico de Barras Horizontais: "Conciliação de Contas e Geração de Relatórios Consomem Mais Tempo" (Visão ranqueada da produtividade).
* Gráfico de Linha: "Horas Salvas Aumentam 350% de 2023 para 2024" (Visão YOY da economia, com anotação da causa).
* Gráfico de Barras Verticais: "Distribuição Manual vs. Automática" (Visão da proporção de esforço).
* Tabela de Detalhes: Tabela detalhada de Atividade, Categoria, Status, Horas Totais, Horas Salvas e Impacto %.

---

## 📌 7. Métrica Criada no Looker Studio

### 💡 **Cálculo principal:**


#### **Produtividade (%)**

```
SUM(horas_economizadas) / SUM(horas_totais)
```
---

## 📌 8. Análises Possíveis

* Identificar quais categorias tiveram maior ganho com automação
* Comparar eficiência entre 2023 e 2024
* Avaliar atividades com maior potencial de automação futura
* Encontrar gargalos nas atividades manuais recorrentes

---

## 📌 9. Possíveis Expansões

* Adicionar dados de 2025, criando tendência de 3 anos
* Criar um modelo de simulação de automação futura
* Criar dashboard operacional para monitoramento mensal
* Integrar com BigQuery para atualizar automaticamente

---

## 📌 10. Links Importantes

* **Dashboard (Looker Studio):** [Looker Studio](https://lookerstudio.google.com/reporting/6f13e190-cc9b-44b3-8044-c603cfb119cc)
* **Planilha intermediária (Google Sheets):** [Google Sheets](https://docs.google.com/spreadsheets/d/1jgw7ri9L8XyLrVRAeubjP291Y0Hq-hTIa-NzjGdoTFI/edit?usp=sharing)

---

## 📸 Campos para Inserção de Imagens

A seguir estão seções preparadas para você inserir imagens do dashboard, do Looker Studio e do Google Sheets:

### **Imagem 1 — Visão Geral do Dashboard**

<img width="873" height="656" alt="Visao geradl do dashboard" src="https://github.com/user-attachments/assets/a558b0ab-283c-41f8-b50f-b419ee174123" />


### **Imagem 2 — Fonte de Dados (Google Sheets)**

<img width="835" height="783" alt="google sheets" src="https://github.com/user-attachments/assets/28a670e5-1572-4d08-8476-2a8472868ca5" />


### **Imagem 3 — Estrutura dos Campos no Looker Studio**

<img width="238" height="381" alt="estrutura de dados looker" src="https://github.com/user-attachments/assets/10566496-2158-44eb-bbb0-113456c9c502" />

---

