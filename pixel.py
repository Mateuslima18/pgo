class Pixel:
    def __init__(self, valor1, valor2, valor3, valor4, valor5):
        self.cor = valor1
        self.brilho = valor2
        self.tamanho = valor3
        self.resolucao = valor4
        self.status = valor5

pixel1 = Pixel("Vermelho","70","20x20","1080p","Ativo")

print('Cor: ' + pixel1.cor)
print('Brilho: ' + pixel1.brilho)
print('Tamanho: ' + pixel1.tamanho)
print('Resolução: ' + pixel1.resolucao)
print('Status: ' + pixel1.status)