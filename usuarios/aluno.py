from usuarios.usuario import Usuario
class Aluno(Usuario):
    def __init__(self, nome, id):
        super().__init__(nome, id, maximo_emprestimo = 3)