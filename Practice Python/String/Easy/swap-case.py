def swap_case(s):
    result=[x.lower() if x.isupper() else x.upper() for x in s]
    return ("").join(result)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
