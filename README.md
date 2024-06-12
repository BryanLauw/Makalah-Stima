# Penerapan Algoritma _Greedy_ dan _Branch and Bound_ dalam Menentukan Daftar Belanja
> by Bryan Cornelius Lauwrence

## Daftar Konten
* [Informasi Umum](#informasi-umum)
* [Deskripsi Singkat](#deskripsi-singkat)
* [Kebutuhan](#kebutuhan)
* [Setup dan Penggunaan](#setup-dan-penggunaan)
* [Kreator](#kreator)

## Informasi Umum
Mengimplementasikan _knapsack problem_ pada permasalahan belanja

## Deskripsi Singkat
_Knapsack problem_ adalah permasalahan untuk mengambil barang yang memiliki bobot tertentu<br>
dengan keuntungan sebesar mungkin. Permasalahan belanja sama seperti _knapsack problem_ karena dengan<br>
anggaran tertentu, kita ingin membeli barang sebanyak-banyaknya.<br>
Algoritma yang digunakan adalah _branch and bound_ untuk daftar barang yang seluruh barangnya berupa _integer_<br>
dan _greedy by density_ untuk daftar barang yang terdapat setidaknya satu barang berupa _fractional_.<br>
Barang yang dibeli juga diberikan prioritas 1 sampai 3. Makin tinggi prioritas, makin dibutuhkan barang tersebut.

## Kebutuhan
1. `Python 3.X`

## Setup dan Penggunaan
1. Siapkan versi python yang sesuai
2. Clone repository ini dengan perintah `git clone https://github.com/BryanLauw/Makalah-Stima.git`
3. Pindah ke direktori utama dengan perintah `cd Makalah-Stima`
4. Jalankan program dengan perintah `python3 src/Main.py`
5. Ikuti instruksi program
6. Program akan memberikan hasil daftar belanja

## Kreator
| NIM | Nama |
|-----|------|
| 13522033 | Bryan Cornelius Lauwrence |