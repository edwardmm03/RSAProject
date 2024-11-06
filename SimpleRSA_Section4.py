import random
import math
from sympy import nextprime

class RSA_KeyGeneration:
    def __init__(self, p, q):
        """Assume p and q are distinct primes"""
        if p == q:
            raise ValueError("p and q must be distinct primes.")
        
        self.__n = p * q
        self.__z = (p - 1) * (q - 1)
        
        # Select a random `e` that is co-prime with `self.__z`
        self.__e = self.generate_e(self.__z)

        # Calculate `d` using Modular Multiplicative Inverse
        self.__d = pow(self.__e, -1, self.__z)

    def generate_e(self, phi_n):
        """Generate an `e` that is co-prime with `phi_n`"""
        while True:
            e = random.randint(2, phi_n - 1)
            if math.gcd(e, phi_n) == 1:
                return e

    def getPrivateKey(self):
        return self.__d, self.__n

    def getPublicKey(self):
        return self.__e, self.__n

# Conversion functions
def string_to_int(text):
    """Convert a string to an integer by encoding ASCII values."""
    return int.from_bytes(text.encode(), 'big')

def int_to_string(number):
    """Convert an integer back to a string after decryption."""
    byte_array = number.to_bytes((number.bit_length() + 7) // 8, 'big')
    
    try:
        # Try decoding with UTF-8
        return byte_array.decode('utf-8')
    except UnicodeDecodeError:
        # Fall back to ISO-8859-1 if UTF-8 fails
        return byte_array.decode('ISO-8859-1')

# Chunking function
def chunk_message(text, chunk_size):
    """Break a text into chunks of a specified byte size."""
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

# File processing function for encryption and decryption
def process_file(source_filename, destination_filename, keygen, mode='encrypt'):
    """Encrypt or decrypt the content of a file, handling it in chunks if necessary."""
    with open(source_filename, 'r', encoding='utf-8') as file:
        content = file.read()

    n = keygen.getPublicKey()[1]  # modulus n
    max_chunk_size = (n.bit_length() // 8) - 1  # Max chunk size in bytes

    if mode == 'encrypt':
        public_key = keygen.getPublicKey()
        encrypted_chunks = []
        
        # Split message into chunks that fit within n
        for chunk in chunk_message(content, max_chunk_size):
            message_int = string_to_int(chunk)
            encrypted_chunk = pow(message_int, public_key[0], public_key[1])
            encrypted_chunks.append(str(encrypted_chunk))
        
        # Write all encrypted chunks to the output file
        with open(destination_filename, 'w', encoding='utf-8') as encrypted_file:
            encrypted_file.write(' '.join(encrypted_chunks))
        print(f"Encrypted content written to {destination_filename}")
    
    elif mode == 'decrypt':
        private_key = keygen.getPrivateKey()
        
        # Read encrypted chunks from file
        with open(source_filename, 'r', encoding='utf-8') as encrypted_file:
            encrypted_chunks = encrypted_file.read().split()
        
        decrypted_message = ''
        
        for encrypted_chunk in encrypted_chunks:
            decrypted_chunk_int = pow(int(encrypted_chunk), private_key[0], private_key[1])
            decrypted_message += int_to_string(decrypted_chunk_int)
        
        # Write decrypted content to a new file
        with open(destination_filename, 'w', encoding='utf-8') as decrypted_file:
            decrypted_file.write(decrypted_message)
        print(f"Decrypted content written to {destination_filename}")
    else:
        raise ValueError("Mode must be either 'encrypt' or 'decrypt'")

# Main program logic for testing encryption and decryption
if __name__ == "__main__":
    # Generate large primes p and q
    bit_length = 10  # Adjust as needed for larger primes in testing
    p = nextprime(random.getrandbits(bit_length))
    q = nextprime(random.getrandbits(bit_length))

    print("P:", p)
    print("Q:", q)

    keygen = RSA_KeyGeneration(p, q)
    
    # Set filenames for input and output
    source_filename = "input.txt"  # Replace with your actual file path
    encrypted_filename = "output.enc"
    decrypted_filename = "output.dec"

    # Encrypt the file content
    process_file(source_filename, encrypted_filename, keygen, mode='encrypt')
    
    # Decrypt the file content
    process_file(encrypted_filename, decrypted_filename, keygen, mode='decrypt')