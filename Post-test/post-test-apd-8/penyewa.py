
from prettytable import PrettyTable
from keuangan import hitung_total

data_penyewa = {}

def tambah_data():
    """Fungsi untuk menambah penyewa baru"""
    print("\n=== TAMBAH DATA PENYEWA ===")
    
    try:
        nama = input("Nama penyewa: ")
        if nama == "" or nama.isspace():
            return False, "Nama tidak boleh kosong!"
        
        kamar = input("Nomor kamar: ")
        if kamar == "" or kamar.isspace():
            return False, "Nomor kamar tidak boleh kosong!"
        
        if kamar in data_penyewa:
            return False, "Kamar sudah ada yang sewa!"
        
        lama = input("Lama sewa (bulan): ")
        if lama == "" or lama.isspace():
            return False, "Lama sewa tidak boleh kosong!"
        
        if not lama.isdigit():
            return False, "Lama sewa harus angka!"
        
        lama = int(lama)
        if lama < 1:
            return False, "Lama sewa minimal 1 bulan!"
        
        total = hitung_total(lama)
        print(f"Total bayar: Rp {total:,}")
        
        if lama >= 12:
            print("Dapat diskon 15%!")
        elif lama >= 6:
            print("Dapat diskon 10%!")
        
        status = input("Status bayar (Lunas/Belum Lunas): ")
        if status.lower() not in ["lunas", "belum lunas"]:
            return False, "Status harus Lunas atau Belum Lunas!"
        
        data_penyewa[kamar] = {
            "nama": nama,
            "lama_sewa": str(lama),
            "status_bayar": status.title()
        }
        
        return True, "Data berhasil ditambahkan!"
        
    except Exception as e:
        return False, f"Error: {e}"

def lihat_data():
    """Fungsi untuk melihat semua data penyewa"""
    
    if len(data_penyewa) == 0:
        return False, "Belum ada data penyewa"
    
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama", "Kamar", "Lama Sewa", "Total Bayar", "Status"]
    
    nomor = 1
    for kamar in data_penyewa:
        nama = data_penyewa[kamar]['nama']
        lama = data_penyewa[kamar]['lama_sewa']
        status = data_penyewa[kamar]['status_bayar']
        total = hitung_total(int(lama))
        
        tabel.add_row([nomor, nama, kamar, f"{lama} bulan", f"Rp {total:,}", status])
        nomor = nomor + 1
    
    print("\n" + str(tabel))
    return True, ""

def ubah_data():
    """Fungsi untuk mengubah data penyewa"""
    
    if len(data_penyewa) == 0:
        return False, "Belum ada data penyewa."
    

    print("\nDaftar Penyewa:")
    list_kamar = list(data_penyewa.keys())
    for i in range(len(list_kamar)):
        kamar = list_kamar[i]
        nama = data_penyewa[kamar]['nama']
        print(f"{i+1}. {nama} - Kamar {kamar}")
    
    try:
        pilih = input("\nPilih nomor: ")
        if pilih == "" or pilih.isspace():
            return False, "Input tidak boleh kosong!"
        
        if not pilih.isdigit():
            return False, "Harus angka!"
        
        pilih = int(pilih)
        if pilih < 1 or pilih > len(list_kamar):
            return False, "Nomor tidak ada!"
        
        kamar_lama = list_kamar[pilih - 1]
        
        print("\n--- Data Lama ---")
        print(f"Nama: {data_penyewa[kamar_lama]['nama']}")
        print(f"Kamar: {kamar_lama}")
        print(f"Lama sewa: {data_penyewa[kamar_lama]['lama_sewa']} bulan")
        print(f"Status: {data_penyewa[kamar_lama]['status_bayar']}")
        
        print("\n--- Data Baru ---")
        nama_baru = input("Nama: ")
        if nama_baru == "" or nama_baru.isspace():
            return False, "Nama tidak boleh kosong!"
        
        kamar_baru = input("Nomor kamar: ")
        if kamar_baru == "" or kamar_baru.isspace():
            return False, "Nomor kamar tidak boleh kosong!"
        
        if kamar_baru != kamar_lama and kamar_baru in data_penyewa:
            return False, "Kamar sudah ada yang sewa!"
        
        lama_baru = input("Lama sewa (bulan): ")
        if lama_baru == "" or lama_baru.isspace():
            return False, "Lama sewa tidak boleh kosong!"
        
        if not lama_baru.isdigit():
            return False, "Lama sewa harus angka!"
        
        lama_baru = int(lama_baru)
        if lama_baru < 1:
            return False, "Lama sewa minimal 1 bulan!"
        
        status_baru = input("Status bayar (Lunas/Belum Lunas): ")
        if status_baru.lower() not in ["lunas", "belum lunas"]:
            return False, "Status harus Lunas atau Belum Lunas!"
        
        if kamar_baru != kamar_lama:
            del data_penyewa[kamar_lama]
        
        data_penyewa[kamar_baru] = {
            "nama": nama_baru,
            "lama_sewa": str(lama_baru),
            "status_bayar": status_baru.title()
        }
        
        return True, "Data berhasil diubah!"
        
    except Exception as e:
        return False, f"Error: {e}"

def hapus_data():
    """Fungsi untuk menghapus data penyewa"""
    
    if len(data_penyewa) == 0:
        return False, "Belum ada data penyewa."
    
    print("\nDaftar Penyewa:")
    list_kamar = list(data_penyewa.keys())
    for i in range(len(list_kamar)):
        kamar = list_kamar[i]
        nama = data_penyewa[kamar]['nama']
        print(f"{i+1}. {nama} - Kamar {kamar}")
    
    try:
        pilih = input("\nPilih nomor yang mau dihapus: ")
        if pilih == "" or pilih.isspace():
            return False, "Input tidak boleh kosong!"
        
        if not pilih.isdigit():
            return False, "Harus angka!"
        
        pilih = int(pilih)
        if pilih < 1 or pilih > len(list_kamar):
            return False, "Nomor tidak ada!"
        
        kamar_hapus = list_kamar[pilih - 1]
        
        print("\n--- Data yang akan dihapus ---")
        print(f"Nama: {data_penyewa[kamar_hapus]['nama']}")
        print(f"Kamar: {kamar_hapus}")
        print(f"Lama sewa: {data_penyewa[kamar_hapus]['lama_sewa']} bulan")
        print(f"Status: {data_penyewa[kamar_hapus]['status_bayar']}")
        
        yakin = input("\nYakin mau hapus? (ya/tidak): ")
        if yakin.lower() == "ya":
            del data_penyewa[kamar_hapus]
            return True, "Data berhasil dihapus!"
        else:
            return True, "Batal hapus."
        
    except Exception as e:
        return False, f"Error: {e}"