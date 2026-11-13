# Verifique quantos elementos únicos existem no array e some seus valores ao final
meu_array=[1,2,2,3,4,4,4,4,5,6,7,7,7]

# 1. Criar um discionário (chave:valor) para receber o número (chave) e a quantidade de vezes que aparece (valor)

meu_dict={}

# percorre o array "meu_array"
for i in meu_array:
    # caso já não haja uma chave equivalente em "meu_dict", cria atribuindo o valor "1"
    if i not in meu_dict:
        meu_dict[i]=1
    # adiciona "+1" ao valor da chave equivalente
    else:
        meu_dict[i]+=1

print(meu_dict)

soma_unicos=0
# 2. Acessa "meu_dict" para achar os números que aparecem apenas uma vez
for chave,valor in meu_dict.items():
    if valor == 1:
        soma_unicos+=chave

print(soma_unicos)
