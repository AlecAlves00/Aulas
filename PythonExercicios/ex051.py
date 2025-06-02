"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,mostre os 10 primeiros termos dessa progressão."""

primeironum = int(input('Digite o primeiro termo: '))
razao = int(input('Qual será a razão da PA: '))
for c in range(10):
    pa = primeironum + c * razao
    print(pa)

