class Livro:
    def __init__(self,nome,paginas,atual = 1):
        self.titulo = nome
        self.paginas = paginas
        self.pagatual = atual
        print(f"Você acabou de abrir o livro {self.titulo} que tem {self.paginas} páginas no total. Você está na página {self.pagatual}")
    def avancar_paginas(self,qntd):
        nova_pagina = self.pagatual + qntd

        if nova_pagina <= self.paginas:
            self.pagatual = nova_pagina
            print(f"Você avançou {qntd} páginas e agora está na página {self.pagatual}")
        else:
            print("Você não pode avançar além do total de páginas do livro")

       
l1   = Livro("10 coisas que eu aprendi",20)  
l1.avancar_paginas(100)