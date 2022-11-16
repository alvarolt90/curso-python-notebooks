import datetime
import random

class Doctor():

    def __init__(self, nombre, apellido, hora_entrada=None):
        self.nombre = nombre
        self.apellido = apellido
        self.hora_entrada = hora_entrada

    def fichar (self):
        self.hora_entrada = datetime.datetime.now()
        print("El doctor "+ self.nombre + " ha fichado a las " + str(self.hora_entrada))

    def tratar_paciente (self, paciente):
        print("El doctor "+self.nombre + " esta atendiendo al paciente " + paciente.nombre)
        num = random.random()
        if (num>0.5):#El paciente esta grave
            paciente.enfermedad = "Covid"
            print("el paciente " + paciente.nombre + " tiene " + paciente.enfermedad)
        else:
            print("el paciente " + paciente.nombre + " no esta grave")

print("Hola")