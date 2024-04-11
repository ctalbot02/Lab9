
def encode(code):
    for i in range(len(code)):
        code[i] += 3
    return code

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
            stored[0] = encode(code)
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


