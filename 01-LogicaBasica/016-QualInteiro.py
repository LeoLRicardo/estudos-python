#Crie um programa que leia um número real qualquer pelo teclado e mostra na tela a porção inteira.
#EX: Digite um número : 6.127
#O número 6.127 tem a parcela inteira 6
import math
n=float(input("Digite um número: "))
print(f"O número: {n}\nTem como parte inteira {math.trunc(n)}")