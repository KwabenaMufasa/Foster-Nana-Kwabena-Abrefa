#Decryption / Decipher

# Declare Variable Characters - Upper and Lower Case
chars = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz']

# Define Function for Plain Text and Cipher - Using a Mapping Table with maketrans() and tranlate() functions
def decode(message, offset):
    dec_chars = str.maketrans(
        f'{chars[0][offset:]}{chars[0][:offset]}{chars[1][offset:]}{chars[1][:offset]}', # Cipher text
        f'{chars[0]}{chars[1]}' # Plain text message/ characters - Concatenated
    )
    return str.translate(message, dec_chars) 

# Set Inputs for Plain Text Message and Cipher/Shift value 
get_option = input("Choose [d]ecode : ")
if get_option == 'd':
    message = input('Enter your ciphertext message: ')
    offset = int(input('Choose the shift (1-26): '))
    if offset < 1 or offset > 26:
        raise Exception(f'Invalid entry: {offset}')
    else:
        print(f'Your decoded message is: {decode(message, offset)}')
else:
    raise Exception(f'Invalid option: {get_option}')