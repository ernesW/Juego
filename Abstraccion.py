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
        

mi_Personaje = personaje("Gojo", 100, 120, 20)
mi_enemigo = personaje("Toji", 100, 10, 10)

mi_Personaje.seubir_nivel(2, 4, 6)
mi_Personaje.atacar(mi_enemigo)
mi_Personaje.print()
mi_enemigo.print()



