class Turma:
    def __init__(self, *nomes_alunos):
        """
        Construtor da classe Turma.
        Aceita uma quantidade variável de nomes de alunos via *args e armazena em uma lista.
        """
        self.alunos = list(nomes_alunos)


turma1 = Turma("Ana", "Bruno", "Carlos")


turma2 = Turma("Larissa")


print("Turma 1:", turma1.alunos)
print("Turma 2:", turma2.alunos)