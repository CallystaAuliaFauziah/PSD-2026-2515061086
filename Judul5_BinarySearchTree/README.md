Tugas Akhir Percobaan 5

Judul Program:

Sistem Pendataan Tinggi Badan Balita Menggunakan Binary Search Tree

<p style="text-align: justify;">
Sistem ini dibuat untuk menyimpan dan mengelola data tinggi badan balita. Data yang dimasukkan berupa nama balita dan tinggi badannya. Pengelolaan data menggunakan struktur Binary Search Tree (BST), di mana data dengan nilai lebih kecil akan ditempatkan di sisi kiri, sedangkan data dengan nilai lebih besar ditempatkan di sisi kanan. Sistem ini memiliki beberapa fitur, yaitu menambahkan data balita, mencari data berdasarkan nama, menampilkan data berdasarkan urutan tinggi dari terendah ke tertinggi, serta menampilkan data berdasarkan urutan proses awal sampai akhir dan dari akhir ke awal. Selain itu, sistem juga dapat menampilkan balita dengan tinggi badan terendah dan tertinggi, serta menghitung jumlah data yang sudah dimasukkan. Penggunaan Binary Search Tree membuat data menjadi lebih teratur dan proses pengolahan seperti pencarian dan penampilan data dapat dilakukan dengan lebih mudah tanpa perlu pengurutan manual.
<p/>

Source Code:

<img width="1632" height="5992" alt="code TAPSD JUDUL 5" src="https://github.com/user-attachments/assets/93be0b6c-3e89-4013-9ed5-a487010e1c82" />

Penjelasan Source Code:

Baris 1: Membuat class Node yang digunakan untuk menyimpan data pada setiap node di Binary Search Tree.

Baris 2-6: Membuat fungsi init() untuk mengatur data awal pada node berupa tinggi badan, nama balita, serta node kiri dan kanan.

Baris 8: Membuat class BSTBalita sebagai class utama untuk menjalankan proses Binary Search Tree.

Baris 9-10: Membuat fungsi init() untuk memberi nilai awal None pada root yang menandakan tree masih kosong.

Baris 12: Membuat fungsi insert_node() yang digunakan untuk menambahkan data baru ke dalam Binary Search Tree.

Baris 13-14: Mengecek apakah root kosong. Jika kosong maka program akan membuat node baru berisi data balita.

Baris 15-16: Jika tinggi badan lebih kecil dari root maka data dimasukkan ke bagian kiri tree.

Baris 17-18: Jika tinggi badan lebih besar dari root maka data dimasukkan ke bagian kanan tree.

Baris 20: Mengembalikan root setelah proses penambahan data selesai.

Baris 22-23: Membuat fungsi insert() untuk memanggil fungsi insert_node() agar data dapat dimasukkan ke BST.

Baris 25: Membuat fungsi search_nama() untuk mencari data balita berdasarkan nama.

Baris 26-27: Mengecek apakah root kosong. Jika kosong maka data dianggap tidak ditemukan.

Baris 28-29: Membandingkan nama yang dicari dengan nama pada node dengan fungsi lower() yang digunakan agar huruf besar dan kecil tetap dianggap sama.

Baris 30: Melakukan pencarian pada subtree kiri lalu menyimpan hasilnya ke variabel kiri.

Baris 31-32: Jika data ditemukan di subtree kiri maka hasil langsung dikembalikan.

Baris 33: Jika belum ditemukan maka pencarian dilanjutkan ke subtree kanan.

Baris 35-36: Membuat fungsi search() untuk menjalankan fungsi pencarian mulai dari root utama.

Baris 38: Membuat fungsi inorder() untuk menampilkan data berdasarkan urutan tinggi badan dari terendah ke tertinggi.

Baris 39-40: Mengecek apakah root kosong. Jika kosong maka fungsi berhenti.

Baris 41: Menelusuri subtree kiri terlebih dahulu.

Baris 42: Menampilkan nama balita dan tinggi badan.

Baris 43: Menelusuri subtree kanan.

Baris 45: Membuat fungsi preorder() untuk menampilkan data dimulai dari root terlebih dahulu.

Baris 46-47: Mengecek apakah root kosong. Jika kosong maka fungsi dihentikan.

Baris 48: Menampilkan data pada root.

Baris 49-50: Menelusuri subtree kiri lalu subtree kanan.

Baris 52: Membuat fungsi postorder() untuk menampilkan data mulai dari subtree terlebih dahulu kemudian root.

Baris 53-54: Mengecek apakah root kosong. Jika kosong maka fungsi dihentikan.

