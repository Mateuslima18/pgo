class Livro:
    def __init__(self, titulo, autor, paginas=100):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

# Criando os objetos
livro1 = Livro("Python Básico", "João Silva", 250)
livro2 = Livro("Aprendendo Lógica", "Maria Souza")

# Imprimindo as informações
print(f"Livro 1: Título='{livro1.titulo}', Autor='{livro1.autor}', Páginas={livro1.paginas}")
print(f"Livro 2: Título='{livro2.titulo}', Autor='{livro2.autor}', Páginas={livro2.paginas}")