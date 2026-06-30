#O mesmo professor do desafio anterior (019) quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostra a ordem sorteada.
#Reutilizei muita coisa do 019
import random
pri=input("Qual nome do primeiro aluno? ")
seg=input("Qual nome do segundo aluno? ")
ter=input("Qual nome do terceiro aluno? ")
qua=input("Qual nome do quarto aluno? ")
alunos=[pri,seg,ter,qua]
random.shuffle(alunos)
print(f"Os alunos que irão apresentar o trabalho em ordem são: 1°-{alunos[0]},2°-{alunos[1]}, 3°-{alunos[2]}, 4°-{alunos[3]}")