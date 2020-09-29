# Enter your code here. Read input from STDIN. Print output to STDOUT
length,width=map(int,input().split())
pattern_count=1
for itr in range(0,length):
    if itr <length//2:
        string='.|.'*(pattern_count)
        print(string.center(width,'-'))
        pattern_count=pattern_count+2
        
    elif itr==length//2:
        print("WELCOME".center(width,'-'))
        
    elif itr>length//2:
        pattern_count=pattern_count-2
        string='.|.'*pattern_count
        print(string.center(width,'-'))
        

