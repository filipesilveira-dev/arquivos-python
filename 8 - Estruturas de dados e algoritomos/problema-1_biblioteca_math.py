# Dado um número inteiro não negativo "x", retorne a raiz quadrada de "x" arredondada para o número inteiro mais próximo. O número inteiro mais próximo também deve ser não negativo.

# Solução: uso da biblioteca "math"

import math

def retorna_raiz(num):
    resultado=math.sqrt(num)
    print(resultado)

retorna_raiz(144)
