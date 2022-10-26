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
              self.text += lista_llave.index(lista[i]) + " "
        return self.text[:-1]  # otra forma de escribirlo es [:-1]


# for i in values:
#               self.text += list(values.keys()
#                                 )[list(values.values()).index(lista[i])] + " "
#         return self.text[:-1]  # otra forma de escribirlo es [:-1]

# class Compress:

#     def compress(self, text):
#         compressed = []
#         values = {}
#         n = 1
#         text_list = text.split(" ")
#         for z in text_list:
#             if not z in values:
#                 values[z] = n
#                 n = n + 1

#         for x in text_list:
#             if x in values:
#                 y = values[x]
#                 compressed.append(y)
#         return compressed, values

#     def uncompress(self, compre, value):
#         text = ""
#         lista = value.keys()
#         lista = list(lista)
#         for x in compre:
#             x -= 1
#             z = lista[x]
#             text = text + ' ' + z
#         return text[1:]


# # def uncompress(self, token_stream, token_table) -> str:
# #     inverted_dict = {value: key for key, value in token_table.items()}
# #     string = ""
# #     for token in token_stream:
# #         string += inverted_dict[token] + " "
# #     return string.strip()




# def uncompress(self, list, dictionary):
#     text = ''
#     for i in list:
#         text += text.join([f'{key} ' for key, value in dictionary.items() if i == value])
#     return text.rstrip()
