nama = str(input("Masukan nama : "))
umur = int(input("Masukan umur : "))
jk_input = int(input("Masukan jenis kelamin (0 = laki-laki, 1 = perempuan) : "))
jk = bool(jk_input)
gender = "laki-laki" if not jk else "perempuan"
tb = float(input("Masukan tinggi badan : "))
bb = float(input("Masukan berat badan : "))

width = 50

print("=" * width)
print("Bio Data Anda".center(width))
print("=" * width)

print(f"Nama                    : {nama}")
print(f"Umur                    : {umur} tahun")
print(f"Jenis Kelamin           : {gender}")
print(f"Tinggi Badan            : {tb} cm")
print(f"Berat Badan             : {bb} kg")
print(f"total integer dan float : {umur+tb+bb:.2f}")

print("=" * width)  
