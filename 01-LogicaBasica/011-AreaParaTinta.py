#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
l=float(input("Qual a largura? "))
a=float(input("Qual a Altura? "))
print(f"A área da pintura é:\n{l*a}\nE a quantidade de tinta para pintá-la é:\n{(l*a)/2}.")