# Gerador de relatórios de testes

Este projeto tem como objetivo visualizar os resultados de testes manuais/automatizados a partir de um arquivo CSV com dados de execução de testes. Usando bibliotecas como `pandas` para manipulação de dados e `plotly.express` para a visualização gráfica, ele filtra os dados e gera gráficos interativos mostrando a distribuição de testes que passaram, falharam ou foram bloqueados em cada suíte de testes.

## Pré-requisitos

### 1. Criação do Ambiente Virtual

A criação do ambiente virtual é importante para isolar as dependências do projeto.

No Windows:

```
python -m venv venv
```

No Linux/macOS:

```
python3 -m venv venv
```

Isso cria um diretório chamado `venv`, onde todas as dependências serão instaladas.

### 2. Ativação do Ambiente Virtual

No Windows (Powershell):

```
.\venv\Scripts\Activate
```

No Linux/macOS:

```
source venv/bin/activate
```

Após ativar, o prompt de comando deve mostrar algo como `(venv)` no início, indicando que você está trabalhando dentro do ambiente virtual.

### 3. Dependências

Antes de rodar o projeto, certifique-se de ter os seguintes pacotes instalados:

- **Python 3.6+**
- **Pandas**: Para manipulação e análise dos dados
- **Plotly**: Para criação de gráficos interativos

Você pode instalar as bibliotecas necessárias usando o `pip`:

```
pip install requirements.txt
```

## Execução

1. Inclua o caminho do arquivo para o qual deseja gerar o relatório, no arquivo `.env.example`
2. Altere o `.env.example` para `.env`
3. Execute o script para gerar o relatório:

```
python tests_report.py
```
