class bancos:  
    def __init__(self, banco, agencia, conta, chave , ):  
        self.banco = banco
        self.agencia = agencia
        self.conta = conta
        self.chave = chave 
        
banco1 = bancos('Nubank', '0000', '00000000-0', 'cpf', )

print(banco1.banco)
print(banco1.agencia)
print(banco1.conta)
print(banco1.chave)
