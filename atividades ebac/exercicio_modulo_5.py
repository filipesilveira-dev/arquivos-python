class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som():
        print("O animal emitiu um som genérico.")

class Cachorro(Animal):
    def emitir_som(self):
        print("O cachorro latiu!")

class Gato(Animal):
    def emitir_som(self):
        print("O gato miou!")

def main():
    cachorro1 = Cachorro("Totó", 5)
    gato1 = Gato("Filé", 5)
    cachorro1.emitir_som()
    gato1.emitir_som()

if __name__ == "__main__":
    main()