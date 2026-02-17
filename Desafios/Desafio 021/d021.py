from rich.console import Console

console = Console()

class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self.destampada = False

    def destampar(self):
        self.destampada = True
        console.print("Caneta destampada.", style="bold green")

    def tampar(self):
        self.destampada = False
        console.print("Caneta tampada.", style="bold yellow")

    def escrever(self, frase):
        if not self.destampada:
            console.print("A caneta está tampada!", style="bold red")
            return
        console.print(frase, style=self.cor)

    def quebrar_linha(self, num_linhas):
        for _ in range(num_linhas):
            print("\n")


c = Caneta("blue")

c.escrever("Tentando escrever")  # bloqueado

c.destampar()

c.escrever("Agora está funcionando")
c.quebrar_linha(2)
c.escrever("Nova linha")

c.tampar()
c.escrever("Não deveria escrever")
