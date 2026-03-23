# 📦 Estrutura de Dados

## 📚 Disciplina

Organização e Abstração na Programação - Professor: Augusto Ortolan

## 🧾 Sistema de Estoque e Vendas em Python

Mini Sistema de Estoque e Vendas com Persistência em Arquivos

## 👥 Integrantes

Gabriel Pasuch Granja - 1138917

Guilherme Silva - 1133534

Guilherme Vieira Marques - 1138951

Luiz Henrique Appelt Weller - 1138930

Ricardo Trento Werner - 1138812

---

## 📌 Descrição do Sistema

Este projeto consiste no desenvolvimento de um sistema de gerenciamento de estoque e vendas, executado no terminal, utilizando a linguagem Python.

O sistema permite:

* Cadastro e listagem de clientes;
* Cadastro e controle de produtos em estoque;
* Realização de vendas;
* Consulta de histórico de vendas;
* Desfazer a última operação realizada.

Além disso, o sistema realiza **persistência automática dos dados** utilizando arquivos `.csv` ou `.txt`, garantindo que as informações não sejam perdidas ao encerrar o programa.

---

## 🧠 Conceitos Aplicados

O projeto foi desenvolvido com foco na aplicação prática dos seguintes conceitos:

* Programação Orientada a Objetos (POO)
* Estruturas de Dados
* Manipulação de arquivos
* Tratamento de erros
* Organização e modularização de código

## 🏗️ Estruturas de Dados Utilizadas

### 🔗 Lista Encadeada

Utilizada para armazenar:

* Produtos
* Clientes

Permite:

* Inserção
* Remoção
* Busca
* Listagem

Foi implementada manualmente, sem uso de estruturas prontas da linguagem.

---

### 📥 Fila (FIFO)

Utilizada para armazenar:

* Vendas realizadas

As vendas são registradas na ordem em que acontecem, garantindo controle cronológico.

---

### 📤 Pilha (LIFO)

Utilizada para:

* Armazenar histórico de operações

Permite a funcionalidade de:

* Desfazer a última ação realizada

---

## 💾 Persistência de Dados

O sistema utiliza arquivos locais para armazenar os dados:

* `clientes.csv` ou `clientes.txt`
* `produtos.csv` ou `produtos.txt`
* `vendas.csv` ou `vendas.txt`

### 🔄 Funcionamento:

* Ao iniciar o sistema, os arquivos são carregados automaticamente
* Caso não existam, são criados automaticamente
* Após qualquer alteração, os dados são salvos automaticamente
* Não existe opção manual de salvar ou carregar

Isso garante:

* Continuidade dos dados entre execuções
* Segurança das informações

---

## ⚙️ Funcionalidades do Sistema

1. Cadastrar cliente
2. Listar clientes
3. Cadastrar produto
4. Listar produtos
5. Pesquisar produto
6. Realizar venda
7. Visualizar fila de vendas
8. Desfazer última operação
9. Exibir valor total do estoque
10. Exibir valor total de vendas
11. Exibir clientes e total gasto
12. Sair

---

## 📏 Regras de Negócio

* Cliente deve estar cadastrado para realizar compra
* Produto deve estar cadastrado para venda
* Quantidade deve ser maior que zero
* Preço deve ser maior que zero
* Estoque nunca pode ficar negativo
* Campos obrigatórios não podem estar vazios
* Operações inválidas não alteram os dados

---

## 🛡️ Tratamento de Erros

O sistema foi desenvolvido para ser resiliente, tratando erros como:

* Entrada inválida do usuário
* IDs inexistentes
* Arquivos inexistentes ou corrompidos
* Tentativas de operações inválidas
* Falhas de leitura/escrita de arquivos
* Dados inconsistentes

Sempre que ocorre um erro:

* O usuário é informado
* A operação é cancelada
* O sistema continua funcionando normalmente

---

## ▶️ Como Executar o Projeto

### ✅ Pré-requisitos:

* Python 3 instalado

### 🚀 Passos:

1. Clone o repositório:

```bash
git clone https://github.com/LuizAppelt/Estrutura_de_Dados_com_Python
```

2. Acesse a pasta do projeto:

```bash
cd seu-repositorio
```

3. Execute o sistema:

```bash
python main.py
```

---

## 📁 Estrutura do Projeto (Exemplo)

```
📦 projeto
 ┣ 📜 main.py
 ┣ 📜 produto.py
 ┣ 📜 cliente.py
 ┣ 📜 venda.py
 ┣ 📜 lista_encadeada.py
 ┣ 📜 fila.py
 ┣ 📜 pilha.py
 ┣ 📜 clientes.csv
 ┣ 📜 produtos.csv
 ┣ 📜 vendas.csv
 ┗ 📜 README.md
```

---

## 📌 Observações Finais

* O sistema é totalmente executado via terminal.
* O foco principal é a aplicação prática de estruturas de dados.
* O código foi desenvolvido com organização e comentários explicativos.
* Todos os integrantes devem contribuir com commits reais no projeto.
