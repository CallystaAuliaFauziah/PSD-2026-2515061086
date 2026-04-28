Tugas Akhir Percobaan 1

Judul Program: Keranjang Belanja

Program ini berfungsi sebagai sistem keranjang belanja sederhana yang memungkinkan pengguna melihat daftar produk, menambahkan barang ke keranjang, menghapus barang dari keranjang, serta melihat riwayat pilihan. Data keranjang disimpan menggunakan struktur Linked List sehingga setiap penambahan dan penghapusan dapat dikelola secara dinamis. Program juga dilengkapi menu interaktif yang memudahkan pengguna dalam menjalankan setiap fitur hingga keluar dari program.

<img width="791" height="826" alt="Screenshot 2026-04-28 183223" src="https://github.com/user-attachments/assets/46fae275-131d-494d-9503-f17ff80ecbca" />
Berdasarkan gambar tersebut, Pada baris 1 program mendefinisikan variabel produk yang berisi beberapa nama barang seperti MacBook, iPad, iPhone, dan Apple Watch. 
Pada baris 2 terdapat variabel harga yang berisi nilai harga dari masing-masing produk. 
Pada baris 4 sampai baris 8 dibuat class Node yang berfungsi sebagai elemen dasar dalam struktur Linked List. 
Pada baris 10 sampai baris 12 dibuat class LinkedList yang digunakan untuk mengelola kumpulan node. 
Pada baris 14 sampai baris 22 terdapat fungsi insert yang digunakan untuk menambahkan data ke dalam Linked List. 
Pada baris 24 sampai baris 26 terdapat fungsi delete yang digunakan untuk menghapus node pertama. 
Pada baris 28 sampai baris 32 terdapat fungsi display yang berfungsi untuk menampilkan seluruh isi Linked List. 
Pada baris 34 terdapat variabel riwayat yang berupa list kosong. Variabel ini disiapkan untuk menyimpan data tambahan seperti Riwayat.

<img width="856" height="880" alt="Screenshot 2026-04-28 183336" src="https://github.com/user-attachments/assets/7bcfc832-e70a-4f56-bc12-b18ec94b64cb" />
Berdasarkan gambar tersebut, Pada baris 36 sampai baris 43 terdapat fungsi menu() yang digunakan untuk menampilkan daftar pilihan kepada pengguna. 
Pada baris 45 terdapat pembuatan objek keranjang = LinkedList(). 
Pada baris 46 terdapat perulangan while True: yang berarti program akan terus berjalan tanpa batas sampai ada perintah untuk berhenti. 
Pada baris 48 pengguna diminta memasukkan pilihan melalui input yang disimpan ke variabel pilih.
Pada baris 50 sampai baris 55 merupakan kondisi if pilih == "1" yang dijalankan jika pengguna memilih menu pertama. 
Pada baris 57 sampai baris 66 merupakan kondisi elif pilih == "2" untuk menambahkan barang ke keranjang. 
Pada baris 68 sampai baris 72 merupakan kondisi elif pilih == "3" untuk menghapus barang dari keranjang. 

<img width="728" height="330" alt="Screenshot 2026-04-28 183454" src="https://github.com/user-attachments/assets/15a560ee-e43d-4d36-8003-388a2ec010ea" />
Berdasarkan gambar tersebut, Pada baris 73 sampai baris 75 merupakan kondisi elif pilih == "4" yang dijalankan ketika pengguna memilih menu untuk menampilkan isi keranjang. 
Pada baris 77 sampai baris 78 merupakan kondisi elif pilih == "5" yang digunakan untuk menampilkan riwayat. 
Pada baris 80 sampai baris 82 merupakan kondisi elif pilih == "6" yang berfungsi untuk mengakhiri program. 
Pada baris 84 sampai baris 85 terdapat kondisi else yang akan dijalankan jika input pengguna tidak sesuai dengan pilihan menu yang tersedia. 

Output:
<img width="382" height="184" alt="Screenshot 2026-04-28 224544" src="https://github.com/user-attachments/assets/4d80d94a-ca23-415e-87ff-bcb6edd77306" />

Link video: https://youtu.be/veumu736q2Y
