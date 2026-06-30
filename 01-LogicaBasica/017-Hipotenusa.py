#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
import math
#Resolvi usar pow aqui ao invés de "**" para praticar as usabilidades do import(nesse caso, "math") 
op=float(input("Digite o número do cateto oposto: "))
ad=float(input("Digite o número do cateto adjacente: "))
h2=math.pow(op,2)+math.pow(ad,2)
print(f"O cateto oposto é: {op}, o Cateto adjacente é: {ad}\nSabendo disso, a hipotenusa é:{math.sqrt(h2)}")