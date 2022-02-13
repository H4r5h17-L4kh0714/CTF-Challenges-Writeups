import sys

ciphertext = '1202010210201201021011200200021121112010202012010210102012102021000200121200210002021210112111200121200002111200121102000021211120010200212001020020102000212'

morse_table = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    " ": " ",
    "\n": ""
}

reverse_morse_table = {value : key for (key,value) in morse_table.items()}

trinity_table = {
    ".": "0",
    "-": "1",
    " ": "2"
}

reverse_trinity_table = {value : key for (key,value) in trinity_table.items()}

def trinity_decode(s):
    return ''.join([reverse_trinity_table[c] for c in s])

def morse_decode(s):
    return ''.join([reverse_morse_table[c] for c in trinity_decode(s).split()])

flag = morse_decode(ciphertext)
print(flag)
