class Biblioteca:

    biblioteca = []

    @classmethod
    def exibir_livros(cls):
        print(f'{'Título:'.ljust(25)} | {'Autor:'.ljust(25)} | {'Ano de Publicação:'.ljust(25)} | {'Status:'}')
        for livro in cls.biblioteca : 
            print(f'{livro._nome.ljust(25)} | {livro._autor.ljust(25)} | {str(livro._ano_publicacao).ljust(25)} | {livro.disponibilidade}')

    def adicionar_livro(self):
        Biblioteca.biblioteca.append(self)

    def remover_livro(self):
        Biblioteca.biblioteca.remove(self)

    @staticmethod
    def verificar_disponibilidade_ano(ano):
        try:
            ano = int(ano)

            livros_disponiveis_ano = []

            for livro in Biblioteca.biblioteca:
                if livro._ano_publicacao == ano and livro.disponivel == True:
                    livros_disponiveis_ano.append(livro)

            if livros_disponiveis_ano:
                print('Os livros encontrados foram:')
                for livro in livros_disponiveis_ano:
                    print(livro)
            else:
                print('Não foi encontrado nenhum livro neste ano.')

        except:
            print('Ano inválido.')

    @staticmethod
    def verificar_disponibilidade_nome(nome):
        try:
            nome = str(nome)

            livros_disponiveis_nome = []

            for livro in Biblioteca.biblioteca:
                if livro._nome == nome and livro.disponivel == True:
                    livros_disponiveis_nome.append(livro)
            if livros_disponiveis_nome:
                print('O livro encontrado foi:')
                for livro in livros_disponiveis_nome:
                    print(livro)
            else:
                print('Não foram encontrados livros com esse nome')
        except:
            print('Nome inválido')