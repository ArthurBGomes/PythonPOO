class Funcionário:
    # Atributo de classe
    empresa = "Curso em Vídeo"
    # Atributos de instância
    def __init__(self,nome,setor,cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    
    def apresentação(self):
        return f" Eu me chamo {self.nome}, atuo no setor de {self.setor} e possuo o cargo {self.cargo} na empresa {self.__class__.empresa}"
    

f1 = Funcionário("Arthur","TI","Dev Techlead")
# f1.empresa = "IFRN"
# print(f1.empresa)
print(f1.apresentação())