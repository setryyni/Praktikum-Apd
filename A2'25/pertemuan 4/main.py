# for i in range(10):
#     print(i + 1)

# for i in range(1, 11, 2):
#      print (i)

# nama = ['bakil','diftya', 'anugrah']

# for i in nama:
#     print(i)

# for i in range(5):
#     print("raffi")

# cuaca == 'hujan'

# while (cuaca == 'hujan' or cuaca == 'Hujan'):
#     print("jangan keluar rumah")
#     cuaca = input("apa cuaca saat ini: ")

# print("pergi keluar rumah")

# angka = 10

# while (angka > 1):
#     print(angka)
#     angka += 2

# for i in range(1,5):
#     for j in range(1,5):
#         print(f"{i} x {j} = {i * j}")

# angka = [2, 5, 8, 12, 15, 7, 20]

# print("Mencari angka yang lebih besar dari 10...")

# for i in angka:
#     print(f"memeriksa angka {i}")
#     if i > 10:
#         print(f"{i} lebih besar dari 10")
#         break

# print("Program selesai")

# for i in range(1, 11):
#     if i % 2 !=0:
#         continue
#     print(f"Angka genap ditemukan yaitu : {i}")

# print("program selesai")

# list comprehension

kuadrat = [i**2 for i in range (1,6)]
print(kuadrat)

angka_genap = [x for x in range(1, 11) if x % 2 == 0]
print(angka_genap)

for x in range(1,11):
    if x % 2 == 0 :
        print(x)