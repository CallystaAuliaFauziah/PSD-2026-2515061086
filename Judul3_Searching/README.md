Tugas Akhir Percobaan 3

Judul Program: Pencarian Tanggal Pemesanan Tiket Stadion Menggunakan Binary Search

Program ini digunakan untuk mengecek ketersediaan tiket stadion berdasarkan tanggal yang sudah diurutkan. Program menerima input berupa jumlah tanggal yang tersedia beserta daftar tanggalnya. Setelah itu, pengguna memasukkan tanggal yang ingin dicek. Data kemudian diproses menggunakan algoritma Binary Search dengan cara membandingkan data di bagian tengah dengan tanggal yang dicari. Jika tanggal yang dicari lebih besar, pencarian dilanjutkan ke bagian kanan. Jika lebih kecil, pencarian dilanjutkan ke bagian kiri. Proses ini terus dilakukan sampai tanggal ditemukan atau tidak ada lagi data yang bisa diperiksa. Hasil akhirnya menampilkan informasi apakah tiket pada tanggal tersebut tersedia atau tidak dapat dipesan.

Source Code:
<img width="1402" height="2230" alt="code judul 3" src="https://github.com/user-attachments/assets/6f1cbb4d-86aa-4eb8-bfe8-a2a4ab613e0c" />

Penjelasan Source Code:
Baris 1: Mendefinisikan fungsi binary_search untuk mencari tanggal dalam data yang sudah terurut.
Baris 2: Menginisialisasi batas kiri pencarian.
Baris 3: Menginisialisasi batas kanan pencarian.
Baris 4: Menginisialisasi posisi hasil pencarian dengan nilai -1 sebagai tanda belum ditemukan.
Baris 5: Melakukan perulangan selama batas kiri masih lebih kecil atau sama dengan batas kanan.
Baris 6: Menentukan posisi tengah dari data.
Baris 7: Menampilkan tanggal yang sedang dicek pada posisi tengah.
Baris 8-10: Mengecek apakah tanggal tengah sama dengan target, jika sama maka posisi disimpan dan pencarian dihentikan.
Baris 11-13: Jika tanggal tengah lebih kecil dari target, maka pencarian dilanjutkan ke bagian kanan.
Baris 14-16: Jika tanggal tengah lebih besar dari target, maka pencarian dilanjutkan ke bagian kiri.
Baris 17: Mengembalikan hasil posisi tanggal yang ditemukan.
Baris 20: Mendefinisikan fungsi utama program main().
Baris 21-25: Menangani input jumlah tanggal dan mengantisipasi jika input bukan angka.
Baris 26: Membuat list kosong untuk menyimpan data tanggal.
Baris 27: Menampilkan instruksi input tanggal.
Baris 28-35: Melakukan perulangan untuk memasukkan tanggal sebanyak jumlah data yang ditentukan dengan validasi input.
Baris 36: Menampilkan daftar tanggal yang tersedia.
Baris 37-42: Meminta input tanggal yang ingin dicek dengan validasi agar hanya menerima angka.
Baris 43: Memanggil fungsi binary_search untuk mencari tanggal dalam data.
Baris 44-47: Menampilkan hasil pencarian, jika ditemukan maka tiket tersedia, jika tidak maka tiket tidak tersedia.
Baris 50-51: Menjalankan fungsi utama ketika program dieksekusi langsung.

Output

Output Awal:
<img width="657" height="152" alt="Output awal" src="https://github.com/user-attachments/assets/c09798c7-8044-46b4-9e27-f33341bf63f6" />

Output Akhir:
<img width="730" height="331" alt="Output akhir" src="https://github.com/user-attachments/assets/e7cebc4d-1cd8-4904-955e-34439006d313" />

Link Youtube Video Presentasi:
