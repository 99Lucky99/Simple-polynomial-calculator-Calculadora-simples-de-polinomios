import sys
import sympy as sp

print("1: para ADIÇÃO \n2: para SUBTRAÇÃO \n3: para MULTIPLICAÇÃO \n4: para DIVISÃO ")
numero_opera = input("Digite o valor da operação: ")
equacao1 = sp.sympify(input("\nDigite a primeira equação polinomial Exemplo. x^3 + x^2 + 2 : "))
equacao2 = sp.sympify(input("\nDigite a segunda equação polinomial Exemplo. x^2 - x + 1 : "))

if numero_opera != '1' and numero_opera != '2' and numero_opera != '3' and numero_opera != '4':
    print("Numero da operação invalido")
    sys.exit()


def operacao(x, y, oper):
    if oper == '1':
        result = x + y
        return result
    elif oper == '2':
        result = x - y
        return result
    elif oper == '3':
        result = sp.expand(x * y)
        return result
    elif oper == '4':
        resultado, resto = sp.div(x, y, domain='QQ', polys=True)
       # fatores = resultado.factor_list()
        expressao = resultado.as_expr() + resto.as_expr() / y.as_expr()
        return sp.pprint(expressao)

if numero_opera == '1' or numero_opera == '2' or numero_opera == '3':
    resultado = operacao(equacao1, equacao2, numero_opera)
    resultado = str(resultado)
    resultadoconvertido = ''
elif numero_opera == '4':
    print("\nO resultado da divisão é:")
    resultado = operacao(equacao1, equacao2, numero_opera)
    sys.exit()

somador_da_troca_do_sinal = 0
for i in resultado:
    if i == '*':
        somador_da_troca_do_sinal = somador_da_troca_do_sinal + 1
        if somador_da_troca_do_sinal == 2:
            resultadoconvertido = resultadoconvertido + '^'
            somador_da_troca_do_sinal = 0
    else:
       somador_da_troca_do_sinal = 0
       resultadoconvertido = resultadoconvertido + i
            
if numero_opera == '1':
    print("\nO resultado da soma é:", resultadoconvertido)
elif numero_opera == '2':
    print("\nO resultado da subtração é:", resultadoconvertido)
elif numero_opera == '3':
    print("\nO resultado da multiplicação é:", resultadoconvertido)

