
# Clínica Veterinária 🐾

Sistema em **Python** com interface gráfica (**Tkinter**) e integração com banco de dados **MySQL** para gerenciamento de uma clínica veterinária.

## 🚀 Funcionalidades
- Cadastro de **clientes**
- Cadastro de **animais**
- Agendamento de **consultas**
- Integração com banco de dados MySQL
- Interface gráfica para uso simples

## 📂 Estrutura do Projeto
```

Clinica vetrinaria com bd/
├── animal.py        # Classe Animal
├── cliente.py       # Classe Cliente
├── clinica.py       # Regras da clínica
├── consulta.py      # Classe Consulta
├── conexao.py       # Configuração da conexão MySQL
├── main.py          # Interface principal (Tkinter)
├── arquivo.sql      # Script para criar/popular o banco de dados

````

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**
- **Tkinter** (Interface gráfica)
- **MySQL** (Banco de dados)

## ⚙️ Como Executar

1. Clone este repositório ou extraia o `.zip`
   ```bash
   git clone https://github.com/Wallace-Lentes/clinica_com_BD.git
   cd Clinica-veterinaria-com-bd
````

2. Crie o banco de dados MySQL a partir do script:

   ```sql
   SOURCE arquivo.sql;
   ```

3. Configure sua conexão no arquivo `conexao.py` com usuário, senha e host corretos.

4. Instale as dependências necessárias:

   ```bash
   pip install mysql-connector-python
   ```

5. Execute o sistema:

   ```bash
   python main.py
   ```
