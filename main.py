import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

from clinica import ClinicaVeterinaria

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Clínica Veterinária APP")
        self.root.geometry("700x600")

        self.clinica = ClinicaVeterinaria()

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill="both")

        self.criar_abas()
        self.atualizar_comboboxes()
        self.atualizar_lista_consultas()

    def criar_abas(self):
        self.aba_cadastro()
        self.aba_agendamento()
        self.aba_historico()
        self.aba_consultas()

    # ------------------- Cadastro -------------------
    def aba_cadastro(self):
        self.tab_cad = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_cad, text="Cadastro")

        # Cliente
        frame_cliente = tk.LabelFrame(self.tab_cad, text="Cadastro de Cliente")
        frame_cliente.pack(padx=10, pady=10, fill="x")

        tk.Label(frame_cliente, text="Nome Cliente:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.entry_nome_cliente = tk.Entry(frame_cliente)
        self.entry_nome_cliente.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        tk.Label(frame_cliente, text="CPF:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.entry_cpf = tk.Entry(frame_cliente)
        self.entry_cpf.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        tk.Button(frame_cliente, text="Cadastrar Cliente", width=25, command=self.cadastrar_cliente)\
            .grid(row=2, column=0, columnspan=2, pady=10)

        # Animal
        frame_animal = tk.LabelFrame(self.tab_cad, text="Cadastro de Animal")
        frame_animal.pack(padx=10, pady=10, fill="x")

        tk.Label(frame_animal, text="Cliente:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.combo_cliente = ttk.Combobox(frame_animal, width=25, state="readonly")
        self.combo_cliente.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        tk.Label(frame_animal, text="Nome Animal:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.entry_nome_animal = tk.Entry(frame_animal)
        self.entry_nome_animal.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        tk.Label(frame_animal, text="Idade:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.entry_idade = tk.Entry(frame_animal)
        self.entry_idade.grid(row=2, column=1, sticky="w", padx=5, pady=5)

        tk.Label(frame_animal, text="Tipo de Animal:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.entry_tipo_animal = tk.Entry(frame_animal)
        self.entry_tipo_animal.grid(row=3, column=1, sticky="w", padx=5, pady=5)

        tk.Label(frame_animal, text="Raça (opcional):").grid(row=4, column=0, sticky="e", padx=5, pady=5)
        self.entry_raca = tk.Entry(frame_animal)
        self.entry_raca.grid(row=4, column=1, sticky="w", padx=5, pady=5)

        tk.Button(frame_animal, text="Cadastrar Animal", width=25, command=self.cadastrar_animal)\
            .grid(row=5, column=0, columnspan=2, pady=10)

    # ------------------- Agendamento -------------------
    def aba_agendamento(self):
        self.tab_ag = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_ag, text="Agendamento")

        frame = tk.Frame(self.tab_ag)
        frame.pack(pady=20)

        tk.Label(frame, text='Cliente').grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.combo_cliente_agenda = ttk.Combobox(frame, width=25, state="readonly")
        self.combo_cliente_agenda.grid(row=0, column=1, sticky="w", padx=5, pady=5)
        self.combo_cliente_agenda.bind("<<ComboboxSelected>>", self.atualizar_animais_por_cliente)

        tk.Label(frame, text='Animal').grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.combo_animal_agenda = ttk.Combobox(frame, width=25, state="readonly")
        self.combo_animal_agenda.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        tk.Label(frame, text='Data/Hora (DD/MM/AAAA HH:MM)').grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.entry_data = tk.Entry(frame)
        self.entry_data.grid(row=2, column=1, sticky="w", padx=5, pady=5)

        tk.Label(frame, text='Observação').grid(row=3, column=0, sticky="ne", padx=5, pady=5)
        self.text_observacao = tk.Text(frame, height=3, width=30)
        self.text_observacao.grid(row=3, column=1, sticky="w", padx=5, pady=5)

        tk.Button(frame, text="Agendar Consulta", width=20, command=self.agendar_consulta).grid(row=4, column=0, pady=10)
        tk.Button(frame, text="Concluir Consulta", width=20, command=self.concluir_consulta).grid(row=4, column=1, pady=10)
        tk.Button(frame, text="Cancelar Consulta", width=20, command=self.cancelar_consulta).grid(row=5, column=0, columnspan=2, pady=10)

    # ------------------- Histórico -------------------
    def aba_historico(self):
        self.tab_hist = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_hist, text="Histórico")

        tk.Label(self.tab_hist, text='Animal').pack(pady=10)
        self.combo_animal_hist = ttk.Combobox(self.tab_hist, width=30, state="readonly")
        self.combo_animal_hist.pack()
        tk.Button(self.tab_hist, text="Exibir Histórico", width=25, command=self.exibir_historico).pack(pady=20)

    # ------------------- Consultas -------------------
    def aba_consultas(self):
        self.tab_cons = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_cons, text="Consultas")

        tk.Label(self.tab_cons, text="Lista de Consultas").pack(pady=10)

        self.tree_consultas = ttk.Treeview(
            self.tab_cons,
            columns=("Cliente", "Animal", "Data/Hora", "Status", "Observações"),
            show='headings'
        )
        self.tree_consultas.heading("Cliente", text="Cliente")
        self.tree_consultas.heading("Animal", text="Animal")
        self.tree_consultas.heading("Data/Hora", text="Data/Hora")
        self.tree_consultas.heading("Status", text="Status")
        self.tree_consultas.heading("Observações", text="Observações")
        self.tree_consultas.pack(fill="both", expand=True, padx=10, pady=10)

        tk.Button(self.tab_cons, text="Atualizar Lista", command=self.atualizar_lista_consultas).pack(pady=5)

    # ------------------- Métodos -------------------
    def limpar_campos(self):
        self.entry_nome_cliente.delete(0, tk.END)
        self.entry_cpf.delete(0, tk.END)
        self.entry_nome_animal.delete(0, tk.END)
        self.entry_idade.delete(0, tk.END)
        self.entry_tipo_animal.delete(0, tk.END)
        self.entry_raca.delete(0, tk.END)

    def cadastrar_cliente(self):
        nome = self.entry_nome_cliente.get().strip()
        cpf = self.entry_cpf.get().strip()
        if not nome or not cpf:
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
            return
        self.clinica.adicionar_cliente(nome, cpf)
        messagebox.showinfo("Sucesso", f"Cliente {nome} cadastrado!")
        self.limpar_campos()
        self.atualizar_comboboxes()

    def cadastrar_animal(self):
        cliente_index = self.combo_cliente.current()
        clientes = self.clinica.listar_clientes()
        if cliente_index < 0 or cliente_index >= len(clientes):
            messagebox.showwarning("Erro", "Selecione um cliente válido.")
            return

        cliente = clientes[cliente_index]
        nome = self.entry_nome_animal.get().strip()
        idade_str = self.entry_idade.get().strip()
        especie = self.entry_tipo_animal.get().strip() or "Desconhecido"
        raca = self.entry_raca.get().strip() or None

        if not nome or not idade_str:
            messagebox.showwarning("Atenção", "Preencha todos os campos obrigatórios.")
            return
        try:
            idade = int(idade_str)
        except ValueError:
            messagebox.showwarning("Erro", "Idade deve ser um número inteiro.")
            return

        self.clinica.adicionar_animal(cliente.id, nome, idade, especie, raca)
        messagebox.showinfo("Sucesso", f"{especie} {nome} cadastrado para {cliente.nome}!")
        self.limpar_campos()
        self.atualizar_comboboxes()

    def atualizar_comboboxes(self):
        clientes = self.clinica.listar_clientes()
        self.combo_cliente['values'] = [f"{c.nome} ({c.cpf})" for c in clientes]
        self.combo_cliente_agenda['values'] = [f"{c.nome} ({c.cpf})" for c in clientes]

        self.combo_cliente.set('')
        self.combo_cliente_agenda.set('')
        self.combo_animal_agenda.set('')
        self.combo_animal_agenda['values'] = []

        animais = self.clinica.listar_animais()
        self.combo_animal_hist['values'] = [f"{a.nome} - {a.especie}" + (f" ({a.raca})" if a.raca else "") for a in animais]

    def atualizar_animais_por_cliente(self, event=None):
        index = self.combo_cliente_agenda.current()
        clientes = self.clinica.listar_clientes()
        if index >= 0 and index < len(clientes):
            cliente = clientes[index]
            animais = self.clinica.listar_animais(cliente.id)
            self.combo_animal_agenda['values'] = [
                f"{a.nome} - {a.especie}" + (f" ({a.raca})" if a.raca else "") for a in animais
            ]
            if animais:
                self.combo_animal_agenda.current(0)
        else:
            self.combo_animal_agenda.set('')
            self.combo_animal_agenda['values'] = []

    def obter_cliente_agenda(self):
        index = self.combo_cliente_agenda.current()
        clientes = self.clinica.listar_clientes()
        if index >= 0 and index < len(clientes):
            return clientes[index]
        return None

    def obter_animal_agenda(self):
        cliente = self.obter_cliente_agenda()
        if not cliente:
            return None
        animais = self.clinica.listar_animais(cliente.id)
        index = self.combo_animal_agenda.current()
        if index >= 0 and index < len(animais):
            return animais[index]
        return None

    def agendar_consulta(self):
        cliente = self.obter_cliente_agenda()
        animal = self.obter_animal_agenda()
        data_hora_str = self.entry_data.get().strip()
        if not cliente or not animal:
            messagebox.showwarning("Erro", "Cliente ou animal não selecionado.")
            return
        try:
            data_hora = datetime.strptime(data_hora_str, "%d/%m/%Y %H:%M")
        except ValueError:
            messagebox.showwarning("Erro", "Formato de data/hora inválido. Use DD/MM/AAAA HH:MM")
            return
        self.clinica.agendar_consulta(cliente.id, animal.id, data_hora)
        messagebox.showinfo("Sucesso", f"Consulta agendada para {animal.nome} de {cliente.nome}.")
        self.atualizar_lista_consultas()

    def concluir_consulta(self):
        animal = self.obter_animal_agenda()
        obs = self.text_observacao.get("1.0", tk.END).strip()
        if not animal:
            messagebox.showwarning("Erro", "Animal não selecionado.")
            return
        consultas = self.clinica.listar_consultas()
        consulta = next((c for c in consultas if c.animal_id == animal.id and c.status == "Agendada"), None)
        if consulta:
            consulta.concluir(obs)
            messagebox.showinfo("Sucesso", f"Consulta concluída para {animal.nome}.")
            self.atualizar_lista_consultas()
        else:
            messagebox.showwarning("Erro", "Nenhuma consulta agendada encontrada.")

    def cancelar_consulta(self):
        animal = self.obter_animal_agenda()
        if not animal:
            messagebox.showwarning("Erro", "Animal não selecionado.")
            return
        consultas = self.clinica.listar_consultas()
        consulta = next((c for c in consultas if c.animal_id == animal.id and c.status == "Agendada"), None)
        if consulta:
            consulta.cancelar()
            messagebox.showinfo("Sucesso", f"Consulta cancelada para {animal.nome}.")
            self.atualizar_lista_consultas()
        else:
            messagebox.showwarning("Erro", "Nenhuma consulta agendada encontrada.")

    def exibir_historico(self):
        index = self.combo_animal_hist.current()
        animais = self.clinica.listar_animais()
        if index < 0 or index >= len(animais):
            messagebox.showwarning("Erro", "Selecione um animal válido.")
            return
        animal = animais[index]
        # Aqui você pode buscar histórico de consultas do animal no banco
        consultas = [c for c in self.clinica.listar_consultas() if c.animal_id == animal.id]
        historico = [f"{c.data_hora.strftime('%d/%m/%Y %H:%M')} - {c.status}: {c.observacoes}" for c in consultas if c.observacoes]
        messagebox.showinfo(f"Histórico de {animal.nome}", "\n".join(historico) if historico else "Nenhuma anotação registrada.")

    def atualizar_lista_consultas(self):
        for row in self.tree_consultas.get_children():
            self.tree_consultas.delete(row)
        consultas = self.clinica.listar_consultas()
        clientes = {c.id: c for c in self.clinica.listar_clientes()}
        animais = {a.id: a for a in self.clinica.listar_animais()}
        for c in consultas:
            cliente_nome = clientes[c.cliente_id].nome if c.cliente_id in clientes else "Desconhecido"
            animal_nome = animais[c.animal_id].nome if c.animal_id in animais else "Desconhecido"
            self.tree_consultas.insert("", tk.END, values=(
                cliente_nome,
                animal_nome,
                c.data_hora.strftime("%d/%m/%Y %H:%M"),
                c.status,
                c.observacoes
            ))

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
