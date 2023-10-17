import re

class LinkerLoader:

    def __init__(self):
        self.spetialChars = r'\{(\d+)\}'

    def linkLoad(self, virtualMachine, startPoint):
        for i in range(startPoint,len(virtualMachine.object_code)):
            alocatedValue = re.sub(self.spetialChars, lambda match: bin(int(match.group(1))+startPoint)[2:],virtualMachine.object_code[i-startPoint])
            virtualMachine.table_ram[i] = alocatedValue
