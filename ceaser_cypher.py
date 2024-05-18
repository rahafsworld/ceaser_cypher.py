alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

word = input("What is the word? ").lower()
shift = int(input("What is the shift amount? "))
direction = input("encrypt or decrypt? ").lower()

def encrypt(word, shift, direction):
    if direction not in ["encrypt", "decrypt"]:
        print("Invalid direction. Please choose 'encrypt' or 'decrypt'.")
        return

    cipher = ""
    for let in word:
        if let not in alphabet[:26]:
            print(f"Invalid character '{let}' in the word.\nPlease use only alphabetic characters.")
            return

        pose = alphabet.index(let)
        new_shift = shift % 26

        if direction == "encrypt":
            new_let = alphabet[pose + new_shift]
        elif direction == "decrypt":
            new_let = alphabet[pose - new_shift]

        cipher += new_let

    print(cipher)

encrypt(word, shift, direction)
