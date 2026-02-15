class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco
    def etiqueta(self):
        return (
            f"{'PRODUTO':^40}\n"
            f"{'-'*40}\n"
            f"Nome:  {self.nome:<25}\n"
            f"Preço: R$ {self.preco:>10.2f}\n"
            f"{'-'*40}"
        )
p1 = Produto("Caixa de Chocolate",15)
print(p1.etiqueta())