from livros.biblioteca import Biblioteca
from usuarios.usuario import Usuario
import os

def limpar():
    os.system('cls')

def iniciar_aplicacao():

    def digite_tecla():
        input('Digite Enter para retornar.')
        exibir_menu_principal()

    def exibir_menu_principal():
            limpar()
            print('======BIBLIOTECA======\n')
            print('1. Biblioteca')
            print('2. Usuários')
            print('3. Sair\n')
            escolha_menu_principal()

    def escolha_menu_principal():
        try:
            resposta = int(input('Escolha uma sessão: '))

            if resposta == 1:
                    limpar()
                    interface_biblioteca()
            elif resposta == 2:
                    limpar()
                    interface_usuarios()
            elif resposta == 3:
                   limpar()
                   print('Aplicação encerrada...')
            else:
                    print('Opção inexistente.')
        except:
                print('Opção Inválida')

    def interface_biblioteca():
            limpar()
            print('======BIBLIOTECA======\n')
            print('1. Exibir Livros')
            print('2. Adicionar Livro')
            print('3. Remover Livro')
            print('4. Verificar Disponibilidade')
            print('5. Voltar\n')
            escolha_menu_biblioteca()

    def escolha_menu_biblioteca():
        
        try:
            resposta = int(input('Escolha uma opção: '))

            if resposta == 1:
                limpar()
                Biblioteca.exibir_livros()
                digite_tecla()

            elif resposta == 2:
                limpar()
                nome = str(input('Digite o nome do Livro: '))
                autor = str(input('Digite o autor do Livro: '))
                ano = int(input('Digite o ano de publicação do Livro: '))
                Biblioteca.adicionar_livro(nome, autor, ano)
                digite_tecla()
                
            elif resposta == 3:
                limpar()
                nome = str(input('Digite o nome do Livro: '))
                Biblioteca.remover_livro(nome)
                digite_tecla()

            elif resposta == 4:
                limpar()
                interface_disponibilidade()

            elif resposta == 5:
                limpar()
                exibir_menu_principal()
                  
            else:
                print('Opção Inexistente')
                digite_tecla()

        except:
            print('Opção Inválida')
            digite_tecla()
                         
    def interface_disponibilidade():
            limpar()
            print('======DISPONIBILIDADE======\n')
            print('1. Verificar por Nome')
            print('2. Verificar por Autor')
            print('3. Verificar por Data de Publicação')
            print('4. Voltar\n')
            escolha_menu_disponibilidade()
            
    def escolha_menu_disponibilidade():
            try:
                resposta = int(input('Escolha uma opção:'))

                if resposta == 1:
                    limpar()
                    nome = input('Insira o nome que deseja verificar.')
                    Biblioteca.verificar_disponibilidade_nome(nome)
                    digite_tecla()
                elif resposta == 2:
                    limpar()
                    autor = input('Insira o autor que deseja verificar.')
                    Biblioteca.verificar_disponibilidade_autor(autor)
                    digite_tecla()
                elif resposta == 3:
                    limpar()
                    data = input('Insira a data que deseja verificar.')
                    Biblioteca.verificar_disponibilidade_ano(data)
                    digite_tecla()
                elif resposta == 4:
                    limpar()
                    interface_biblioteca()
                else:
                    print('Opção Inexistente')
                    digite_tecla()
            except:
                print('Opção inválida.')
                digite_tecla()
 
    def interface_usuarios():
            print('======USUÁRIOS======\n')
            print('1. Cadastrar Usuário')
            print('2. Cadastrar Aluno')
            print('3. Cadastrar Professor')
            print('4. Remover Usuário')
            print('5. Voltar')


    exibir_menu_principal()

        