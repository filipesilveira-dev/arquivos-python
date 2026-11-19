class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print(f"{self.nome} está comendo!")

# A classe cachorro herda os atributos e métodos da classe Animal
class Cachorro(Animal):
    def latir(self):
        print(f"{self.nome} está latindo: au au")

meu_cachorrinho = Cachorro("Goku")

# Chama o método que está em Animal
meu_cachorrinho.comer()
# Chama o método que está apenas em Cachorro
meu_cachorrinho.latir()