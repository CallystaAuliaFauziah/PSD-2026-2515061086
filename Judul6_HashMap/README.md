Tugas Akhir Percobaan 6

Judul Program:

Sistem Inventaris Barang Laboratorium Menggunakan Hash Map dengan Separate Chaining

<p align="justify">
Sistem ini dibuat untuk mengelola data inventaris barang laboratorium menggunakan struktur data Hash Map dengan metode Separate Chaining. Setiap barang memiliki kode barang sebagai key dan nama barang sebagai value. Metode hashing digunakan untuk menentukan lokasi penyimpanan data pada hash table sehingga proses pencarian data dapat dilakukan dengan cepat. Apabila terjadi collision atau dua kode barang menghasilkan indeks yang sama, data akan disimpan dalam linked list pada bucket yang sama menggunakan metode Separate Chaining. Sistem memiliki fitur menambah barang, mencari barang berdasarkan kode barang, menghapus barang, serta menampilkan seluruh data inventaris yang tersimpan pada hash table. Selain itu, sistem dilengkapi dengan penanganan kesalahan input menggunakan try-except sehingga pengguna dapat menginputkan ulang data apabila terjadi kesalahan.
</p>

Source Code:

<img width="1832" height="4738" alt="code TA PSD LASTTTTT" src="https://github.com/user-attachments/assets/c070e60c-db51-42ee-aa3a-c11b90d43ee3" />

Penjelasan Source Code:

Baris 1: Membuat class Node yang digunakan untuk menyimpan data pada setiap node linked list.

Baris 2: Membuat fungsi init() yang akan dijalankan saat objek node dibuat.

Baris 3: Menyimpan kode barang ke dalam atribut kode_barang.

Baris 4: Menyimpan nama barang ke dalam atribut nama_barang.

Baris 5: Memberikan nilai awal None pada atribut next.

Baris 7: Membuat class InventarisLaboratorium.

Baris 8: Membuat fungsi init() pada class InventarisLaboratorium.

Baris 9: Menyimpan ukuran hash table ke dalam atribut SIZE.

Baris 10: Membuat hash table berupa list yang berisi nilai None sebanyak ukuran yang ditentukan.

Baris 12: Membuat fungsi hash_function().

Baris 13: Menghasilkan indeks penyimpanan menggunakan operasi modulo.

Baris 15: Membuat fungsi tambah_barang().

Baris 16: Menentukan indeks penyimpanan berdasarkan hasil fungsi hash.

Baris 17: Membuat variabel current yang menunjuk node pertama pada bucket.

Baris 18: Membuat perulangan untuk menelusuri linked list.

Baris 19: Mengecek apakah kode barang sudah ada.

Baris 20: Memperbarui nama barang jika kode barang ditemukan.

Baris 21: Menampilkan pesan bahwa data berhasil diperbarui.

Baris 22: Menghentikan fungsi menggunakan return.

Baris 23: Berpindah ke node berikutnya.

Baris 24: Membuat node baru.

Baris 25: Menghubungkan node baru dengan node pertama pada bucket.

Baris 26: Menjadikan node baru sebagai node pertama pada bucket.

Baris 27: Menampilkan pesan bahwa barang berhasil ditambahkan.

Baris 29: Membuat fungsi cari_barang().

Baris 30: Menentukan indeks berdasarkan hasil fungsi hash.

Baris 31: Membuat variabel current yang menunjuk node pertama pada bucket.

Baris 32: Membuat perulangan untuk menelusuri linked list.

Baris 33: Mengecek apakah kode barang yang dicari ditemukan.

Baris 34: Mengembalikan node yang ditemukan.

Baris 35: Berpindah ke node berikutnya.

Baris 36: Mengembalikan nilai None jika data tidak ditemukan.

Baris 38: Membuat fungsi hapus_barang().

Baris 39: Menentukan indeks berdasarkan hasil fungsi hash.

Baris 40: Membuat variabel current yang menunjuk node pertama pada bucket.

Baris 41: Membuat variabel prev untuk menyimpan node sebelumnya.

Baris 42: Membuat perulangan untuk menelusuri linked list.

Baris 43: Mengecek apakah kode barang yang akan dihapus ditemukan.

Baris 44: Mengecek apakah node yang dihapus berada pada posisi pertama.

Baris 45: Mengarahkan bucket ke node berikutnya jika node pertama dihapus.

Baris 46: Menjalankan kondisi jika node yang dihapus bukan node pertama.

Baris 47: Menghubungkan node sebelumnya dengan node setelah node yang dihapus.

Baris 48: Menampilkan pesan bahwa barang berhasil dihapus.

Baris 49: Mengembalikan nilai True.

Baris 50: Memindahkan posisi prev ke node saat ini.

Baris 51: Memindahkan posisi current ke node berikutnya.

Baris 52: Menampilkan pesan bahwa barang tidak ditemukan.

Baris 53: Mengembalikan nilai False.

