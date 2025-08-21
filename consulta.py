from datetime import datetime
from conexao import criar_conexao

class Consulta:
    def __init__(self, id, cliente_id, animal_id, data_hora, status, observacoes):
        self.id = id
        self.cliente_id = cliente_id
        self.animal_id = animal_id
        self.data_hora = data_hora
        self.status = status
        self.observacoes = observacoes

    @staticmethod
    def agendar(cliente_id, animal_id, data_hora):
        conn = criar_conexao()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO consultas (cliente_id, animal_id, data_hora, status) VALUES (%s, %s, %s, 'Agendada')",
            (cliente_id, animal_id, data_hora)
        )
        conn.commit()
        consulta_id = cursor.lastrowid
        conn.close()
        return Consulta(consulta_id, cliente_id, animal_id, data_hora, "Agendada", "")

    @staticmethod
    def listar():
        conn = criar_conexao()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT c.id, c.cliente_id, c.animal_id, c.data_hora, c.status, c.observacoes
            FROM consultas c
        """)
        consultas = [Consulta(*row) for row in cursor.fetchall()]
        conn.close()
        return consultas

    def concluir(self, observacoes):
        conn = criar_conexao()
        cursor = conn.cursor()
        cursor.execute("UPDATE consultas SET status='Concluida', observacoes=%s WHERE id=%s", (observacoes, self.id))
        conn.commit()
        conn.close()
        self.status = "Concluida"
        self.observacoes = observacoes

    def cancelar(self):
        conn = criar_conexao()
        cursor = conn.cursor()
        cursor.execute("UPDATE consultas SET status='Cancelada' WHERE id=%s", (self.id,))
        conn.commit()
        conn.close()
        self.status = "Cancelada"
