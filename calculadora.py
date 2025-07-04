def soma (x, y):     
    return x + y 

def subtrai (x, y):
    return x - y

def multiplica (x, y):
    return x * y

def divide (x, y):
    if y == 0:
        return "Erro na divisão:0 não se divide!"
    return x / y

print("Selecione a operação:")
print("1. Soma")
print("2. subtração")
print("3. multiplicação")
print("4. divisao")

escolha = input("escolha o numero da operação (1/2/3/4): ")

num1 = float(input("digite o primeiro numero:"))
num2 = float(input("digite o segundo numero "))

if escolha == '1':
    print("Resultado:", soma(num1, num2))

elif escolha == '2':
    print("Resultado:", subtrai(num1, num2))

elif escolha == '3':
    print("Resultado:", multiplica(num1, num2))

elif escolha == '4':
    print("Resultado:", divide(num1, num2))

else:
    print("Opção invalida. ")
