def evaluar(anno):
    if anno % 4 != 0: 
        return str(anno) + "No es bisiesto" 
    elif anno % 100 != 0 
        return str(anno) + "Es bisiesto" 
    elif anno % 400 == 0 
        return str(anno) + "Es bisiesto" 
    else: 
        return str(anno) + "No es bisiesto";

if __name__ == '__main__':
    print("Año:", end="")
    anno = int(input())

    respuesta = evaluar(anno)
    print(respuesta)
