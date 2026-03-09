import customtkinter
from CTkMessagebox import CTkMessagebox
import funcoes  # Importa seu arquivo de lógica de backend

# Define a aparência padrão
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # --- Configurações da Janela Principal ---
        self.title("Gerenciador de Estoque")
        self.geometry("1000x600")

        # Carrega os dados iniciais usando sua função
        try:
            self.estoque, _ = funcoes.carregar_estoque_csv()
        except FileNotFoundError:
            self.estoque = []
        except Exception as e:
            self.estoque = []
            CTkMessagebox(title="Erro ao Carregar",
                          message=f"Não foi possível carregar o estoque.csv: {e}",
                          icon="cancel")

        # --- Layout da Janela ---
        # Configura o grid para ter duas colunas: controles (peso 1) e lista (peso 2)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # --- Frame da Esquerda (Controles) ---
        self.frame_controles = customtkinter.CTkFrame(self, width=350)
        self.frame_controles.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # --- Frame da Direita (Lista) ---
        self.frame_lista = customtkinter.CTkFrame(self)
        self.frame_lista.grid(row=0, column=1, padx=(0, 20), pady=20, sticky="nsew")

        # --- Widgets do Frame de Controles (Esquerda) ---
        self.tabview = customtkinter.CTkTabview(self.frame_controles)
        self.tabview.pack(padx=20, pady=20, fill="both", expand=True)

        self.tab_cadastrar = self.tabview.add("Cadastrar")
        self.tab_editar = self.tabview.add("Editar")
        self.tab_excluir = self.tabview.add("Excluir / Limpar")

        self.criar_widgets_cadastrar()
        self.criar_widgets_editar()
        self.criar_widgets_excluir()

        # --- Widgets do Frame de Lista (Direita) ---
        self.label_lista = customtkinter.CTkLabel(self.frame_lista, text="Lista de Produtos",
                                                  font=customtkinter.CTkFont(size=16, weight="bold"))
        self.label_lista.pack(padx=10, pady=10)

        # Caixa de texto para exibir a lista
        self.textbox_lista = customtkinter.CTkTextbox(self.frame_lista, state="disabled", font=("Consolas", 13))
        self.textbox_lista.pack(padx=20, pady=10, fill="both", expand=True)

        self.btn_atualizar_lista = customtkinter.CTkButton(self.frame_lista, text="Atualizar Lista",
                                                           command=self.gui_atualizar_lista)
        self.btn_atualizar_lista.pack(padx=20, pady=(0, 20), fill="x")

        # --- Carregamento Inicial ---
        self.gui_atualizar_lista()

    # --- Funções para criar os widgets das abas ---

    def criar_widgets_cadastrar(self):
        frame = self.tab_cadastrar
        
        # Nome
        self.label_cad_nome = customtkinter.CTkLabel(frame, text="Nome do Produto:")
        self.label_cad_nome.pack(padx=10, pady=(10, 5), anchor="w")
        self.entry_cad_nome = customtkinter.CTkEntry(frame, placeholder_text="Ex: Parafuso Sextavado")
        self.entry_cad_nome.pack(padx=10, pady=0, fill="x")

        # Quantidade
        self.label_cad_qtd = customtkinter.CTkLabel(frame, text="Quantidade:")
        self.label_cad_qtd.pack(padx=10, pady=(10, 5), anchor="w")
        self.entry_cad_qtd = customtkinter.CTkEntry(frame, placeholder_text="Ex: 100")
        self.entry_cad_qtd.pack(padx=10, pady=0, fill="x")

        # Preço
        self.label_cad_preco = customtkinter.CTkLabel(frame, text="Preço (R$):")
        self.label_cad_preco.pack(padx=10, pady=(10, 5), anchor="w")
        self.entry_cad_preco = customtkinter.CTkEntry(frame, placeholder_text="Ex: 15.50")
        self.entry_cad_preco.pack(padx=10, pady=0, fill="x")

        # Botão
        self.btn_cadastrar = customtkinter.CTkButton(frame, text="Cadastrar Produto", command=self.gui_cadastrar)
        self.btn_cadastrar.pack(padx=10, pady=20, fill="x")

    def criar_widgets_editar(self):
        frame = self.tab_editar

        # ID para Editar
        self.label_edit_id = customtkinter.CTkLabel(frame, text="ID do Produto para Editar:")
        self.label_edit_id.pack(padx=10, pady=(10, 5), anchor="w")
        self.entry_edit_id = customtkinter.CTkEntry(frame, placeholder_text="Digite o ID do produto")
        self.entry_edit_id.pack(padx=10, pady=0, fill="x")

        # Separador
        sep = customtkinter.CTkFrame(frame, height=2, fg_color="gray50")
        sep.pack(fill="x", padx=10, pady=15)
        
        self.label_edit_info = customtkinter.CTkLabel(frame, text="Novos Dados (deixe vazio para manter)")
        self.label_edit_info.pack(padx=10, pady=0, anchor="w")
        
        # Novo Nome
        self.label_edit_nome = customtkinter.CTkLabel(frame, text="Novo Nome:")
        self.label_edit_nome.pack(padx=10, pady=(10, 5), anchor="w")
        self.entry_edit_nome = customtkinter.CTkEntry(frame)
        self.entry_edit_nome.pack(padx=10, pady=0, fill="x")

        # Nova Quantidade
        self.label_edit_qtd = customtkinter.CTkLabel(frame, text="Nova Quantidade:")
        self.label_edit_qtd.pack(padx=10, pady=(10, 5), anchor="w")
        self.entry_edit_qtd = customtkinter.CTkEntry(frame)
        self.entry_edit_qtd.pack(padx=10, pady=0, fill="x")

        # Novo Preço
        self.label_edit_preco = customtkinter.CTkLabel(frame, text="Novo Preço (R$):")
        self.label_edit_preco.pack(padx=10, pady=(10, 5), anchor="w")
        self.entry_edit_preco = customtkinter.CTkEntry(frame)
        self.entry_edit_preco.pack(padx=10, pady=0, fill="x")

        # Botão
        self.btn_editar = customtkinter.CTkButton(frame, text="Salvar Edição", command=self.gui_editar)
        self.btn_editar.pack(padx=10, pady=20, fill="x")

    def criar_widgets_excluir(self):
        frame = self.tab_excluir

        # --- Excluir por ID ---
        self.label_del_id = customtkinter.CTkLabel(frame, text="ID do Produto para Excluir:")
        self.label_del_id.pack(padx=10, pady=(10, 5), anchor="w")
        self.entry_del_id = customtkinter.CTkEntry(frame, placeholder_text="Digite o ID")
        self.entry_del_id.pack(padx=10, pady=0, fill="x")

        self.btn_excluir = customtkinter.CTkButton(frame, text="Excluir Produto", command=self.gui_excluir,
                                                   fg_color="#db524b", hover_color="#b0423d")
        self.btn_excluir.pack(padx=10, pady=10, fill="x")

        # --- Limpar Lista ---
        sep = customtkinter.CTkFrame(frame, height=2, fg_color="gray50")
        sep.pack(fill="x", padx=10, pady=25)
        
        self.label_del_all = customtkinter.CTkLabel(frame, text="Ação Irreversível:", text_color="#db524b",
                                                     font=customtkinter.CTkFont(weight="bold"))
        self.label_del_all.pack(padx=10, pady=0, anchor="w")

        self.btn_limpar = customtkinter.CTkButton(frame, text="Limpar Toda a Lista de Produtos",
                                                  command=self.gui_limpar_lista,
                                                  fg_color="#c9241d", hover_color="#a31d17")
        self.btn_limpar.pack(padx=10, pady=10, fill="x")

    # --- Funções de Lógica da GUI ---

    def gui_atualizar_lista(self):
        """Puxa os dados da variável self.estoque e exibe no textbox."""
        self.textbox_lista.configure(state="normal")  # Habilita para escrever
        self.textbox_lista.delete("1.0", "end")  # Limpa o conteúdo

        if not self.estoque:
            self.textbox_lista.insert("1.0", "Nenhum produto cadastrado.")
        else:
            # Ordena a lista por ID para exibição
            estoque_ordenado = sorted(self.estoque, key=lambda p: p['id'])
            for produto in estoque_ordenado:
                linha = (f"ID: {produto['id']:<4} | "
                         f"Nome: {produto['nome']:<30} | "
                         f"Qtd: {produto['quantidade']:<5} | "
                         f"Preço: R$ {produto['preco']:.2f}\n")
                self.textbox_lista.insert("end", linha)

        self.textbox_lista.configure(state="disabled")  # Desabilita para o usuário

    def gui_cadastrar(self):
        """Pega os dados dos entries, valida e chama as funções do backend."""
        nome = self.entry_cad_nome.get().strip().upper()
        qtd_str = self.entry_cad_qtd.get().strip()
        preco_str = self.entry_cad_preco.get().strip().replace(",", ".")

        # --- Validações ---
        if not nome:
            CTkMessagebox(title="Erro", message="O nome do produto não pode estar vazio.", icon="cancel")
            return

        # Verifica duplicidade (lógica do seu 'cadastrar_produto')
        for produto in self.estoque:
            if produto['nome'].lower() == nome.lower():
                CTkMessagebox(title="Erro", message=f"O produto '{nome}' já está cadastrado (ID: {produto['id']}).",
                              icon="cancel")
                return
        
        try:
            quantidade = int(qtd_str)
            if quantidade < 0:
                 raise ValueError("Quantidade não pode ser negativa")
        except ValueError:
            CTkMessagebox(title="Erro", message="Quantidade inválida! Deve ser um número inteiro positivo.", icon="cancel")
            return
            
        try:
            preco = float(preco_str)
            if preco < 0:
                raise ValueError("Preço não pode ser negativo")
        except ValueError:
            CTkMessagebox(title="Erro", message="Preço inválido! Use ponto para decimais (ex: 10.50).", icon="cancel")
            return

        # --- Se tudo estiver OK ---
        try:
            id_atual = funcoes.gerar_novo_id(self.estoque)
            
            novo_produto = {
                "id": id_atual,
                "nome": nome,
                "quantidade": quantidade,
                "preco": preco
            }

            self.estoque.append(novo_produto)
            funcoes.salvar_estoque_csv(self.estoque)
            funcoes.registrar_log("Cadastro de novo produto", nome)
            
            CTkMessagebox(title="Sucesso", message=f"Produto '{nome}' cadastrado com sucesso!", icon="check")
            
            # Limpa os campos de cadastro
            self.entry_cad_nome.delete(0, "end")
            self.entry_cad_qtd.delete(0, "end")
            self.entry_cad_preco.delete(0, "end")
            
            self.gui_atualizar_lista() # Atualiza a lista
            self.tabview.set("Cadastrar") # Volta para a aba de cadastro

        except Exception as e:
            CTkMessagebox(title="Erro Inesperado", message=f"Ocorreu um erro: {e}", icon="cancel")

    def gui_editar(self):
        """Pega os dados de edição, valida e atualiza o produto."""
        id_str = self.entry_edit_id.get().strip()
        
        # Valida o ID
        try:
            id_editar = int(id_str)
        except ValueError:
            CTkMessagebox(title="Erro", message="ID inválido! Deve ser um número inteiro.", icon="cancel")
            return

        # Busca o produto
        produto = next((p for p in self.estoque if p["id"] == id_editar), None)
        if produto is None:
            CTkMessagebox(title="Erro", message="Produto não encontrado!", icon="cancel")
            return

        # Pega os novos dados (lógica do seu 'editar_produto')
        novo_nome = self.entry_edit_nome.get().strip().upper()
        nova_qtd_str = self.entry_edit_qtd.get().strip()
        novo_preco_str = self.entry_edit_preco.get().strip().replace(",", ".")

        try:
            # Atualiza o nome se foi fornecido
            if novo_nome:
                # Verifica duplicidade (exceto ele mesmo)
                for p in self.estoque:
                    if p['nome'].lower() == novo_nome.lower() and p['id'] != id_editar:
                         raise ValueError(f"O nome '{novo_nome}' já pertence a outro produto (ID: {p['id']}).")
                produto["nome"] = novo_nome

            # Atualiza a quantidade se foi fornecida
            if nova_qtd_str:
                produto["quantidade"] = int(nova_qtd_str)

            # Atualiza o preço se foi fornecido
            if novo_preco_str:
                produto["preco"] = float(novo_preco_str)

            # Salva e registra
            funcoes.salvar_estoque_csv(self.estoque)
            funcoes.registrar_log("Edição do produto", produto["nome"])
            
            CTkMessagebox(title="Sucesso", message="Produto atualizado com sucesso!", icon="check")

            # Limpa campos de edição
            self.entry_edit_id.delete(0, "end")
            self.entry_edit_nome.delete(0, "end")
            self.entry_edit_qtd.delete(0, "end")
            self.entry_edit_preco.delete(0, "end")
            
            self.gui_atualizar_lista() # Atualiza a lista

        except ValueError as e:
             CTkMessagebox(title="Erro de Validação", message=f"Dado inválido: {e}", icon="cancel")
        except Exception as e:
            CTkMessagebox(title="Erro Inesperado", message=f"Ocorreu um erro: {e}", icon="cancel")

    def gui_excluir(self):
        """Pega o ID, confirma e exclui o produto."""
        id_str = self.entry_del_id.get().strip()

        try:
            id_excluir = int(id_str)
        except ValueError:
            CTkMessagebox(title="Erro", message="ID inválido! Deve ser um número inteiro.", icon="cancel")
            return

        # Busca o produto
        produto = next((p for p in self.estoque if p["id"] == id_excluir), None)
        if produto is None:
            CTkMessagebox(title="Erro", message="Produto não encontrado!", icon="cancel")
            return

        # --- Confirmação ---
        msg = CTkMessagebox(title="Confirmar Exclusão", 
                            message=f"Tem certeza que deseja excluir '{produto['nome']}' (ID: {produto['id']})?",
                            icon="question", option_1="Cancelar", option_2="Sim, Excluir")
        
        if msg.get() == "Sim, Excluir":
            try:
                self.estoque.remove(produto)
                funcoes.salvar_estoque_csv(self.estoque)
                funcoes.registrar_log("Exclusão do produto", produto["nome"])
                
                CTkMessagebox(title="Sucesso", message=f"Produto '{produto['nome']}' excluído!", icon="check")
                
                self.entry_del_id.delete(0, "end") # Limpa o campo
                self.gui_atualizar_lista() # Atualiza a lista

            except Exception as e:
                CTkMessagebox(title="Erro Inesperado", message=f"Ocorreu um erro ao excluir: {e}", icon="cancel")

    def gui_limpar_lista(self):
        """Pede confirmação e limpa a lista inteira."""
        
        # --- Confirmação Rígida ---
        dialog = customtkinter.CTkInputDialog(
            text=f"Esta ação é IRREVERSÍVEL e apagará todos os {len(self.estoque)} produtos.\n\n"
                 "Digite 'CONFIRMAR' em maiúsculas para prosseguir:",
            title="CONFIRMAÇÃO DE EXCLUSÃO TOTAL"
        )
        
        entrada = dialog.get_input()
        
        if entrada == "CONFIRMAR":
            try:
                num_produtos = len(self.estoque)
                self.estoque.clear() # Limpa a lista em memória
                funcoes.salvar_estoque_csv(self.estoque) # Salva a lista vazia no arquivo
                funcoes.registrar_log("Limpeza total do estoque", f"{num_produtos} produtos apagados")
                
                CTkMessagebox(title="Sucesso", message="Todos os produtos foram excluídos.", icon="check")
                self.gui_atualizar_lista() # Atualiza a lista
                
            except Exception as e:
                CTkMessagebox(title="Erro", message=f"Ocorreu um erro ao limpar a lista: {e}", icon="cancel")
        else:
            CTkMessagebox(title="Cancelado", message="Ação cancelada. Nenhum produto foi excluído.")


if __name__ == "__main__":
    app = App()
    app.mainloop()