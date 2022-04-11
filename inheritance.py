class kendaraan:
  def __init__(self, merk, harga, tahun):
    self.merk = merk
    self.harga = harga
    self.tahun = tahun
 
  def printname(self):
    print(self.merk, 'Harga: Rp,',self.harga, 'Keluaran Tahun :',self.tahun)

class mobil(kendaraan):
  pass

car1 = mobil("BMW", "90.000.000", "2009")
car1.printname()
car1 = mobil("Lamborghini", "2.500.000.000", "2020")
car1.printname()
