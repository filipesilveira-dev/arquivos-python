# Retorne a média de todos os salários, com exceção do maior e do menor

salary=[4000, 3000, 1000, 2000]
salary_sorted=sorted(salary)

for item in salary_sorted:
    if item == salary_sorted[0] or item == salary_sorted[-1]:
        salary_sorted.remove(item)

n=len(salary_sorted)
acumulador=0
for item in salary_sorted:
    acumulador += item

media = acumulador//n

print(media)


