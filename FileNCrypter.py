from hashlib import md5
from Cryptodome.Cipher import AES
from os import urandom


def derive_key_and_iv(password, salt, key_length, iv_length):
    d = d_i = b''
    while len(d) < key_length + iv_length:
        d_i = md5(d_i + password.encode('utf-8') + salt).digest()
        d += d_i
    return d[:key_length], d[key_length:key_length + iv_length]


class FileNCrypter:
    # Variables
    __password = ""

    # Constructor
    def __init__(self, password):
        self.__password = password

    #  Encrypt
    def encrypt(self, in_file, out_file, key_length=32):
        bs = AES.block_size
        salt = urandom(bs)
        key, iv = derive_key_and_iv(self.__password, salt, key_length, bs)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        out_file.write(salt)

        finished = False
        while not finished:
            chunk = in_file.read(1024 * bs)
            if len(chunk) == 0 or len(chunk) % bs != 0:
                padding_length = (bs - len(chunk) % bs) or bs
                chunk += str.encode(padding_length * chr(padding_length))
                finished = True
            out_file.write(cipher.encrypt(chunk))

    # Decrypt

    def decrypt(self, in_file, out_file, key_length=32):
        bs = AES.block_size
        salt = in_file.read(bs)
        key, iv = derive_key_and_iv(self.__password, salt, key_length, bs)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        next_chunk = ''
        finished = False
        while not finished:
            chunk, next_chunk = next_chunk, cipher.decrypt(in_file.read(1024 * bs))
            if len(next_chunk) == 0:
                padding_length = chunk[-1]
                chunk = chunk[:-padding_length]
                finished = True
            out_file.write(bytes(x for x in chunk))
