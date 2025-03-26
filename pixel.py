class pixeis:  
    def __init__(self,livro, autor, preço, quantidade , avaliação, ):  
        self.livro = livro
        self.autor = autor
        self.avaliação = avaliação
        self.quantidade= quantidade  
        self.preço = preço

pixel1 = pixeis('peter pan', 'J. M. Barrie', '82% gostaram desse livro', ' 282 páginas', '$46,71')

print(pixel1.livro)
print(pixel1.autor)
print(pixel1.avaliação)
print(pixel1.quantidade)
print(pixel1.preço)
