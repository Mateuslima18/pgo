import random

# 12. Sistema de Pontuação e Energia no Jogo  
class JogadorComPontos:  
    def __init__(self):  
        self.energia = 100  
        self.pontos = 0  

    def descansar(self):  
        self.energia = min(self.energia + 20, 100)  

    def atacar_inimigo(self, inimigo):  
        if self.energia >= 10:  
            self.energia -= 10  
            inimigo.tomar_dano(10)  
            if inimigo.vida <= 0:  
                self.pontos += 10  
                print(f"Inimigo derrotado! Você ganhou 10 pontos. Total de pontos: {self.pontos}.")  
        else:  
            print("Sem energia suficiente para atacar!")  


# 10. Classe Inimigo com atributos nome e vida  
class InimigoComVida:  
    def __init__(self, nome):  
        self.nome = nome  
        self.vida = 100  

    def tomar_dano(self, dano):  
        self.vida -= dano  
        if self.vida <= 0:  
            print(f"{self.nome} foi derrotado!")  

    def atacar(self, alvo):  
        if isinstance(alvo, JogadorComPontos):  
            dano = 10  
            alvo.energia = max(alvo.energia - dano, 0)  
            print(f"{self.nome} atacou o jogador causando {dano} de dano. Energia do jogador: {alvo.energia}")  


# 13. Criando um Sistema de Menu Interativo  
class MenuInterativo:  
    def __init__(self, jogador):  
        self.jogador = jogador  

    def exibir_menu(self):  
        print("1. Descansar")  
        print("2. Atacar Inimigo")  
        print("3. Sair")  

    def iniciar_jogo(self):  
        inimigo = InimigoComVida("Inimigo")  
        while inimigo.vida > 0 and self.jogador.energia > 0:  
            self.exibir_menu()  
            opcao = input("Escolha uma opção: ")  

            if opcao == "1":  
                self.jogador.descansar()  
                print(f"Energia do jogador: {self.jogador.energia}")  
            elif opcao == "2":  
                self.jogador.atacar_inimigo(inimigo)  
                if inimigo.vida > 0:  
                    inimigo.atacar(self.jogador)  
            elif opcao == "3":  
                print("Saindo do jogo...")  
                break  
            else:  
                print("Opção inválida!")  

        if self.jogador.energia <= 0:  
            print("Você perdeu! Energia esgotada.")  
        elif inimigo.vida <= 0:  
            print("Parabéns! Você derrotou o inimigo.")  


# Testando o sistema de pontos e energia com menu interativo  
jogador_pontos = JogadorComPontos()  
menu = MenuInterativo(jogador_pontos)  
menu.iniciar_jogo()