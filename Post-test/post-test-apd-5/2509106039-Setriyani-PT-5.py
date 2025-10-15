# Program Penyewaan Kost
import os

data_user = [
    ["admin", "admin123", "admin"]
]

data_penyewa = []

clear = os.system('cls' if os.name == 'nt' else 'clear')

print("===================================")
print("PROGRAM MANAJEMEN PENYEWA KOST")
print("===================================")

while True:
    print("\n===== SELAMAT DATANG =====")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    print("==========================")
   
    pilihan_awal = input("Pilih menu (1/2/3): ")

    if pilihan_awal != "1" and pilihan_awal != "2" and pilihan_awal != "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("ERROR: Pilihan tidak valid! Silakan pilih 1, 2, atau 3.")
        continue
   
    if pilihan_awal == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n===== REGISTER AKUN BARU =====")
       
        username_baru = input("Masukkan username baru: ")
       
        if username_baru == "":
            print("ERROR: Username tidak boleh kosong!")
            continue
       
        username_ada = False
        for user in data_user:
            if user[0] == username_baru:
                username_ada = True
                break
       
        if username_ada == True:
            print("ERROR: Username sudah digunakan! Gunakan username lain.")
            continue
       
        password_baru = input("Masukkan password baru: ")
       
        if password_baru == "":
            print("ERROR: Password tidak boleh kosong!")
            continue

       
        print("\nPilih role:")
        print("1. Admin")
        print("2. Penyewa")
        role_pilih = input("Pilih role (1/2): ")
       
        if role_pilih == "1":
            role_baru = "admin"
        elif role_pilih == "2":
            role_baru = "penyewa"
        else:
            print("ERROR: Pilihan role tidak valid!")
            continue
       
        user_baru = [username_baru, password_baru, role_baru]
        data_user.append(user_baru)
       
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Register berhasil! Silakan login.")
        continue
   
    elif pilihan_awal == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Terima kasih! Program selesai.")
        break
   
    elif pilihan_awal == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n===== LOGIN =====")
       
        username_input = input("Username: ")
        password_input = input("Password: ")
       
        if username_input == "" or password_input == "":
            print("ERROR: Username dan password tidak boleh kosong!")
            input("Tekan Enter untuk melanjutkan...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
       
        login_berhasil = False
        role_user = ""
       
        for user in data_user:
            if user[0] == username_input and user[1] == password_input:
                login_berhasil = True
                role_user = user[2]
                break
       
        if login_berhasil == False:
            print("ERROR: Username atau password salah!")
            input("Tekan Enter untuk melanjutkan...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
       
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nLogin berhasil! Selamat datang " + username_input + "!")
        input("Tekan Enter untuk melanjutkan...")
       
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n===== MENU UTAMA =====")
            print("User: " + username_input + " (" + role_user + ")")
            print("======================")
           
            if role_user == "admin":
                print("1. Tambah Data Penyewa")
                print("2. Lihat Data Penyewa")
                print("3. Ubah Data Penyewa")
                print("4. Hapus Data Penyewa")
                print("5. Logout")
            else:
                print("1. Tambah Data Penyewa")
                print("2. Lihat Data Penyewa")
                print("3. Logout")
           
            print("======================")
           
            pilihan = input("Pilih menu: ")
           
            if role_user == "admin":
                if pilihan != "1" and pilihan != "2" and pilihan != "3" and pilihan != "4" and pilihan != "5":
                    print("ERROR: Pilihan tidak valid!")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
            else:
                if pilihan != "1" and pilihan != "2" and pilihan != "3":
                    print("ERROR: Pilihan tidak valid!")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
           
            if pilihan == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\n--- Tambah Data Penyewa ---")
               
                nama = input("Nama penyewa: ")
           
                if nama == "":
                    print("ERROR: Nama tidak boleh kosong!")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
               
                kamar = input("Nomor kamar: ")
               
                if kamar == "":
                    print("ERROR: Nomor kamar tidak boleh kosong!")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
               
                kamar_terpakai = False
                for penyewa in data_penyewa:
                    if penyewa[1] == kamar:
                        kamar_terpakai = True
                        break
               
                if kamar_terpakai == True:
                    print("ERROR: Nomor kamar " + kamar + " sudah dipakai!")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
               
                lama = input("Lama sewa (bulan): ")
               
                if lama == "":
                    print("ERROR: Lama sewa tidak boleh kosong!")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
               
                angka_valid = True
                for karakter in lama:
                    if karakter < "0" or karakter > "9":
                        angka_valid = False
                        break
               
                if angka_valid == False:
                    print("ERROR: Lama sewa harus berupa angka!")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
               
                if int(lama) < 1:
                    print("ERROR: Lama sewa minimal 1 bulan!")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
               
                bayar = input("Status pembayaran (Lunas/Belum Lunas): ")
               
                if bayar != "Lunas" and bayar != "Belum Lunas" and bayar != "lunas" and bayar != "belum lunas":
                    print("ERROR: Status pembayaran harus 'Lunas' atau 'Belum Lunas'!")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
               
                data_baru = [nama, kamar, lama, bayar]
                data_penyewa.append(data_baru)
               
                print("\nData berhasil ditambahkan!")
                input("Tekan Enter untuk melanjutkan...")
           
            elif pilihan == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\n--- Lihat Data Penyewa ---")
               
                if len(data_penyewa) == 0:
                    print("Belum ada data penyewa.")
                else:
                    nomor = 1
                    for data in data_penyewa:
                        print("\n" + "=" * 30)
                        print("Penyewa ke-" + str(nomor))
                        print("=" * 30)
                        print("Nama              : " + data[0])
                        print("Nomor Kamar       : " + data[1])
                        print("Lama Sewa         : " + data[2] + " bulan")
                        print("Status Pembayaran : " + data[3])
                        nomor = nomor + 1
               
                input("\nTekan Enter untuk melanjutkan...")
           
            elif pilihan == "3":
                if role_user == "admin":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\n--- Ubah Data Penyewa ---")
                   
                    if len(data_penyewa) == 0:
                        print("Belum ada data penyewa.")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                   
                    nomor = 1
                    for data in data_penyewa:
                        print(str(nomor) + ". " + data[0] + " - Kamar " + data[1])
                        nomor = nomor + 1
                   
                    pilih = input("\nPilih nomor penyewa yang mau diubah: ")
                   
                    if pilih == "":
                        print("ERROR: Input tidak boleh kosong!")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                   
                    angka_valid = True
                    for karakter in pilih:
                        if karakter < "0" or karakter > "9":
                            angka_valid = False
                            break
                   
                    if angka_valid == False:
                        print("ERROR: Input harus berupa angka!")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                   
                    pilih = int(pilih)
                   
                    if pilih < 1 or pilih > len(data_penyewa):
                        print("ERROR: Nomor tidak valid!")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                   
                    indeks = pilih - 1
                   
                    print("\nData lama:")
                    print("Nama              : " + data_penyewa[indeks][0])
                    print("Nomor Kamar       : " + data_penyewa[indeks][1])
                    print("Lama Sewa         : " + data_penyewa[indeks][2] + " bulan")
                    print("Status Pembayaran : " + data_penyewa[indeks][3])
                   
                    print("\nMasukkan data baru:")
                    nama_baru = input("Nama penyewa: ")
                   
                    if nama_baru == "":
                        print("ERROR: Nama tidak boleh kosong!")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                   
                    kamar_baru = input("Nomor kamar: ")
                   
                    if kamar_baru == "":
                        print("ERROR: Nomor kamar tidak boleh kosong!")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
       
                    kamar_terpakai = False
                    for i in range(len(data_penyewa)):
                        if i != indeks and data_penyewa[i][1] == kamar_baru:
                            kamar_terpakai = True
                            break
                   
                    if kamar_terpakai == True:
                        print("ERROR: Nomor kamar " + kamar_baru + " sudah dipakai!")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                   
                    lama_baru = input("Lama sewa (bulan): ")
                   
                    if lama_baru == "":
                        print("ERROR: Lama sewa tidak boleh kosong!")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                   
                    angka_valid = True
                    for karakter in lama_baru:
                        if karakter < "0" or karakter > "9":
                            angka_valid = False
                            break
                   
                    if angka_valid == False:
                        print("ERROR: Lama sewa harus berupa angka!")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                   
                    if int(lama_baru) < 1:
                        print("ERROR: Lama sewa minimal 1 bulan!")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                   
                    bayar_baru = input("Status pembayaran (Lunas/Belum Lunas): ")
                   
                    if bayar_baru != "Lunas" and bayar_baru != "Belum Lunas" and bayar_baru != "lunas" and bayar_baru != "belum lunas":
                        print("ERROR: Status pembayaran harus 'Lunas' atau 'Belum Lunas'!")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                   
                    data_penyewa[indeks][0] = nama_baru
                    data_penyewa[indeks][1] = kamar_baru
                    data_penyewa[indeks][2] = lama_baru
                    data_penyewa[indeks][3] = bayar_baru
                   
                    print("\nData berhasil diubah!")
                    input("Tekan Enter untuk melanjutkan...")
               
                elif role_user == "penyewa":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Logout berhasil!")
                    break
           
            elif pilihan == "4":
                if role_user == "admin":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\n--- Hapus Data Penyewa ---")
                   
                    if len(data_penyewa) == 0:
                        print("Belum ada data penyewa.")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                   
                    nomor = 1
                    for data in data_penyewa:
                        print(str(nomor) + ". " + data[0] + " - Kamar " + data[1])
                        nomor = nomor + 1
                   
                    pilih = input("\nPilih nomor penyewa yang mau dihapus: ")
                   
                    if pilih == "":
                        print("ERROR: Input tidak boleh kosong!")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                   
                    angka_valid = True
                    for karakter in pilih:
                        if karakter < "0" or karakter > "9":
                            angka_valid = False
                            break
                   
                    if angka_valid == False:
                        print("ERROR: Input harus berupa angka!")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                   
                    pilih = int(pilih)
                   
                    if pilih < 1 or pilih > len(data_penyewa):
                        print("ERROR: Nomor tidak valid!")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                   
                    indeks = pilih - 1
                   
                    yakin = input("Yakin mau hapus data " + data_penyewa[indeks][0] + "? (ya/tidak): ")
                   
                    if yakin == "ya" or yakin == "Ya":
                        data_penyewa.pop(indeks)
                        print("Data berhasil dihapus!")
                    else:
                        print("Penghapusan dibatalkan.")
                   
                    input("Tekan Enter untuk melanjutkan...")
               
                elif role_user == "penyewa":
                    print("ERROR: Anda tidak punya akses untuk menu ini!")
                    input("Tekan Enter untuk melanjutkan...")
           
            elif pilihan == "5":
                if role_user == "admin":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Logout berhasil!")
                    break
