from prettytable import PrettyTable
from utils import bersihkan_layar, tampilkan_judul, ambil_waktu
from auth import register, login
from penyewa import tambah_data, lihat_data, ubah_data, hapus_data, data_penyewa
from pencarian import cari_penyewa
from keuangan import lihat_statistik, hitung_total

def menu_cari():
    """Fungsi untuk menu cari penyewa"""
    bersihkan_layar()
    tampilkan_judul("CARI PENYEWA")
    
    if len(data_penyewa) == 0:
        print("Belum ada data penyewa.")
        input("\nTekan Enter...")
        return
    
    nama_cari = input("Nama yang dicari: ")
    if nama_cari == "" or nama_cari.isspace():
        print("Nama tidak boleh kosong!")
        input("\nTekan Enter...")
        return
    
    list_kamar = list(data_penyewa.keys())
    hasil = cari_penyewa(list_kamar, 0, nama_cari, data_penyewa)
    
    if len(hasil) == 0:
        print(f"\nTidak ada penyewa dengan nama '{nama_cari}'")
    else:
        print(f"\nKetemu {len(hasil)} penyewa:")
        
        tabel = PrettyTable()
        tabel.field_names = ["Nama", "Kamar", "Lama Sewa", "Total Bayar", "Status"]
        
        for kamar in hasil:
            nama = data_penyewa[kamar]['nama']
            lama = data_penyewa[kamar]['lama_sewa']
            status = data_penyewa[kamar]['status_bayar']
            total = hitung_total(int(lama))
            
            tabel.add_row([nama, kamar, f"{lama} bulan", f"Rp {total:,}", status])
        
        print("\n" + str(tabel))
    
    input("\nTekan Enter...")

def menu_statistik():
    """Fungsi untuk menu statistik"""
    bersihkan_layar()
    tampilkan_judul("STATISTIK PENYEWA")
    
    stats = lihat_statistik(data_penyewa)
    
    tabel = PrettyTable()
    tabel.field_names = ["Keterangan", "Jumlah"]
    
    tabel.add_row(["Total Penyewa", f"{stats['total']} orang"])
    tabel.add_row(["Sudah Lunas", f"{stats['lunas']} orang"])
    tabel.add_row(["Belum Lunas", f"{stats['belum_lunas']} orang"])
    tabel.add_row(["Total Pendapatan", f"Rp {stats['pendapatan']:,}"])
    
    print("\n" + str(tabel))
    print(f"\nWaktu: {ambil_waktu()}")
    
    input("\nTekan Enter...")

def menu_admin(username):
    """Menu untuk admin"""
    while True:
        bersihkan_layar()
        tampilkan_judul(f"MENU ADMIN - {username}")
        
        print("1. Tambah Data Penyewa")
        print("2. Lihat Data Penyewa")
        print("3. Ubah Data Penyewa")
        print("4. Hapus Data Penyewa")
        print("5. Cari Penyewa")
        print("6. Statistik")
        print("7. Logout")
        print("=" * 50)
        
        pilihan = input("Pilih menu (1-7): ")
        
        if pilihan == "1":
            bersihkan_layar()
            tampilkan_judul("TAMBAH DATA PENYEWA")
            berhasil, pesan = tambah_data()
            print(pesan)
            input("\nTekan Enter...")
            
        elif pilihan == "2":
            bersihkan_layar()
            tampilkan_judul("LIHAT DATA PENYEWA")
            berhasil, pesan = lihat_data()
            if not berhasil:
                print(pesan)
            input("\nTekan Enter...")
            
        elif pilihan == "3":
            bersihkan_layar()
            tampilkan_judul("UBAH DATA PENYEWA")
            berhasil, pesan = ubah_data()
            print(pesan)
            input("\nTekan Enter...")
            
        elif pilihan == "4":
            bersihkan_layar()
            tampilkan_judul("HAPUS DATA PENYEWA")
            berhasil, pesan = hapus_data()
            print(pesan)
            input("\nTekan Enter...")
            
        elif pilihan == "5":
            menu_cari()
            
        elif pilihan == "6":
            menu_statistik()
            
        elif pilihan == "7":
            bersihkan_layar()
            print("Logout berhasil!")
            break
            
        else:
            print("Pilihan tidak ada!")
            input("\nTekan Enter...")

def menu_penyewa(username):
    """Menu untuk penyewa"""
    while True:
        bersihkan_layar()
        tampilkan_judul(f"MENU PENYEWA - {username}")
        
        print("1. Tambah Data Penyewa")
        print("2. Lihat Data Penyewa")
        print("3. Cari Penyewa")
        print("4. Logout")
        print("=" * 50)
        
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == "1":
            bersihkan_layar()
            tampilkan_judul("TAMBAH DATA PENYEWA")
            berhasil, pesan = tambah_data()
            print(pesan)
            input("\nTekan Enter...")
            
        elif pilihan == "2":
            bersihkan_layar()
            tampilkan_judul("LIHAT DATA PENYEWA")
            berhasil, pesan = lihat_data()
            if not berhasil:
                print(pesan)
            input("\nTekan Enter...")
            
        elif pilihan == "3":
            menu_cari()
            
        elif pilihan == "4":
            bersihkan_layar()
            print("Logout berhasil!")
            break
            
        else:
            print("Pilihan tidak ada!")
            input("\nTekan Enter...")

print("===================================")
print("PROGRAM MANAJEMEN PENYEWA KOST")
print("===================================")

while True:
    print("\n=== SELAMAT DATANG ===")
    print("1. Login")
    print("2. Register (Penyewa)")
    print("3. Keluar")
    print("=" * 50)
    
    pilihan = input("Pilih menu (1-3): ")
    
    if pilihan == "1":
        # Menu Login
        bersihkan_layar()
        tampilkan_judul("LOGIN")
        
        username = input("Username: ")
        password = input("Password: ")
        
        berhasil, pesan, role = login(username, password)
        
        if berhasil:
            bersihkan_layar()
            print(f"Login berhasil! Selamat datang {username}!")
            print(f"Waktu login: {ambil_waktu()}")
            input("\nTekan Enter...")
            
            if role == "admin":
                menu_admin(username)
            else:
                menu_penyewa(username)
        else:
            print(pesan)
            input("\nTekan Enter...")
            bersihkan_layar()
    
    elif pilihan == "2":
        bersihkan_layar()
        berhasil, pesan = register()
        print(pesan)
        input("\nTekan Enter...")
        bersihkan_layar()
    
    elif pilihan == "3":
        bersihkan_layar()
        print("Terima kasih!")
        break
    
    else:
        bersihkan_layar()
        print("Pilihan tidak ada! Pilih 1, 2, atau 3.")