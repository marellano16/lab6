# COP3502C Lab 6: Software Engineering
# Malia Arellano

def encode(password):
    encoded_password = ""
    for i in password:
        j = (int(i) + 3) % 10
        encoded_password = encoded_password + str(j)
    return encoded_password

def decode(password):
    decoded = ""
    for i in password:
        decoded += str((int(i) - 3) % 10)
    return decoded

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")

        option = int(input("\nPlease enter an option: "))
        if option == 1:
            user_password = input("Please enter your password to encode: ")
            user_password_encoded = encode(user_password)
            print("Your password has been encoded and stored!\n")

        elif option == 2:
            print(f"The encoded password is {user_password_encoded}, and the original password is {decode(user_password_encoded)}.")

        elif option == 3:
            break


if __name__ == "__main__":
    main()
