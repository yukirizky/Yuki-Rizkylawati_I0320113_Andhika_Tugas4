# Syarat mendaftar kursus online
usia = int(input("Masukkan usia :"))
ujian = input("Apakah anda lulus ujian kualifikasi :")

if (usia>=21) and (ujian == "Y") :
    print ("Anda dapat mendaftar di kursus")
else:
    print("Anda tidak dapat mendaftar kursus")
