""""
Al importar un módulo, Python busca en varios lugares.
El Interprete primero busca un módulo integrado. Luego (si no se encuentra el módulo incorporado), Python busca en una
lista de directorios definidos en sys.path. La búsqueda es en este orden.
    + El directorio actual.
    + PYTHONPATH (una variable de entorno con una lista de directorios).
    + El directorio predeterminado dependiente de la instalación.
"""
import sys
print(sys.path)

import modulos1.saludos as s
saludo = s.Saludo()

