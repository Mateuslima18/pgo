class Smartphone:  
    def __init__(self, marca, modelo, armazenamento, cor, preco):  
        self.marca = marca
        self.modelo = modelo
        self.armazenamento = armazenamento
        self.cor = cor
        self.preco = preco

smart1 = Smartphone('Samsung', 'A15', '256gb', 'Azul escuro', '1200,00')

print(smart1.marca)
print(smart1.modelo)
print(smart1.armazenamento)
print(smart1.cor)
print(smart1.preco)