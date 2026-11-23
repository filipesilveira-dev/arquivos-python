# Try/except: são muito utilizados para o tratamento de erros. É possível especificar as tratativas em casos de erros em específico
try:
    # Aqui é expecificado o que a função deve fazer caso ocorra tudo bem
    numero=int(input("Digite um número: "))
    resultado=10/numero
    print(resultado)
# Trata especificamente o erro de valor inserido
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número")
# Trata especificamente o erro de divisão por zero
except ZeroDivisionError:
    print("Não existe divisão por zero!")