from conexao import criar_conexao

class Animal:
    def __init__(self, id, cliente_id, nome, idade, especie, raca=None):
        self.id = id
        self.cliente_id = cliente_id
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.raca = raca
        self.historico = []

    @staticmethod
    def adicionar(cliente_id, nome, idade, especie, raca=None):
        conn = criar_conexao()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO animais (cliente_id, nome, idade, especie, raca) VALUES (%s, %s, %s, %s, %s)",
            (cliente_id, nome, idade, especie, raca)
        )
        conn.commit()
        animal_id = cursor.lastrowid
        conn.close()
        return Animal(animal_id, cliente_id, nome, idade, especie, raca)

    @staticmethod
    def listar(cliente_id=None):
        conn = criar_conexao()
        cursor = conn.cursor()
        if cliente_id:
            cursor.execute("SELECT id, cliente_id, nome, idade, especie, raca FROM animais WHERE cliente_id=%s", (cliente_id,))
        else:
            cursor.execute("SELECT id, cliente_id, nome, idade, especie, raca FROM animais")
        animais = [Animal(*row) for row in cursor.fetchall()]
        conn.close()
        return animais

    @staticmethod
    def buscar_por_id(animal_id):
        conn = criar_conexao()
        cursor = conn.cursor()
        cursor.execute("SELECT id, cliente_id, nome, idade, especie, raca FROM animais WHERE id=%s", (animal_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Animal(*row)
        return None
