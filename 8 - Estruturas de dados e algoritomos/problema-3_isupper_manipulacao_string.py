# Definimos o uso de letras maiúsculas em uma palavra como correto quando o seguinte caso é válido:
# Todas as letras desta palavra são maiúsculas, como "EUA"
# Dada uma palavra de string, reotnre verdadeiro se o uso de letras maiúsculas está correto.

minha_string="EUA"
contador=0
for letra in minha_string:
    if letra.isupper():
        contador += 1

if contador == len(minha_string):
    print("Verdadeiro")
else:
    print("Falso")

