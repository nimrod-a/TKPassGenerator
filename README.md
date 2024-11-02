# TKPassGenerator
A simple Python program for generating pseudo-random passwords and passphrases. 
The GUI is built using TKinter, the standard GUI library for Python. 

> [!WARNING] 
Do not use for actual passwords!

While the password generator uses the Electronic Frontier Foundation long wordlist for generating passphrases, Python's `random` module generates less
randomness then using actual dice. 

### Run
```Python
$ pip install -r requirements.txt 
$ python3 tkPassGenerator.py
```
On Linux, `xclip` or another interface to clipboard selection must be installed for the copy function to work. 

> [!TIP]
Look into EFF's guide on dice Dice-Generated Passphrases [here](https://www.eff.org/dice) if you want to generate secure passphrases!
>
