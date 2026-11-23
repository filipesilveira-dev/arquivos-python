# Função lambda (função anônima): é uma função que não precisa ser iniciada do "def ..". ela já pode ser inciada dentro do processo. Ideais para cenários onde funções simples são necessárias.

# Função normal
def soma1 (x,y):
    return x+y
print(soma1(3,3))

# Função lambda: primeiro os parâmetros, depois ":" e por fim o "return"
soma2 = lambda x,y:x+y
print (soma2(5,5))

meu_arrayzinho=[1,2,3,4,5]
duplicados = map(lambda numero : numero * 2, meu_arrayzinho)
# O "list" transforma "duplicados" em array
print(list(duplicados))