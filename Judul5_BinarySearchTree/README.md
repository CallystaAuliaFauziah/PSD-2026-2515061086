Tugas Akhir Percobaan 5

Judul Program:

Sistem Pendataan Tinggi Badan Balita Menggunakan Binary Search Tree

<p style="text-align: justify;">
Sistem ini dibuat untuk menyimpan dan mengelola data tinggi badan balita. Data yang dimasukkan berupa nama balita dan tinggi badannya. Pengelolaan data menggunakan struktur Binary Search Tree (BST), di mana data dengan nilai lebih kecil akan ditempatkan di sisi kiri, sedangkan data dengan nilai lebih besar ditempatkan di sisi kanan. Sistem ini memiliki beberapa fitur, yaitu menambahkan data balita, mencari data berdasarkan nama, menampilkan data berdasarkan urutan tinggi dari terendah ke tertinggi, serta menampilkan data berdasarkan urutan proses awal sampai akhir dan dari akhir ke awal. Selain itu, sistem juga dapat menampilkan balita dengan tinggi badan terendah dan tertinggi, serta menghitung jumlah data yang sudah dimasukkan. Penggunaan Binary Search Tree membuat data menjadi lebih teratur dan proses pengolahan seperti pencarian dan penampilan data dapat dilakukan dengan lebih mudah tanpa perlu pengurutan manual.
</p>

Source Code:

<img width="1632" height="5992" alt="code TAPSD JUDUL 5" src="https://github.com/user-attachments/assets/93be0b6c-3e89-4013-9ed5-a487010e1c82" />

Penjelasan Source Code:

Baris 1: Membuat class Node yang digunakan untuk menyimpan data pada setiap node di Binary Search Tree.

Baris 2: Membuat fungsi init() yang akan dijalankan saat object node dibuat.

Baris 3: Menyimpan data tinggi badan balita ke dalam atribut tinggi.

Baris 4: Menyimpan data nama balita ke dalam atribut nama.

Baris 5: Memberikan nilai awal None pada node kiri.

Baris 6: Memberikan nilai awal None pada node kanan.

Baris 8: Membuat class BSTBalita sebagai class utama Binary Search Tree.

Baris 9: Membuat fungsi init() pada class BSTBalita.

Baris 10: Memberikan nilai awal None pada root yang menandakan bahwa tree masih kosong.

Baris 12: Membuat fungsi insert_node() untuk menambahkan data baru ke dalam Binary Search Tree.

Baris 13: Mengecek apakah root kosong.

Baris 14: Jika root kosong maka program membuat node baru berisi data tinggi badan dan nama balita.

Baris 15: Mengecek apakah tinggi badan lebih kecil dari root.

Baris 16: Jika lebih kecil maka data dimasukkan ke subtree kiri menggunakan rekursif.

Baris 17: Mengecek apakah tinggi badan lebih besar dari root.

Baris 18: Jika lebih besar maka data dimasukkan ke subtree kanan menggunakan rekursif.

Baris 19: Mengembalikan root setelah proses penambahan data selesai.

Baris 21: Membuat fungsi insert().

Baris 22: Menjalankan fungsi insert_node() untuk menambahkan data ke BST.

Baris 24: Membuat fungsi search_nama() untuk mencari data berdasarkan nama balita.

Baris 25: Mengecek apakah root kosong.

Baris 26: Jika kosong maka fungsi mengembalikan None.

Baris 27: Membandingkan nama input dengan nama pada node menggunakan lower() agar huruf besar dan kecil dianggap sama.

Baris 28: Jika nama ditemukan maka node dikembalikan.

Baris 29: Melakukan pencarian pada subtree kiri dan hasilnya disimpan ke variabel kiri.

Baris 30: Mengecek apakah data ditemukan di subtree kiri.

Baris 31: Jika ditemukan maka hasil langsung dikembalikan.

Baris 32: Jika belum ditemukan maka pencarian dilanjutkan ke subtree kanan.

Baris 34: Membuat fungsi search().

Baris 35: Menjalankan fungsi search_nama() mulai dari root utama.

Baris 37: Membuat fungsi inorder() untuk menampilkan data berdasarkan urutan tinggi badan dari terendah ke tertinggi.

Baris 38: Mengecek apakah root kosong.

Baris 39: Jika kosong maka fungsi dihentikan menggunakan return.

Baris 40: Menelusuri subtree kiri terlebih dahulu.

Baris 41: Menampilkan nama balita dan tinggi badannya.

Baris 42: Menelusuri subtree kanan.

Baris 44: Membuat fungsi preorder().

Baris 45: Mengecek apakah root kosong.

