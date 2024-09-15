USD = 0.000065
EUR = 0.00006
JPY = 0.0092

IDR = float(input("Masukkan nominal uang: "))

# print("Rp", IDR, " = USD", USD * IDR, " = EUR", EUR * IDR, " = JPY", JPY * IDR)
print("Rp", IDR, " = USD", round(USD * IDR, 2), " = EUR", round(EUR * IDR, 2), " = JPY", round(JPY * IDR, 2))