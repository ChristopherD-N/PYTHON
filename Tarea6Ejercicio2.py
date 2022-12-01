class Alumno:
    
    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        
    def imprimir(self):
        print("Nombre:", self.nombre, "Nota:", self.nota)
    
    def resultado(self):
        
        if self.nota < 5:
            print("El alumno esta suspenso")
        else:
            print("El alumno esta aprobado")
            
            
alumno1 = Alumno()
alumno2 = Alumno()

alumno1.inicializar("Maria", 7)
alumno2.inicializar("Pablo", 3)

alumno1.imprimir()
alumno1.resultado()
alumno2.imprimir()
alumno2.resultado()
    

    
        

    

        
    
