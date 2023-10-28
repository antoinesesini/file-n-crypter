from FileNCrypter import FileNCrypter
import pyfiglet
import platform
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


def verify_file(file):
    if os.path.isfile(file) and os.path.exists(file) and os.access(file, os.R_OK):
        return True
    else:
        return False


def gui_app():
    def encrypt_file():
        file_path = file_entry.get()
        password = password_entry.get()

        if verify_file(file_path):
            file_crypter = FileNCrypter(password)
            with open(file_path, "rb") as in_file:
                out_file_path = os.path.dirname(file_path) + "/" + os.path.splitext(os.path.basename(file_path))[
                    0] + "_enc" + os.path.splitext(os.path.basename(file_path))[1]
                with open(out_file_path, "wb") as out_file:
                    file_crypter.encrypt(in_file, out_file)
            result_label.config(text="Your file has been encrypted successfully!")
            result_label["foreground"] = "green"
        else:
            result_label.config(text="The specified file doesn't exist!", foreground="red")

    def decrypt_file():
        file_path = file_entry.get()
        password = password_entry.get()

        if verify_file(file_path):
            file_crypter = FileNCrypter(password)
            with open(file_path, "rb") as in_file:
                out_file_path = os.path.dirname(file_path) + "/" + os.path.splitext(os.path.basename(file_path))[
                    0] + "_dec" + os.path.splitext(os.path.basename(file_path))[1]
                with open(out_file_path, "wb") as out_file:
                    file_crypter.decrypt(in_file, out_file)
            result_label.config(text="Your file has been decrypted successfully!")
            result_label["foreground"] = "green"
        else:
            result_label.config(text="The specified file doesn't exist!", foreground="red")

    def browse_file():
        file_path = filedialog.askopenfilename()
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

    root = tk.Tk()
    root.title("FileNCrypter")
    root.geometry("400x300")

    file_label = ttk.Label(root, text="File :")
    file_label.pack(pady=10)
    file_entry = ttk.Entry(root, width=40)
    file_entry.pack()

    browse_button = ttk.Button(root, text="Browse", command=browse_file)
    browse_button.pack()

    password_label = ttk.Label(root, text="Password :")
    password_label.pack(pady=10)
    password_entry = ttk.Entry(root, show="*", width=40)
    password_entry.pack()

    encrypt_button = ttk.Button(root, text="Encrypt", command=encrypt_file)
    encrypt_button.pack()

    decrypt_button = ttk.Button(root, text="Decrypt", command=decrypt_file)
    decrypt_button.pack()

    result_label = ttk.Label(root, text="", foreground="green")
    result_label.pack(pady=10)

    root.mainloop()


def terminal_app():
    print()
    print()
    print()
    ASCII_art = pyfiglet.figlet_format("FileNCrypter", font='big')
    print(ASCII_art)
    print()
    print()

    # We ask the user if he wants to encrypt or decrypt a file
    print("What kind of operation do you want to do ?")
    print("1 - Encrypt a file")
    print("2 - Decrypt a file")
    print("3 - Exit")
    choice = input("Your choice : ")
    print()
    print()
    print()
    # Encryption
    if choice == "1":
        file = input("Which file do you want to encrypt ? ")
        if verify_file(file):
            password = input("Which password do you want to use ? ")
            file_crypter = FileNCrypter(password)
            with open(file, "rb") as in_file:
                out_file_path = os.path.dirname(file) + "/" + os.path.splitext(os.path.basename(file))[0] + "_enc" + os.path.splitext(os.path.basename(file))[1]
                with open(out_file_path, "wb") as out_file:
                    file_crypter.encrypt(in_file, out_file)
            print("Your file has been encrypted successfully !")
            print(
                "You can find your encrypted version in the original file's directory as " + out_file_path)
        else:
            print("The specified file doesn't exist !")
            terminal_app()
    # Decryption
    elif choice == "2":
        file = input("Which file do you want to decrypt ? ")
        if verify_file(file):
            password = input("What is the password ? ")
            file_crypter = FileNCrypter(password)
            with open(file, "rb") as in_file:
                out_file_path = os.path.dirname(file) + "/" + os.path.splitext(os.path.basename(file))[0] + "_dec" + os.path.splitext(os.path.basename(file))[1]
                with open(out_file_path, "wb") as out_file:
                    file_crypter.decrypt(in_file, out_file)
            print("Your file has been decrypted successfully !")
            print(
                "You can find your decrypted version in the original file's directory as " + out_file_path)
        else:
            print("The specified file doesn't exist !")
            terminal_app()
    # Exit
    elif choice == "3":
        exit()
    # Not valid entry
    else:
        print("Please choose a number between 1 and 3 !")
        terminal_app()


def main():
    if platform.system() != "Darwin" and platform.system() != "Linux":
        print("This program is only available on macOS !")
        exit()
    print("Welcome to FileNCrypter !")
    print("Choose your interface :")
    print("1 - Graphical User Interface")
    print("2 - Terminal Interface")
    print("3 - Exit")
    choice = input("Your choice : ")
    print()
    print()
    print()
    if choice == "1":
        gui_app()
    elif choice == "2":
        terminal_app()
    elif choice == "3":
        exit()
    else:
        print("Please choose a number between 1 and 3 !")
        main()


if __name__ == "__main__":
    main()
