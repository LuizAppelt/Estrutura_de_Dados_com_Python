# main.py
import os
from entidades import Cliente, Produto, Venda
from estruturas import ListaEncadeada, Fila, Pilha

COR_CADASTRO = '\033[96m'  # Ciano
COR_LISTAGEM = '\033[92m'  # Verde
COR_OPERACAO = '\033[93m'  # Amarelo
COR_RELATORIO = '\033[95m' # Roxo
COR_SISTEMA = '\033[91m'   # Vermelho
RESET = '\033[0m'          # Volta para a cor padrao do terminal

# Inicializacao estruturas globais
clientes = ListaEncadeada()
produtos = ListaEncadeada()
vendas = Fila()
historico = Pilha()

# Nomes arquivos
ARQ_CLIENTES = 'clientes.txt'
ARQ_PRODUTOS = 'produtos.txt'
ARQ_VENDAS = 'vendas.txt'

# --- FUNCOES ---

def carregar_dados():
    # Carrega clientes
    if os.path.exists(ARQ_CLIENTES):
        try:
            with open(ARQ_CLIENTES, 'r') as f:
                for linha in f:
                    linha = linha.strip()
                    if linha == "": continue
                    partes = linha.split(';')
                    if len(partes) == 2:
                        clientes.inserir(Cliente(int(partes[0]), partes[1]))
        except Exception as e:
            print("Erro ao carregar clientes:", e)

    # Carrega produtos
    if os.path.exists(ARQ_PRODUTOS):
        try:
            with open(ARQ_PRODUTOS, 'r') as f:
                for linha in f:
                    linha = linha.strip()
                    if linha == "": continue
                    partes = linha.split(';')
                    if len(partes) == 4:
                        produtos.inserir(Produto(int(partes[0]), partes[1], int(partes[2]), float(partes[3])))
        except Exception as e:
            print("Erro ao carregar produtos:", e)

    # Carrega vendas
    if os.path.exists(ARQ_VENDAS):
        try:
            with open(ARQ_VENDAS, 'r') as f:
                for linha in f:
                    linha = linha.strip()
                    if linha == "": continue
                    partes = linha.split(';')
                    if len(partes) == 5:
                        vendas.enfileirar(Venda(int(partes[0]), int(partes[1]), int(partes[2]), int(partes[3]), float(partes[4])))
        except Exception as e:
            print("Erro ao carregar vendas:", e)

def salvar_dados():
    # Salva todos os clientes reescrevendo o arquivo
    try:
        with open(ARQ_CLIENTES, 'w') as f:
            for c in clientes.listar_todos():
                f.write(f"{c.id};{c.nome}\n")
    except Exception as e:
        print("Erro ao salvar clientes:", e)

    # Salva todos os produtos
    try:
        with open(ARQ_PRODUTOS, 'w') as f:
            for p in produtos.listar_todos():
                f.write(f"{p.id};{p.nome};{p.quantidade};{p.preco}\n")
    except Exception as e:
        print("Erro ao salvar produtos:", e)

    # Salva todas as vendas
    try:
        with open(ARQ_VENDAS, 'w') as f:
            for v in vendas.listar_todos():
                f.write(f"{v.id};{v.id_cliente};{v.id_produto};{v.quantidade};{v.valor_total}\n")
    except Exception as e:
        print("Erro ao salvar vendas:", e)




        