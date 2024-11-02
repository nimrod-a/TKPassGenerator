import random
import string
from tkinter import *
import pyperclip

# initialize window
root = Tk()
root.geometry("450x450")
root.title("TKPassGenerator")

output_pass = StringVar()

# define possible character sets for password
possible_chars = [string.ascii_uppercase,
                  string.digits,
                  string.ascii_lowercase]

# variable for "include special characters" checkbox
include_special = BooleanVar()
include_special.set(True)

# variable for "generate passphrase" checkbox
is_passphrase = BooleanVar()
is_passphrase.set(False)

# load EFF wordlist & strip empty spaces
with open('eff_large_wordlist.txt', 'r') as f:
    wordlist = [line.strip() for line in f]


def randPassGenerator():
    password = ""
    # generate passphrase if checkbox is checked
    if is_passphrase.get():
        # get passphrase length
        num_words = pass_len.get()
        passphrase = []
        for i in range(num_words):
            # select random word from wordlist
            word = random.choice(wordlist)
            passphrase.append(word)
            # add '-' as seperator
        password = '-'.join(passphrase)
    else:
        # include special chars in set if checked
        if include_special.get():
            possible_chars.append(string.punctuation)
        else:
            if string.punctuation in possible_chars:
                possible_chars.remove(string.punctuation)
        # generate password
        for chars in range(pass_len.get()):
            char_type = random.choice(possible_chars)
            password += random.choice(char_type)

    output_pass.set(password)


def copyPass():
    pyperclip.copy(output_pass.get())


pass_head = Label(root, text='Pass Length',
                  font='arial 14 bold').pack(pady=10)

pass_len = IntVar()
length = Scale(root, from_=4, to_=12 if is_passphrase.get() else 32,
               variable=pass_len, orient=HORIZONTAL, length=200, font='arial 16')
length.pack()

# checkbox for special characters, unless passphrase checked
include_special_checkbox = Checkbutton(root, text='Include Special Characters', variable=include_special,
                                       state=DISABLED if is_passphrase.get() else NORMAL)
include_special_checkbox.pack(pady=15)

# checkbox for passphrase
passphrase_checkbox = Checkbutton(root, text='Generate Passphrase', variable=is_passphrase, command=lambda: [
    # update length if checked
    length.config(to=12 if is_passphrase.get() else 64),
    # grey out special character checkbox if checked
    include_special_checkbox.config(
        state=DISABLED if is_passphrase.get() else NORMAL)
])
passphrase_checkbox.pack(pady=10)

# generate password button
generate_pass_button = Button(root, command=randPassGenerator, text="Generate Pass", font="Arial 11 bold",
                              bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5)
generate_pass_button.pack(pady=20)

pass_label = Label(root, text='Random Generated Password',
                   font='arial 12 bold').pack(pady="30 10")
Entry(root, textvariable=output_pass, width=32, font='arial 16').pack()

# copy to clipboard button
copy_to_clipboard = Button(root, text='Copy to Clipboard', command=copyPass, font="Arial 11",
                           bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5)
copy_to_clipboard.pack(pady=20)

root.mainloop()