Baris 55: Membuat fungsi tampilkan_inventaris().

Baris 56: Menampilkan judul sistem inventaris barang laboratorium.

Baris 57: Membuat perulangan untuk menelusuri seluruh bucket.

Baris 58: Menampilkan nomor bucket.

Baris 59: Membuat variabel current yang menunjuk node pertama pada bucket.

Baris 60: Membuat perulangan untuk menampilkan seluruh node.

Baris 61: Menjalankan fungsi print().

Baris 62: Menampilkan kode barang dan nama barang.

Baris 63: Menentukan agar output tetap berada pada baris yang sama.

Baris 64: Menutup fungsi print().

Baris 65: Berpindah ke node berikutnya.

Baris 66: Menampilkan tulisan NULL.

Baris 68: Membuat fungsi deteksi_error().

Baris 69: Membuat perulangan agar pengguna dapat menginput ulang jika terjadi kesalahan.

Baris 70: Memulai blok try.

Baris 71: Meminta input dari pengguna dan mengubahnya menjadi integer.

Baris 72: Menangkap kesalahan ValueError.

Baris 73: Menampilkan pesan bahwa input tidak valid.

Baris 75: Membuat fungsi main().

Baris 76: Membuat objek inventaris dari class InventarisLaboratorium.

Baris 78: Membuat perulangan agar program terus berjalan.

Baris 79: Menampilkan judul sistem.

Baris 80: Menampilkan menu tambah barang.

Baris 81: Menampilkan menu cari barang.

Baris 82: Menampilkan menu hapus barang.

Baris 83: Menampilkan menu tampilkan barang inventaris.

Baris 84: Menampilkan menu keluar.

Baris 85: Meminta pengguna memasukkan pilihan menu.

Baris 87: Mengecek apakah pengguna memilih menu nomor 1.

Baris 88: Memanggil fungsi deteksi_error() untuk meminta kode barang.

Baris 89: Meminta input nama barang.

Baris 90: Menjalankan fungsi tambah_barang().

Baris 92: Mengecek apakah pengguna memilih menu nomor 2.

Baris 93: Memanggil fungsi deteksi_error() untuk meminta kode barang yang dicari.

Baris 94: Menjalankan fungsi cari_barang().

Baris 95: Mengecek apakah data ditemukan.

Baris 96: Menampilkan informasi bahwa data ditemukan.

Baris 97: Menampilkan kode barang.

Baris 98: Menampilkan nama barang.

Baris 99: Menjalankan kondisi jika data tidak ditemukan.

Baris 100: Menampilkan pesan bahwa barang tidak ditemukan.

Baris 102: Mengecek apakah pengguna memilih menu nomor 3.

Baris 103: Memanggil fungsi deteksi_error() untuk meminta kode barang yang akan dihapus.

Baris 104: Menjalankan fungsi hapus_barang().

Baris 106: Mengecek apakah pengguna memilih menu nomor 4.

Baris 107: Menjalankan fungsi tampilkan_inventaris().

Baris 109: Mengecek apakah pengguna memilih menu nomor 5.

Baris 110: Menampilkan pesan terima kasih.

Baris 111: Menghentikan perulangan menggunakan break.

Baris 113: Menjalankan kondisi jika pilihan menu tidak tersedia.

Baris 114: Menampilkan pesan bahwa pilihan tidak valid.

Baris 116: Mengecek apakah file dijalankan sebagai program utama.

Baris 117: Menjalankan fungsi main().

Output:

Output Awal:

<img width="438" height="172" alt="Screenshot 2026-06-07 214618" src="https://github.com/user-attachments/assets/dcd8540b-c3ce-44d2-93cc-b96b15349dcc" />

Output Ketika Menu 1 Dijalankan:

<img width="532" height="258" alt="Screenshot 2026-06-07 214701" src="https://github.com/user-attachments/assets/53e48de9-ac2b-49a9-b122-ae0589826d7c" />

Output Ketika Menu 2 Dijalankan:

<img width="431" height="267" alt="Screenshot 2026-06-07 214733" src="https://github.com/user-attachments/assets/cd47b703-d04f-4a83-847c-3e38b2066fe3" />

Output Ketika Menu 3 Dijalankan:

<img width="432" height="223" alt="Screenshot 2026-06-07 214802" src="https://github.com/user-attachments/assets/875ea40e-5963-4f48-ae73-f355b4c7c05b" />

Output Ketika Menu 4 Dijalankan:

<img width="427" height="425" alt="Screenshot 2026-06-07 214844" src="https://github.com/user-attachments/assets/f7be4f7b-de32-46f9-ba25-6f7aac89d3a7" />

Output Ketika Menu 5 Dijalankan:

<img width="638" height="177" alt="Screenshot 2026-06-07 214903" src="https://github.com/user-attachments/assets/cbea2901-c296-488d-b259-934bd9246e2d" />

Link Youtube Video Presentasi:

https://youtu.be/C4aQxmjB9GQ
