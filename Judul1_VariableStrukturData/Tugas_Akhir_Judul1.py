produk = ["MacBook", "IPad", "IPhone", "Apple Watch"]
harga = [19000000, 7000000, 17000000, 15000000]

class Node:
    def __init__(self, data, harga):
        self.data = data
        self.harga = harga
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data, harga):
        new = Node(data, harga)
        if self.head == None:
            self.head = new
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = new

    def delete(self):
        if self.head != None:
            self.head = self.head.next

    def display(self):
        cur = self.head
        while cur != None:
            print(cur.data, "-", cur.harga)
            cur = cur.next

riwayat = []

def menu():
    print("DAFTAR MENU KERANJANG BELANJA")
    print("1. Tampilkan Daftar Produk")
    print("2. Tambahkan Barang")
    print("3. Hapus Barang")
    print("4. Tampilkan Keranjang")
    print("5. Riwayat")
    print("6. Keluar")
    

keranjang = LinkedList()
while True:
    menu()
    pilih = input("Pilih daftar menu keranjang belanja: ")

    if pilih == "1":
        print("Daftar produk:")
        for i in range(len(produk)):
            print(i+1, produk[i], "-", harga[i])
        print("Address:", id(produk))

    elif pilih == "2":
        print("Daftar produk:")
        for i in range(len(produk)):
         print(i+1, produk[i], "-", harga[i])
        i = int(input("Masukkan nomor produk: ")) - 1
        if i >= 0 and i < len(produk):
            keranjang.insert(produk[i], harga[i])
            riwayat.append(produk[i])
        else:
            print("Produk tidak ada")

    elif pilih == "3":
        print("Isi Keranjang:")
        keranjang.display()
        keranjang.delete()
        print("Barang berhasil dihapus")

    elif pilih == "4":
        keranjang.display()

    elif pilih == "5":
        print("Riwayat:", riwayat)

    elif pilih == "6":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak ada dalam daftar menu")