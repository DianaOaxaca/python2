class mamifero():
    #...
    # Atributos de instancia
    alimentacion = ''   # carnívoro, omnívoro, etc
    # ...
    # Cuántos puede tener y cuántos van a sobrevivir
    def reproducirse(self, max_progenie):
        self.progenie +=  choice(range( max_progenie))
    def crecer(self, crecimiento):
        self.altura += crecimiento
        self.peso += crecimiento * 0.4
perro = mamifero()
perro.alimentacion

perro.alimentacion = 'omnivoro'
perro.alimentacion
perro.altura = 43
perro.peso = 6.1


class animal():
    tipo = ''
    def __init__(self, tipo) -> None:
        self.tipo = tipo
    def haz_ruido(self):
        gallina = "kiiriki"
        if gallina:
            print(gallina)
        else:
            print("no es gallina")

tipo = animal('pollo')
tipo.haz_ruido()

##ejemplo de Phabel
class animal():
    nombre = ''
    edad = 0
    ruido = ''

    def __init__(self, nombre, edad, ruido):
        self.nombre = nombre
        self.edad = edad
        self.ruido = ruido

    def haz_ruido(self):
        print(self.ruido)

perro = animal('Rex', 10, 'XOXO')
perro.haz_ruido()
