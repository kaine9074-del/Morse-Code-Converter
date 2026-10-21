de_codeing = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "-----": "0"

}
codeing = {
    "A": "._",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "  "
}

words = []
leters = []

def Convert_to_Morse_Code():
    prompt = input("What text would you like to convert? ").upper().strip()
    for letter in prompt:
        if letter in codeing:
            print(codeing[letter], end=" ")
        else:
            print("")
            print(f"Warning, character {letter} not recognized. skipping")

def Convert_to_String():
    prompt2 = input("What morse code would you like to convert? ").strip()

    words = prompt2.split("   ")

    for word in words:
        letters_in = word.split(" ")
        new_word = ""

        for letter in letters_in:
            if letter in de_codeing:
                new_word += de_codeing[letter]
            else:
                print("")
                print(f"Warning, {letter} not recognized. skipping")
        leters.append(new_word)

    print(" ".join(leters))
    
def Main_menu():
    while True:
        print("")
        print("1. Encode text to Morse code")
        print("2. Decode Morsse code to text")
        print("3. Exit")
        user_input = input("What would you like to do? ")
        if user_input == "1":
            Convert_to_Morse_Code()
        elif user_input == "2":
            Convert_to_String()
        elif user_input == "3":
            print("bye")
            break
        else:
            print("Invalid response")




Main_menu()