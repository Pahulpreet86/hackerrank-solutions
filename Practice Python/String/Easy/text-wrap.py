import textwrap

def wrap(string, max_width):
    result=[]
    count=int(len(string)/max_width)
    prev_itr=0
    while(count!=0):
        if prev_itr==0:
            result.append(string[:max_width])
            prev_itr=max_width
        else:
            new_itr=prev_itr+max_width
            result.append(string[prev_itr:new_itr])
            prev_itr=new_itr
        count=count-1
    result.append(string[prev_itr:])
    return ("\n").join(result)





if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
