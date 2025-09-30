# angka = 5

# if angka > 5:
#     print("angka lebih besar 5")

# contoh 1

# cuaca = "Hujan"

# if cuaca == "Hujan":
#     print("dirumah aja")
# else :
#     print("nongkrong")

# contoh 2

#nilai = 70

# if nilai <= 70:
#     print("Lulus")
# else:
#     print("Tidak Lulus")

# status = "lulus" if nilai>= 70 else "tidak lulus"
# print(status)

# contoh 3

# cuaca = 'Mendung'

# if cuaca == "Hujan":
#     print("dirumah aja")
# elif cuaca == "mendung":
#     print("Makan mie")
# else:
#     print("nongkrong")

# usia = int (input("Masukan usia anda : "))

# if usia <= 0:
#     print("Usia tidak valid")
# elif usia <= 13:
#     print("Anak-anak")
# elif usia <= 18:
#     print("remaja")
# elif usia <= 40:
#     print("dewasa")
# else:
#     print("tua")

# contoh 4

# nilai = int(input("Masukan nilai: "))

# if nilai >= 90:
#     print("A")
# elif nilai >= 70:
#     print("B")
# elif nilai >= 60:
#     print("C")
# else:
#     print("D")

#contoh 5

# a = 2
# b = 5
# c = 6

# if a<b :
#     if a <c:
#         print ("a paling kecil")
#     else :
#         print ("c lebih kecil dari a")
# elif a<c:
#     print("clebih besar")
# else :
#     print ("a paling besar")

# contoh 6

# tinggi_badan = float(input("masukan tinggi badan: "))

# status= "diizinkan" if tinggi_badan >= 145 else ("tidak diizinkan masuk")
# print (status)

# contoh 7

# a = 100000
# b = 50000

total_belanjaan = int(input("Masukan data belanjaan: "))

if total_belanjaan >= 100000:
     print("mendapatkan diskon 20%")
     bayar = total_belanjaan * 0.2
     print(bayar)
     total = total_belanjaan - bayar
     print("total belanjaan", float(total_belanjaan))
elif total_belanjaan >= 50000:
    print("mendapatkan diskon 10")
    bayar = total_belanjaan * 0.1
    print(bayar)
    total = total_belanjaan - bayar
    print("total belanjaan", float(total_belanjaan))
else :
     print("tidak mendapatkan diskon")

#  contoh 8

# nilai = int(input("Masukan :"))
# kelas = input(("Masukan kelas :"))

# if nilai >= 80 and kelas == "A":
#    print ("IPK 4")

# elif nilai >= 80 and kelas "B":
#   print ("IPK 3")

# else:
#    print ("IPK 2")
