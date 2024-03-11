def evaluar(dividendo, divisor):
    if dividendo % divisor == 0: 
        cociente = dividendo // divisor
        residuo = dividendo % divisor
        respuesta = "La división es exacta. \n" \
                "Cociente: " + str(cociente) + "\n" \
                "Residuo: " + str(residuo)
        return respuesta 
    else: 
        cociente = dividendo // divisor 
        residuo = dividendo % divisor 
        respuesta = "La división es exacta. \n" \
                "Cociente: " + str(cociente) + "\n" \
                "Residuo: " + str(residuo)
        return respuesta

if __name__ == '__main__':
    print("Dividendo:", end="")
    dividendo = int(input())
    print("Divisor:", end="")
    divisor = int(input())

    respuesta = evaluar(dividendo, divisor)
    print(respuesta)
