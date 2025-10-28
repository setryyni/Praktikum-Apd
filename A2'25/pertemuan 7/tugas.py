# while True:
#     try:
#         nama = input("Masukkan nama: ").strip()
#         if not nama:
#             raise ValueError("Nama tidak boleh kosong atau hanya berisi spasi!")
#         print(f"Halo, {nama}!")
#         break
#     except ValueError as e:
#         print(e)

# while True:
#     try:
#         password = input("Masukkan password: ")

#         if len(password) < 8:
#             raise ValueError("Password harus memiliki minimal 8 karakter.")

#         if not any(char.isdigit() for char in password):
#             raise ValueError("Password harus mengandung setidaknya satu angka.")

#         print("Password diterima!")
#         break

#     except ValueError as e:
#         print(e)

barang = {
    "A001": "Pensil",
    "A002": "Buku",
    "A003": "Penghapus"
}

try:
    kode = input("Masukkan kode barang:").upper()
    print("Barang ditemukan:", barang[kode])

except KeyError:
    print("Kode barang tidak ditemukan!")

