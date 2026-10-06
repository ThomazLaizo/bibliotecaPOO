from livros.livro import Livro
from livros.biblioteca import Biblioteca
from usuarios.usuario import Usuario
from usuarios.aluno import Aluno
from usuarios.professor import Professor
from livros.interface import iniciar_aplicacao


geovanna = Aluno('Geovanna Nascimento', 1234123)
geraldo = Professor('Geraldo Passos', 321123)
diarioDeUmBanana = Livro('Diário de Um Banana', 'Jeff Kinney', 2007)
oPequenoPrincipe = Livro('O Pequeno Príncipe', 'Antonie de Saint-Exupéry', 1943)
domCasmurro = Livro('Dom Casmurro', 'Machado de Assis', 1899)
oSenhorDosAneis = Livro('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954)
harryPotter = Livro('Harry Potter e a P.F', 'J.K. Rowling', 1997)
oHobbit = Livro('O Hobbit', 'J.R.R. Tolkien', 1937)
cemAnosDeSolidao = Livro('Cem Anos de Solidão', 'Gabriel García Márquez', 1967)

iniciar_aplicacao()