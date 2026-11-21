class Hamyon:
    def __init__(self, egasi, balans):
        self.egasi = egasi
        self.balans = balans

    def pul_korsat(self):
        print(f"Egasi: {self.egasi}")
        print(f"Balans: {self.balans} so'm")


class ElektronHamyon(Hamyon):
    def __init__(self, egasi, balans, xizmat):
        super().__init__(egasi, balans)
        self.xizmat = xizmat

    def pul_korsat(self):
        super().pul_korsat()
        print(f"Xizmat: {self.xizmat}")


hamyon = ElektronHamyon("Jasur", 150000, "Payme")
hamyon.pul_korsat()
