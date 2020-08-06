if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    x=[itr for itr in range(0,x+1)]
    y=[itr for itr in range(0,y+1)]
    z=[itr for itr in range(0,z+1)]

    print([combination for combination in [[xi,yi,zi] for xi in x for yi in y for zi in z] if sum(combination)!=n])

