if __name__ == '__main__':
    python_students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name,score])

    [print(x) for x in sorted([x[0] for x in python_students if x[1]==min([x[1] for x in python_students if x[1]!=min([x[1] for x in python_students])])])]

