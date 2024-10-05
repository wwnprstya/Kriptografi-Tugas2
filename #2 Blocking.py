def blocking_plaintext_fixed(plaintext, kolom, K):
    # Mengonversi plaintext menjadi huruf besar, spasi diubah menjadi underscore untuk visualisasi
    plaintext = plaintext.replace(" ", "_").upper()
    
    # Tentukan panjang plaintext dan siapkan blok sesuai ketentuan K dan kolom
    panjang_karakter = len(plaintext)
    baris = K  # Jumlah baris sesuai dengan K
    
    # Membuat blok dengan ukuran baris x kolom
    blok = [['' for _ in range(kolom)] for _ in range(baris)]
    
    idx = 0
    for i in range(kolom):
        for j in range(baris):
            if idx < panjang_karakter:
                blok[j][i] = plaintext[idx]
                idx += 1
            else:
                blok[j][i] = '_'  # Mengisi blok kosong dengan underscore sebagai spasi kosong

    # Cetak blok sesuai ketentuan (per kolom vertikal)
    print("Blok yang diisi secara vertikal:")
    for i, b in enumerate(blok, start=1):
        print(f"Block {i:2}: {'  '.join(b)}")
    
    # Menghasilkan ciphertext dengan pembacaan horizontal per kolom
    ciphertext = ''
    for i in range(baris):
        for j in range(kolom):
            ciphertext += blok[i][j]

    # Format ciphertext menjadi blok 5 karakter
    formatted_ciphertext = ' '.join([ciphertext[i:i+5] for i in range(0, len(ciphertext), 5)])
    
    return formatted_ciphertext

# Main Program
plaintext = "WAWAN IENDY PRASTYA"
kolom = 5
K = 4
ciphertext = blocking_plaintext_fixed(plaintext, kolom, K)

# Menampilkan hasil
print("\nCiphertext Blocking (K=4, 5 kolom):", ciphertext)
