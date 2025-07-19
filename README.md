📄 Exportador NF-e
O Exportador NF-e é uma ferramenta desenvolvida em Python com interface gráfica que facilita a análise de notas fiscais eletrônicas (NF-e) em formato XML. Ele extrai automaticamente as informações dos produtos, emitente e destinatário e exporta os dados para um arquivo Excel (.xlsx), simplificando o processo de conferência e análise.

🚀 Funcionalidades
Leitura de arquivos XML de NF-e;

Extração de dados como:

CNPJ e Razão Social do emitente e destinatário;

Datas de emissão e saída;

Produtos, códigos, quantidades, valores unitários e totais;

Exportação automática dos dados para planilhas Excel;

Interface gráfica simples com Tkinter.

🛠 Tecnologias utilizadas

Python 3

Tkinter (interface gráfica)

pandas (manipulação de dados)

openpyxl (exportação para Excel)

xml.etree.ElementTree (leitura de XML)

📝 Exemplo de saída

O arquivo gerado conterá colunas como:

Emitente CNPJ

Emitente Razão

Destinatário CNPJ

Destinatário Razão

Data Emissão

Data Saída

Produto

Código

Quantidade

Valor Unitário

Valor Total

⚠️ Observações

O projeto espera que os XMLs estejam no layout padrão da NF-e.

Apenas arquivos .xml são processados.

O programa ignora arquivos que apresentarem erros de leitura.
