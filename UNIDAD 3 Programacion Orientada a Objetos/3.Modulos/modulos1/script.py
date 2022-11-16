#Primera forma, si queremos usar varias funciones de un módulo

"""
import saludos

print("Empezando Primera forma parte 1")
saludos.saludo2()
s = saludos.Saludo()
s.saludar()
saludos.despedir()


#Lo mismo pero asignando un alias
import saludos as sal

print("Empezando Primera forma parte 2")
sal.saludo2()
s = sal.Saludo()
s.saludar()
sal.despedir()

"""
#Segunda forma, importamos aquello que necesitamos
#from saludos import despedir
#from saludos import saludo2, despedir
#from saludos import Saludo

#from saludos import despedir, saludo2
from saludos import Saludo
saludo = Saludo()
saludo.saludar()

