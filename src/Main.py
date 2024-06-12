from Fractional.BarangFractional import *
from Fractional.DaftarBelanjaFractional import *
from Fractional.Greedy import *
from Integer.BarangInteger import *
from Integer.DaftarBelanjaInteger import *
from Integer.BranchNBound import *
import os
import sys

def inputBarangInteger(i: int) -> BarangInteger:
    nama = input(f"Masukkan nama barang ke-{i}: ")
    lop = True
    while lop:
        try:
            harga = input(f"Masukkan harga satuan barang ke-{i}: ")
            harga = int(harga)
            if (harga % 100 != 0):
                print("Mohon masukkan angka dalam pecahan 100")
            else: lop = False
        except Exception:
            print("Mohon masukkan angka dalam pecahan 100")
    lop = True
    while lop:
        try:
            prioritas = input(f"Masukkan prioritas barang ke-{i}: ")
            prioritas = int(prioritas)
            if (prioritas < 1 or prioritas > 3):
                print("Mohon masukkan angka dari 1 sampai 3")
            else: lop = False
        except Exception:
            print("Mohon masukkan angka dari 1 sampai 3")
    return BarangInteger(nama, harga, prioritas)

def inputBarangFractional(i: int) -> BarangFractional:
    nama = input(f"Masukkan nama barang ke-{i}: ")
    lop = True
    while lop:
        try:
            harga = input(f"Masukkan harga satuan barang ke-{i}: ")
            harga = int(harga)
            if (harga % 100 != 0):
                print("Mohon masukkan angka dalam pecahan 100")
            else: lop = False
        except Exception:
            print("Mohon masukkan angka dalam pecahan 100")
    lop = True
    while lop:
        try:
            prioritas = input(f"Masukkan prioritas barang ke-{i}: ")
            prioritas = int(prioritas)
            if (prioritas < 1 or prioritas > 3):
                print("Mohon masukkan angka dari 1 sampai 3")
            else: lop = False
        except Exception:
            print("Mohon masukkan angka dari 1 sampai 3")
    lop = True
    pecahan = input("Apakah barang tersebut dapat berupa pecahan (y/n): ")
    if (pecahan == "y"): pecahan = True
    else: pecahan = False
    while lop:
        try:
            amount = input("Masukkan jumlah barang tersebut yang ingin dibeli: ")
            if (pecahan): amount = float(amount)
            else: amount = int(amount)
            if (amount < 0): print("Jumlah harus positif")
            else: lop = False
        except Exception:
            print("Masukkan jumlah yang sesuai")
    return BarangFractional(nama, harga, prioritas, amount, pecahan)


def main():
    loop = "y"
    inputSalah = True
    while (loop == "y"):
        while (inputSalah):
            budget = input("Masukkan budget maksimal: ")
            try:
                budget = int(budget)
                if (budget < 0 and budget%100 != 0):
                    print("Masukkan angka dalam pecahan 100")
                else: inputSalah = False
            except Exception:
                print("Masukkan angka dalam pecahan 100")
        inputSalah = True

        while (inputSalah):
            print("Silakan pilih jenis barang yang ingin dibeli:")
            print("1. Seluruh barang hanya dapat dibeli dalam jumlah bulat (Branch & Bound)")
            print("2. Terdapat barang yang dibeli dalam jumlah pecahan (Greedy)")
            masukkan1 = input("Pilihan: ")
            try:
                masukkan1 = int(masukkan1)
                if (masukkan1 < 1 or masukkan1 > 2):
                    print("Mohon masukkan 1 atau 2\n")
                else: inputSalah = False
            except Exception:
                print("Mohon masukkan bilangan bulat\n")
        inputSalah = True

        if (masukkan1 == 1):
            di = DaftarBelanjaInteger(budget)
            while (inputSalah):
                n = input("Masukkan banyak jenis barang: ")
                try:
                    n = int(n)
                    if (n < 0): print("Banyak jenis barang harus positif")
                    else: inputSalah = False
                except Exception:
                    print("Mohon masukkan bilangan")
            if (n < 0): n = 0
            inputSalah = True

            for i in range(n):
                b = inputBarangInteger(i+1)
                nBarang = input("Masukkan jumlah barang tersebut yang ingin dibeli: ")
                while (inputSalah):
                    try:
                        nBarang = int(nBarang)
                        if (nBarang <= 0): print("Masukkan barang lebih dari 0")
                        else: inputSalah = False
                    except Exception:
                        print("Masukkan angka")
                di.tambahBarang(b, int(nBarang))

            bnb = BranchNBound(di)
            x = bnb.process()
        else:
            df = DaftarBelanjaFractional(budget)
            while (inputSalah):
                n = input("Masukkan banyak jenis barang: ")
                try:
                    n = int(n)
                    if (n < 0): print("Banyak jenis barang harus positif")
                    else: inputSalah = False
                except Exception:
                    print("Mohon masukkan bilangan")
            if (n < 0): n = 0
            inputSalah = True

            for i in range(n):
                b = inputBarangFractional(i+1)
                df.tambahBarang(b)

            g = Greedy(df)
            x = g.process()
        
        daftarBarang = x[0]
        uangKeluar = x[1]
        print("\nBerikut saran barang yang harus Anda beli:")
        for i in range(len(daftarBarang)):
            print(f"{i+1}. {daftarBarang[i][1]} sebanyak {daftarBarang[i][0]}")
        print(f"Biaya yang diperlukan adalah {uangKeluar} rupiah\n")

        loop = input("Apakah Anda ingin melakukan perhitungan lain?(y/n) ")
        loop = loop.lower()
        inputSalah = True

if __name__ == "__main__":
    os.system('cls' if sys.platform.startswith('win') else 'clear')
    print("Selamat datang di penentuan daftar belanja!\n")
    main()