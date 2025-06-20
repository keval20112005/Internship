import password_generator as pg

def main():
    print("----- Password Generator -----")
    length = int(input("Enter password length: "))
    password = pg.generate_password(length)
    print("Generated Password:", password)

main()
