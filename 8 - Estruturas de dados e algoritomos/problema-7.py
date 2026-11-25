# Dado um array inteiro, retorne verdadeiro se algum valor aparecer pelo menos duas vezes no array e retorne falso se cada elemento for distinto
meu_array=[1,1,1,3,3,4,3,2,4,2]
meu_dicionario={}

for item in meu_array:
    if item not in meu_dicionario:
        meu_dicionario[item] = 1
    else:
        meu_dicionario[item] += 1

contador=0
for chave, valor in meu_dicionario.items():
    if valor >= 2:
        contador = 1

if contador > 0:
    print("Verdadeiro")
else:
    print("Falso")