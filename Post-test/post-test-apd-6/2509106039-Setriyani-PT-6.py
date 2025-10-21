import os

data_user = {
    "admin": {
        "password": "admin123",
        "role": "admin"
    }
}

data_penyewa = {}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print("===================================")
print("PROGRAM MANAJEMEN PENYEWA KOST")
print("===================================")

while True:
    print("\n===== SELAMAT DATANG =====")
    print("1. Login")
    print("2. Register (Penyewa)")
    print("3. Keluar")
    print("==========================")
   
    pilihan_awal = input("Pilih menu (1/2/3): ")

    if pilihan_awal not in ["1", "2", "3"]:
        clear_screen()
        print("Pilihan tidak valid.")
        continue
   
    if pilihan_awal == "2":
        clear_screen()
        print("\n===== REGISTER AKUN PENYEWA =====")
       
        username_baru = input("Masukkan username baru: ")
        password_baru = input("Masukkan password baru: ")
       
        if username_baru in data_user:
            print("Username sudah digunakan! Gunakan yang lain.")
            input("Tekan Enter untuk melanjutkan...")
            clear_screen()
            continue
       
        data_user[username_baru] = {
            "password": password_baru,
            "role": "penyewa"
        }
       
        clear_screen()
        print("Register berhasil! Silakan login.")
        continue
   
    elif pilihan_awal == "3":
        clear_screen()
        print("Terima kasih! Program selesai.")
        break
   
    elif pilihan_awal == "1":
        clear_screen()
        print("\n===== LOGIN =====")
       
        username_input = input("Username: ")
        password_input = input("Password: ")
       
        if username_input not in data_user or data_user[username_input]["password"] != password_input:
            print("Username atau password salah!")
            input("Tekan Enter untuk melanjutkan...")
            clear_screen()
            continue
       
        role_user = data_user[username_input]["role"]
        clear_screen()
        print(f"\nLogin berhasil! Selamat datang {username_input}!")
        input("Tekan Enter untuk melanjutkan...")
       
        while True:
            clear_screen()
            print("\n===== MENU UTAMA =====")
            print(f"User: {username_input} ({role_user})")
            print("======================")
           
            if role_user == "admin":
                print("1. Tambah Data Penyewa")
                print("2. Lihat Data Penyewa")
                print("3. Ubah Data Penyewa")
                print("4. Hapus Data Penyewa")
                print("5. Logout")
                menu_valid = ["1", "2", "3", "4", "5"]
            else:
                print("1. Tambah Data Penyewa")
                print("2. Lihat Data Penyewa")
                print("3. Logout")
                menu_valid = ["1", "2", "3"]
           
            print("======================")
           
            pilihan = input("Pilih menu: ")
           
            if pilihan not in menu_valid:
                print("Pilihan tidak valid!")
                input("Tekan Enter untuk melanjutkan...")
                continue
           
            if pilihan == "1":
                clear_screen()
                print("\n--- Tambah Data Penyewa ---")
               
                nama = input("Nama penyewa: ")
           
                if nama == "":
                    print("Nama tidak boleh kosong!")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
               
                kamar = input("Nomor kamar: ")
               
                if kamar == "":
                    print("Nomor kamar tidak boleh kosong!")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
               
                if kamar in data_penyewa:
                    print(f"Nomor kamar {kamar} sudah dipakai!")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
               
                lama = input("Lama sewa (bulan): ")
               
                if lama == "":
                    print("Lama sewa tidak boleh kosong!")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
               
                if not lama.isdigit():
                    print("Lama sewa harus berupa angka!")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
               
                if int(lama) < 1:
                    print("Lama sewa minimal 1 bulan!")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
               
                bayar = input("Status pembayaran (Lunas/Belum Lunas): ")
               
                if bayar.lower() not in ["lunas", "belum lunas"]:
                    print("Status pembayaran harus 'Lunas' atau 'Belum Lunas'!")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
               
                data_penyewa[kamar] = {
                    "nama": nama,
                    "lama_sewa": lama,
                    "status_bayar": bayar.title()
                }
               
                print("\nData berhasil ditambahkan!")
                input("Tekan Enter untuk melanjutkan...")
           
            elif pilihan == "2":
                clear_screen()
                print("\n--- Lihat Data Penyewa ---")
               
                if len(data_penyewa) == 0:
                    print("Belum ada data penyewa.")
                else:
                    nomor = 1
                    for kamar, data in data_penyewa.items():
                        print("\n" + "=" * 30)
                        print(f"Penyewa ke-{nomor}")
                        print("=" * 30)
                        print(f"Nama              : {data['nama']}")
                        print(f"Nomor Kamar       : {kamar}")
                        print(f"Lama Sewa         : {data['lama_sewa']} bulan")
                        print(f"Status Pembayaran : {data['status_bayar']}")
                        nomor += 1
               
                input("\nTekan Enter untuk melanjutkan...")
           
            elif pilihan == "3":
                if role_user == "admin":
                    clear_screen()
                    print("\n--- Ubah Data Penyewa ---")
                   
                    if len(data_penyewa) == 0:
                        print("Belum ada data penyewa.")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                   
                    list_kamar = list(data_penyewa.keys())
                    for i, kamar in enumerate(list_kamar, 1):
                        print(f"{i}. {data_penyewa[kamar]['nama']} - Kamar {kamar}")
                   
                    pilih = input("\nPilih nomor penyewa yang mau diubah: ")
                   
                    if pilih == "":
                        print("Input tidak boleh kosong!")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                   
                    if not pilih.isdigit():
                        print("Input harus berupa angka!")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                   
                    pilih = int(pilih)
                   
                    if pilih < 1 or pilih > len(list_kamar):
                        print("Nomor tidak valid!")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                   
                    kamar_lama = list_kamar[pilih - 1]
                   
                    print("\nData lama:")
                    print(f"Nama              : {data_penyewa[kamar_lama]['nama']}")
                    print(f"Nomor Kamar       : {kamar_lama}")
                    print(f"Lama Sewa         : {data_penyewa[kamar_lama]['lama_sewa']} bulan")
                    print(f"Status Pembayaran : {data_penyewa[kamar_lama]['status_bayar']}")
                   
                    print("\nMasukkan data baru:")
                    nama_baru = input("Nama penyewa: ")
                   
                    if nama_baru == "":
                        print("Nama tidak boleh kosong!")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                   
                    kamar_baru = input("Nomor kamar: ")
                   
                    if kamar_baru == "":
                        print("Nomor kamar tidak boleh kosong!")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
       
                    if kamar_baru != kamar_lama and kamar_baru in data_penyewa:
                        print(f"Nomor kamar {kamar_baru} sudah dipakai!")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                   
                    lama_baru = input("Lama sewa (bulan): ")
                   
                    if lama_baru == "":
                        print("Lama sewa tidak boleh kosong!")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                   
                    if not lama_baru.isdigit():
                        print("Lama sewa harus berupa angka!")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                   
                    if int(lama_baru) < 1:
                        print("Lama sewa minimal 1 bulan!")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                   
                    bayar_baru = input("Status pembayaran (Lunas/Belum Lunas): ")
                   
                    if bayar_baru.lower() not in ["lunas", "belum lunas"]:
                        print("Status pembayaran harus 'Lunas' atau 'Belum Lunas'!")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                   
                    if kamar_baru != kamar_lama:
                        del data_penyewa[kamar_lama]
                   
                    data_penyewa[kamar_baru] = {
                        "nama": nama_baru,
                        "lama_sewa": lama_baru,
                        "status_bayar": bayar_baru.title()
                    }
                   
                    print("\nData berhasil diubah!")
                    input("Tekan Enter untuk melanjutkan...")
               
                else:  
                    clear_screen()
                    print("Logout berhasil!")
                    break
           
            elif pilihan == "4":
                if role_user == "admin":
                    clear_screen()
                    print("\n--- Hapus Data Penyewa ---")
                   
                    if len(data_penyewa) == 0:
                        print("Belum ada data penyewa.")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                   
                    list_kamar = list(data_penyewa.keys())
                    for i, kamar in enumerate(list_kamar, 1):
                        print(f"{i}. {data_penyewa[kamar]['nama']} - Kamar {kamar}")
                   
                    pilih = input("\nPilih nomor penyewa yang mau dihapus: ")
                   
                    if pilih == "":
                        print("Input tidak boleh kosong!")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                   
                    if not pilih.isdigit():
                        print("Input harus berupa angka!")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                   
                    pilih = int(pilih)
                   
                    if pilih < 1 or pilih > len(list_kamar):
                        print("Nomor tidak valid!")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                   
                    kamar_hapus = list_kamar[pilih - 1]
                   
                    yakin = input(f"Yakin mau hapus data {data_penyewa[kamar_hapus]['nama']}? (ya/tidak): ")
                   
                    if yakin.lower() == "ya":
                        del data_penyewa[kamar_hapus]
                        print("Data berhasil dihapus!")
                    else:
                        print("Penghapusan dibatalkan.")
                   
                    input("Tekan Enter untuk melanjutkan...")
           
            elif pilihan == "5":
                if role_user == "admin":
                    clear_screen()
                    print("Logout berhasil!")
                    break