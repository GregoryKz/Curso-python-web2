class Pessoa ():
    def __init__(self, nome, idade, pet, cpf,cartao):
        self.nome = nome
        self.idade = idade
        self.pet = pet
        self.cpf = cpf
        self.cartao = cartao
    def apresentar (self):
        print (f" Olá meu nome é:{self.nome}tenho:{self.idade}anos, meu cpf:{self.cpf},meu  cartão e {self.cartao} "
               )
        
        
pessoa1 = Pessoa("Gregory", 20, "Não tem", "012345678998", "1326546978987")
pessoa2 = Pessoa("Ericson", 18, "Tem gato", "79856432100", "54468546546")
pessoa3 = Pessoa("Ana", 19, "Tem cachorro", "456789465", "5646564541")
pessoa4 = Pessoa("Luiza", 22, "Não", "4564645645", "354654156")

print (vars(pessoa1))
print (pessoa2.nome)


nome = input ("DIgite o nome do seu objeto:")
idade= int(input("Digite a idade do seu objeto:"))
pet = input ("Digite se o objeto tem pet:")
if (pet == "Sim"):
    animal = input("Digte qual pet ele tem:")
else:
    animal = "Não"

cpf = input("Digite o cpf do obejto:")
cartao = input("Digite o cartão do objeto:")

pessoa5 = Pessoa(nome,idade,animal,cpf,cartao)
pessoa5.apresentar()