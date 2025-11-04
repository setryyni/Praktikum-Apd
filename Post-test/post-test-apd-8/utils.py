import os
from datetime import datetime

def bersihkan_layar():
    """Membersihkan layar terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_judul(judul):
    """Menampilkan judul dengan format rapi"""
    print("=" * 50)
    print(judul.center(50))
    print("=" * 50)

def ambil_waktu():
    """Mengambil waktu saat ini dalam format rapi"""
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")
