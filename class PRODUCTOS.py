class Producto:
    def __init__(self, nombre, fecha_caducidad, numero_lote):
        self.nombre = nombre
        self.fecha_caducidad = fecha_caducidad
        self.numero_lote = numero_lote
    def __str__(self):
        return self.nombre + " FECHA DE CADUCIDAD: " + self.fecha_caducidad + " NÚMERO DE LOTE: " + self.numero_lote

class Frescos(Producto):
    def __init__(self, nombre, fecha_caducidad, numero_lote, fecha_envasado, pais_origen):
        super().__init__(nombre, fecha_caducidad, numero_lote)
        self.fecha_envasado = fecha_envasado
        self.pais_origen = pais_origen

    def __str__(self):
        return f"{super().__str__()} | Envasado: {self.fecha_envasado} | Origen: {self.pais_origen}"

class Refrigerados(Producto):
    def __init__(self, nombre, fecha_caducidad, numero_lote, cod_organismo):
        super().__init__(nombre, fecha_caducidad, numero_lote)
        self.cod_organismo = cod_organismo

    def __str__(self):
        return f"{super().__str__()} | Código organismo: {self.cod_organismo}"

class Congelados(Producto):
    def __init__(self, nombre, fecha_caducidad, numero_lote, temperatura):
        super().__init__(nombre, fecha_caducidad, numero_lote)
        self.temperatura = temperatura

    def __str__(self):
        return f"{super().__str__()} | Temperatura: {self.temperatura}°C"

def agregar_frescos(lista_frescos):
    nombre = input("Dime el nombre del producto: ")
    fecha_caducidad = input("Dime la fecha de caducidad: ")
    numero_lote = int(input("Dime el número de lote: "))
    fecha_envasado = input("Dime la fecha de envasado: ")
    pais_origen = input("Dime el país de origen: ")
    producto = Frescos(nombre, fecha_caducidad, numero_lote, fecha_envasado, pais_origen)
    lista_frescos.append(producto)

def agregar_refrigerados(lista_refrigerados):
    nombre = input("Dime el nombre del producto: ")
    fecha_caducidad = input("Dime la fecha de caducidad: ")
    numero_lote = int(input("Dime el número de lote: "))
    producto = Refrigerados(nombre)
    lista_refrigerados.append(producto)

def agregar_congelados(lista_congelados):
    nombre = input("Dime el nombre del producto: ")
    fecha_caducidad = input("Dime la fecha de caducidad: ")
    numero_lote = int(input("Dime el número de lote: "))
    producto = Congelados(nombre)
    lista_congelados.append(producto)

def imprimir_listas(lista_frescos, lista_refrigerados, lista_congelados):
    print("LISTA FRESCOS: ")
    for fresco in lista_frescos:
        print(fresco)
    print("LISTA REFRIGERADOS: ")
    for refrigerado in lista_refrigerados:
        print(refrigerado)
    print("LISTA CONGELADOS:")
    for congelado in lista_congelados:
        print(congelado)

def main():
    lista_frescos = []
    lista_refrigerados = []
    lista_congelados = []
    print("1. FRESCOS")
    print("2. REFRIGERADOS")
    print("3. CONGELADOS")
    print("4. TERMINAR")
    tipo = int(input("Dime que tipo de producto quieres agregar: "))
    while tipo == 1  or tipo == 2 or tipo == 3:
        match tipo:
            case 1:
                agregar_frescos(lista_frescos)
            case 2:
                agregar_refrigerados(lista_refrigerados)
            case 3:
                agregar_congelados(lista_congelados)
            case 4:
                print("TERMINANDO LISTA...")
        print("1. FRESCOS")
        print("2. REFRIGERADOS")
        print("3. CONGELADOS")
        print("4. TERMINAR")
        tipo = int(input("Dime que tipo de producto quieres agregar: "))
    imprimir_listas(lista_frescos, lista_refrigerados, lista_congelados)


main()
