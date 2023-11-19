import re

from src.utils.convertions import decimalToBinary


class LinkerLoader:

    def __init__(self):
        self.spetialNums= r'\{(\d+)\}'
    
    # Función que se encarga de reemplazar las posiciones en memoria por su valor en binario no relativo sino exacto
    def matchBinary(self, match):
        return decimalToBinary(int(match.group(1))+self.startPoint)[2:]

    # Carga y actualiza la máquina para empezar a correr las instrucciones desde este punto
    def linkLoad(self, virtualMachine, startPoint):
        self.startPoint = startPoint
        self.virtualMachine = virtualMachine
        self.virtualMachine.instruccion_actual = startPoint
        self.virtualMachine.instruccion_siguiente = startPoint

        for i in range(startPoint,len(virtualMachine.object_code)):
            row = virtualMachine.object_code[i-startPoint]    
            alocatedValue = re.sub(self.spetialNums, self.matchBinary, row)
            virtualMachine.table_ram[i] = alocatedValue