Baris 55-56: Menelusuri subtree kiri dan subtree kanan.

Baris 57: Menampilkan data root paling akhir.

Baris 59: Membuat fungsi find_min() untuk mencari data balita dengan tinggi badan paling rendah.

Baris 60-61: Mengecek apakah tree kosong. Jika kosong maka fungsi mengembalikan None.

Baris 62: Membuat variabel current untuk menyimpan posisi node saat ini.

Baris 63-64: Melakukan perulangan menuju node paling kiri karena nilai terkecil pada BST berada di sebelah kiri.

Baris 65: Mengembalikan node dengan tinggi badan paling rendah.

Baris 67: Membuat fungsi find_max() untuk mencari data balita dengan tinggi badan paling tinggi.

Baris 68-69: Mengecek apakah tree kosong. Jika kosong maka fungsi mengembalikan None.

Baris 70: Membuat variabel current untuk menyimpan posisi node saat ini.

Baris 71-72: Melakukan perulangan menuju node paling kanan karena nilai terbesar pada BST berada di sebelah kanan.

Baris 73: Mengembalikan node dengan tinggi badan paling tinggi.

Baris 75: Membuat fungsi count_nodes() untuk menghitung jumlah seluruh data balita.

Baris 76-77: Mengecek apakah root kosong. Jika kosong maka fungsi mengembalikan nilai 0.

Baris 78: Menghitung jumlah node pada subtree kiri dan kanan secara rekursif lalu ditambah 1 untuk root.

Baris 80: Membuat fungsi sum_nodes() untuk menghitung total seluruh tinggi badan balita.

Baris 81-82: Mengecek apakah root kosong. Jika kosong maka fungsi mengembalikan nilai 0.

Baris 83: Menjumlahkan seluruh tinggi badan balita dari subtree kiri, subtree kanan, dan root.

Baris 85: Membuat fungsi main() sebagai pusat jalannya program.

Baris 86: Membuat objek bst dari class BSTBalita.

Baris 87: Membuat variabel pilih dengan nilai awal 0.

Baris 88: Membuat perulangan while agar program terus berjalan sampai pengguna memilih menu keluar.

Baris 89-99: Menampilkan daftar menu pada sistem pendataan tinggi badan balita.

Baris 100: Memulai blok try untuk menangani kesalahan input.

Baris 101: Meminta pengguna memasukkan pilihan menu lalu mengubah input menjadi tipe integer.

Baris 102-104: Menangani kesalahan jika pengguna memasukkan selain angka lalu program kembali ke menu utama.

Baris 105: Mengecek apakah pengguna memilih menu nomor 1.

Baris 106-107: Meminta input nama balita dan tinggi badan.

Baris 108: Menambahkan data balita ke Binary Search Tree menggunakan fungsi insert().

Baris 109: Menampilkan pesan bahwa data berhasil ditambahkan.

Baris 110-111: Menampilkan pesan kesalahan jika input tidak valid.

Baris 112: Mengecek apakah pengguna memilih menu nomor 2.

Baris 113: Meminta input nama balita yang ingin dicari.

Baris 114: Menjalankan fungsi pencarian data menggunakan search().

Baris 115-116: Jika data ditemukan maka program menampilkan nama dan tinggi badan balita.

Baris 117-118: Jika data tidak ditemukan maka program menampilkan pesan gagal.

Baris 119-122: Menampilkan seluruh data balita berdasarkan urutan tinggi badan dari terendah ke tertinggi menggunakan traversal inorder.

Baris 123-126: Menampilkan data berdasarkan urutan dari data pertama ke terakhir menggunakan traversal preorder.

Baris 127-130: Menampilkan data berdasarkan urutan dari data terakhir ke pertama menggunakan traversal postorder.

Baris 131-134: Menampilkan data balita dengan tinggi badan paling rendah menggunakan fungsi find_min().

Baris 135-138: Menampilkan data balita dengan tinggi badan paling tinggi menggunakan fungsi find_max().

Baris 139-140: Menampilkan jumlah seluruh data balita menggunakan fungsi count_nodes().

Baris 141-142: Menampilkan total seluruh tinggi badan balita menggunakan fungsi sum_nodes().

Output:

output awal:

Baris 143-145: Mengecek apakah pengguna memilih menu keluar, lalu program menampilkan pesan selesai dan menghentikan perulangan.

Baris 146-147: Menampilkan pesan jika pilihan menu yang dimasukkan tidak tersedia.

Baris 149-150: Mengecek apakah file dijalankan sebagai program utama. Jika benar maka fungsi main() akan dijalankan.
