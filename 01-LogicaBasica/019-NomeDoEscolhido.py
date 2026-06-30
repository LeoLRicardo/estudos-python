#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
import random
pri=input("Qual nome do primeiro aluno? ")
seg=input("Qual nome do segundo aluno? ")
ter=input("Qual nome do terceiro aluno? ")
qua=input("Qual nome do quarto aluno? ")
alunos=[pri,seg,ter,qua]
print(f"O aluno a apagar o quadro é: {random.choice(alunos)}")