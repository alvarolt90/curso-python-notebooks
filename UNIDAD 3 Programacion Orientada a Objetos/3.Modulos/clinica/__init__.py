from paciente import Paciente
from doctor import Doctor
#import doctor as d
if __name__ == "__main__":
    doctor1 = Doctor("doctor1","apellido")
    print("El doctor "+doctor1.nombre + " va a fichar")
    doctor1.fichar()

    paciente = Paciente("paciente1","dolor de cabeza")

    doctor1.tratar_paciente(paciente);





