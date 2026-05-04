Tugas Akhir Percobaan 2

Judul Program: Pengurutan Skor Game Menggunakan Bubble Sort

Program Pengurutan Skor Game Menggunakan Bubble Sort digunakan untuk mengelola data skor pemain dalam sebuah game agar tersusun rapi dalam bentuk leaderboard. Program ini menerima input berupa jumlah pemain dan skor masing-masing pemain. Data skor yang awalnya tidak berurutan kemudian diproses menggynakan algoritma Bubble Sort, yaitu dengan cara membandingkan dua elemen yang berdekatan dan menukarnya jika urutannya tidak sesuai. Proses ini dilakukan berulang hingga seluruh data tersusun dengan benar. Pada programini, pengurutan dilakukan secara descending, sehingga skor tertinggi berada di posisi teratas. Hasil akhirnya ditampilkan dalam bentuk peringkat pemain, mulai dari skor tertinggi hingga terendah, sehingga memudahkan dalam mengetahui pemain dengan skor terbaik.

Source Code:
<img width="1248" height="1926" alt="coding judul 2 sd" src="https://github.com/user-attachments/assets/22221811-17a5-4fdb-afd3-b9fbab1ef383" />

Penjelasan Source Code:
Baris 1: Mendefinisikan fungsi untuk menukar dua elemen dalam array
Baris 2: Menyimpan nilai elemen ke-i ke variabel sementara
Baris 3: Mengisi posisi ke-i dengan nilai dari posisi ke-j
Baris 4: Mengisi posisi ke-j dengan nilai yang tadi disimpan
Baris 6: Fungsi untuk mengurutkan array menggunakan Bubble Sort
Baris 7: Perulangan luar untuk menentukan jumlah tahap pengurutan
Baris 8: Penanda apakah terjadi pertukaran dalam satu putaran
Baris 9: Perulangan dalam untuk membandingkan elemen bersebelahan
Baris 10: Membandingkan dua elemen
Baris 11: Menukar posisi jika urutan salah
Baris 12: Menandai bahwa terjadi pertukaran
Baris 13-14: Menghentikan loop jika jika sudah tidak ada pertukaran atau berarti data sudah terurut
Baris 16: Fungsi utama program
Baris 17-18: Fungsi utama program
Baris 19-21: Menangani jika input bukan angka
Baris 22: Membuat list kosong untuk menyimpan skor
Baris 23: Menampilkan instruksi input
Baris 24: Perulangan untuk input sebanyak jumlah pemain
Baris 25: Loop agar input valid
Baris 26-27: Memasukkan skor pemain
Baris 28: Menambahkan skor ke dalam list
Baris 29: Keluar dari loop jika input valid
Baris 30-31: Menangani input salah
Baris 33: Menampilkan data sebelum diurutkan
Baris 35: Memanggil fungsi untuk mengurutkan skor
Baris 37: Menampilkan judul hasil
Baris 38: Loop untuk menampilkan hasil
Baris 39: Menampilkan skor berdasarkan peringkat
Baris 42-43: Menjalankan fungsi main() saat program dijalankan langsung

Output:
Output awal
<img width="355" height="132" alt="Screenshot 2026-05-05 005411" src="https://github.com/user-attachments/assets/6fb72d2f-99e8-4ec1-8973-4243a317fbeb" />

Output akhir
<img width="675" height="257" alt="Screenshot 2026-05-05 005455" src="https://github.com/user-attachments/assets/63b51010-6689-4bb9-870b-b4698d7be006" />

Link youtube presentasi:
