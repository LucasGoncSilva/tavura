<h1 align="center">
  <img src="./logo.svg" height="300" width="300" alt="Logo tavura"/><br>
  Tavura
</h1>

![GitHub License](https://img.shields.io/github/license/AndersonJader0/AlphaTask?labelColor=101010)

<!-- ![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/AndersonJader0/AlphaTask/XXXXXX.yml?style=flat&labelColor=%23101010) -->

Este projeto de código aberto foi desenvolvido para facilitar o gerenciamento de Product Backlog Items (PBIs) no Azure DevOps. A ferramenta automatiza a coleta e organização de dados, oferecendo uma visão consolidada dos itens do backlog em um relatório Excel, ideal para análise e planejamento por equipes de sustentação.

O principal objetivo da automação é coletar informações sobre PBIs com base em seus status ou estados, como "Done", "Accepted", "Review", e organizar essas informações de maneira estruturada em uma tabela Excel. Isso permite que as equipes de sustentação tenham uma visão clara e ordenada dos itens a serem priorizados ou revisados, otimizando o fluxo de trabalho e a tomada de decisões.

A automação percorre os work items registrados no Azure DevOps, com foco específico nos PBIs. O script coleta dados essenciais como:

- Número do PBI: Identificador único do backlog item.
- Nome: Nome descritivo do PBI para fácil identificação.
- Effort: Esforço estimado ou horas trabalhadas no item.
- Status: Estado atual do PBI (e.g., "New", "Review", "Done").
- Feature: Subgrupo ou categoria ao qual o PBI pertence.

Esses dados são compilados em um relatório Excel bem estruturado, permitindo o trabalho colaborativo posterior.

A ferramenta foi projetada com foco em equipes de sustentação de empresas, que lidam diariamente com o acompanhamento de PBIs no Azure DevOps. Ela simplifica a tarefa de organizar dados do backlog, economizando tempo e reduzindo a necessidade de trabalho manual repetitivo. A seguir os benefícios do uso da ferramenta:

- Automação de tarefas repetitivas: Reduz a necessidade de extração e organização manual de dados.
- Relatórios customizados: Geração de relatórios Excel com informações essenciais para análises detalhadas.
- Eficiência operacional: Melhora a visibilidade do progresso dos itens no backlog, ajudando na priorização e resolução de problemas.
- Interface amigável: Possibilidade de interação através de uma interface gráfica, tornando o uso acessível para qualquer membro da equipe.

## Stack

![Python](https://img.shields.io/badge/Python-blue?style=for-the-badge&logo=python&logoColor=FFD43B)

![Selenium](https://img.shields.io/badge/selenium-338221?style=for-the-badge&logo=selenium&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

<!-- ![Azure](https://img.shields.io/badge/azure%20devops-%230072C6?style=for-the-badge&logo=devops&logoColor=white) -->

![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Ruff logo](https://img.shields.io/badge/Ruff-2b0231?style=for-the-badge&logo=ruff)

## Licença

This project is under [MPLv2 - Mozilla Public License Version 2.0](https://choosealicense.com/licenses/mpl-2.0/). A short and simple permissive license with conditions only requiring preservation of copyright and license notices. Licensed works, modifications, and larger works may be distributed under different terms and without source code.
