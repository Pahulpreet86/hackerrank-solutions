if __name__ == '__main__':
    s = input()
    if [char for char in s if char.isalnum()]:
        print(True)
    else:
        print(False)
    if [char for char in s if char.isalpha()]:
        print(True)
    else:
        print(False)
    if [char for char in s if char.isdigit()]:
        print(True)
    else:
        print(False)
    if [char for char in s if char.islower()]:
        print(True)
    else:
        print(False)
    if [char for char in s if char.isupper()]:
        print(True)
    else:
        print(False)
    
