def iniciar_aplicacao():
    def exibir_menu_principal():
            print('======BIBLIOTECA======\n')
            print('1. Biblioteca')
            print('2. Usuários')
            print('3. Sair\n')
            escolha_menu_principal()

    def interface_biblioteca():
            print('======BIBLIOTECA======\n')

    def interface_usuarios():
            print('======USUÁRIOS======\n')

    def escolha_menu_principal():
        try:
            resposta = int(input('Escolha uma sessão: '))

            if resposta == 1:
                    interface_biblioteca()
            elif resposta == 2:
                    interface_usuarios()
            elif resposta == 3:
                   print('Aplicação encerrada...')
            else:
                    print('Opção inexistente.')
        except:
                print('Opção Inválida')

    exibir_menu_principal()

        