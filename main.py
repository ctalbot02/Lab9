
stored =[]
def encode(code):
    for i in range(len(code)):
        code[i] += 3
    return code

def decode(password):
    string = ""
    for item in password:
        if item == "0":
            string = string + "7"
        elif item == "1":
            string = string + "8"
        elif item == "2":
            string = string + "9"
        elif item == "3":
            string = string + "0"
        elif item == "4":
            string = string + "1"
        elif item == "5":
            string = string + "2"
        elif item == "6":
            string = string + "3"
        elif item == "7":
            string = string + "4"
        elif item == "8":
            string = string + "5"
        elif item == "9":
            string = string + "6"
        else:
            string = string + "-"
    return string


def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")
        choice = input("Please enter an option: ")

        if choice == "1":
            password = input("Please enter your password to encode: ")
            stored[0] = encode(password)
            print("Your password has been encoded and stored!")
            print("")
        elif choice == "2":
            print(f"The encoded password is {encode(stored[0])}, and the original password is {decode(stored[0])}.")
            print("")
        elif choice == "3":
            exit()
        else:
            print("Not an option")


if __name__ == '__main__':
    main()


