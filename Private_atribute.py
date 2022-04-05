class data():
    __barang = 200 # private
 
    def __init__(self, nama_barang):
        self.nama = nama_barang
 
    def harga_barang(self,harga_barang):
       hasil = self.__barang * harga_barang
       return hasil
 
produk = data("Skincare")
print(produk.harga_barang(125000))
