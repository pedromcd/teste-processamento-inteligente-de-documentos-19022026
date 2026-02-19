# Teste Técnico (Extração de informações em Faturas de Energia)

Para garantir o eficiente gerenciamento dos créditos de energia provenientes de usinas de energia renovável, é fundamental a extração precisa e automática de dados das notas fiscais de energia elétrica. Além disso, possuir conhecimento sobre faturas de energia elétrica é importante para o sucesso na gestão desses recursos.

Logo, é proposto dois testes como parte da avaliação dos conhecimentos técnicos e teóricos dos candidatos. Essa avaliação tem o objetivo de medir a compreensão do participante no contexto da extração de dados de notas fiscais e no entendimento básico de faturas de energia elétrica.

# Teste 1

Em busca pela eficiência na leitura de faturas, a equipe de desenvolvimento propõe a criação de uma rotina que, a partir de faturas de energia elétrica em formato de PDF, seja capaz de extrair importantes informações.

Nesta atividade, você deve editar o arquivo read.py e desenvolver uma rotina capaz de realizar a leitura da fatura fatura_cpfl.pdf em formato de PDF e retornar as seguintes informações:

- Titular da fatura (Nome e Documento)
- Endereço completo do titular da fatura
- Classificação da Instalação
- Número da instalação
- Valor a Pagar para a distribuidora
- Data de Vencimento
- Mês ao qual a fatura é referente
- Tarifa total com tributos
- Tarifa total Aneel
- Quantidade em kWh do Consumo da fatura
- Saldo em kWh acumulado na Instalação
- Somatório das quantidades das energias compensadas (injetadas)
- Somatório dos Valores Totais das Operações R$
- Contribuição de iluminação Pública
- Alíquotas do ICMS, PIS e COFINS em %
- Linha digitável para pagamento

Organize a saída e visualização das informações extraídas.

# Documentação do Teste 1

A solução implementada realiza a leitura do arquivo, identifica padrões textuais específicos e retorna os dados estruturados de forma organizada para visualização no terminal.

O processamento foi desenvolvido visando clareza, organização e facilidade de manutenção do código.

## Requisitos de Execução

Para executar o projeto corretamente, é necessário:

- Python 3.x instalado
- Instalação da biblioteca pdfplumber

Instalação da dependência:
```
pip install pdfplumber
```

Execução do código:
```
python read.py
```

## Estratégia de Desenvolvimento

A implementação foi estruturada seguindo um fluxo de processamento dividido em etapas:

- Leitura do arquivo PDF
- Extração completa do texto da fatura
- Identificação de padrões textuais
- Extração das informações solicitadas
- Organização dos dados em estrutura dicionário
- Exibição formatada da saída

Utilizei a biblioteca pdfplumber para extração do texto, pois o arquivo fornecido contém texto estruturado (não é um documento escaneado), eliminando a necessidade de OCR.

## Extração das Informações

As seguintes informações foram extraídas:

- Titular (nome e CPF)
- Endereço completo
- Classificação da instalação
- Número da instalação
- Valor total a pagar
- Data de vencimento
- Mês de referência
- Consumo total em kWh
- Saldo acumulado em kWh
- Valores de energias compensadas
- Contribuição de iluminação pública
- Alíquotas de ICMS, PIS e COFINS
- Linha digitável para pagamento

Para isso, utilizei expressões regulares específicas baseadas nos padrões identificados no documento.

## Organização da Saída

Os dados são organizados em um dicionário Python e exibidos de forma estruturada no terminal, juntamente com a identificação do arquivo processado.

A saída apresenta:

- Identificação do arquivo analisado
- Lista organizada dos campos extraídos
- Visualização clara para validação manual

Essa abordagem facilita testes com diferentes faturas e possibilita futura exportação para formatos como JSON ou CSV.

# Teste 2

Contexto: Você recebeu a fatura "fatura_cemig.pdf" e deve desenvolver um script para extrair seus dados. Antes de iniciar a programação, é essencial compreender e interpretar as informações presentes nesta fatura.

