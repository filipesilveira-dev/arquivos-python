# Dado um array, definimos uma soma acumulada de um array como runningSum[i] = sum(meu_array[0]+meu_array[i]). Retorne a soma acumulada de meu_array. A soma acumulada é obtida com [1, 1+2, 1+2+3, 1+2+3+4]

meu_array=[1,2,3,4]
soma_acumulada=[]
contador=0
for num in meu_array:
    contador += num
    soma_acumulada.append(contador)
print (soma_acumulada)
