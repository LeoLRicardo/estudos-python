#Faça um programa que leia um ângulo qualquer e mostra na tela o valor do seno, cosseno e tangente desse ângulo
import math
a=int(input("Digite aqui o número inteiro do ângulo:"))
print(f"Referente ao ângulo {a}°")
print(f"o Seno é:{(math.sin(math.radians(a))):.2f}")
print(f"O Cosseno é:{(math.cos(math.radians(a))):.2f}")
print(f"A Tangente é:{(math.tan(math.radians(a))):.2f}")