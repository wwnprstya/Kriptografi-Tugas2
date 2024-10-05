def permute_group(text, group_size=4):
    """
    Permutes the text in groups of 'group_size' characters.
    
    Args:
        text (str): The plaintext to permute.
        group_size (int): The size of each group (default is 4).
        
    Returns:
        str: The permuted ciphertext.
    """
    # Gantikan spasi dengan underscore
    text = text.replace(' ', '_')

    permuted_text = []
    # Bagi teks menjadi kelompok-kelompok
    for i in range(0, len(text), group_size):
        group = text[i:i+group_size]

        # Jika panjang grup lebih kecil dari group_size, tidak dipermutasi
        if len(group) < group_size:
            permuted_text.append(group)
        else:
            # Permutasi dengan aturan yang diberikan
            # Karakter pertama <-> Karakter terakhir, Karakter kedua <-> Karakter ketiga
            permuted_group = [group[0], group[1], group[2], group[3]]
            permuted_text.append(''.join(permuted_group))

    # Gabungkan kembali hasil permutasi
    return ''.join(permuted_text)

def format_plaintext(plaintext):
    """
    Formats the plaintext with spaces between each character.
    
    Args:
        plaintext (str): The plaintext to format.
        
    Returns:
        str: The formatted plaintext.
    """
    return ' '.join(plaintext)

def format_ciphertext(ciphertext, group_size=4):
    """
    Formats the ciphertext into groups of characters.
    
    Args:
        ciphertext (str): The ciphertext to format.
        group_size (int): The size of each group (default is 4).
        
    Returns:
        str: The formatted ciphertext with spaces between groups.
    """
    formatted = []
    for i in range(0, len(ciphertext), group_size):
        formatted.append(ciphertext[i:i+group_size])
    return ' '.join(formatted)

# Main Program
plaintext = "WAWAN IENDY PRASTYA"

# Tampilkan Plaintext
print("Plaintext:")
formatted_plaintext = format_plaintext(plaintext)
print(formatted_plaintext)

# Hasil permutasi
ciphertext = permute_group(plaintext)

# Format Ciphertext sesuai kebutuhan Anda
formatted_ciphertext = format_ciphertext(ciphertext)

# Tampilkan hasil permutasi
print("\nCiphertext:")
print(formatted_ciphertext)

# Tabel plaintext dan ciphertext
print("\nTabel:")
print(f"Plaintext : {plaintext}")
print(f"Ciphertext: {formatted_ciphertext}")
