class livros:  
    def __init__(self,livro, autor, preço, quantidade , avaliação, ):  
        self.livro = livro
        self.autor = autor
        self.avaliação = avaliação
        self.quantidade= quantidade  
        self.preço = preço

livro1 = livros('peter pan', 'J. M. Barrie', '82% gostaram desse livro', ' 282 páginas', '$46,71')

print(livro1.livro)
print(livro1.autor)
print(livro1.avaliação)
print(livro1.quantidade)
print(livro1.preço)
