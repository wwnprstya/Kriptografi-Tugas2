def rot_n(text, n):
    result = []
    for char in text:
        # Proses hanya huruf
        if char.isalpha():
            # Rotasi huruf besar (A-Z)
            if char.isupper():
                rotated_char = chr(((ord(char) - ord('A') + n) % 26) + ord('A'))
            else:
                rotated_char = chr(((ord(char) - ord('a') + n) % 26) + ord('a'))
            result.append(rotated_char)
        else:
            # Jika spasi, tetap di spasi
            result.append(char)
    return ''.join(result)

def display_substitution(plaintext, ciphertext):
    # Tampilkan susunan alfabet normal dan alfabet yang digeser 10 huruf (ROT10)
    alphabet_normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_rotated = rot_n(alphabet_normal, 10)
    
    # Menampilkan hasil dengan format yang sesuai
    print("Alfabet Normal  :")
    print(' '.join(alphabet_normal))
    
    print("\nAlfabet ROT10   :")
    print(' '.join(alphabet_rotated))

    print("\n\nPlaintext :")
    for char in plaintext:
        print(char, end=' ')
    print("\n\nCiphertext:")
    for char in ciphertext:
        print(char, end=' ')

# Plaintext yang diberikan
plaintext = "WAWAN IENDY PRASTYA"

# Menggunakan ROT10 untuk substitusi
ciphertext = rot_n(plaintext, 10)

# Menampilkan hasil
display_substitution(plaintext, ciphertext)

# Tampilkan juga dalam format tabel
print("\n\nTabel:")
print(f"Plaintext : {plaintext}")
print(f"Ciphertext: {ciphertext}")
