def count_substring(string, sub_string):
    count=0

    while(string.find(sub_string)!=-1):
        start=string.find(sub_string)
        end=start+len(sub_string)
        string=string[0: start]+string[end-1:]
        count=count+1

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
