class Polisi:
    def _init_(self, inputNama, inputPemberani, inputPangkat):
        self.nama = inputNama
        self.Pemberani = inputPemberani
        self.pangkat = inputPangkat

polres1 = Polisi("Pistol",100,"Satlantas")
polres2 = Polisi("Senapan",150,"Patmor")

print(polres1.pangkat)