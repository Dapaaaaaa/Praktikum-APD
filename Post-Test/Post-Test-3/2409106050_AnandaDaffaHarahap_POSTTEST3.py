# Ini untuk import OS agar bisa menjalankan perintah berikutnya
import os
from time import sleep

# Ini untuk menjalankan perintah clear screen untuk terminal
os.system("cls")

# Design garis
# Ini untuk menentukan panjang garis
width = 50

print("="*width)

# Program untuk menghitung bangun ruang
print("Menu Program Menghitung Bangun Ruang".center(width))

print("=" * width)

print("1. Kubus \n2. Balok \n3. Prisma \n4. Limas \n5. Tabung \n6. Kerucut \n7. Bola \n8. Keluar program")

print("="*width)

# Masukan Input Pengguna
menu = int(input("Pilih Menu : "))

# Ini untuk menjalankan perintah clear screen untuk terminal
os.system("cls")

# Menu pertama yaitu untuk menghitung kubus
if menu == 1: # Menu kubus
    print("=" * width)
    print("Pilih kebutuhan".center(width))
    print("=" * width)
    print("1. Volume \n2. Luas permukaan")
    print("=" * width)
    kebutuhan = int(input("Pilih : "))

    # Ini untuk menjalankan perintah clear screen untuk terminal
    os.system("cls")

    # blok code dimana proses terjadi
    if kebutuhan == 1:
        print("=" * width)
        sisi = float(input("Masukan sisi : "))
        v = sisi * sisi * sisi
        print("=" * width)
        print(f"Volume kubus adalah : {v:.2f} cm³")
        print("=" * width)

    # jika bukan input 1 (volume) maka akan masuk ke kebutuhan 2 yaitu luas permukaan 
    elif kebutuhan == 2:
        print("=" * width)
        sisi = float(input("Masukan sisi : "))
        lp = 6 * sisi * sisi
        print("=" * width)
        print(f"Luas permukaan kubus adalah : {lp:.2f} cm³")
        print("=" * width)

    # jika inputnya bukan 1 atau 2 maka dia akan menghasilkan output "Pilihan tidak tersedia"
    else:
        print("=" * width)
        print("Maaf tidak ada pilihan ini".center(width))
        print("=" * width)

    # blok kode ini untuk membuat screen atau layar mati atau clear dalam 2 detik
    sleep(2)

    # Ini untuk menjalankan perintah clear screen untuk terminal setekah sleep
    os.system("cls")

elif menu == 2: # Menu balok

    print("=" * width)
    print("Pilih kebutuhan".center(width))
    print("=" * width)
    print("1. Volume \n2. Luas permukaan")
    print("=" * width)
    kebutuhan = int(input("Pilih : "))

    os.system("cls")


    if kebutuhan == 1:
        print("=" * width)
        p = float(input("Masukan panjang : "))
        l = float(input("Masukan lebar : "))
        t = float(input("Masukan tinggi : "))
        v = p * l * t
        print("=" * width)
        print(f"Volume bangun balok adalah : {v:.2f} cm³")
        print("="*width)

    elif kebutuhan == 2:
        print("=" * width)
        p = float(input("Masukan panjang : "))
        l = float(input("Masukan lebar : "))
        t = float(input("Masukan tinggi : "))
        lp = 2 * (( p * l) +  ( p * t ) + ( l * t ))
        print("=" * width)
        print(f"Luas permukaan bangun balok adalah : {lp:.2f} cm³")
        print("=" * width)
    else:
        print("Maaf tidak ada pilihan ini".center(width))

    sleep(2)

    os.system("cls")

elif menu == 3: # Menu prisma

    print("=" * width)
    print("Pilih kebutuhan".center(width))
    print("=" * width)
    print("1. Volume \n2. Luas permukaan")
    print("=" * width)
    kebutuhan = int(input("Pilih : "))

    os.system("cls")

    if kebutuhan == 1:
        print("=" * width)
        la = float(input("Masukan luas alas : "))
        t = float(input("Masukan tinggi : "))
        v = la * t
        print("=" * width)
        print(f"Volume bangun prisma adalah : {v:.2f} cm³")
        print("=" * width)

    elif kebutuhan == 2:
        print("=" * width)
        ka = float(input("Masukan keliling alas : "))
        la = float(input("Masukan luas alas : "))
        t = float(input("Masukan tinggi : "))
        lp = (ka * t) + 2 * la
        print("=" * width)
        print(f"Luas permukaan bangun prisma adalah : {lp:.2f} cm³")
        print("=" * width)

    else:
        print("=" * width)
        print("Maaf tidak ada pilihan ini".center(width))
        print("=" * width)

    sleep(2)

    os.system("cls")

