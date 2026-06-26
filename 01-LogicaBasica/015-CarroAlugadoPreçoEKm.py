#Escreva um programa que pergunta a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km=float(input("Qual o número de Km percorrido pelo carro alugado? "))
d=int(input("Qual a quantidade de dias que ele foi alugado? "))
print(f"Você precisa pagar: R${60*d + 0.15*km}")