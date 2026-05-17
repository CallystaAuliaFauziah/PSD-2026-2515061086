Tugas Akhir Percobaan 4

Judul Program:
Program Antrian Reservasi Ruang Belajar Perpustakaan Menggunakan Queue Array

<p align="justify">
Program ini digunakan untuk mengatur antrian reservasi ruang belajar perpustakaan menggunakan struktur data Queue Array. Program bekerja dengan prinsip FIFO (First In First Out), yaitu mahasiswa yang pertama masuk antrian akan diproses lebih dahulu. Program menyediakan beberapa menu seperti menambahkan reservasi, menghapus reservasi, melihat antrian paling depan, menampilkan seluruh antrian, dan keluar dari program. Pada program ini digunakan konsep circular queue, sehingga ketika indeks array sudah mencapai batas akhir maka posisi akan kembali ke awal array menggunakan operator modulo %. Dengan cara ini, ruang kosong pada array dapat digunakan kembali tanpa harus memindahkan data sebelumnya.
<p/>

Source Code:

<img width="1572" height="3636" alt="code TA4 BISMILLAH FIX" src="https://github.com/user-attachments/assets/8e353be3-a139-4422-8cb7-47322d299636" />

Penjelasan Source Code:
Baris 1: Membuat class QueueReservasi sebagai class utama untuk program antrian reservasi ruang belajar.

Baris 2-6: Membuat fungsi awal init() untuk menentukan kapasitas queue, membuat list kosong untuk menyimpan data antrian, serta memberi nilai awal -1 pada front dan rear sebagai tanda queue masih kosong.

Baris 8-9: Membuat fungsi is_empty() untuk mengecek apakah queue kosong dengan memeriksa nilai front. Jika front bernilai -1 maka queue kosong.

Baris 11-12: Membuat fungsi is_full() untuk mengecek apakah queue penuh menggunakan konsep circular queue dengan operator modulo %.

Baris 14: Membuat fungsi enqueue() untuk menambahkan data baru ke dalam queue dengan parameter nama yang digunakan untuk menerima nama mahasiswa.

Baris 15-17: Mengecek apakah queue penuh. Jika penuh maka program menampilkan pesan “Antrian reservasi penuh” lalu proses dihentikan menggunakan return.

Baris 18-22: Mengecek apakah queue kosong. Jika kosong maka posisi front dan rear diisi indeks 0. Jika queue tidak kosong maka posisi rear digeser satu langkah secara melingkar menggunakan modulo %.

Baris 23-24: Menyimpan nama mahasiswa ke dalam queue lalu menampilkan pesan bahwa mahasiswa berhasil masuk antrian reservasi.

Baris 26: Membuat fungsi dequeue() untuk menghapus data paling depan pada queue.

Baris 27-29: Mengecek apakah queue kosong. Jika kosong maka program menampilkan pesan “Antrian reservasi kosong” lalu proses dihentikan menggunakan return.

Baris 30: Menampilkan nama mahasiswa yang sedang menggunakan ruang belajar berdasarkan posisi paling depan queue.

Baris 31-35: Mengecek apakah queue hanya memiliki satu data. Jika iya maka front dan rear dikembalikan menjadi -1 agar queue kosong kembali. Jika masih ada data lain maka posisi front digeser satu langkah secara melingkar menggunakan modulo %.

Baris 37: Membuat fungsi peek() untuk melihat data paling depan pada queue tanpa menghapus data tersebut.

Baris 38-41: Mengecek apakah queue kosong. Jika kosong maka program menampilkan pesan “Antrian reservasi kosong”, jika tidak maka program menampilkan data mahasiswa yang berada di posisi paling depan antrian.

Baris 43: Membuat fungsi display() untuk menampilkan seluruh isi queue.

Baris 44-46: Mengecek apakah queue kosong. Jika kosong maka program menampilkan pesan lalu proses dihentikan menggunakan return.

