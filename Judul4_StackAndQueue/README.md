Tugas Akhir Percobaan 4

Judul Program:
Program Antrian Reservasi Ruang Belajar Perpustakaan Menggunakan Queue Array

Program ini digunakan untuk mengatur antrian reservasi ruang belajar perpustakaan menggunakan struktur data Queue Array. Program bekerja dengan prinsip FIFO (First In First Out), yaitu mahasiswa yang pertama masuk antrian akan diproses lebih dahulu. Program menyediakan beberapa menu seperti menambahkan reservasi, menghapus reservasi, melihat antrian paling depan, menampilkan seluruh antrian, dan keluar dari program. Pada program ini digunakan konsep circular queue, sehingga ketika indeks array sudah mencapai batas akhir maka posisi akan kembali ke awal array menggunakan operator modulo %. Dengan cara ini, ruang kosong pada array dapat digunakan kembali tanpa harus memindahkan data sebelumnya.

Source Code:
<img width="1572" height="3332" alt="code TA SD 4 FIX BANGET HARUSNYA" src="https://github.com/user-attachments/assets/9b0592f5-abe9-4caa-a3d9-32ed6b40fb10" />

Penjelasan Source Code:
Baris 1: Membuat class QueueReservasi sebagai class utama untuk program antrian reservasi.
Baris 2-6: Membuat bagian awal program untuk menentukan kapasitas queue, membuat list kosong untuk menyimpan data, serta memberi nilai awal -1 pada front dan rear sebagai tanda queue masih kosong.
Baris 7-8: Membuat method is_empty() untuk mengecek apakah queue kosong dengan memeriksa nilai front.
Baris 9-10: Membuat method is_full() untuk mengecek apakah queue penuh menggunakan konsep circular queue dengan operator modulo %.
Baris 11: Membuat method enqueue() untuk menambahkan data ke dalam queue.
Baris 12-14: Mengecek apakah queue penuh. Jika penuh maka program menampilkan pesan dan proses penambahan data dihentikan.
Baris 15-19: Mengecek apakah queue kosong. Jika kosong maka front dan rear diisi indeks pertama, jika tidak maka posisi rear digeser satu langkah secara melingkar.
Baris 20-21: Menyimpan nama mahasiswa ke queue lalu menampilkan pesan bahwa reservasi berhasil ditambahkan.
Baris 22: Membuat method dequeue() untuk menghapus data paling depan pada queue.
Baris 23-25: Mengecek apakah queue kosong. Jika kosong maka program menampilkan pesan dan proses dihentikan.
Baris 26: Menampilkan nama mahasiswa yang selesai menggunakan ruang belajar.
Baris 27-31: Mengecek apakah queue hanya memiliki satu data. Jika iya maka queue dikosongkan kembali, jika tidak maka posisi front digeser satu langkah secara melingkar.
Baris 32: Membuat method peek() untuk melihat data paling depan pada queue.
Baris 33-36: Mengecek apakah queue kosong. Jika kosong maka program menampilkan pesan, jika tidak maka data paling depan ditampilkan.
Baris 37: Membuat method display() untuk menampilkan seluruh isi queue.
Baris 38-40: Mengecek apakah queue kosong. Jika kosong maka program menampilkan pesan dan proses dihentikan.
Baris 41-47: Menampilkan seluruh data queue menggunakan perulangan mulai dari posisi front sampai rear. Indeks bergerak secara melingkar menggunakan modulo %.
Baris 48: Membuat fungsi utama main().
Baris 49-50: Membuat objek queue bernama reservasi dan menjalankan perulangan menu program.
Baris 51-56: Menampilkan menu program antrian reservasi ruang belajar.
Baris 57-61: Menggunakan try-except untuk menerima input pilihan menu dan menangani kesalahan jika pengguna memasukkan selain angka.
Baris 62: Mengecek apakah pengguna memilih menu nomor 1.
Baris 63-67: Meminta input nama mahasiswa lalu menambahkan data ke queue menggunakan method enqueue().
Baris 68-69: Mengecek pilihan menu nomor 2 lalu memproses antrian menggunakan method dequeue().
Baris 70-71: Mengecek pilihan menu nomor 3 lalu menampilkan antrian paling depan menggunakan method peek().
Baris 72-73: Mengecek pilihan menu nomor 4 lalu menampilkan seluruh isi antrian menggunakan method display().
Baris 74-76: Mengecek pilihan menu nomor 5, menampilkan pesan selesai, lalu menghentikan program.
Baris 77-78: Menampilkan pesan jika pilihan menu yang dimasukkan tidak sesuai.
Baris 79-80: Menjalankan fungsi main() saat program dijalankan.

Output:

Output Awal:


Output Ketika Menjalankan Menu Nomor 1:


Output Ketika Menjalankan Menu Nomor 2:


Output Ketika Menjalankan Menu Nomor 3:


Output Ketika Menjalankan Menu Nomor 4:


Output Ketika Menjalankan Menu Nomor 5:


Link Youtube Video Presentasi: 
