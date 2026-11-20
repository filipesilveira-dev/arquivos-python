#1 Exercício - Exiba os números de 1 a 5

# Sem utilizar list comprehension: exibe um array com cada número no range de 1 a 6
meu_array1=[]
for elemento in range(1,6):
    meu_array1.append(elemento)
print(meu_array1)

# Utilizando list comprehension: exibe um array com cada número no range de 1 a 6
meu_array2=[elemento for elemento in range(1,6)]
print(meu_array2)

#2 Exercício - Exiba as iniciais de cada palavra do array palavras
# Sem utilizar list comprehension:
palavras=["python", "javascript", "java"]
iniciais1=[]
for palavra in palavras:
    iniciais1.append(palavra[0])
print(iniciais1)
# Utilizando list comprehension:
palavras=["python", "javascript", "java"]
iniciais2=[palavra[0] for palavra in palavras]
print(iniciais2)

#3 Exercício - pegue os quadros dos números ímpares dos números de 1 a 10
# Sem utilizar list comprehension:
numeros_impares=[]
for numero in range(1,11):
    if numero%2!=0:
        numeros_impares.append(numero**2)
print(numeros_impares)

# Utilizando list comprehension:
numeros_impares2=[numero**2 for numero in range(1,11) if numero%2!=0]
print(numeros_impares2)