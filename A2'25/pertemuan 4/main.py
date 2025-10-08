# for i in range(10):
#     print(i + 1)

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(1,11,2):
#     print(i)

#for loop untuk list
# nama = ['bakil', 'diftya', 'anugrah']
# for i in nama:
#     print(i)

# for i in range(3):
#     print("Raffi")

# while loop
# jawab = "ya"
# hitung = 0

# while (jawab == "ya"):
#     hitung += 1
#     jawab = input("ulang lagi? : ")

# print(f"total jawab ya {hitung}")

# cuaca = 'hujan'

# while (cuaca == 'hujan' or cuaca == 'Hujan'):
#     print("jangan keluar rumah")
#     cuaca = input("apa cuaca saat ini :")

# print("pergi keluar rumah")

# angka = 10

# while (angka > 1):
#     print(angka)
#     angka -= 2

# for i in range(1,5):
#     for j in range(1,5):
#         print(f"{i} x {j} = {i * j}")
#     print()

# break memberhentikan secara terpaksa, karna angkany terpenuhi maka program di hentikan
# angka = [2, 5, 8, 12, 15, 7, 20]

# print("mencari Angka yang lebih besar dari 10....")

# for i in angka:
#     print(f"memeriksa angka {i}")
#     if i > 10:
#         print(f"{i} lebih besar dari 10")
#         break

# print("Program Selesai")

#continue
# for i in range (1, 11):
#     if i % 2 != 0:
#         continue
#     print(f"Angka genap di temukan yaitu : {i}")

# print("Program Selesai")

# for i in range (1, 11):
#     if i % 2 == 0:
#         continue
#     print(f"Angka di temukan yaitu : {i}")

# print("Program Selesai")

# kuatdrat = [i**2 for i in range(1,6)]
# print(kuatdrat)

# angka_genap = [x for x in range(1,11) if x%2==0]
# print(angka_genap)

# angka_ganjil = [i for i in range(1,11) if i%2!=0]
# print(angka_ganjil)

# for i in range (1,6):
#     print("*" * i)
# print()
# for i in range (1,6):
#     print("*" * (6-i))

# a = 5
# for i in range (1,6):
#     print(" " a +"*" * (2*i-1))
#     a-=1