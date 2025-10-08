# postest kemaren
import os
from time import sleep

username = "setri" 
password = "039"

login_berhasil = False

for i in range(0,5):
    print("============================================================")
    print("                    SISTEM RENTAL MOBIL                     ")
    print("============================================================")

    nama = input("Masukkan username: ")
    pw = input("Masukkan password: ")

    if nama == username and pw == password:
        print("Login berhasil!\n")
        login_berhasil = True
        break
    else:
        print(f"Username atau password salah!")
else:
        print("Terlalu banyak percobaan gagal. Program berhenti.")

if login_berhasil:
  for i in range(10):
    print("============================================================")
    print("                    SISTEM RENTAL MOBIL                     ")
    print("============================================================")
    print("1. Input Data Customer & Keputusan Rental")
    print("2. Keluar dari Program")
    print("============================================================")

    pilihan = input("Pilih menu (1/2): ")

    if pilihan == "1":
        print("============================================================")
        print("                 INPUT DATA CUSTOMER                        ")
        print("============================================================")

        usia = int(input("Masukkan usia customer: "))
        punya_sim = input("Apakah memiliki SIM A? (ya/tidak): ").lower()
        deposit = int(input("Masukkan jumlah deposit (Rp): "))
        pengalaman = int(input("Masukkan pengalaman mengemudi (tahun): "))

        if usia < 21:
            hasil = "Tolak: Usia tidak mencukupi"
        elif punya_sim != "ya":
            hasil = "Tolak: Tidak memiliki SIM A"
        elif deposit < 500000:
            hasil = "Tolak: Deposit tidak cukup"
        elif pengalaman < 4:
            hasil = "Setujui untuk mobil standar saja"
        else:
            hasil = "Setujui untuk semua jenis mobil"

        print(f"{'============================================================'}")
        print(f"{'-------------------RINGKASAN DATA CUSTOMER------------------'}")
        print(f"{'============================================================'}")
        print(f"      {'Kolom'}       |       {'Nilai'}      ")
        print(f"{'------------------------------------------------------------'}")
        print(f"{'Usia'}              |          {usia} tahun")
        print(f"{'SIM A'}             |          {'Ada' if punya_sim == 'ya' else 'Tidak ada'}")
        print(f"{'Deposit'}           |          Rp {deposit}")
        print(f"{'Pengalaman'}        |          {pengalaman} tahun")
        print(f"{'------------------------------------------------------------'}")
        print(f"{"Keputusan"}         |{hasil}")
        print(f"{'============================================================'}")
        print(f"{'Terima kasih telah menggunakan sistem rental mobil'}")
        print(f"{'============================================================'}")

    elif pilihan == "2":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.\n")

sleep(5)
os.system('cls')
os.system('cls')