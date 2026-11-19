# Uma classe é um molde
# Vamos usar esse molde para construir coisas que queremos que tem o mesmo padrão

# -- Atributos de um pokémon --
# - Nome
# - HP
# - Tipo
# - Ataque
# - Altura
# - Peso

class MoldePokemon:
    # Método construtor: métodos são funções no contexto de POO. No método construtor serão passados os atributos necessários naquela classe
    # Self: tem a função de armazenar e manipular as informações dos atributos
    def __init__(self, nome, hp, tipo, ataque, altura, peso):
        # Inicialização dos atributos
        self.nome = nome
        self.hp = hp
        self.tipo = tipo
        self.ataque = ataque
        self.altura = altura
        self.peso = peso

    # Método da classe que utiliza o atributo inicializado com "self" para mostrar o nome do pokémon
    def mostrar_nome_pokemon(self):
        print(f"O nome do pokémon é: {self.nome}")

    # Método da classe que utiliza o atributo inicializado com "self" para mostrar a altura do pokémon
    def mostrar_altura_pokemon(self):
        print(f"A altura do pokémon é: {self.altura}")

pokemon1=MoldePokemon("Pikachu", 100, "Elétrico", 150, 50, 10)

print(pokemon1.nome)