Baris 46: Jika kosong maka fungsi dihentikan.

Baris 47: Menampilkan data pada root terlebih dahulu.

Baris 48: Menelusuri subtree kiri.

Baris 49: Menelusuri subtree kanan.

Baris 51: Membuat fungsi postorder().

Baris 52: Mengecek apakah root kosong.

Baris 53: Jika kosong maka fungsi dihentikan.

Baris 54: Menelusuri subtree kiri.

Baris 55: Menelusuri subtree kanan.

Baris 56: Menampilkan data root paling akhir.

Baris 58: Membuat fungsi find_min() untuk mencari tinggi badan paling rendah.

Baris 59: Mengecek apakah tree kosong.

Baris 60: Jika kosong maka fungsi mengembalikan None.

Baris 61: Membuat variabel current untuk menyimpan posisi node saat ini.

Baris 62: Membuat perulangan selama node kiri masih ada.

Baris 63: Menggeser posisi current ke node kiri.

Baris 64: Mengembalikan node dengan nilai paling kecil.

Baris 66: Membuat fungsi find_max() untuk mencari tinggi badan paling tinggi.

Baris 67: Mengecek apakah tree kosong.

Baris 68: Jika kosong maka fungsi mengembalikan None.

Baris 69: Membuat variabel current untuk menyimpan posisi node saat ini.

Baris 70: Membuat perulangan selama node kanan masih ada.

Baris 71: Menggeser posisi current ke node kanan.

Baris 72: Mengembalikan node dengan nilai paling besar.

Baris 74: Membuat fungsi count_nodes() untuk menghitung jumlah seluruh data balita.

Baris 75: Mengecek apakah root kosong.

Baris 76: Jika kosong maka fungsi mengembalikan nilai 0.

Baris 77: Menghitung jumlah node pada subtree kiri dan kanan lalu ditambah 1 untuk root.

Baris 79: Membuat fungsi sum_nodes() untuk menghitung total seluruh tinggi badan balita.

Baris 80: Mengecek apakah root kosong.

Baris 81: Jika kosong maka fungsi mengembalikan nilai 0.

Baris 82: Menjumlahkan seluruh tinggi badan pada subtree kiri, subtree kanan, dan root.

Baris 84: Membuat fungsi main() sebagai program utama.

Baris 85: Membuat object bst dari class BSTBalita.

Baris 86: Membuat variabel pilih dengan nilai awal 0.

Baris 87: Membuat perulangan while agar program terus berjalan sampai pengguna memilih menu keluar.

Baris 88: Menampilkan judul sistem.

Baris 89: Menampilkan menu tambah data balita.

Baris 90: Menampilkan menu cari data balita berdasarkan nama.

Baris 91: Menampilkan menu data berdasarkan urutan tinggi badan.

Baris 92: Menampilkan menu data dari pertama ke terakhir.

Baris 93: Menampilkan menu data dari terakhir ke pertama.

Baris 94: Menampilkan menu balita terpendek.

Baris 95: Menampilkan menu balita tertinggi.

Baris 96: Menampilkan menu jumlah data balita.

Baris 97: Menampilkan menu total tinggi seluruh balita.

Baris 98: Menampilkan menu keluar dari sistem.

Baris 99: Memulai blok try untuk menangani kesalahan input.

Baris 100: Meminta pengguna memasukkan pilihan menu.

Baris 101-103: Menangani kesalahan jika input bukan angka lalu program kembali ke menu utama.

Baris 104: Mengecek apakah pengguna memilih menu nomor 1.

Baris 105: Memulai blok try untuk menangani kesalahan input data.

Baris 106: Meminta input nama balita.

Baris 107: Meminta input tinggi badan balita.

Baris 108: Menambahkan data balita ke dalam BST menggunakan fungsi insert().

Baris 109: Menampilkan pesan bahwa data berhasil ditambahkan.

Baris 110-111: Menampilkan pesan kesalahan jika input tidak valid.

Baris 112: Mengecek apakah pengguna memilih menu nomor 2.

Baris 113: Meminta input nama balita yang ingin dicari.

Baris 114: Menjalankan fungsi search() untuk mencari data balita.

Baris 115: Mengecek apakah data ditemukan.

Baris 116: Jika data ditemukan maka program menampilkan nama dan tinggi badan balita.

Baris 117-118: Jika data tidak ditemukan maka program menampilkan pesan bahwa data tidak ditemukan.

Baris 119: Mengecek apakah pengguna memilih menu nomor 3.

Baris 120: Menampilkan judul data berdasarkan urutan tinggi badan.

Baris 121: Menjalankan fungsi inorder().

Baris 122: Membuat baris baru menggunakan print().

