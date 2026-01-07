Pin = "12345"

while True:
    password = input("Enter your password: ")
    if Pin == password:
        print("Access Granted")
        break
    else:
        continue