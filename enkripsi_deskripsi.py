print('Enkripsi & Deskripsi Untuk Mengunci File')
try:
    path = input(r"Masukan Path:")
    kunci = int(input("Masukan Password:"))
    print(f"\nFile Path: {path}")
    print(f"\nKunci Encripsi/Deskripsi: {kunci}\n")
    
    file = open(path, 'rb')
    data = file.read()
    file.close()
    
    data = bytearray(data)
    for index, nilai in enumerate(data):
        data[index] = nilai ^ kunci
    
    file = open(path, 'wb')
    file.write(data)
    file.close()
    print('Enkripsi/Deskripsi File Telah Selesai \n')
    
except Exception as e: 
    print (e)
    
    
    
    
    
    