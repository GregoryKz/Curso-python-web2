class Pai :
    def __init__(self, valor, nome):
        self.valor = valor
        self.nome = nome
    def mostrar (self):
        print (f"Classe pai", self.valor)
class Filho (Pai):
    def __init__(self, valor, nome):
        super().__init__(valor, nome)
    
    def mostrar(self):
        print(f"Classe filho", self.valor)
        
        