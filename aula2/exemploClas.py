#Mini munndo: Escola
# Preciso de um obejto que presente o aluno, o professor e direção/diretora

class Pessoa:
    def __init__(self, nome, idade, cpf, ra, escola, fucao):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.ra = ra
        self.escola = escola
        self.fucao = fucao
        
    def __str__(self):
        return f"Ola meu nome é {self.nome}"
    
aluno1 = Pessoa("Skill fucão", 35, "000000000-10", "132456786", "SENAC", "Aluno")
diretor1 = Pessoa("José", 19, "000000","5466","SENAC", "Diretor")
professor1 = Pessoa("Pedro", 20, "1321","13132","Senac", "Professor")
print(vars(aluno1))
#print(vars(diretor1))
#print(vars(professor1))
print(aluno1)