Baris 123: Mengecek apakah pengguna memilih menu nomor 4.

Baris 124: Menampilkan judul data dari pertama ke terakhir.

Baris 125: Menjalankan fungsi preorder().

Baris 126: Membuat baris baru menggunakan print().

Baris 127: Mengecek apakah pengguna memilih menu nomor 5.

Baris 128: Menampilkan judul data dari terakhir ke pertama.

Baris 129: Menjalankan fungsi postorder().

Baris 130: Membuat baris baru menggunakan print().

Baris 131: Mengecek apakah pengguna memilih menu nomor 6.

Baris 132: Menjalankan fungsi find_min() lalu menyimpan hasilnya ke variabel min_node.

Baris 133: Mengecek apakah data minimum ditemukan.

Baris 134: Menampilkan data balita dengan tinggi badan paling rendah.

Baris 135: Mengecek apakah pengguna memilih menu nomor 7.

Baris 136: Menjalankan fungsi find_max() lalu menyimpan hasilnya ke variabel max_node.

Baris 137: Mengecek apakah data maksimum ditemukan.

Baris 138: Menampilkan data balita dengan tinggi badan paling tinggi.

Baris 139: Mengecek apakah pengguna memilih menu nomor 8.

Baris 140: Menampilkan jumlah seluruh data balita menggunakan fungsi count_nodes().

Baris 141: Mengecek apakah pengguna memilih menu nomor 9.

Baris 142: Menampilkan total seluruh tinggi badan balita menggunakan fungsi sum_nodes().

Baris 143: Mengecek apakah pengguna memilih menu nomor 10.

Baris 144: Menampilkan pesan bahwa program selesai dijalankan.

Baris 145: Menghentikan perulangan menggunakan break.

Baris 146: Menjalankan kondisi jika pilihan menu tidak tersedia.

Baris 147: Menampilkan pesan bahwa pilihan tidak valid.

Baris 149: Mengecek apakah file dijalankan sebagai program utama.

Baris 150: Menjalankan fungsi main().

Output:

Output Awal:

<img width="640" height="296" alt="Screenshot 2026-05-26 142512" src="https://github.com/user-attachments/assets/c2a58231-2804-4d0a-b0e8-989fad7d6edd" />

Output Setelah Menu 1 Dijalankan:

<img width="655" height="621" alt="Screenshot 2026-05-26 143721" src="https://github.com/user-attachments/assets/b322af0f-91e9-4ab9-b9ec-d8d7e12973f7" />

Output Setelah Menu 2 Dijalankan:

<img width="647" height="589" alt="Screenshot 2026-05-26 143529" src="https://github.com/user-attachments/assets/799d7240-82ee-4af8-9d79-eb5a870df0f8" />

Output Setelah Menu 3 Dijalankan:

<img width="713" height="590" alt="Screenshot 2026-05-26 142915" src="https://github.com/user-attachments/assets/801670d1-334a-4b46-95cd-32b296fa0798" />

Output Setelah Menu 4 Dijalankan:
<img width="706" height="596" alt="Screenshot 2026-05-26 142932" src="https://github.com/user-attachments/assets/6909f252-8650-4e84-9b4f-4d4c293d876b" />

Output Setelah Menu 5 Dijalankan:

<img width="624" height="591" alt="Screenshot 2026-05-26 142948" src="https://github.com/user-attachments/assets/3d971808-deab-426b-a3da-038a6ca13533" />

Output Setelah Menu 6 Dijalankan:

<img width="684" height="566" alt="Screenshot 2026-05-26 143020" src="https://github.com/user-attachments/assets/34940580-97b5-43a8-9aac-98bdca712506" />

Output Setelah Menu 7 Dijalankan:

<img width="674" height="574" alt="Screenshot 2026-05-26 143034" src="https://github.com/user-attachments/assets/53cc7453-bd34-4580-8ee0-3e9aa25df00f" />

Output Setelah Menu 8 Dijalankan:

<img width="651" height="572" alt="Screenshot 2026-05-26 143050" src="https://github.com/user-attachments/assets/b6fa9f85-2b6c-422f-8dd9-ccf16539b674" />

Output Setelah Menu 9 Dijalankan:

<img width="683" height="567" alt="Screenshot 2026-05-26 143107" src="https://github.com/user-attachments/assets/0eccf680-9b9c-467f-ab41-748736a11c7c" />

Output Setelah Menu 10  Dijalankan:

<img width="631" height="295" alt="Screenshot 2026-05-26 143836" src="https://github.com/user-attachments/assets/1a184adc-7319-4837-a878-b23236dc4752" />

Link Youtube Video Presentasi:
