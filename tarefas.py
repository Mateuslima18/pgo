class Tarefas:  
    def __init__(self, cadastro, situacao, abertura, fechamento):  
        self.cadastro = cadastro
        self.situacao = situacao
        self.abertura = abertura
        self.fechamento = fechamento
        
tarefa1 = Tarefas('email e senha', 'concluida ou pendente', 'data de abertura', 'data de fechamento')

print(tarefa1.cadastro)
print(tarefa1.situacao)
print(tarefa1.abertura)
print(tarefa1.fechamento)