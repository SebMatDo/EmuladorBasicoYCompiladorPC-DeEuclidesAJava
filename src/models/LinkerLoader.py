import re

class LinkerLoader:

    def __init__(self):
        # Define opcodes
        self.opcodes = {
            'Parar': '0000000000000000',
            'Cargar': '0001',
            'CargarValor': '0010',
            'Almacenar': '0011',
            'SaltarSiCero': '010000',
            'SaltarSiNeg': '010001',
            'SaltarSiPos': '010010',
            'SaltarSiDes': '010011',
            'Saltar': '010100',
            'Copiar': '011000000000',
            'Sumar': '011000000001',
            'Restar': '011000000010',
            'Mult': '011000000011',
            'Div': '011000000100',
            'A': '00',
            'B': '01',
            'C': '10',
            'D': '11'
        }
        self.spetialNums= r'\{(\d+)\}'
        self.spetialVars = r'\{([A-Za-z]*)\}'
        self.spetialGeneral = r'\{(.*?)\}'
    
    def matchBinary(self ,match):
        return bin(int(match.group(1))+self.startPoint)[2:]
    
    def matchLabels(self, match):
        return self.opcodes[str(match.group(1))]
        

    def linkLoad(self, virtualMachine, startPoint):
        self.startPoint = startPoint
        self.virtualMachine = virtualMachine
        self.virtualMachine.instruccion_actual = startPoint
        self.virtualMachine.instruccion_siguiente = startPoint

        for i in range(startPoint,len(virtualMachine.object_code)):
            row = virtualMachine.object_code[i-startPoint]
            matches = re.findall(self.spetialGeneral, row)
            if matches:
                jumps = ['SaltarSiCero','SaltarSiNeg','SaltarSiPos','SaltarSiDes','Saltar']
                virtualMachine.instrucciones_asm[i] = [int(j) if j.isdigit() else j for j in matches]
                if virtualMachine.instrucciones_asm[i][0] in jumps:
                    virtualMachine.instrucciones_asm[i][1]+=startPoint
                

            alocatedValue = re.sub(self.spetialNums, self.matchBinary, row)
            alocatedValue = re.sub(self.spetialVars, self.matchLabels, alocatedValue)
            virtualMachine.table_ram[i] = alocatedValue
