# 🛡️ Scripts de Automação e Segurança (Python)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

Este repositório contém scripts que desenvolvi para automatizar tarefas de rotina de TI, com foco em **Auditoria de Acessos (IAM)** e **Análise de Logs**.
O objetivo é usar Python para garantir segurança e poupar tempo em tarefas manuais.

## 📂 O que tem aqui?

### 1. Auditoria de IAM (`iam_audit.py`)
* **O problema:** Funcionários são desligados, mas às vezes o acesso deles continua ativo no sistema.
* **O que o script faz:** Cruza a base de dados do RH (CSV) com a lista de usuários do Sistema. Se achar alguém com status "Desligado" mas com acesso ativo, ele gera um relatório Excel para bloqueio imediato.
* **Libs:** Pandas.

### 2. Scanner de Logs (`log_scanner.py`)
* **O problema:** É difícil achar ataques no meio de milhares de linhas de log.
* **O que o script faz:** Lê arquivos de log, procura por falhas de login ("Login failed") e avisa se um mesmo IP errou a senha muitas vezes seguidas (possível Brute Force).

### 3. Organizador de Arquivos (`clean_downloads.py`)
* **O problema:** Pastas de Downloads/Rede bagunçadas.
* **O que o script faz:** Monitora uma pasta e move os arquivos automaticamente para subpastas (Imagens, Documentos, etc) baseado na extensão.

## 🚀 Como usar

1. Clone o repositório.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
