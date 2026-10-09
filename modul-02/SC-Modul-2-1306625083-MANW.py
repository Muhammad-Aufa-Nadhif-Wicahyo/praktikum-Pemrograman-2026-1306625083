# -*- coding: utf-8 -*-
"""SC-Modul-2-1306625083





"""

print("Program Faktor Bilangan")
print("Nama : Muhammad Aufa Nadhif Wicahyo")
print("NIM : 1306625083")
print()

while True :
  a = int(input("masukkan bilangan < 100 (masukkan 0 untuk selesai) = "))
  b = int(input("masukkan bilangan < 100 (masukkan 0 untuk selesai) = "))

  hasil_a = []
  hasil_b = []

  if a >= 100 or b >= 100:
    print("Error")
    break

  elif a == 0 and b == 0 :
    print ("Program Selesai")
    break

  for i in range(1, a+1):
    if a % i == 0:
      hasil_a.append(i)

  for i in range(1, b+1):
    if b % i == 0:
      hasil_b.append(i)

    hasil_sama = []

    for i in hasil_a:
      if i in hasil_b:
        hasil_sama.append(i)

  print("Bilangan", a, "-> faktornya =", hasil_a)
  print("Bilangan", b, "-> faktornya =", hasil_b)
  print("Bilangan", a, "dan", b, "-> faktor yang sama =")

  print()