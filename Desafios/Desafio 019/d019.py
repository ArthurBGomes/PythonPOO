from rich import print
import time
class Livro:
    def __init__(self,nome,paginas,atual = 1):
        self.titulo = nome
        self.paginas = paginas
        self.pagatual = atual
        print(f"Você acabou de abrir o livro {self.titulo} que tem {self.paginas} páginas no total. Você está na página {self.pagatual}")
    def avancar_paginas(self,qntd=1):
        cont = 0
        for n in range(0,qntd,1):
            if not self.fim_do_livro:
                self.pagatual += 1
                print(f" Pág{self.pagatual}:arrow_forward:",end=" ")
                cont += 1
                time.sleep(0.2)
        print(f"\nVocê avançou {cont} páginas e agora está na página {self.pagatual}")
        if self.fim_do_livro:
            print(f":closed_book:[red] Você chegou ao final do livro[/]")
           
    @property
    def fim_do_livro(self):
        return True if self.pagatual == self.paginas else False

       
l1   = Livro("10 coisas que eu aprendi",20)  
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(100)