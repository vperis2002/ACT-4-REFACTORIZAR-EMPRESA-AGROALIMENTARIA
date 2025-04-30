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

class Refrigerados(Producto):
    def __init__(self, nombre, fecha_caducidad, numero_lote, cod_organismo):
        super().__init__(nombre, fecha_caducidad, numero_lote)
        self.cod_organismo = cod_organismo

class Congelados(Producto):
    def __init__(self, nombre, fecha_caducidad, numero_lote, temperatura):
        super().__init__(nombre, fecha_caducidad, numero_lote)
        self.temperatura = temperatura

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
                nombre = input("Dime el nombre del producto: ")
                fecha_caducidad = input("Dime la fecha de caducidad: ")
                numero_lote = int(input("Dime el número de lote: "))
                fecha_envasado = input("Dime la fecha de envasado: ")
                pais_origen = input("Dime el país de origen: ")
                producto = Frescos(nombre, fecha_caducidad, numero_lote, fecha_envasado, pais_origen)
                lista_frescos.append(producto)
            case 2:
                nombre = input("Dime el nombre del producto: ")
                fecha_caducidad = input("Dime la fecha de caducidad: ")
                numero_lote = int(input("Dime el número de lote: "))
                producto = Refrigerados(nombre)
                lista_refrigerados.append(producto)
            case 3:
                nombre = input("Dime el nombre del producto: ")
                fecha_caducidad = input("Dime la fecha de caducidad: ")
                numero_lote = int(input("Dime el número de lote: "))
                producto = Congelados(nombre)
                lista_congelados.append(producto)
            case 4:
                print("TERMINANDO LISTA...")
        print("1. FRESCOS")
        print("2. REFRIGERADOS")
        print("3. CONGELADOS")
        print("4. TERMINAR")
        tipo = int(input("Dime que tipo de producto quieres agregar: "))
    print("LISTA FRESCOS: ")
    for fresco in lista_frescos:
        print(fresco)
    print("LISTA REFRIGERADOS: ")
    for refrigerado in lista_refrigerados:
        print(refrigerado)
    print("LISTA CONGELADOS:")
    for congelado in lista_congelados:
        print(congelado)

main()