Atividade: Analise a fatura e redija um documento respondendo os pontos abaixo. As respostas podem ser inseridas neste 'README'.

 - Identifique as principais diferenças entre a fatura "fatura_cemig.pdf" e uma fatura convencional de energia elétrica "fatura_cemig_convencional.pdf".
 - Descreva e explique os termos e valores apresentados na seção "Valores Faturados" da fatura "fatura_cemig.pdf".
 - Considerando que a instalação da "fatura_cemig.pdf" participa do Sistema de Compensação de Energia Elétrica, identifique e explique qual informação na seção "Informações Gerais" da fatura é considerada a mais importante.
 - Identifique o consumo da instalação referente ao mês de julho de 2023.

# Resposta para o Teste 2

## 1 - Principais diferenças entre a fatura fatura_cemig.pdf e a fatura fatura_cemig_convencional.pdf

A principal diferença entre as duas faturas está relacionada à participação da instalação no Sistema de Compensação de Energia Elétrica (SCEE).

Na fatura fatura_cemig.pdf, observa-se a presença de itens específicos relacionados à geração distribuída e compensação de energia, como:

- Energia SCEE s/ ICMS
- Energia compensada GD II
- Energia compensada adicional

Esses itens indicam que a unidade consumidora participa de um sistema de compensação de energia, no qual a energia gerada (por exemplo, por meio de usina solar) é convertida em créditos e utilizada para abater o consumo da rede.

Já na fatura fatura_cemig_convencional.pdf, não há registros de compensação de energia ou créditos acumulados. A cobrança é composta basicamente por:

- Energia Elétrica
- Contribuição de Iluminação Pública
- Total da fatura

Ou seja, a fatura convencional apresenta apenas consumo faturado, enquanto a outra inclui geração, compensação e abatimentos.

## 2 - Descrição da seção “Valores Faturados” da fatura fatura_cemig.pdf

A seção “Valores Faturados” detalha todos os itens que compõem o valor final da fatura, incluindo cobranças e abatimentos.

Os principais itens observados são:

- Energia Elétrica (kWh): representa o consumo efetivamente faturado no período, com quantidade, preço unitário e valor total - correspondente.
- Energia SCEE s/ ICMS: relacionada ao Sistema de Compensação de Energia Elétrica, indicando parcela de energia vinculada ao sistema de compensação, sem incidência de ICMS.
- Energia compensada GD II: corresponde à energia compensada proveniente de geração distribuída. Esse valor aparece negativo, pois representa um crédito que reduz o total a pagar.
- Energia compensada adicional: também aparece como valor negativo, atuando como abatimento na fatura.
- Bônus Itaipu: desconto aplicado conforme legislação específica, reduzindo o valor final.
- Contribuição de Iluminação Pública Municipal: tributo municipal cobrado junto à conta de energia.
- O valor final (“TOTAL”) resulta da soma dos valores positivos (cobranças) menos os valores negativos (compensações e bônus).

## 3 - Informação mais importante na seção “Informações Gerais”

Considerando que a instalação participa do Sistema de Compensação de Energia Elétrica, a informação mais relevante na seção “Informações Gerais” é o:

**Saldo Atual de Geração (kWh)**

Esse saldo representa a quantidade de energia excedente gerada e acumulada como crédito. Esses créditos podem ser utilizados para compensar consumo futuro, reduzindo o valor das próximas faturas.

Para a gestão eficiente de créditos de energia renovável, essa informação é essencial, pois permite acompanhar o estoque de energia disponível para compensação.

## 4 - Consumo referente a Julho de 2023

No histórico de consumo da fatura fatura_cemig.pdf, o consumo referente ao mês de JUL/23 é:

**199 kWh**

Esse valor representa a quantidade de energia consumida no período de faturamento correspondente ao mês de julho de 2023.

# Requisitos dos Desafios:

1. Utilize a linguagem Python para desenvolver a solução.
2. No mesmo README, inclua uma seção detalhada que explique claramente os passos necessários para executar o código. Certifique-se de que as instruções sejam precisas, organizadas e fáceis de entender, pois os avaliadores seguirão essa documentação.
3. Faça um fork do repositório, para iniciar o desenvolvimento.
4. A entrega deve ser realizada por meio de um pull request para o repositório original. Caso não consiga, os arquivos podem ser enviados para o email falecom@dg.energy, porém com penalidade de pontos.
5. Abra o pull request também faltando 5 minutos para o prazo final da entrega do teste. Se o pull request for realizado antes dos 5 minutos restantes haverá eliminação do candidato.
6. A entrega deve ser realizada até às 12:30h.
