def fibonacci(limite):
    a, b = 0, 1
    fb = [a, b]
    
    while b < limite:
        a, b = b, a + b
        fb.append(b)
    return fb

valor = int(input("Digite um numero: "))
fb = fibonacci(valor)


if valor in fb:
    print(f"Sim!O número {valor} pertence à sequência de Fibonacci.")
else:
    print(f"Não!O número {valor} não pertence à sequência de Fibonacci.")
