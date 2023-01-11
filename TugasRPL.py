#MENGHITUNG  HARGA PARKIR BERDASARKAN LAMMA PARKIR 

masuk = int(input("Masukkan Jam Berapa Anda Masuk Parkir  : "))
keluar = int(input("Masukkan Jam Berapa Anda Keluar Parkir: "))

lamaParkir = keluar - masuk 
hargaParkir = 2_000

if lamaParkir ==2:
    print(f"Biaya Parkir 2 Jam Pertama : RP.{hargaParkir},00")
elif lamaParkir >=3:
    biayaParkir = (lamaParkir - 2) * 500 + hargaParkir
    print(f"Biaya Parkir Anda Sebesar : RP.{biayaParkir},00")
else:
    print("EROR")
    