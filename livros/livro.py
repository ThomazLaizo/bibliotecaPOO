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

    def emprestar_livro(nome, usuario):

        tipo_usuario = usuario.__class__.__name__

        livro_encontrado = None                    
        for livro in Biblioteca.biblioteca:        
            if livro._nome.lower() == nome.lower():
                livro_encontrado = livro           
                break                              
        if livro_encontrado:                       
            if livro_encontrado.disponivel == True:
                if len(usuario.lista_emprestados) < int(usuario.maximo_emprestimo):
                    usuario.lista_emprestados.append(livro_encontrado._nome)
                    livro_encontrado.disponivel = not livro_encontrado.disponivel
                    print(f'O livro {nome} foi emprestado para o(a) {tipo_usuario}(a) {usuario._nome} com sucesso!')
                else: 
                    print(f'O(A) {tipo_usuario}(a) {usuario._nome} atingiu o limite de livros emprestados e o {livro_encontrado._nome} não pôde ser emprestado.')
            else:
                print(f'O livro {livro_encontrado._nome} não está disponível para ser emprestado.')

    def devolver_livro(nome, usuario):

        tipo_usuario = usuario.__class__.__name__

        livro_encontrado = None                    
        for livro in Biblioteca.biblioteca:        
            if livro._nome.lower() == nome.lower():
                livro_encontrado = livro           
                break                              
        if livro_encontrado:
            if livro_encontrado.disponivel == False:
                if livro_encontrado._nome in usuario.lista_emprestados:
                    usuario.lista_emprestados.remove(livro_encontrado._nome)
                    livro_encontrado.disponivel = not livro_encontrado.disponivel
                    print(f'O livro {nome} foi devolvido pelo(a) {tipo_usuario}(a) {usuario._nome} com sucesso!')
                else:
                    print(f'O livro {livro_encontrado._nome} não foi emprestado por {usuario._nome}')
            else:
                print(f'O livro {livro_encontrado._nome} já foi devolvido.')
        else:
            print(f'O livro {nome} não foi localizado na biblioteca.')

    @property
    def disponibilidade(self):
        return 'Disponível' if self.disponivel == True else 'Indisponível'