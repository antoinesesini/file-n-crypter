# FileNCrypter
**FileNCrypter** is a home-made **file encryption tool** for **MacOS and Linux** that enables to encrypt files in order to ensure their confidentiality.
It has been done using **Python 3.12** and the **PyCryptodome** library.
The app is either available as a **CLI** or as a **GUI** application.

<u>Important :</u>  
It is a **personal project** that have been done in order to learn more about cryptography (particularly symmetric encryption using Advanced Encryption Standard - AES algorithm) and Python programming language.
**It is purely educational and should not be used for any other purpose**.

## Documentation

### File encryption and symetric cryptography overview

The Advanced Encryption Standard (AES) is a widely used symmetric encryption algorithm. 
It employs various key lengths, including 128, 192, and 256 bits, to secure data through substitution-permutation network rounds. 
AES is renowned for its robust security and efficiency.

In order to encrypt a file, we use the AES algorithm in **CBC mode** (Cipher Block Chaining).
The AES algorithm is a block cipher algorithm, which means that it encrypts data in fixed-size blocks.
To encrypt a file, we need to split it into groups of blocks with the size = AES.block_size (16 bytes = 128 bits).
And we give those blocks to the AES algorithm cipher to encrypt them or decrypt them.

### Project structure and implementation

The application is completely coded in the **app.py** file except the FileNCrypter class which is in the **FileNCrypter.py** file.
We choosed to define a FileNCrypter class in order to provide a simple interface that just needs a password and 
input/output files to perform the encryption/decryption.

The entire interfaces are coded in the **app.py** that is the file to execute to launch the application.
It offers the choice between the CLI and the GUI application and asks the user to provide a password and an input file.

### Usage

The application requires **Python 3.12** and the **PyCryptodome** library to be installed on your computer.
**PyFiglet** library is also required to run the CLI application.

To test it, you can just navigate into the project directory and run the following command in your terminal :
```shell
python3.12 app.py
```
Then, you will be asked to choose between the CLI and the GUI application and to provide a password and an input file.

The encryption process will create a new file with the same name as the input file but with **_enc** at the end of the name.
The encrypted file will keep the same extension as the input file.
Same for the decryption process, the decrypted file will have the same name as the input file but with **_dec** at the end of the name.
It will also keep the same extension as the input file.
Those files will be created in the same directory as the input file.

## Conclusion

It has been a very interesting project to learn more about cryptography and Python programming language.
It was also a good way to learn more about the PyCryptodome library and its AES implementation.
