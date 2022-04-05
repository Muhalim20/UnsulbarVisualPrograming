class barang():
    jumlah_barang = 0
 
    def __init__(self, input_barang):
        self.nama = input_barang # public
        barang.jumlah_barang +=1

        
Laptop = barang("Laptop")
Mouse = barang("Mouse")
Keyboard = barang("Keyboard")
 
print(barang.jumlah_barang)

