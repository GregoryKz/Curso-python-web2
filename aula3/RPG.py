import random

class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida 
    def atacar (self):
        return 10
    def ataque_critico(self):
        return random.randint(20, 40)  #  ran e de range e  int de inteiro (aqui fica os valores e intervalos)
    def sofrer_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} sofreu {dano} de dano. Vida agora {self.vida}")
    def estar_vivo(self):
        return self.vida > 0


class Guerreiro (Personagem):
    def __init__(self, nome, vida, forca):
        super().__init__(nome, vida)
        self.forca = forca

    def atacar(self):
        print(f"{self.nome} atacou com a espada!")
        return self.forca
class Mago (Personagem):
    def __init__(self, nome, vida, mana):
        super().__init__(nome, vida)
        self.mana = mana

    def atacar(self):
        if self.mana >= 25:
            self.mana -= 10
            print(f"{self.nome} lança bola de fogo!")
            return 25
        else:
            print(f"{self.nome} usa faísca! Mana está baixa.")
            return 5
            
class Arqueiro (Personagem):
    def __init__(self, nome, vida, flechas):
        super().__init__(nome, vida)
        self.flechas = flechas

    def atacar(self):
        if self.flechas > 0:
            self.flechas -= 1
            print(f"{self.nome} dispara! Flechas restantes: {self.flechas}")
            return 20
        else:
            print(f"{self.nome} não tem flechas! Jogou pedra.")
            return 5
mago1 = Mago("Gargamel", 125, 100)
guerreiro1 = Guerreiro("Asta", 200, 30)


def combate(mago1, guerreiro1):
    turno = 1

    while mago1.estar_vivo() and guerreiro1.estar_vivo():
        print(f"\n--- Turno {turno} ---")

        dano = mago1.atacar()
        guerreiro1.sofrer_dano(dano)

        if not guerreiro1.estar_vivo():
            print(f"{guerreiro1.nome} foi derrotado!")
            break  # Encerra o combate


        dano = guerreiro1.atacar()
        mago1.sofrer_dano(dano)

        if not mago1.estar_vivo():
            print(f"{mago1.nome} foi derrotado!")
            break

        turno += 1

# Iniciar o combate
combate(mago1, guerreiro1)
