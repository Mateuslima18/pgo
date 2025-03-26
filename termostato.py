class Termostatos:  
    def __init__(self,sensores, regulador, parafusos, porcas , custo, ):  
        self.sensores = sensores
        self.regulador = regulador
        self.parafusos = parafusos
        self.porcas= porcas  
        self.custo = custo

termo1 = Termostatos('Elgin', 'Elgin', '15', '15', '50,00')

print(termo1.sensores)
print(termo1.regulador)
print(termo1.parafusos)
print(termo1.porcas)
print(termo1.custo)