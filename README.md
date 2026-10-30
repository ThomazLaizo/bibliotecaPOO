# 📚 Biblioteca POO
 
Sistema de gerenciamento de biblioteca para terminal, desenvolvido em Python com foco em **Programação Orientada a Objetos**. Permite cadastrar livros e usuários, controlar empréstimos e devoluções e consultar a disponibilidade do acervo.
 
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)
![POO](https://img.shields.io/badge/paradigma-POO-blueviolet)
![Terminal](https://img.shields.io/badge/interface-terminal-black?logo=windowsterminal&logoColor=white)
![Plataforma](https://img.shields.io/badge/plataforma-Windows-0078D6?logo=windows&logoColor=white)
![Licença](https://img.shields.io/badge/licen%C3%A7a-MIT-green)
![Último commit](https://img.shields.io/github/last-commit/ThomazLaizo/bibliotecaPOO)
![Tamanho do repositório](https://img.shields.io/github/repo-size/ThomazLaizo/bibliotecaPOO)
![Linguagem principal](https://img.shields.io/github/languages/top/ThomazLaizo/bibliotecaPOO)
 
> 🚧 **Projeto em desenvolvimento.** Veja o [roadmap](#️-roadmap) para o que está planejado.
 
## ✨ Funcionalidades
 
**Livros**
- Exibir o acervo em formato de tabela
- Adicionar e remover livros (sem duplicatas, ignorando maiúsculas/minúsculas)
- Consultar disponibilidade por **nome**, **autor** ou **ano de publicação**
**Usuários**
- Cadastro de usuário genérico, **aluno** ou **professor**
- Limite de empréstimos por tipo de usuário (aluno: 3, professor: 5, genérico: definido no cadastro)
- Consulta da lista de livros emprestados por usuário
**Empréstimos e devoluções**
- Empréstimo com validação de disponibilidade do livro e do limite do usuário
- Devolução com verificação de que o livro realmente está com aquele usuário
## 🧠 Conceitos de POO aplicados
 
| Conceito | Onde aparece |
|---|---|
| **Herança** | `Aluno` e `Professor` herdam de `Usuario` |
| **Encapsulamento** | Atributos protegidos por convenção (`_nome`, `_autor`, `_id`...) |
| **Propriedades** | `@property disponibilidade` em `Livro` |
| **Métodos de classe e estáticos** | `@classmethod` e `@staticmethod` em `Biblioteca` |
| **Polimorfismo / `super()`** | Construtores de `Aluno` e `Professor` chamam `Usuario.__init__` com limites diferentes |
| **Sobrescrita de `__str__`** | Representação textual de `Livro` e `Usuario` |
 
## 🗂️ Estrutura do projeto
 
```
bibliotecaPOO/
├── app.py                 # Ponto de entrada da aplicação
├── livros/
│   ├── biblioteca.py      # Acervo: adicionar, remover, exibir e consultar livros
│   ├── livro.py           # Classe Livro + regras de empréstimo e devolução
│   └── interface.py       # Menus interativos no terminal
├── usuarios/
│   ├── usuario.py         # Classe base Usuario
│   ├── aluno.py           # Aluno (limite de 3 empréstimos)
│   └── professor.py       # Professor (limite de 5 empréstimos)
├── LICENSE
└── README.md
```
 
## ⚙️ Requisitos
 
- **Python 3.12 ou superior** (o código usa aspas aninhadas em f-strings, recurso das versões mais recentes)
- **Windows** (a limpeza de tela usa o comando `cls`; veja o [roadmap](#️-roadmap))
- Nenhuma biblioteca externa é necessária
## ▶️ Como executar
 
```bash
# 1. Clone o repositório
git clone https://github.com/ThomazLaizo/bibliotecaPOO.git
 
# 2. Entre na pasta do projeto
cd bibliotecaPOO
 
# 3. Execute
python app.py
```
 
## 🖥️ Como usar
 
Ao iniciar, o menu principal é exibido:
 
```
======BIBLIOTECA======
 
1. Gerenciamento de Livros
2. Gerenciamento de Usuários
3. Empréstimos & Devoluções
4. Sair
```
 
Fluxo sugerido para testar:
 
1. Vá em **Gerenciamento de Livros** e adicione alguns livros.
2. Vá em **Gerenciamento de Usuários → Cadastro** e cadastre um aluno ou professor.
3. Vá em **Empréstimos & Devoluções** e empreste um livro informando o título e o ID do usuário.
> ⚠️ Por enquanto os dados ficam apenas **em memória**: ao encerrar o programa, tudo é perdido.
 
## 🛣️ Roadmap
 
- [ ] Persistência com **banco de dados**
- [ ] **Interface web**
- [ ] **Deploy** da aplicação
- [ ] Compatibilidade com Linux e macOS (limpeza de tela multiplataforma)
- [ ] Corrigir a remoção de usuários (devolução automática dos livros pendentes)
- [ ] Tratamento de erros mais específico (substituir `except` genéricos)
- [ ] Testes automatizados
## 📄 Licença
 
Distribuído sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
 
## 👤 Autor
 
Feito por **[Thomaz Silva Laizo](https://github.com/ThomazLaizo)**.