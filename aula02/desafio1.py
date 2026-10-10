nota=[]

print("Programa de notas")

nota1 = float(input("Digite a sua 1º nota "))

while nota1 <= 0 or nota1 > 10:
    print("1º nota inválida, tente novamente")
    nota1 = float(input("Digite a sua 1º nota: "))
    if nota1 > 0 and nota1 <= 10:
        break
nota2 = float(input("Digite a sua 2º nota "))
while nota2 <= 0 or nota2 > 10:
    print("2º nota inválida, tente novamente")
    nota2 = float(input("Digite a sua 2º nota: "))
    if nota2 > 0 and nota2 <= 10:
        break
nota3 = float(input("Digite a sua 3º nota "))
while nota3 <= 0 or nota3 > 10:
    print("3º nota inválida, tente novamente")
    nota3 = float(input("Digite a sua 3º nota: "))
    if nota3 > 0 and nota3 <= 10:
        break
nota4 = float(input("Digite a sua 4º nota "))
while nota4 <= 0 or nota4 > 10:
    print("4º nota inválida, tente novamente")
    nota4 = float(input("Digite a sua 4º nota: "))
    if nota4 > 0 and nota4 <= 10:
        break

nota.append(nota1)
nota.append(nota2)
nota.append(nota3)
nota.append(nota4)

print("A maior nota é" , (max(nota)))
print("A menor nota é" , (min(nota)))
print("A soma das notas são" , (sum(nota)))
print("Existem" , (len(nota)) , "notas na lista")

media = sum(nota) / len(nota)

print(f"A média das notas é {media:.1f}")

if media >= 7:
    print("Você foi aprovado")
else:
    print("Você foi reprovado")
