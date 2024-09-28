# Funções para as operações da calculadora
def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro! Divisão por zero."

# Menu da calculadora
def calculadora():
    print("Selecione a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    while True:
        escolha = input("Digite o número da operação desejada (1/2/3/4): ")

        # Verificar se a escolha é válida
        if escolha in ('1', '2', '3', '4'):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                print(f"{num1} + {num2} = {soma(num1, num2)}")

            elif escolha == '2':
                print(f"{num1} - {num2} = {subtracao(num1, num2)}")

            elif escolha == '3':
                print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")

            elif escolha == '4':
                resultado = divisao(num1, num2)
                print(f"{num1} / {num2} = {resultado}")
            
            # Verificar se o usuário deseja realizar outra operação
            outra_operacao = input("Deseja fazer outra operação? (s/n): ")
            if outra_operacao.lower() != 's':
                break
        else:
            print("Escolha inválida. Por favor, tente novamente.")

# Executar a calculadora
calculadora()
