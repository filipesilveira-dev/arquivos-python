# Quantos números do array apresentam uma quantidade de dígitos pares
nums = [12,345,6,7896]
nums_string=[]
cont_par=0
# Cria um novo array como base em "nums", mas com strings
for i in nums:
    nums_string.append(str(i))

#  Percorre o array de strings e, em cada elemento, verifica seu comprimento
for i in nums_string:
    comprimento=len(i)
    # Caso o comprimento seja divisível por 2 (par), o contador é incrementado
    if comprimento%2 == 0:
        cont_par += 1

print(cont_par)
        
    