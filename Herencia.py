class personaje():

    def __init__(self, nombre, vida, fuerza, defensa) -> None:
        self.nombre = nombre
        self.vida = vida
        self.fuerza = fuerza
        self.defensa = defensa

    def print(self):
        print(self.nombre, ":")
        print("-Vida:", self.vida)
        print("-Fuerza:", self.fuerza)
        print("-Defensa:", self.defensa)

    def seubir_nivel(self, vida, fuerza, defensa):
        self.vida = self.vida + vida
        self.fuerza = self.fuerza + fuerza
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")
    
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha hecho", daño, "puntos de daño a", enemigo.nombre)
        
        if enemigo.esta_vivo():
            print("la vida de", enemigo.nombre, "es", enemigo.vida )
        else:
            enemigo.morir()

class hechicero(personaje):
    
    def __init__(self, nombre, vida, fuerza, defensa, magia) -> None:
        super().__init__(nombre, vida, fuerza, defensa)
        self.magia = magia

    def cambiar_magia(self):
        opcion = int(input("Elige el tipo de magia: (1) Magia Azul daño 7. (2) Magia Roja daño 9."))
        if opcion == 1:
            self.magia = 7
        elif opcion == 2:
            self.magia = 9
        else:
            print("El numero introducido es incorrecto")

    def print(self):
        super().print()
        print("-Magia:", self.magia)

    def daño(self, enemigo):
        return self.fuerza * self.magia - enemigo.defensa

class peleador(personaje):

    def __init__(self, nombre, vida, fuerza, defensa, espada) -> None:
        super().__init__(nombre, vida, fuerza, defensa)
        self.espada = espada

    def cambiar_espada(self):
        opcion = int(input("Elige una espada: (1) Espada Zenin daño 7. (2) Espada Alabarda daño 9."))
        if opcion == 1:
            self.espada = 7
        elif opcion == 2:
            self.espada = 9
        else:
            print("El numero introducido es incorrecto")

    def print(self):
        super().print()
        print("-Espada:", self.espada)

    def daño(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa

Persona = personaje("Paco", 100, 8, 5)
Gojo = hechicero("Gojo", 100, 8, 5, 5)
Toji = peleador("Toji", 100, 8, 5, 5)

# Toji.cambiar_espada()
Gojo.cambiar_magia()

Persona.atacar(Gojo)
Gojo.atacar(Toji)
Toji.atacar(Persona)

Persona.print()
Gojo.print()
Toji.print()