elif menu == 4: # Menu limas

    print("=" * width)
    print("Pilih kebutuhan".center(width))
    print("=" * width)
    print("1. Volume \n2. Luas permukaan")
    print("=" * width)
    kebutuhan = int(input("Pilih : "))

    os.system("cls")

    if kebutuhan == 1:
        print("=" * width)
        la = float(input("Masukan luas alas : "))
        t = float(input("Masukan tinggi : "))
        v = la * t / 3
        print("=" * width)
        print(f"Volume bangun limas adalah : {v:.2f} cm³")
        print("=" * width)

    elif kebutuhan == 2:
        print("=" * width)
        ls = float(input("Masukan luas seluruh sisi limas : "))
        la = float(input("Masukan luas alas : "))
        lp = ls + la
        print("=" * width)
        print(f"Luas permukaan bangun limas adalah : {lp:.2f} cm³")
        print("=" * width)

    else:
        print("=" * width)
        print("Maaf tidak ada pilihan ini".center(width))
        print("=" * width)

    sleep(2)

    os.system("cls")

elif menu == 5: # Menu tabung

    print("=" * width)
    print("Pilih kebutuhan".center(width))
    print("=" * width)
    print("1. Volume \n2. Luas permukaan")
    print("=" * width)
    kebutuhan = int(input("Pilih : "))

    os.system("cls")

    if kebutuhan == 1:
        print("=" * width)
        r = float(input("Masukan jari-jari : "))
        t = float(input("Masukan tinggi : "))
        v = 3.14 * (r * r) * t
        print("=" * width)
        print(f"Volume bangun tabung adalah : {v:.2f} cm³")
        print("=" * width)

    elif kebutuhan == 2:
        print("=" * width)
        r = float(input("Masukan jari-jari : "))
        t = float(input("Masukan tinggi : "))
        lp = 2 * 3.14 * r * (r + t)
        print("=" * width)
        print(f"Luas permukaan bangun tabung adalah : {lp:.2f} cm³")
        print("=" * width)

    else:
        print("=" * width)
        print("Maaf tidak ada pilihan ini".center(width))
        print("=" * width)

    sleep(2)

    os.system("cls")

elif menu == 6: # Menu kerucut

    print("=" * width)
    print("Pilih kebutuhan".center(width))
    print("=" * width)
    print("1. Volume \n2. Luas permukaan")
    print("=" * width)
    kebutuhan = int(input("Pilih : "))

    os.system("cls")

    if kebutuhan == 1:
        print("=" * width)
        r = float(input("Masukan jari-jari : "))
        t = float(input("Masukan tinggi : "))
        v = 3.14 * r * r * t / 3
        print("=" * width)
        print(f"Volume bangun kerucut adalah : {v:.2f} cm³")
        print("=" * width)

    elif kebutuhan == 2:
        print("=" * width)
        r = float(input("Masukan jari-jari : "))
        t = float(input("Masukan tinggi : "))
        s = pow(r * r + t * t, 0.5)
        lp = 3.14 * r * s
        print("=" * width)
        print(f"Luas permukaan bangun kerucut adalah : {lp:.2f} cm³")
        print("=" * width)
        
    else:
        print("=" * width)
        print("Maaf tidak ada pilihan ini".center(width))
        print("=" * width)

    sleep(2)

    os.system("cls")

elif menu == 7: # Menu bola

    print("=" * width)
    print("Pilih kebutuhan".center(width))
    print("=" * width)
    print("1. Volume \n2. Luas permukaan")
    print("=" * width)
    kebutuhan = int(input("Pilih : "))  

    os.system("cls")

    if kebutuhan == 1:
        print("=" * width)
        r = float(input("Masukan jari-jari : "))
        v = 4 * 3.14 * r * r * r / 3
        print("=" * width)
        print(f"Volume bangun bola adalah : {v:.2f} cm³")
        print("=" * width)

    elif kebutuhan == 2:
        print("=" * width)
        r = float(input("Masukan jari-jari : "))
        lp = 4 * 3.14 * r * r
        print("=" * width)
        print(f"Luas permukaan bangun bola adalah : {lp:.2f} cm³")
        print("=" * width)

    else:
        print("=" * width)
        print("Maaf tidak ada pilihan ini".center(width))
        print("=" * width)

    sleep(2)

    os.system("cls")

elif menu == 8:
    print("=" * width)
    print("Anda berhasil keluar!".center(width))    
    print("=" * width)

    sleep(2)

    os.system("cls")

else:
    print("=" * width)
    print("Maaf tidak ada pilihan ini".center(width))    
    print("=" * width)

    sleep(2)

    os.system("cls")
