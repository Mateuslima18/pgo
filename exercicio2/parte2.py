# 2.1 Encapsulamento
class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.__vida = vida
        self.__defesa = 0

    def mostrar_vida(self):
        return self.__vida

    @property
    def vida(self):
        return self.__vida

    @property
    def defesa(self):
        return self.__defesa

    @defesa.setter
    def defesa(self, valor):
        if 0 <= valor <= 100:
            self.__defesa = valor

class Pontuacao:
    def __init__(self):
        self.__pontos = 0

    def adicionar_pontos(self, valor):
        if valor > 0:
            self.__pontos += valor

    @property
    def pontos(self):
        return self.__pontos

    @pontos.setter
    def pontos(self, valor):
        if valor >= 0:
            self.__pontos = valor

class Inimigo(Personagem):
    def __init__(self, nome, vida, forca):
        super().__init__(nome, vida)
        self.__forca = forca

    def atacar(self):
        print(f"{self.nome} ataca com força {self.__forca}!")

class Jogador(Personagem):
    def __init__(self, nome, energia, pontos):
        super().__init__(nome, 100)
        self.__energia = energia
        self.pontuacao = Pontuacao()
        self.pontuacao.adicionar_pontos(pontos)

    def usar_energia(self, valor):
        self.__energia = max(0, self.__energia - valor)

    def recuperar_energia(self, valor):
        self.__energia = min(100, self.__energia + valor)

class Menu:
    def __init__(self, titulo):
        self.titulo = titulo

    def exibir(self):
        print(f"--- {self.titulo} ---")

class Jogo:
    def __init__(self):
        self.__dificuldade = 1
        self.menu = Menu("Menu Principal")

    @property
    def dificuldade(self):
        return self.__dificuldade

    @dificuldade.setter
    def dificuldade(self, valor):
        if valor in [1, 2, 3]:
            self.__dificuldade = valor

    def iniciar(self):
        self.menu.exibir()
        print("Jogo iniciado.")

# Continuação virá com Herança, Polimorfismo e demais partes...
