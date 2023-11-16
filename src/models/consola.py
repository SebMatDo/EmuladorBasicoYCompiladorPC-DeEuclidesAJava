import sys
from io import StringIO

class CapturadorSalida:
    def __init__(self):
        self.IO = StringIO()
        self.STANDARD_IO = sys.stdout # Guardar la salida estándar original esto es como un backup
        sys.stdout = self # Redirigir la salida estándar al objeto capturador

    def write(self, mensaje):
        self.IO.write(mensaje)

    def flush(self):
        self.IO = StringIO()
    
    # DESTRUCTOR
    def __del__(self):
        sys.stdout = self.STANDARD_IO # Restaurar la salida estándar original
        print('Console destructor called.')