# Função para gerar a sequência de Fibonacci até o número informado
def fibonacci_sequence(num):
    fibonacci = [0, 1]
    while fibonacci[-1] < num:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

# Função para verificar se o número pertence à sequência de Fibonacci
def is_in_fibonacci(num):
    sequence = fibonacci_sequence(num)
    if num in sequence:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."

# Exemplo de teste
num = 8  # Você pode alterar este valor para testar outros números
result = is_in_fibonacci(num)
print(result)