class Usuario:

    def __init__(self, nome, id, maximo_emprestimo):
        self._nome = nome
        self._id = int(id)
        self.lista_emprestados = []
        self.maximo_emprestimo = maximo_emprestimo

    def __str__(self):
        return (f'Nome: {self._nome} | ID: {self._id}')

    def exibir_emprestados(self):
        if self.lista_emprestados:
            print(f'Lista de Livros emprestados para {self._nome}:')
            for livro in self.lista_emprestados:
                print(livro)
        else:
            print('Este usuário não pegou nenhum livro emprestado.')