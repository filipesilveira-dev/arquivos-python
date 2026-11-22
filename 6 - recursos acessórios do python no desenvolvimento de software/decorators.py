# Início introdução de decorators: decorators permitem acrescentar atributos/metadados/métodos à determinada função. São "acessórios" à função que srá decorada. O mesmo decorator pode ser reutilizado ao longo do código.

# Função "decoradora"
def meu_decorator(func):
    # Método que encapsula a função (func)
    def wrapper():
        print("Antes da execução da minha despedida")
        # Chamada da função que será encapsulada
        func()
        print("Depois da execução da minha despedida")
    return wrapper

# Chamada do decorator
@meu_decorator
# Função que será "decorada"
def despedida():
    print("Tchau!")

despedida()