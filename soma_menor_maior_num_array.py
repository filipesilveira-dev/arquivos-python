# Dado um array, some o menor e o maior número dentro dele

meu_array=[1,5,33,8,77,43,124,6,8,99]

# Ordena do menor para o maior
meu_array.sort()
# Pega o primeiro elemento (menor)
menor_num=meu_array[0]
# Pega o útlimo elemento (maior)
maior_num=meu_array[-1]

# Utilização de método para pegar os valores (menos linhas de código)
# maior_num=max(meu_array)
# menor_num=min(meu_array)

soma=maior_num +menor_num
print(soma)