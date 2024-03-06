import time

def primeiraIda():
    print("Ligando o primeiro interruptor")
    time.sleep(2)  
    print("Desligando o primeiro interruptor")
    print("Ligando o segundo interruptor")

def segundaIda():
    print("Você entrou na sala das lâmpadas")
    l1 = input("A lâmpada 1 está acesa? (s/n): ")
    l2 = input("A lâmpada 2 está quente? (s/n): ")
    l3 = input("A lâmpada 3 está quente? (s/n): ")
    if l1 == "s":
        print("O primeiro interruptor controla a lâmpada 1.")
    elif l2 == "s":
        print("O segundo interruptor controla a lâmpada 2.")
    elif l3 == "s":
        print("O terceiro interruptor controla a lâmpada 3.")
    else:
        print("Erro: As condições não correspondem a nenhum interruptor.")

print("Primeira ida:")
primeiraIda()

print("\nSegunda ida:")
segundaIda()