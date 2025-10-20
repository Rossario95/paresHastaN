def imprimirParesHastaN(n):
    if type(n) != int or n < 1:
        raise Exception("n debe ser entero positivo.")
    n = n - n % 2
    imprimirParesHastaNAux(n)
    print()

def imprimirParesHastaNAux(n):
    if n == 0:
        return
    else:
        imprimirParesHastaNAux(n - 2)
        print(n, end=" ")

# Ejemplo de ejecución
imprimirParesHastaN(10)
