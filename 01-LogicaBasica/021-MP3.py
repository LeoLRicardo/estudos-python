#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3
import pygame
pygame.mixer.init()
pygame.mixer.music.load("01-LogicaBasica/Linkin021.mp3")
pygame.mixer.music.play()
input("Ouvindo a música... Aperte ENTER para encerrar.")