def hitung_total(lama_sewa):
    """Fungsi untuk menghitung total bayar dengan diskon"""
    harga_per_bulan = 1500000
    
    total = lama_sewa * harga_per_bulan
    
    diskon = 0
    if lama_sewa >= 12:
        diskon = total * 0.15  
    elif lama_sewa >= 6:
        diskon = total * 0.10  
    
    total_akhir = total - diskon
    return int(total_akhir)

def lihat_statistik(data_penyewa):
    """Fungsi untuk melihat statistik penyewa"""
    jumlah_penyewa = len(data_penyewa)
    sudah_bayar = 0
    belum_bayar = 0
    total_uang = 0
    
    for kamar in data_penyewa:
        if data_penyewa[kamar]['status_bayar'] == 'Lunas':
            sudah_bayar = sudah_bayar + 1
            total_uang = total_uang + hitung_total(int(data_penyewa[kamar]['lama_sewa']))
        else:
            belum_bayar = belum_bayar + 1
    
    hasil = {
        'total': jumlah_penyewa,
        'lunas': sudah_bayar,
        'belum_lunas': belum_bayar,
        'pendapatan': total_uang
    }
    
    return hasil