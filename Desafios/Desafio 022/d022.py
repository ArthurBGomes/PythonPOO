from rich import print
from rich.panel import Panel
class ControleRemoto:
    canal_min:int = 1
    canal_max:int = 6
    vol_min:int = 1
    vol_max:int = 5
    def __init__(self,canal=1,volume=2):
        self.canal_atual: int = canal
        self.volume: int = volume
        self.ligado: bool = False
    def liga_desliga(self):
        self.ligado = not self.ligado
    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min
            else:
                self.canal_atual += 1
    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max
            else:
                self.canal_atual -= 1
    def volume_mais(self):
        if self.ligado:
            if self.volume != ControleRemoto.vol_max:
                self.volume += 1
    def volume_menos(self):
        if self.ligado:
            if self.volume != ControleRemoto.vol_min:
                self.volume -= 1
    def mostrar_tv(self):
        conteudo = ''
        if not self.ligado:
            conteudo += f":prohibited:[red]TV Desligada[/]:prohibited:"
        else:
            conteudo += "Canais:"
            for canal in range(__class__.canal_min,__class__.canal_max+1):
                if canal == self.canal_atual:
                    conteudo += f"[yellow on yellow] {canal} [/yellow on yellow]"
                else:
                    conteudo += f" {canal} "
            conteudo += f"\nVolume:"
            for volume in range(ControleRemoto.vol_min,ControleRemoto.vol_max + 1):
                if volume <= self.volume:
                    conteudo += f" [black on green].[/] "
                else:
                    conteudo += f" [black on white].[/]"
        tv = Panel(conteudo, title=f" [ TV ]", width=30,)
        print(tv)
tv = ControleRemoto(1,1)
while True:
    tv.mostrar_tv() 
    comando = str(input(f" <CH> - VOL +"))
    match comando:
        case '0':
            break
        case '@':
            tv.liga_desliga()
        case '>':
            tv.canal_mais()
    
        case '<':
            tv.canal_menos()
        case '+':
            tv.volume_mais()
        case '-':
            tv.volume_mais()
    print("\n"* 20)
