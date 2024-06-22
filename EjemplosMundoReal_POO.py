class Habitacion:
    def __init__(self, numero, capacidad, precio_por_noche):
        self.numero = numero
        self.capacidad = capacidad
        self.precio_por_noche = precio_por_noche
        self.reservada = False
    
    def reservar(self):
        if not self.reservada:
            self.reservada = True
            print(f"Habitación {self.numero} reservada.")
        else:
            print(f"Habitación {self.numero} no disponible para reservar.")

    def liberar(self):
        if self.reservada:
            self.reservada = False
            print(f"Habitación {self.numero} liberada.")
        else:
            print(f"Habitación {self.numero} no estaba reservada.")

    def mostrar_informacion(self):
        estado = "Reservada" if self.reservada else "Disponible"
        print(f"Habitación {self.numero}: Capacidad {self.capacidad}, Precio por noche {self.precio_por_noche}, Estado: {estado}")


class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, numero, capacidad, precio_por_noche):
        habitacion = Habitacion(numero, capacidad, precio_por_noche)
        self.habitaciones.append(habitacion)

    def buscar_habitacion(self, numero):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero:
                return habitacion
        return None


# Ejemplo de uso del sistema de reservas en el hotel
hotel = Hotel("Hotel Ejemplo")

hotel.agregar_habitacion(101, 2, 50)
hotel.agregar_habitacion(102, 3, 75)
hotel.agregar_habitacion(103, 4, 100)

habitacion101 = hotel.buscar_habitacion(101)
habitacion102 = hotel.buscar_habitacion(102)
habitacion103 = hotel.buscar_habitacion(103)

habitacion101.mostrar_informacion()
habitacion101.reservar()
habitacion101.reservar()
habitacion102.reservar()
habitacion101.liberar()
habitacion101.mostrar_informacion()
