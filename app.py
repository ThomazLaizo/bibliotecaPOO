from livros.livro import Livro
from livros.biblioteca import Biblioteca
from usuarios.usuario import Usuario
from usuarios.aluno import Aluno
from usuarios.professor import Professor


geovanna = Aluno('Geovanna Nascimento', 1234123)
geraldo = Professor('Geraldo Passos', 321123)
diarioDeUmBanana = Livro('Diário de Um Banana', 'Jeff Kinney', 2007)
oPequenoPrincipe = Livro('O Pequeno Príncipe', 'Antonie de Saint-Exupéry', 1943)
domCasmurro = Livro('Dom Casmurro', 'Machado de Assis', 1899)
oSenhorDosAneis = Livro('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954)
harryPotter = Livro('Harry Potter e a P.F', 'J.K. Rowling', 1997)
oHobbit = Livro('O Hobbit', 'J.R.R. Tolkien', 1937)
cemAnosDeSolidao = Livro('Cem Anos de Solidão', 'Gabriel García Márquez', 1967)

Biblioteca.adicionar_livro(diarioDeUmBanana)
Biblioteca.adicionar_livro(oPequenoPrincipe)
Biblioteca.adicionar_livro(domCasmurro)
Biblioteca.adicionar_livro(oSenhorDosAneis)
Biblioteca.adicionar_livro(harryPotter)
Biblioteca.adicionar_livro(oHobbit)
Biblioteca.adicionar_livro(cemAnosDeSolidao)

Livro.emprestar_livro(oPequenoPrincipe, geraldo)
Livro.emprestar_livro(domCasmurro, geraldo)
Livro.emprestar_livro(oSenhorDosAneis, geraldo)
Livro.emprestar_livro(harryPotter, geraldo)
Livro.emprestar_livro(oHobbit, geraldo)
Livro.emprestar_livro(cemAnosDeSolidao, geraldo)


Biblioteca.exibir_livros()