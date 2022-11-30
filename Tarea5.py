def añoBisiesto(Año):
    if (Año % 4 == 0 and Año % 100 != 0) or Año % 400 == 0:
        print("El año ",Año,"es bisiesto")
    else:
        print("El año ",Año,"no es bisiesto")
        
añoBisiesto(2024)
