from cliente import Cliente
from animal import Animal
from consulta import Consulta

class ClinicaVeterinaria:
    # Não precisamos mais de listas em memória
    def __init__(self):
        pass

    # Adicionar cliente usando o banco de dados
    def adicionar_cliente(self, nome, cpf):
        return Cliente.adicionar(nome, cpf)

    # Listar clientes do banco
    def listar_clientes(self):
        return Cliente.listar()

    # Adicionar animal para um cliente
    def adicionar_animal(self, cliente_id, nome, idade, especie, raca=None):
        return Animal.adicionar(cliente_id, nome, idade, especie, raca)

    # Listar animais (opcional por cliente)
    def listar_animais(self, cliente_id=None):
        return Animal.listar(cliente_id)

    # Agendar consulta
    def agendar_consulta(self, cliente_id, animal_id, data_hora):
        return Consulta.agendar(cliente_id, animal_id, data_hora)

    # Listar todas as consultas
    def listar_consultas(self):
        return Consulta.listar()

    # Concluir uma consulta
    def concluir_consulta(self, consulta_id, observacoes):
        consulta = next((c for c in self.listar_consultas() if c.id == consulta_id), None)
        if consulta:
            consulta.concluir(observacoes)
            return consulta
        return None

    # Cancelar uma consulta
    def cancelar_consulta(self, consulta_id):
        consulta = next((c for c in self.listar_consultas() if c.id == consulta_id), None)
        if consulta:
            consulta.cancelar()
            return consulta
        return None
