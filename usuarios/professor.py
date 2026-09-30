from usuarios.usuario import Usuario
class Professor(Usuario):
    def __init__(self, nome, id):
        super().__init__(nome, id, maximo_emprestimo = 5)