class Usuario:
    usuarios = []

    def __init__(self, nome, id, maximo_emprestimo):
        self._nome = nome
        self._id = int(id)
        self.lista_emprestados = []
        self.maximo_emprestimo = maximo_emprestimo

    def __str__(self):
        return (f'Nome: {self._nome} | ID: {self._id}')

    def exibir_emprestados(id):
        usuario_encontrado = None
        for usuario in Usuario.usuarios:
            if usuario._id == id:
                usuario_encontrado = usuario
                break
        
        if usuario_encontrado:
            if usuario.lista_emprestados:
                print(f'Lista de Livros emprestados para {usuario._nome}:')
                for livro in usuario.lista_emprestados:
                    print(livro)
            else:
                print('Este usuário não pegou nenhum livro emprestado.')
        else:
            print(f'O usuário {usuario._nome} não existe')

    def cadastrar_usuario(nome, id, maximo_emprestimo):
        usuario = Usuario(nome, id, maximo_emprestimo)
        usuario_existe = any(usuario._id == id for usuario in Usuario.usuarios)

        if not usuario_existe:
            Usuario.usuarios.append(usuario)
            print(f'O usuário {nome} foi cadastrado com sucesso!')
        else:
            print(f'O usuário de ID: {id} já existe')

    def remover_usuario(id):
        usuario_encontrado = None
        for usuario in Usuario.usuarios:
            if usuario._id == id:
                usuario_encontrado = usuario
                break

        if usuario_encontrado:
            Usuario.usuarios.remove(usuario_encontrado)
            print(f'O usuário {usuario_encontrado._nome} foi removido com sucesso.')
        else:
            print(f'Usuário de ID: {id} não encontrado')