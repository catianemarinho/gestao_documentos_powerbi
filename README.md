# Gestão de assinaturas de documentos com Python e Power BI

Este repositório contém um projeto de gestão de assinaturas de documento digital utilizando Python para consumo da API Rest e geração do DataFrame, integrando com o Power BI para a criação de um dashboard interativo. O objetivo desse projeto é permitir que os usuários possam acompanhar o processo de assinatura de contratos do seu negócio, de forma eficiente e visualmente atrativa.

<div align="center">
    <img src="https://github.com/catianemarinho/acompanhamento_de_acoes/assets/97571709/23cc61da-e87f-46cb-8f76-1b8dedf336e4">
</div>

## Funcionalidades

- Extração de Dados: Utilizei a biblioteca `requests` para extrair dados da API Rest do sistema utilizado paga a gestão dos documentos assinados digitalmente. Isso inclui "key" do documento, data de upload, data de finalização, status atual e outros indicadores relevantes.

- Pré-processamento: Os dados extraídos são pré-processados para garantir que estejam em um formato adequado para análise. Isso pode incluir tratamento de valores ausentes, criação do DataFrame e outros indicadores personalizados.

- Integração com Power BI: O DataFrame criado é importado para o Power BI, uma ferramenta de visualização de dados poderosa. O Power BI nos permite criar gráficos, tabelas e outros elementos visuais para construir um dashboard interativo.

- Criação de Dashboard: No Power BI, criamos um dashboard interativo que exibe os dados dos documentos de forma clara e compreensível. Os usuários podem filtrar os dados por status, período de tempo ou outros critérios, permitindo uma análise detalhada.

## Estrutura do Repositório

O repositório está organizado da seguinte maneira:

- `script_documents.py`: Este arquivo contém o código em Python responsável por extrair, pré-processar os dados e gerar o DataFrame utilizando as bibliotecas `requests e pandas`.

- `dashboard_documents.pbix`: Aqui você encontrará o arquivo do Power BI que contém o dashboard interativo criado com base nos dados extraídos. Este arquivo pode ser aberto no Power BI Desktop.

- `README.md`: O arquivo que você está lendo agora, fornecendo informações sobre o projeto, sua finalidade e instruções básicas de uso.

## Como Utilizar

1. Certifique-se de ter o Python instalado em seu sistema.

2. Instale as bibliotecas necessárias. Você pode fazer isso executando o seguinte comando:

   ```bash
   pip install requests
   pip install pandas
3. Altere o arquivo `script_documents.py` inserindo a sua credencial da API Rest
4. Vá para a pasta e execute o script de extração de dados, por exemplo:
    ```bash
    python script_documents.py
4. Abra o arquivo `dashboard_documents.pbix` usando o Power BI Desktop.
5. No Power BI Desktop, atualize a fonte de dados para refletir os dados extraídos no passo 4.
6. Explore o dashboard interativo criado no Power BI. Use filtros e gráficos para analisar o desempenho das ações ao longo do tempo.

## Contribuições

Contribuições para este projeto são bem-vindas! Se você tiver sugestões de melhorias, correções de bugs ou novas funcionalidades, sinta-se à vontade para enviar um pull request.

## Aviso Legal

Este projeto é apenas para fins educacionais e informativos. Não oferece aconselhamento financeiro nem recomendações de investimento. Sempre realize sua própria pesquisa antes de tomar decisões financeiras.

## Contato

- **mail**: cat.50@hotmail.com