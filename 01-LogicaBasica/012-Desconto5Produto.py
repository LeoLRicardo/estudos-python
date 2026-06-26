#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
p=(float(input("Qual o preço do produto? ")))
print(f"O preço do produto era: {p} e passou a ser: {p-(5/100*p)}")