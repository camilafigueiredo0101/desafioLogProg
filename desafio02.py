def verificaFibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    if b == numero:
        return True
    else:
        return False

num = int(input("Digite um número para verificar se ele pertence à sequência de Fibonacci: "))

if verificaFibonacci(num):
    print(f"O número {num} pertence à sequência.")
else:
    print(f"O número {num} não pertence à sequência.")
