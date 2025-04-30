class Turma:
    def __init__(self, *nomes_alunos):
        """
        Construtor da classe Turma.
        Aceita uma quantidade variável de nomes de alunos via *args e armazena em uma lista.
        """
        self.alunos = list(nomes_alunos)

# Criando uma turma com "Ana", "Bruno" e "Carlos"
turma1 = Turma("Ana", "Bruno", "Carlos")

# Criando uma turma apenas com "Larissa"
turma2 = Turma("Larissa")

# Imprimindo a lista de alunos de cada turma
print("Turma 1:", turma1.alunos)
print("Turma 2:", turma2.alunos)