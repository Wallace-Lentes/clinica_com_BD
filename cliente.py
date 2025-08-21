from conexao import criar_conexao

class Cliente:
    def __init__(self, id, nome, cpf):
        self.id = id
        self.nome = nome
        self.cpf = cpf

    @staticmethod
    def adicionar(nome, cpf):
        conn = criar_conexao()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes (nome, cpf) VALUES (%s, %s)", (nome, cpf))
        conn.commit()
        cliente_id = cursor.lastrowid
        conn.close()
        return Cliente(cliente_id, nome, cpf)

    @staticmethod
    def listar():
        conn = criar_conexao()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, cpf FROM clientes")
        clientes = [Cliente(id, nome, cpf) for id, nome, cpf in cursor.fetchall()]
        conn.close()
        return clientes

    @staticmethod
    def buscar_por_id(cliente_id):
        conn = criar_conexao()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, cpf FROM clientes WHERE id=%s", (cliente_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Cliente(*row)
        return None
