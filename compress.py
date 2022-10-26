# Carla Sofia Centeleghe
# Parcial
#text = "hola mundo hola" -> lista = [1, 2, 1] -> diccionario = {"hola": 1, "mundo": 2}

class Compress():
    
    def __init__(self): # inicialiso, creo lo que voy a usar en el codigo
        self.values = {} # diccionario, en la lista la palabra es la clave y el nuemro es el valor asignado
        self.text = ""
        self.lista = []  # lista

    def compress(self,text):  # en compress debo comprimir el texto y luego asignarle un valor, para asi usar el dicionario
        text = text.split(" ")
        contar = 1
        for i in text:
            if i not in self.values:
                self.values[i] = contar
                contar += 1
            self.lista.append(self.values[i])

        return [self.lista, self.values]

    def uncompress(self, lista, values): # ahora tengo que descomprimir, es decir el camino al revez
        #text = ''
        lista_llave = values.keys()
        lista_llave = list(lista_llave)
        for i in self.lista:
              self.text += lista_llave.index(self.lista[i]) + " "
        return self.text[:-1]  # otra forma de escribirlo es [:-1]


