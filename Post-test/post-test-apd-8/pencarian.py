def cari_penyewa(list_kamar, posisi, nama_cari, data_penyewa):
    """Fungsi rekursif untuk mencari penyewa berdasarkan nama"""
    
    if posisi >= len(list_kamar):
        return []
    
    kamar_sekarang = list_kamar[posisi]
    nama_penyewa = data_penyewa[kamar_sekarang]['nama']
    
    hasil = []
    
    if nama_cari.lower() in nama_penyewa.lower():
        hasil.append(kamar_sekarang)
    
    hasil_selanjutnya = cari_penyewa(list_kamar, posisi + 1, nama_cari, data_penyewa)

    hasil = hasil + hasil_selanjutnya
    
    return hasil