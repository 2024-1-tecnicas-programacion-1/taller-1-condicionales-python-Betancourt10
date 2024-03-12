def evaluar(peso, estatura, edad):
    edad = edad 
    total =peso / (estatura**2) 

    if edad < 45 and edad > 0: 
        if total <22.0 and total > 0: 
            return "Bajo." 
        elif total >= 22.0 and total > 0: 
            return "Medio." 
        else: 
            return "Error." 
    elif edad >= 45 and edad > 0: 
        if total < 22.0 and total > 0: 
            return "Medio." 
        elif total >= 22.0 and total > 0: 
            return "Alto." 
        else: 
            return "Error." 
    else: 
        return "Error."

if __name__ == '__main__':
    print("Peso:", end="")
    peso = int(input())
    print("Estatura:", end="")
    estatura = float(input())
    print("Edad:", end="")
    edad = int(input())
        
    respuesta = evaluar(peso, estatura, edad)
    print(respuesta)
