class Jogador:  
    total_jogadores = 0   

    def __init__(self, nome):  
        self.nome = nome  
        Jogador.total_jogadores += 1  

    @classmethod  
    def exibir_total_jogadores(cls):  
        return cls.total_jogadores  


class Jogo:  
    dificuldade_global = "Normal" 


class Personagem:  
    @staticmethod  
    def calcular_dano_base(forca):  
        return forca * 1.5  


class Loja:  
    preco_itens = [100, 200, 300]   
    @classmethod  
    def ajustar_preco_itens(cls, fator):  
        cls.preco_itens = [preco * fator for preco in cls.preco_itens]  


class Fase:  
    tempo_maximo = 300  