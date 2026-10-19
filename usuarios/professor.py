from usuarios.usuario import Usuario
class Professor(Usuario):
    def __init__(self, nome, id):
        super().__init__(nome, id, maximo_emprestimo = 5)

    def cadastrar_professor(nome, id):
            professor = Professor(nome, id)
            professor_existe = any(professor._id == id for professor in Usuario.usuarios)
    
            if not professor_existe:
                Usuario.usuarios.append(professor)
                print(f'O professor {nome} foi cadastrado com sucesso!')
            else:
                print(f'O professor de ID: {id} já existe')