Baris 47: Menampilkan judul daftar antrian reservasi.

Baris 48: Membuat variabel i untuk menyimpan posisi awal pembacaan data queue dari posisi front.

Baris 49-53: Melakukan perulangan untuk menampilkan seluruh isi queue mulai dari posisi front sampai rear. Perulangan berhenti ketika indeks mencapai posisi rear. Indeks bergerak secara melingkar menggunakan modulo %.

Baris 55: Membuat fungsi utama main() sebagai pusat jalannya program.

Baris 56: Membuat objek queue bernama reservasi dari class QueueReservasi.

Baris 57: Membuat perulangan while True agar menu program terus berjalan sampai pengguna memilih keluar.

Baris 58-63: Menampilkan tampilan menu program antrian reservasi ruang belajar.

Baris 64: Memulai blok try untuk menangani kemungkinan kesalahan input.

Baris 65: Meminta pengguna memasukkan pilihan menu lalu mengubah input menjadi tipe integer menggunakan int().

Baris 66-68: Menangkap kesalahan ValueError jika pengguna memasukkan selain angka, lalu menampilkan pesan bahwa pilihan tidak valid dan program kembali ke menu utama menggunakan continue.

Baris 69: Mengecek apakah pengguna memilih menu nomor 1.

Baris 70: Meminta pengguna memasukkan nama mahasiswa.

Baris 71: Mengecek apakah input nama hanya berisi huruf menggunakan fungsi isalpha().

Baris 72: Menambahkan nama mahasiswa ke dalam queue menggunakan fungsi enqueue().

Baris 73-74: Menjalankan kondisi else jika input nama mengandung angka atau simbol, lalu menampilkan pesan kesalahan input.

Baris 75-76: Mengecek apakah pengguna memilih menu nomor 2 lalu menjalankan fungsi dequeue() untuk memproses antrian paling depan.

Baris 77-78: Mengecek apakah pengguna memilih menu nomor 3 lalu menjalankan fungsi peek() untuk melihat antrian paling depan.

Baris 79-80: Mengecek apakah pengguna memilih menu nomor 4 lalu menjalankan fungsi display() untuk menampilkan seluruh isi antrian.

Baris 81-83: Mengecek apakah pengguna memilih menu nomor 5, menampilkan pesan terima kasih, lalu menghentikan program menggunakan break.

Baris 84-85: Menjalankan kondisi jika pilihan menu tidak sesuai lalu menampilkan pesan bahwa pilihan tidak valid.

Baris 87-88: Mengecek apakah file dijalankan sebagai program utama lalu menjalankan fungsi main().

Output:


Output Awal:
<img width="452" height="187" alt="Output awal" src="https://github.com/user-attachments/assets/52345e71-061d-42df-9143-5659d7dad201" />

Output Ketika Menjalankan Menu Nomor 1:

<img width="570" height="397" alt="Output menu 1" src="https://github.com/user-attachments/assets/7d656388-4973-4c9d-b34b-e45627fdbd07" />

Output Ketika Menjalankan Menu Nomor 2:

<img width="492" height="360" alt="Output menu 2" src="https://github.com/user-attachments/assets/34691105-c83e-44a1-ba99-c139c0508dcf" />

Output Ketika Menjalankan Menu Nomor 3:

<img width="552" height="367" alt="Output menu 3" src="https://github.com/user-attachments/assets/ac0ed416-3d0e-40c1-a227-361206ef7ef3" />

Output Ketika Menjalankan Menu Nomor 4:

<img width="487" height="372" alt="Output menu 4" src="https://github.com/user-attachments/assets/e54f6f71-e898-4075-82a7-71f94e632c66" />

Output Ketika Menjalankan Menu Nomor 5:

<img width="587" height="212" alt="Output menu 5" src="https://github.com/user-attachments/assets/6fa5e854-f393-4177-be1d-34906975e922" />

Link Youtube Video Presentasi: 
