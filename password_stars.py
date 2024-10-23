min_length_password = int(input("Enter the minimum length for your password: "))


def get_password():
    while True:
        password = input("Enter your password: ")

        if len(password) < min_length_password:
            print(f"Password must be at least {min_length_password} characters long. Please try again.")
        else:
            print('*' * len(password))
            break

get_password()
