from livros.biblioteca import Biblioteca
from usuarios.usuario import Usuario

class Livro:
    def __init__(self, nome, autor, ano_publicacao):
        self._nome = nome
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self.disponivel = True

    def __str__(self):
        return (f'Título: {self._nome}, Autor: {self._autor}, Ano de Publicação: {self._ano_publicacao}')

    def emprestar_livro(self, usuario):
        tipo_usuario = usuario.__class__.__name__
        if usuario._id in Usuario.usuarios:
            if self in Biblioteca.biblioteca and self.disponivel == True:
                if len(usuario.lista_emprestados) < int(usuario.maximo_emprestimo):
                    usuario.lista_emprestados.append(self._nome)
                    self.disponivel = not self.disponivel
                else: 
                    print(f'O {tipo_usuario} {usuario._nome} atingiu o limite de livros emprestados e o {self._nome} não pôde ser emprestado.')
            else:
                print(f'O livro {self._nome} não está disponível para ser emprestado.')
        else:
            print(f'O usuário de ID: {usuario._id} não foi encontrado')

    def devolver_livro(self, usuario):
        if self in Biblioteca.biblioteca:
            if self.disponivel == False:
                usuario.lista_emprestados.remove(self._nome)
                self.disponivel = not self.disponivel
            else:
                print(f'O livro {self._nome} já foi devolvido.')
        else:
            print(f'O livro {self._nome} não foi localizado na biblioteca.')

    @property
    def disponibilidade(self):
        return 'Disponível' if self.disponivel == True else 'Indisponível'