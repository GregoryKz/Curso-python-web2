class Pessoa ():
    def __init__(self, nome, idade, pet, cpf,cartao):
        self.nome = nome
        self.idade = idade
        self.pet = pet
        self.cpf = cpf
        self.cartao = cartao
    def apresentar (self):
        print (f"nome:{self.nome}, idade:{self.idade},cpf:{self.cpf}, cartao{self.cartao} "
               )
        
        
pessoa1 = Pessoa("Gregory", 20, "Não tem", "012345678998", "1326546978987")
pessoa2 = Pessoa("Ericson", 18, "Tem gato", "79856432100", "54468546546")
pessoa3 = Pessoa("Ana", 19, "Tem cachorro", "456789465", "5646564541")
pessoa4 = Pessoa("Luiza", 22, "Não", "4564645645", "354654156")

print (vars(pessoa1))
print (pessoa2.nome)