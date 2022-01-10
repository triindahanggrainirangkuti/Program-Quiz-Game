print("Selamat datang di permainan kuis saya!")

bermain = input("Apakah kamu ingin bermain? ")

if bermain != "ya":
    quit()
    
print("Oke, Mari bermain!")
skor = 0

pertanyaan = input("Tipe data Phyton yang menyatakan True(1) atau False(0) disebut ")
if pertanyaan == "boolean":
    print("Benar")
    skor += 1
else:
    print("Salah")
    
pertanyaan = input("Tipe data Phyton yang menyatakan karakter/kalimat disebut ")
if pertanyaan == "string":
    print("Benar")
    skor += 1
else:
    print("Salah")

pertanyaan = input("Tipe data Phyton yang menyatakan bilangan bulat disebut ")
if pertanyaan == "integer":
    print("Benar")
    skor += 1
else:
    print("Salah")
    
pertanyaan = input("Tipe data Phyton yang menyatakan bilangan desimal disebut ")
if pertanyaan == "float":
    print("Benar")
    skor += 1
else:
    print("Salah")
    
pertanyaan = input("Tipe data Phyton yang menyatakan bilangan berbaris 2 disebut ")
if pertanyaan == "biner":
    print("Benar")
    skor += 1
else:
    print("Salah")

pertanyaan = input("Tipe data Phyton yang menyatakan bilangan berbaris 8 disebut ")
if pertanyaan == "oktal":
    print("Benar")
    skor += 1
else:
    print("Salah")
    
pertanyaan = input("Tipe data Phyton yang menyatakan bilangan berbaris 16 disebut ")
if pertanyaan == "hexadesimal":
    print("Benar")
    skor += 1
else:
    print("Salah")
    
pertanyaan = input("Tipe data yang menyatakan pasangan angka real dan imajiner disebut ")
if pertanyaan == "complex":
    print("Benar")
    skor += 1
else:
    print("Salah")
    
pertanyaan = input("Tipe data Phyton yang bisa diubah disebut ")
if pertanyaan == "list":
    print("Benar")
    skor += 1
else:
    print("Salah")

pertanyaan = input("Tipe data Phyton yang tidak bisa diubah disebut ")
if pertanyaan == "tuple":
    print("Benar")
    skor += 1
else:
    print("Salah")
    
print("Kamu berhasil menjawab " + str(skor)+ " pertanyaan yang benar")
print("Kamu mendapatkan nilai " + str(skor/10 * 100)+"%.") 
