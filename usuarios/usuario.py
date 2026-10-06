class Usuario:
    usuarios = []

    def __init__(self, nome, id, maximo_emprestimo):
        self._nome = nome
        self._id = int(id)
        self.lista_emprestados = []
        self.maximo_emprestimo = maximo_emprestimo

    def __str__(self):
        return (f'Nome: {self._nome} | ID: {self._id}')

    def exibir_emprestados(self):
        if self in Usuario.usuarios:
            if self.lista_emprestados:
                print(f'Lista de Livros emprestados para {self._nome}:')
                for livro in self.lista_emprestados:
                    print(livro)
            else:
                print('Este usuário não pegou nenhum livro emprestado.')
        else:
            print(f'O usuário {self._nome} não existe')

    def cadastrar_usuario(self):
        if self._id not in Usuario.usuarios:
            Usuario.usuarios.append(self._id)
        else:
            print(f'O usuário de ID: {self._id} já existe')

    def remover_usuario(self):
        if self._id in Usuario.usuarios:
            Usuario.usuarios.remove(self._id)
        else:
            print(f'Usuário de ID: {self._id} não encontrado')