# Dado um array de tamanho "n", retorne o elemento majoritário. O elemento majoritário é aquele que aparece mais de "n/2" vezes. Você pode assumir que o elemento majoritário sempre existe no array.

meu_array=[3,2,3]
n=len(meu_array)
item_majoritario=n/2

meu_dicionario={}
for elemento in meu_array:
    if elemento not in meu_dicionario:
        meu_dicionario[elemento] = 1
    else:
        meu_dicionario[elemento] += 1

for chave,valor in meu_dicionario.items():
    if valor >= item_majoritario:
        print(chave)

# Obs: para percorrer um array[] com "for" utilizamos a variável de contexto unitário, como "item" para representar cada elemento do array. No caso de percorrer um dicionário, é necessário passar "chave, valor" e especificar o método ".items()" do dicionário{} que está sendo percorrido.