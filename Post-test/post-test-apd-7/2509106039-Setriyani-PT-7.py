import os
from datetime import datetime

data_user = {
    "admin": {
        "password": "admin123",
        "role": "admin"
    }
}

data_penyewa = {}
current_user = None 

def clear_screen():
    """Prosedur untuk membersihkan layar"""
    os.system('cls' if os.name == 'nt' else 'clear')

def cetak_header(judul):
    """
    Prosedur untuk mencetak header
    Parameter: judul (str)
    """
    lebar = 50
    print("\n" + "=" * lebar)
    print(judul.center(lebar))
    print("=" * lebar)

def hitung_total_pembayaran(lama_sewa, harga_per_bulan=1500000):
    """
    Fungsi untuk menghitung total pembayaran dengan diskon
    Parameter: lama_sewa (int), harga_per_bulan (int)
    Return: total pembayaran (int)
    """

    lama = int(lama_sewa)
    total = lama * harga_per_bulan

    if lama >= 12:
        diskon = total * 0.15
    elif lama >= 6:
        diskon = total * 0.10
    else:
        diskon = 0
    
    return int(total - diskon)

def cari_penyewa_rekursif(daftar_kamar, index, nama_dicari):
    """
    Fungsi rekursif untuk mencari penyewa berdasarkan nama
    Parameter: daftar_kamar (list), index (int), nama_dicari (str)
    Return: list hasil pencarian
    """

    hasil = []
    
    if index >= len(daftar_kamar):
        return hasil
    

    kamar_sekarang = daftar_kamar[index]
    nama_penyewa = data_penyewa[kamar_sekarang]['nama'].lower()
    
    if nama_dicari.lower() in nama_penyewa:
        hasil.append(kamar_sekarang)
    
    hasil.extend(cari_penyewa_rekursif(daftar_kamar, index + 1, nama_dicari))
    
    return hasil

def tampilkan_statistik():
    """
    Fungsi untuk menampilkan statistik penyewa
    Return: dictionary berisi statistik
    """

    total_penyewa = len(data_penyewa)
    lunas = 0
    belum_lunas = 0
    total_pendapatan = 0
    
    for kamar, data in data_penyewa.items():
        if data['status_bayar'].lower() == 'lunas':
            lunas += 1
            total_pendapatan += hitung_total_pembayaran(data['lama_sewa'])
        else:
            belum_lunas += 1
    
    statistik = {
        'total': total_penyewa,
        'lunas': lunas,
        'belum_lunas': belum_lunas,
        'pendapatan': total_pendapatan
    }
    
    return statistik

def get_waktu_sekarang():
    """
    Fungsi untuk mendapatkan waktu sekarang
    Return: string waktu format dd/mm/yyyy HH:MM:SS
    """
    sekarang = datetime.now()
    waktu_format = sekarang.strftime("%d/%m/%Y %H:%M:%S")
    return waktu_format

print("===================================")
print("PROGRAM MANAJEMEN PENYEWA KOST")
print("===================================")

