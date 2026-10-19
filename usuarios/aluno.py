from usuarios.usuario import Usuario
class Aluno(Usuario):
    def __init__(self, nome, id):
        super().__init__(nome, id, maximo_emprestimo = 3)

    def cadastrar_aluno(nome, id):
            aluno = Aluno(nome, id)
            aluno_existe = any(aluno._id == id for aluno in Usuario.usuarios)
    
            if not aluno_existe:
                Usuario.usuarios.append(aluno)
                print(f'O aluno {nome} foi cadastrado com sucesso!')
            else:
                print(f'O aluno de ID: {id} já existe')