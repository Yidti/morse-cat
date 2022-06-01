from morse_code import MorseCode
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def morse_cat():
    dit = '.'
    dah = '-'
    space = {'btw_dits_n_dahs': "", 'btw_letters': " ", 'btw_words': " / "}
    morse = MorseCode(dit, dah, **space)

    while True:
        print('-------------- Start --------------')
        response = input("Type encode(0) or decode(1) for Morse code? blank to quit. (0/1): ")
        if response == "":
            print("Bye!")
            break
        else:
            try:
                if int(response) == 0:
                    print('-------------- Encode --------------')
                    encode_input = input("Please enter any words for encoding to Morse code: ")
                    encode_result = morse.encode(encode_input)
                    repeat = input("Enter blank to try again... ")
                    cls()
                elif int(response) == 1:
                    print('-------------- Decode --------------')
                    decode_input = input("Please enter any Morse Code for decoding: ")
                    decode_result = morse.decode(decode_input)
                    repeat = input("Enter blank to try again... ")
                    cls()
                else:
                    print("Invalid input")
            except ValueError:
                print("Invalid input")


if __name__ == '__main__':


    morse_cat()
