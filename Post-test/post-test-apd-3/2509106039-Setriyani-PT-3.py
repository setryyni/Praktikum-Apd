# Program Sistem Rental Mobil

print(f"{'============================================================'}")
print(f"{'                     SISTEM RENTAL MOBIL                    '}")
print(f"{'============================================================'}")

usia = int(input("Masukkan usia customer: "))
punya_sim = input("Apakah memiliki SIM A? (ya/tidak): ").lower()
deposit = int(input("Masukkan jumlah deposit (Rp): "))
pengalaman = int(input("Masukkan pengalaman mengemudi (tahun): "))

if usia < 21:
    print("Tolak: Usia tidak mencukupi")
elif punya_sim != "ya":
    print("Tolak: Tidak memiliki SIM A")
elif deposit < 500000:
    print("Tolak: Deposit tidak cukup")
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