while True:
    print("\n===== SELAMAT DATANG =====")
    print("1. Login")
    print("2. Register (Penyewa)")
    print("3. Keluar")
    print("==========================")
   
    try:
        pilihan_awal = input("Pilih menu (1/2/3): ")

        if pilihan_awal not in ["1", "2", "3"]:
            raise ValueError("Pilihan tidak valid! Pilih 1, 2, atau 3.")
    
    except ValueError as e:
        clear_screen()
        print(f"Error: {e}")
        continue
   
    if pilihan_awal == "2":
        clear_screen()
        cetak_header("REGISTER AKUN PENYEWA")
       
        try:
            username_baru = input("Masukkan username baru: ")
            
            if username_baru == "" or username_baru.isspace():
                raise ValueError("Username tidak boleh kosong atau hanya berisi spasi!")
            
            password_baru = input("Masukkan password baru: ")
            
            if password_baru == "" or password_baru.isspace():
                raise ValueError("Password tidak boleh kosong atau hanya berisi spasi!")
            
            if len(password_baru) < 8:
                raise ValueError("Password minimal memiliki panjang 8 karakter!")
            
            ada_angka = False
            for char in password_baru:
                if char.isdigit():
                    ada_angka = True
                    break
            
            if not ada_angka:
                raise ValueError("Password wajib mengandung minimal 1 angka!")
           
            if username_baru in data_user:
                raise ValueError("Username sudah digunakan! Gunakan yang lain.")
           
            data_user[username_baru] = {
                "password": password_baru,
                "role": "penyewa"
            }
           
            clear_screen()
            print("✓ Register berhasil! Silakan login.")
        
        except ValueError as e:
            print(f"Error: {e}")
            input("Tekan Enter untuk melanjutkan...")
            clear_screen()
        
        continue
   
    elif pilihan_awal == "3":
        clear_screen()
        print("Terima kasih! Program selesai.")
        break
   
    elif pilihan_awal == "1":
        clear_screen()
        cetak_header("LOGIN")
       
        try:
            username_input = input("Username: ").strip()
            password_input = input("Password: ").strip()
           
            if username_input not in data_user:
                raise ValueError("Username tidak ditemukan!")
            
            if data_user[username_input]["password"] != password_input:
                raise ValueError("Password salah!")
           
            current_user = username_input
            role_user = data_user[username_input]["role"]
            clear_screen()
            print(f"✓ Login berhasil! Selamat datang {username_input}!")
            print(f"Waktu login: {get_waktu_sekarang()}")
            input("Tekan Enter untuk melanjutkan...")
        
        except ValueError as e:
            print(f"Error: {e}")
            input("Tekan Enter untuk melanjutkan...")
            clear_screen()
            continue
    
        while True:
            clear_screen()
            cetak_header(f"MENU UTAMA - {username_input} ({role_user})")
           
            if role_user == "admin":
                print("1. Tambah Data Penyewa")
                print("2. Lihat Data Penyewa")
                print("3. Ubah Data Penyewa")
                print("4. Hapus Data Penyewa")
                print("5. Cari Penyewa")
                print("6. Statistik")
                print("7. Logout")
                menu_valid = ["1", "2", "3", "4", "5", "6", "7"]
            else:
                print("1. Tambah Data Penyewa")
                print("2. Lihat Data Penyewa")
                print("3. Cari Penyewa")
                print("4. Logout")
                menu_valid = ["1", "2", "3", "4"]
           
            print("======================")
           
            try:
                pilihan = input("Pilih menu: ")
               
                if pilihan not in menu_valid:
                    raise ValueError("Pilihan tidak valid!")
            
            except ValueError as e:
                print(f"Error: {e}")
                input("Tekan Enter untuk melanjutkan...")
                continue
           
            if pilihan == "1":
                clear_screen()
                cetak_header("TAMBAH DATA PENYEWA")
               
                try:
                    nama = input("Nama penyewa: ")
                    
                    if nama == "" or nama.isspace():
                        raise ValueError("Nama tidak boleh kosong atau hanya berisi spasi!")
                   
                    kamar = input("Nomor kamar: ").strip()
                    
                    if kamar == "" or kamar.isspace():
                        raise ValueError("Nomor kamar tidak boleh kosong atau hanya berisi spasi!")
                   
                    if kamar in data_penyewa:
                        raise KeyError(f"Nomor kamar {kamar} sudah dipakai!")
                   
                    lama = input("Lama sewa (bulan): ")
                    
                    if lama == "" or lama.isspace():
                        raise ValueError("Lama sewa tidak boleh kosong!")
                    
                    if not lama.isdigit():
                        raise TypeError("Lama sewa harus berupa angka!")
                    
                    lama_int = int(lama)
                    
                    if lama_int < 1:
                        raise ValueError("Lama sewa minimal 1 bulan!")
                   
                    total_bayar = hitung_total_pembayaran(lama_int)
                    print(f"\nTotal pembayaran: Rp {total_bayar:,}")
                    
                    if lama_int >= 6:
                        print(f" Anda mendapat diskon {'15%' if lama_int >= 12 else '10%'}!")
                   
                    bayar = input("Status pembayaran (Lunas/Belum Lunas): ").strip()
                   
                    if bayar.lower() not in ["lunas", "belum lunas"]:
                        raise ValueError("Status pembayaran harus 'Lunas' atau 'Belum Lunas'!")
                   
                    data_penyewa[kamar] = {
                        "nama": nama,
                        "lama_sewa": str(lama_int),
                        "status_bayar": bayar.title()
                    }
                   
                    print("\n✓ Data berhasil ditambahkan!")
                
                except ValueError as e:
                    print(f"ValueError: {e}")
                except TypeError as e:
                    print(f"TypeError: {e}")
                except KeyError as e:
                    print(f"KeyError: {e}")
                
                finally:
                    input("Tekan Enter untuk melanjutkan...")
           
            elif pilihan == "2":
                clear_screen()
                cetak_header("LIHAT DATA PENYEWA")
               
                try:
                    if len(data_penyewa) == 0:
                        raise ValueError("Belum ada data penyewa.")
                    
                    nomor = 1
                    for kamar, data in data_penyewa.items():
                        total_bayar = hitung_total_pembayaran(data['lama_sewa'])
                        
                        print(f"\n--- Penyewa ke-{nomor} ---")
                        print("=" * 40)
                        print(f"Nama              : {data['nama']}")
                        print(f"Nomor Kamar       : {kamar}")
                        print(f"Lama Sewa         : {data['lama_sewa']} bulan")
                        print(f"Total Pembayaran  : Rp {total_bayar:,}")
                        print(f"Status Pembayaran : {data['status_bayar']}")
                        print("=" * 40)
                        nomor += 1
                
                except ValueError as e:
                    print(f"Info: {e}")
                
                finally:
                    input("\nTekan Enter untuk melanjutkan...")
           
            elif pilihan == "3" and role_user == "penyewa":
                clear_screen()
                cetak_header("CARI PENYEWA")
                
                try:
                    if len(data_penyewa) == 0:
                        raise ValueError("Belum ada data penyewa.")
                    
                    nama_cari = input("Masukkan nama yang dicari: ").strip()
                    
                    if nama_cari == "" or nama_cari.isspace():
                        raise ValueError("Nama tidak boleh kosong atau hanya berisi spasi!")
                    
                    list_kamar = list(data_penyewa.keys())
                    hasil = cari_penyewa_rekursif(list_kamar, 0, nama_cari)
                    
                    if len(hasil) == 0:
                        print(f"\nTidak ditemukan penyewa dengan nama '{nama_cari}'")
                    else:
                        print(f"\nDitemukan {len(hasil)} penyewa:")
                        for kamar in hasil:

                            data = data_penyewa[kamar]
                            total_bayar = hitung_total_pembayaran(data['lama_sewa'])
                            
                            print("\n" + "=" * 40)
                            print(f"Nama              : {data['nama']}")
                            print(f"Nomor Kamar       : {kamar}")
                            print(f"Lama Sewa         : {data['lama_sewa']} bulan")
                            print(f"Total Pembayaran  : Rp {total_bayar:,}")
                            print(f"Status Pembayaran : {data['status_bayar']}")
                            print("=" * 40)
                
                except ValueError as e:
                    print(f"Error: {e}")
                
                finally:
                    input("\nTekan Enter untuk melanjutkan...")
                
            elif pilihan == "3" and role_user == "admin":
                clear_screen()
                cetak_header("UBAH DATA PENYEWA")
               
                try:
                    if len(data_penyewa) == 0:
                        raise ValueError("Belum ada data penyewa.")
                   
                    list_kamar = list(data_penyewa.keys())
                    for i, kamar in enumerate(list_kamar, 1):
                        print(f"{i}. {data_penyewa[kamar]['nama']} - Kamar {kamar}")
                   
                    pilih = input("\nPilih nomor penyewa yang mau diubah: ")
                    
                    if pilih == "" or pilih.isspace():
                        raise ValueError("Input tidak boleh kosong!")
                    
                    if not pilih.isdigit():
                        raise TypeError("Input harus berupa angka!")
                    
                    pilih_int = int(pilih)
                   
                    if pilih_int < 1 or pilih_int > len(list_kamar):
                        raise IndexError("Nomor tidak valid! Pilih nomor yang tersedia.")
                   
                    kamar_lama = list_kamar[pilih_int - 1]
                   
                    print("\n--- Data Lama ---")
                    # Variabel lokal
                    data_lama = data_penyewa[kamar_lama]
                    total_bayar_lama = hitung_total_pembayaran(data_lama['lama_sewa'])
                    
                    print("=" * 40)
                    print(f"Nama              : {data_lama['nama']}")
                    print(f"Nomor Kamar       : {kamar_lama}")
                    print(f"Lama Sewa         : {data_lama['lama_sewa']} bulan")
                    print(f"Total Pembayaran  : Rp {total_bayar_lama:,}")
                    print(f"Status Pembayaran : {data_lama['status_bayar']}")
                    print("=" * 40)
                   
                    print("\n--- Masukkan Data Baru ---")
                    nama_baru = input("Nama penyewa: ")
                    
                    if nama_baru == "" or nama_baru.isspace():
                        raise ValueError("Nama tidak boleh kosong atau hanya berisi spasi!")
                   
                    kamar_baru = input("Nomor kamar: ").strip()
                    
                    if kamar_baru == "" or kamar_baru.isspace():
                        raise ValueError("Nomor kamar tidak boleh kosong atau hanya berisi spasi!")
       
                    if kamar_baru != kamar_lama and kamar_baru in data_penyewa:
                        raise KeyError(f"Nomor kamar {kamar_baru} sudah dipakai!")
                   
                    lama_baru = input("Lama sewa (bulan): ")
                    
                    if lama_baru == "" or lama_baru.isspace():
                        raise ValueError("Lama sewa tidak boleh kosong!")
                    
                    if not lama_baru.isdigit():
                        raise TypeError("Lama sewa harus berupa angka!")
                    
                    lama_baru_int = int(lama_baru)
                    
                    if lama_baru_int < 1:
                        raise ValueError("Lama sewa minimal 1 bulan!")
                    
                    total_bayar = hitung_total_pembayaran(lama_baru_int)
                    print(f"\nTotal pembayaran: Rp {total_bayar:,}")
                   
                    bayar_baru = input("Status pembayaran (Lunas/Belum Lunas): ").strip()
                   
                    if bayar_baru.lower() not in ["lunas", "belum lunas"]:
                        raise ValueError("Status pembayaran harus 'Lunas' atau 'Belum Lunas'!")
                   
                    if kamar_baru != kamar_lama:
                        del data_penyewa[kamar_lama]
                   
                    data_penyewa[kamar_baru] = {
                        "nama": nama_baru,
                        "lama_sewa": str(lama_baru_int),
                        "status_bayar": bayar_baru.title()
                    }
                   
                    print("\n✓ Data berhasil diubah!")
                
                except ValueError as e:
                    print(f"ValueError: {e}")
                except TypeError as e:
                    print(f"TypeError: {e}")
                except IndexError as e:
                    print(f"IndexError: {e}")
                except KeyError as e:
                    print(f"KeyError: {e}")
                
                finally:
                    input("Tekan Enter untuk melanjutkan...")

            elif pilihan == "4" and role_user == "penyewa":
                clear_screen()
                print("✓ Logout berhasil!")
                break
                
            elif pilihan == "4" and role_user == "admin":
                clear_screen()
                cetak_header("HAPUS DATA PENYEWA")
               
                try:
                    if len(data_penyewa) == 0:
                        raise ValueError("Belum ada data penyewa.")
                   
                    list_kamar = list(data_penyewa.keys())
                    for i, kamar in enumerate(list_kamar, 1):
                        print(f"{i}. {data_penyewa[kamar]['nama']} - Kamar {kamar}")
                   
                    pilih = input("\nPilih nomor penyewa yang mau dihapus: ")
                    
                    if pilih == "" or pilih.isspace():
                        raise ValueError("Input tidak boleh kosong!")
                    
                    if not pilih.isdigit():
                        raise TypeError("Input harus berupa angka!")
                    
                    pilih_int = int(pilih)
                   
                    if pilih_int < 1 or pilih_int > len(list_kamar):
                        raise IndexError("Nomor tidak valid! Pilih nomor yang tersedia.")
                   
                    kamar_hapus = list_kamar[pilih_int - 1]
                   
                    data_hapus = data_penyewa[kamar_hapus]
                    total_bayar = hitung_total_pembayaran(data_hapus['lama_sewa'])
                    
                    print("\n--- Data yang akan dihapus ---")
                    print("=" * 40)
                    print(f"Nama              : {data_hapus['nama']}")
                    print(f"Nomor Kamar       : {kamar_hapus}")
                    print(f"Lama Sewa         : {data_hapus['lama_sewa']} bulan")
                    print(f"Total Pembayaran  : Rp {total_bayar:,}")
                    print(f"Status Pembayaran : {data_hapus['status_bayar']}")
                    print("=" * 40)
                   
                    yakin = input(f"\nYakin mau hapus data ini? (ya/tidak): ").strip()
                   
                    if yakin.lower() == "ya":
                        del data_penyewa[kamar_hapus]
                        print("Data berhasil dihapus!")
                    else:
                        print("Penghapusan dibatalkan.")
                
                except ValueError as e:
                    print(f"ValueError: {e}")
                except TypeError as e:
                    print(f"TypeError: {e}")
                except IndexError as e:
                    print(f"IndexError: {e}")
                
                finally:
                    input("Tekan Enter untuk melanjutkan...")
            
            elif pilihan == "5" and role_user == "admin":
                clear_screen()
                cetak_header("CARI PENYEWA")
                
                try:
                    if len(data_penyewa) == 0:
                        raise ValueError("Belum ada data penyewa.")
                    
                    nama_cari = input("Masukkan nama yang dicari: ").strip()
                    
                    if nama_cari == "" or nama_cari.isspace():
                        raise ValueError("Nama tidak boleh kosong atau hanya berisi spasi!")
                    
                    list_kamar = list(data_penyewa.keys())
                    hasil = cari_penyewa_rekursif(list_kamar, 0, nama_cari)
                    
                    if len(hasil) == 0:
                        print(f"\nTidak ditemukan penyewa dengan nama '{nama_cari}'")
                    else:
                        print(f"\nDitemukan {len(hasil)} penyewa:")
                        for kamar in hasil:

                            data = data_penyewa[kamar]
                            total_bayar = hitung_total_pembayaran(data['lama_sewa'])
                            
                            print("\n" + "=" * 40)
                            print(f"Nama              : {data['nama']}")
                            print(f"Nomor Kamar       : {kamar}")
                            print(f"Lama Sewa         : {data['lama_sewa']} bulan")
                            print(f"Total Pembayaran  : Rp {total_bayar:,}")
                            print(f"Status Pembayaran : {data['status_bayar']}")
                            print("=" * 40)
                
                except ValueError as e:
                    print(f"ValueError: {e}")
                
                finally:
                    input("\nTekan Enter untuk melanjutkan...")
            
            elif pilihan == "6" and role_user == "admin":
                clear_screen()
                cetak_header("STATISTIK PENYEWA")
                
                try:
                    stats = tampilkan_statistik()
                    
                    print(f"\nTotal Penyewa        : {stats['total']} orang")
                    print(f"Sudah Lunas         : {stats['lunas']} orang")
                    print(f"Belum Lunas         : {stats['belum_lunas']} orang")
                    print(f"Total Pendapatan    : Rp {stats['pendapatan']:,}")
                    print(f"\nWaktu: {get_waktu_sekarang()}")
                
                except Exception as e:
                    print(f"Error: {e}")
                
                finally:
                    input("\nTekan Enter untuk melanjutkan...")
           
            elif pilihan == "7" and role_user == "admin":
                clear_screen()
                print("Logout berhasil!")
                break