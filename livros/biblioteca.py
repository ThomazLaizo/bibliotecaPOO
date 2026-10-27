class Biblioteca:

    biblioteca = []

    @classmethod
    def exibir_livros(cls):
        if Biblioteca.biblioteca:
            print(f'{'Título:'.ljust(25)} | {'Autor:'.ljust(25)} | {'Ano de Publicação:'.ljust(25)} | {'Status:'}')
            for livro in cls.biblioteca : 
                print(f'{livro._nome.ljust(25)} | {livro._autor.ljust(25)} | {str(livro._ano_publicacao).ljust(25)} | {livro.disponibilidade}')
        else:
            print('A biblioteca está vazia.')

    def adicionar_livro(nome, autor, ano):
        from livros.livro import Livro

        livro_existe = any(livro._nome.lower() == nome.lower() for livro in Biblioteca.biblioteca)
        novo_livro = Livro(nome,  autor, ano)

        if not livro_existe :
            Biblioteca.biblioteca.append(novo_livro)
            print(f'O livro {nome} foi adicionado com sucesso.')
        else:
            print(f'O livro {nome} já existe.')

    def remover_livro(nome):

        livro_encontrado = None
        for livro in Biblioteca.biblioteca:
            if livro._nome.lower() == nome.lower():
                livro_encontrado = livro
                break

        if livro_encontrado:
            Biblioteca.biblioteca.remove(livro_encontrado)
            print(f'O livro {nome} foi removido com sucesso.')
        else:
            print(f'O livro {nome} não foi encontrado.')

    @staticmethod
    def verificar_disponibilidade_ano(ano):
        try:
            ano = int(ano)

            livros_disponiveis_ano = []

            for livro in Biblioteca.biblioteca:
                if livro._ano_publicacao == ano and livro.disponivel == True:
                    livros_disponiveis_ano.append(livro)

            if livros_disponiveis_ano:
                print('Os livros encontrados foram:\n')
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
                if livro._nome.lower() == nome.lower() and livro.disponivel == True:
                    livros_disponiveis_nome.append(livro)
            if livros_disponiveis_nome:
                print('O livro encontrado foi:\n')
                for livro in livros_disponiveis_nome:
                    print(livro)
            else:
                print('Não foram encontrados livros com esse nome.')
        except:
            print('Nome inválido.')

    @staticmethod
    def verificar_disponibilidade_autor(autor):
        try:
            autor = str(autor)

            livros_disponiveis_autor = []

            for livro in Biblioteca.biblioteca:
                if livro._autor.lower() == autor.lower() and livro.disponivel == True:
                    livros_disponiveis_autor.append(livro)
            if livros_disponiveis_autor:
                print('O livro encontrado foi:\n')
                for livro in livros_disponiveis_autor:
                    print(livro)
            else:
                print('Não foram encontrados livros deste autor.')
        except:
            print('Autor inválido.')